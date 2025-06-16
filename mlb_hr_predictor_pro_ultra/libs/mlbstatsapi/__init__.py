
class MLBStatsAPI:
    def get_teams(self, sportId=1):
        return {
            "teams": [{"name": "Yankees"}, {"name": "Dodgers"}, {"name": "Cubs"}]
        }
