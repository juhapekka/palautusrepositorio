class Player:
    def __init__(self, dict):
        for key, value in dict.items():
            setattr(self, key, value)

    def __str__(self):
        return f"{self.name} team {self.team}  goals {self.goals} assists {self.assists}"
