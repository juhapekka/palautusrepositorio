import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

#    print("JSON-muotoinen vastaus:")
#    print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN\n")

    suomalaiset_players = filter(lambda player: player.nationality == "FIN", players)
    sortatut_suomalaiset_players = sorted(suomalaiset_players, key=lambda player: player.points, reverse=True)

    for player in sortatut_suomalaiset_players:
        print(player)

if __name__ == "__main__":
    main()
