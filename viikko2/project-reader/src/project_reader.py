from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        dd = toml.loads(content)

        nimi = dd["tool"]["poetry"].get("name", "nimetön")
        kuv = dd["tool"]["poetry"].get("description", "-")
        lisenssi = dd["tool"]["poetry"].get("license", "-")
        authorit = dd["tool"]["poetry"].get("authors", [])
        
        dep = list(dd["tool"]["poetry"]["dependencies"].keys())
        dev_dep = list(dd["tool"]["poetry"]["group"]["dev"]["dependencies"].keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(nimi, kuv, dep, dev_dep, lisenssi, authorit)
