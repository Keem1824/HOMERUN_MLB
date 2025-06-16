
from mlbstatsapi import MLBStatsAPI
from pybaseball import playerid_lookup
from core import predict_hr
from data.statcast_features import get_batter_features
import pandas as pd
import numpy as np
import datetime

api = MLBStatsAPI()
today = datetime.date.today().strftime('%Y-%m-%d')

def get_today_games():
    schedule = api.get_schedule(date=today)
    games = []
    for g in schedule['dates'][0]['games']:
        home = g['teams']['home']['team']['name']
        away = g['teams']['away']['team']['name']
        home_id = g['teams']['home']['team']['id']
        away_id = g['teams']['away']['team']['id']
        home_pitcher = g['teams']['away'].get('probablePitcher', {}).get('fullName', 'TBD')
        away_pitcher = g['teams']['home'].get('probablePitcher', {}).get('fullName', 'TBD')
        games.append({'home': home, 'away': away, 'home_id': home_id, 'away_id': away_id,
                      'home_pitcher': home_pitcher, 'away_pitcher': away_pitcher})
    return games

def build_team_features(team_id):
    roster = api.get_team_roster(team_id)
    players = roster['roster']
    result = []
    for p in players:
        name = p['person']['fullName']
        pid = p['person']['id']
        try:
            feats = get_batter_features(pid)
            feats['player'] = name
            result.append(feats)
        except:
            continue
    return pd.DataFrame(result)

def simulate_full_slate():
    games = get_today_games()
    all_results = []

    for g in games:
        for team_id, team_name, opponent, opp_pitcher in [
            (g['home_id'], g['home'], g['away'], g['away_pitcher']),
            (g['away_id'], g['away'], g['home'], g['home_pitcher'])
        ]:
            print(f"📊 Simulating {team_name} vs {opponent}...")
            try:
                team_df = build_team_features(team_id)
                if team_df.empty: continue

                pitcher = {
                    'HR_per9': 1.3,
                    'avg_pitch_speed': 94.0,
                    'slider_pct': 22,
                    'curve_pct': 10,
                    'fastball_pct': 55
                }
                weather = {
                    'temp': 75,
                    'wind_speed': 10,
                    'wind_dir': 1,
                    'humidity': 55
                }

                result = predict_hr(team_df, pitcher, weather)
                result['team'] = team_name
                result['opponent'] = opponent
                result['pitcher'] = opp_pitcher
                all_results.append(result)
            except Exception as e:
                print(f"❌ Error with {team_name}: {e}")

    df = pd.concat(all_results)
    df.to_csv(f"real_slate_hr_predictions_{today}.csv", index=False)
    print(f"✅ Saved: real_slate_hr_predictions_{today}.csv")

if __name__ == "__main__":
    simulate_full_slate()
