
from mlbstatsapi import MLBStatsAPI
import pandas as pd

api = MLBStatsAPI()

def get_all_teams():
    teams = api.get_teams(sportId=1)['teams']
    return sorted([t['name'] for t in teams])

def get_team_id_by_name(team_name):
    teams = api.get_teams(sportId=1)['teams']
    for team in teams:
        if team['name'].lower() == team_name.lower():
            return team['id']
    return None

def get_current_roster(team_name):
    team_id = get_team_id_by_name(team_name)
    if not team_id:
        raise ValueError(f"Team not found: {team_name}")
    roster = api.get_team_roster(team_id, rosterType="active")
    players = roster['roster']
    return pd.DataFrame([{
        'player': p['person']['fullName'],
        'id': p['person']['id'],
        'position': p.get('position', {}).get('abbreviation', ''),
        'jerseyNumber': p.get('jerseyNumber', ''),
    } for p in players])

def get_all_active_rosters():
    teams = api.get_teams(sportId=1)['teams']
    all_data = []
    for t in teams:
        team_name = t['name']
        team_id = t['id']
        try:
            roster = api.get_team_roster(team_id, rosterType="active")
            for p in roster['roster']:
                all_data.append({
                    'team': team_name,
                    'player': p['person']['fullName'],
                    'id': p['person']['id'],
                    'position': p.get('position', {}).get('abbreviation', ''),
                    'jerseyNumber': p.get('jerseyNumber', '')
                })
        except Exception as e:
            print(f"❌ Error loading roster for {team_name}: {e}")
    return pd.DataFrame(all_data)
