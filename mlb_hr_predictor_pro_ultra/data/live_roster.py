
from mlbstatsapi import MLBStatsAPI
import pandas as pd

api = MLBStatsAPI()

def get_all_teams():
    return [team['name'] for team in api.get_teams(sportId=1)['teams']]
