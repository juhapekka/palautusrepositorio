class Player:
    def __init__(self, dict):
        for key, value in dict.items():
            setattr(self, key, value)

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} team {self.team:5}  {self.goals:3} + {self.assists:3} = {self.points:4}"
