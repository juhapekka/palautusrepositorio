LOVE = 0
FIFTEEN = 1
THIRTY = 2
FORTY = 3
ADVANTAGE_MARGIN = 1
WIN_MARGIN = 2

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def tasa_pisteet(self):
        nimet = {
            LOVE: "Love-All",
            FIFTEEN: "Fifteen-All",
            THIRTY: "Thirty-All"
        }

        return nimet.get(self.m_score1, "Deuce")
        
    def johto_tai_voitto(self):
        vastaukset = {
            ADVANTAGE_MARGIN: "Advantage player1",
            -ADVANTAGE_MARGIN: "Advantage player2",
            WIN_MARGIN: "Win for player1",
            -WIN_MARGIN: "Win for player2"
        }

        minus_result = self.m_score1 - self.m_score2

        # Tarkat osumat
        if minus_result in vastaukset:
            return vastaukset[minus_result]
        # Tilanne on suurempi tai pienempi kuin määritellyt rajat
        elif minus_result >= WIN_MARGIN:
            return "Win for player1"
        else:
            return "Win for player2"
        
    def laske_pisteet(self):
        nimet = {
            LOVE: "Love",
            FIFTEEN: "Fifteen",
            THIRTY: "Thirty",
            FORTY: "Forty"
        }

        score1 = nimet.get(self.m_score1, 'Unknown')
        score2 = nimet.get(self.m_score2, 'Unknown')

        return f"{score1}-{score2}"


    def get_score(self):
        score = ""

        if self.m_score1 == self.m_score2:
            score = self.tasa_pisteet()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self.johto_tai_voitto()
        else:
            score = self.laske_pisteet()

        return score
