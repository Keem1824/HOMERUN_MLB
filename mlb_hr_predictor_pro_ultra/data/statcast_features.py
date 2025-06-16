
from pybaseball import statcast_batter
from datetime import datetime, timedelta

def get_batter_features(player_id):
    end = datetime.now()
    start = end - timedelta(days=60)
    df = statcast_batter(start, end, player_id)
    df = df.dropna(subset=['launch_speed', 'launch_angle'])
    if df.empty:
        raise ValueError("No data")
    avg_exit = df['launch_speed'].mean()
    avg_angle = df['launch_angle'].mean()
    return {
        'HR_rate': df['events'].eq('home_run').mean(),
        'ISO': 0.2,
        'wOBA': 0.3,
        'ExitVelo': avg_exit,
        'LaunchAngle': avg_angle,
        'barrel_rate': (df['launch_speed'] > 95).mean(),
        'hard_hit_pct': (df['launch_speed'] > 90).mean()
    }
