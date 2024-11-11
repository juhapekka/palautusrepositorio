import requests
import re
from rich import print
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def intro():
    print(Text("NHL statistics by nationality\n", style="italic dim"))
    
def hae_seasonit(baseurl):
    response = requests.get(baseurl)
    return re.findall(r'\d{4}-\d{2}', response.text)

def valitse_seasoni(seasons):
    season = ""
    while season not in seasons:
        season = Prompt.ask(f"Select season [purple][{'/'.join(seasons)}][/purple]")
    return season

def kysy_nationality(stats):
    nationality = ""
    prompti = f"Choose nationality [purple][{'/'.join(stats.nationalities)}][/purple]"

    while nationality not in stats.nationalities:
        nationality = Prompt.ask(prompti)
    return nationality

def luo_taulu(players, nationality, season):
    columns = [("name", "cyan", "left"), ("team", "purple", "left"),
               ("goals", "green", "right"), ("assists", "green", "right"),
               ("points", "green", "right")]

    taulu = Table(title=f"Top scorers of {nationality} season {season}")

    for c in columns:
        taulu.add_column(c[0], style=c[1], justify=c[2])

    for p in players:
        taulu.add_row(*[Text(str(getattr(p, a)), style=c) for a, c, _ in columns])
    return taulu

def main():
    baseurl = "https://studies.cs.helsinki.fi/nhlstats/"

    intro()
    seasons = hae_seasonit(baseurl)
    season = valitse_seasoni(seasons)

    url = f"{baseurl}{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = kysy_nationality(stats)
        players = stats.top_scorers_by_nationality(nationality)
        taulu = luo_taulu(players, nationality, season)
        print(taulu, "\n")

if __name__ == "__main__":
    main()
