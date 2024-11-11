from player import Player
from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader:PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality:str) -> list[Player]:
        players = filter(lambda player: player.nationality == nationality, self.reader.players)
        return sorted(players, key=lambda player: player.points, reverse=True)
