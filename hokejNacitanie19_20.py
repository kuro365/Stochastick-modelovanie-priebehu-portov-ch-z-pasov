import pandas as pd

# Načítanie údajov zo súboru CSV
file_path = r'sezona19_20.csv'
data = pd.read_csv(file_path)

# Získanie počtu riadkov
pocet_riadkov = data.shape[0]

print("==================")
print("Počet riadkov:", pocet_riadkov)

game_id_list = []
season_list = []
type_list = []
date_time_GMT_list = []
away_team_id_list = []
home_team_id_list = []
away_goals_list = []
home_goals_list = []
outcome_list = []
home_rink_side_start_list = []

for index, row in data.iterrows():
    game_id_list.append(row['game_id'])
    season_list.append(row['season'])
    type_list.append(row['type'])
    date_time_GMT_list.append(row['date_time_GMT'])
    away_team_id_list.append(row['away_team_id'])
    home_team_id_list.append(row['home_team_id'])
    away_goals_list.append(row['away_goals'])
    home_goals_list.append(row['home_goals'])
    outcome_list.append(row['outcome'])
    home_rink_side_start_list.append(row['home_rink_side_start'])

# Testovací výpis prvých 5 prvkov zo všetkých vytvorených listov
print("==================")
print("game_id_list:", game_id_list[:5])
print("season_list:", season_list[:5])
print("type_list:", type_list[:5])
print("away_team_id_list:", away_team_id_list[:5])
print("home_team_id_list:", home_team_id_list[:5])
print("away_goals_list:", away_goals_list[:5])
print("home_goals_list:", home_goals_list[:5])
print("outcome_list:", outcome_list[:5])
print("home_rink_side_start_list:", home_rink_side_start_list[:5])
print("==================")

# Získanie všetkých rôznych hodnôt v type_list
rozne_hodnoty_type = set(type_list)
print("Všetky rôzne hodnoty v type_list:", len(set(type_list)))
for hodnota_type in rozne_hodnoty_type:
    print(hodnota_type)
print("==================")
    
print("ROZDELENIE ZÁPASOV PLAYOFF/REGULAR")
R = 0
P = 0
for i in range (pocet_riadkov):
    if (type_list[i]== "P"):
        P += 1
    if (type_list[i]== "R"):
        R += 1
print("playoff", P, "regular", R)

print("==================")
print("kontrola ci vsetky z jednej sezony")
# Získanie všetkých rôznych hodnôt v season_list
rozne_hodnoty_sezona = set(season_list)

print("Všetky rôzne hodnoty v season_list:", len(rozne_hodnoty_sezona))
for hodnota_sezona in rozne_hodnoty_sezona:
    print(hodnota_sezona)
    
print("==================")
print("vsetky mozne vysledky")
# Získanie všetkých rôznych hodnôt v outcome_list
rozne_hodnoty_vysledok = set(outcome_list)
print("Všetky rôzne hodnoty v outcome_list:", len(rozne_hodnoty_vysledok))
for hodnota_vysledok in rozne_hodnoty_vysledok:
    print(hodnota_vysledok)
    
print("==================")
W = 0
OW = 0
OL = 0
L = 0
for i in range (pocet_riadkov):
    if (outcome_list[i]== "home win REG"):
        W += 1
    if (outcome_list[i]== "home win OT"):
        OW += 1
    if (outcome_list[i]== "away win OT"):
        OL += 1
    if (outcome_list[i]== "away win REG"):
        L += 1
print("home wins:", W)
print("home OT wins:", OW)
print("away wins:", L)
print("away OT wins:", OL)

print("==================")
print("GOLY")
home_goals = 0
away_goals = 0
for i in range (pocet_riadkov):
    home_goals += home_goals_list[i]
    away_goals += away_goals_list[i]
print("počet domácich gólov:", home_goals)
print("počet hosťujúcich gólov:", away_goals)
print("priemer domáci:", home_goals/pocet_riadkov)
print("priemer hostia:", away_goals/pocet_riadkov)
