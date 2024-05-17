import pandas as pd

# Načítanie údajov zo súboru CSV
file_path = r'sezona19_20_goals.csv'
data = pd.read_csv(file_path)

# Získanie počtu riadkov
pocet_riadkov = data.shape[0]

print("2019/2020")
print("==================")
print("Počet riadkov:", pocet_riadkov)

# Vytvorenie listov pre jednotlivé kategórie
play_id_list = data['play_id'].tolist()
game_id_list = data['game_id'].tolist()
team_id_for_list = data['team_id_for'].tolist()
team_id_against_list = data['team_id_against'].tolist()
event_list = data['event'].tolist()
secondaryType_list = data['secondaryType'].tolist()
x_list = data['x'].tolist()
y_list = data['y'].tolist()
period_list = data['period'].tolist()
periodType_list = data['periodType'].tolist()
periodTime_list = data['periodTime'].tolist()
periodTimeRemaining_list = data['periodTimeRemaining'].tolist()
dateTime_list = data['dateTime'].tolist()
goals_away_list = data['goals_away'].tolist()
goals_home_list = data['goals_home'].tolist()
description_list = data['description'].tolist()
st_x_list = data['st_x'].tolist()
st_y_list = data['st_y'].tolist()

# Počet rôznych hodnôt v liste game_id
unique_game_ids = len(set(game_id_list))
print("Počet rôznych hodnôt v liste game_id:", unique_game_ids)

# Získanie všetkých rôznych hodnôt z period_list
rozne_hodnoty_period_list = set(period_list)
print("Všetky rôzne hodnoty z period_list:", rozne_hodnoty_period_list)

# Počet riadkov pre jednotlivé periodTypes
pocet_riadkov_period_types = data['period'].value_counts()

print("Počet riadkov pre jednotlivé period:")
print(pocet_riadkov_period_types)

import matplotlib.pyplot as plt

# Filtrovanie údajov pre period = 1
filtered_data_period_1 = data[data['period'] == 1]
filtered_data_period_2 = data[data['period'] == 2]
filtered_data_period_3 = data[data['period'] == 3]

# Vytvorenie viacerých podgrafov
fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
# Histogram pre period 1
axs[0].hist(filtered_data_period_1['periodTime'], bins=20, color='blue', alpha=0.5)
axs[0].set_title('1. tretina')
axs[0].set_xlabel('čas v 1. tretine (s)', fontsize=15)
axs[0].set_ylabel('absolútna početnosť gólov')
axs[0].grid(True)
# Histogram pre period 2
axs[1].hist(filtered_data_period_2['periodTime'], bins=20, color='green', alpha=0.5)
axs[1].set_title('2. tretina')
axs[1].set_xlabel('čas v 2. tretine (s)', fontsize=15)
axs[1].grid(True)
# Histogram pre period 3
axs[2].hist(filtered_data_period_3['periodTime'], bins=20, color='red', alpha=0.5)
axs[2].set_title('3. tretina')
axs[2].set_xlabel('čas v 3. tretine (s)', fontsize=15)
axs[2].grid(True)
# Názov celého grafu
plt.suptitle('Absolútne početnosti gólov v zápasoch sezóny 2019/2020', fontsize=25)
# Zobrazenie grafu
plt.tight_layout()
plt.show()

# Vytvorenie viacerých podgrafov
fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

# Histogram pre period 1
axs[0].hist(filtered_data_period_1['periodTime'], bins=20, range=(0, 1200), color='blue', alpha=0.5, density=True)
axs[0].set_title('1. tretina')
axs[0].set_xlabel('čas v 1. tretine (s)', fontsize=15)
axs[0].set_ylabel('Relatívne početnosti')
axs[0].grid(True)

# Histogram pre period 2
axs[1].hist(filtered_data_period_2['periodTime'], bins=20, range=(0, 1200), color='green', alpha=0.5, density=True)
axs[1].set_title('2. tretina')
axs[1].set_xlabel('čas v 2. tretine (s)', fontsize=15)
axs[1].grid(True)

# Histogram pre period 3
axs[2].hist(filtered_data_period_3['periodTime'], bins=20, range=(0, 1200), color='red', alpha=0.5, density=True)
axs[2].set_title('3. tretina')
axs[2].set_xlabel('čas v 3. tretine (s)', fontsize=15)
axs[2].grid(True)

# Názov celého grafu
plt.suptitle('Relatívne početnosti gólov v zápasoch sezóny 2019/2020', fontsize=25)

# Zobrazenie grafu
plt.tight_layout()
plt.show()

print("=================")
# Počet rôznych game_id
pocet_roznych_game_id = data['game_id'].nunique()
# Počet riadkov v jednotlivých obdobiach
pocet_riadkov_period_1 = len(data[data['period'] == 1])
pocet_riadkov_period_2 = len(data[data['period'] == 2])
pocet_riadkov_period_3 = len(data[data['period'] == 3])
# Výpočet priemerného počtu riadkov na jedno game_id
priemerny_pocet_riadkov_na_game_id = (pocet_riadkov_period_1 + pocet_riadkov_period_2 + pocet_riadkov_period_3) / pocet_roznych_game_id
print("Počet rôznych game_id:", pocet_roznych_game_id)
print("Počet riadkov v period 1:", pocet_riadkov_period_1)
print("Počet riadkov v period 2:", pocet_riadkov_period_2)
print("Počet riadkov v period 3:", pocet_riadkov_period_3)
print("Priemerný počet riadkov na jedno game_id:", priemerny_pocet_riadkov_na_game_id)


print("=================")
diff_list = []
# Naplnenie zoznamu nulami
for _ in range(pocet_riadkov):
    diff_list.append(0)
# Naplnenie zoznamu podľa podmienok
for i in range(pocet_riadkov):
    if (goals_away_list[i] + goals_home_list[i] == 1):
        diff_list[i] = 0
    if (goals_away_list[i] + goals_home_list[i] > 1):
        if (goals_away_list[i] == goals_away_list[i-1]):
            diff_list[i] = goals_away_list[i] - goals_home_list[i-1]
        if (goals_home_list[i] == goals_home_list[i-1]):
            diff_list[i] = goals_away_list[i-1] - goals_home_list[i]
print(diff_list[:10])
print("-2 ale znamena ze vyhravali domaci o 2!!!")
print("rozdiely v skóre pred gólom - funguje správne")


print("=================")
matchTime_list = []
# Naplnenie zoznamu
for i in range(pocet_riadkov):
    matchTime_list.append((period_list[i]-1)*1200 + periodTime_list[i])
print(matchTime_list[:15])
print("sekunda zápasu, v ktorej padol gól")


print("=================")
import matplotlib.pyplot as plt
data['diff_list'] = diff_list
data['matchTime'] = matchTime_list
# Filtrácia dát podľa podmienky diff_list == 0
filtered_data0 = data[data['diff_list'] == 0 & (data['matchTime'] <= 3600)]
# Vytvorenie histogramu s rozdelením podľa matchTime
plt.hist(filtered_data0['matchTime'], bins=60, range=(0, 3600), color='skyblue')
plt.axvline(x=1200, color='black', linestyle='--', linewidth=2)
plt.axvline(x=2400, color='black', linestyle='--', linewidth=2)
plt.xlabel('matchTime')
plt.ylabel('Počet')
plt.title('Rozdelenie gólov podľa času pri nerozhodnom stave')
plt.show()
# Filtrácia dát podľa podmienky diff_list == 1
filtered_data1 = data[abs(data['diff_list']) == 1 & (data['matchTime'] <= 3600)]
# Vytvorenie histogramu s rozdelením podľa matchTime
plt.hist(filtered_data1['matchTime'], bins=60, range=(0, 3600), color='skyblue')
plt.axvline(x=1200, color='black', linestyle='--', linewidth=2)
plt.axvline(x=2400, color='black', linestyle='--', linewidth=2)
plt.xlabel('matchTime')
plt.ylabel('Počet')
plt.title('Rozdelenie gólov podľa času gólovom rozdiele 1')
plt.show()
# Filtrácia dát podľa podmienky diff_list >= 2
filtered_data2 = data[abs(data['diff_list']) >= 2 & (data['matchTime'] <= 3600)]
# Vytvorenie histogramu s rozdelením podľa matchTime
plt.hist(filtered_data2['matchTime'], bins=60, range=(0, 3600), color='skyblue')
plt.axvline(x=1200, color='black', linestyle='--', linewidth=2)
plt.axvline(x=2400, color='black', linestyle='--', linewidth=2)
plt.xlabel('matchTime')
plt.ylabel('Počet')
plt.title('Rozdelenie gólov podľa času gólovom rozdiele >= 2')
plt.show()


print("=====================")
print("získavanie reálnych dát")
# Načítanie údajov zo súboru CSV
file_path2 = r'C:\Users\Kurucovci\OneDrive\Marek\VŠ\BP\sezona19_20.csv'
data2 = pd.read_csv(file_path2)
# Odstránenie riadkov, kde hodnota v stĺpci "outcome" je "tbc win tbc"
data2 = data2[data2['outcome'] != 'tbc win tbc']

# Získanie počtu riadkov
pocet_riadkov2 = data2.shape[0]
print(pocet_riadkov2)

outcome_list = data2['outcome'].tolist()
game_id_list2 = data2['game_id'].tolist()
score50 = [0] * pocet_riadkov2
score40 = [0] * pocet_riadkov2
score30 = [0] * pocet_riadkov2
score20 = [0] * pocet_riadkov2
score10 = [0] * pocet_riadkov2
score5 = [0] * pocet_riadkov2
score3 = [0] * pocet_riadkov2
score2 = [0] * pocet_riadkov2

for i in range (pocet_riadkov2):
    for j in range (pocet_riadkov):
        if game_id_list2[i] == game_id_list[j]:
            if matchTime_list[j] < 120:
                score2[i] = goals_home_list[j] - goals_away_list[j]
            if matchTime_list[j] < 180:
                score3[i] = goals_home_list[j] - goals_away_list[j]
            if matchTime_list[j] < 300:
                score5[i] = goals_home_list[j] - goals_away_list[j]
            if matchTime_list[j] < 600:
                score10[i] = goals_home_list[j] - goals_away_list[j]
            if matchTime_list[j] < 1200:
                score20[i] = goals_home_list[j] - goals_away_list[j]
            if matchTime_list[j] < 1800:
                score30[i] = goals_home_list[j] - goals_away_list[j]
            if matchTime_list[j] < 2400:
                score40[i] = goals_home_list[j] - goals_away_list[j]
            if matchTime_list[j] < 3000:
                score50[i] = goals_home_list[j] - goals_away_list[j]
                
#print("score2", score2[:15])
#print("score3", score3[:15])
#print("score5", score5[:15])
#print("score10", score10[:15])
#print("score20", score20[:15])
#print("score30", score30[:15])
#print("score40", score40[:15])
#print("score50", score50[:15])
#print(len(score50), "fungujeeeeeee")
#print(set(score2), "score2")
#print(set(score3), "score3")
#print(set(score5), "score5")
#print(set(score10), "score10")
#print(set(score20), "score20")
#print(set(score30), "score30")
#print(set(score40), "score40")
#print(set(score50), "score50")

print("========= cas 2min =========")
hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score2[i] == -2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score2[i] == -1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score2[i] == 0:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("0:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score2[i] == 1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score2[i] == 2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)



print("========= cas 3min =========")
hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score3[i] == -2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score3[i] == -1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score3[i] == 0:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("0:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score3[i] ==1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score3[i] == 2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)



print("========= cas 5min =========")
hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score5[i] == -3:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-3:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score5[i] == -2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score5[i] == -1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score5[i] == 0:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("0:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score5[i] == 1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score5[i] == 2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)



print("========= cas 10min =========")
hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score10[i] <= -4:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-4 a menej:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score10[i] == -3:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-3:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score10[i] == -2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score10[i] == -1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score10[i] == 0:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("0:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score10[i] == 1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score10[i] == 2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score10[i] == 3:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+3:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score10[i] >= 4:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+4 a viac:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)



print("========= cas 20min =========")
hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score20[i] <= -4:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-4 a menej:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score20[i] == -3:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-3:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score20[i] == -2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score20[i] == -1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score20[i] == 0:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("0:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score20[i] == 1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score20[i] == 2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score20[i] == 3:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+3:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score20[i] >= 4:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+4 a viac:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)



print("========= cas 30min =========")
hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score30[i] <= -4:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-4 a menej:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score30[i] == -3:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-3:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score30[i] == -2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score30[i] == -1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score30[i] == 0:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("0:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score30[i] == 1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score30[i] == 2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score30[i] == 3:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+3:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score30[i] >= 4:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+4 a viac:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)



print("========= cas 40min =========")
hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score40[i] <= -4:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-4 a menej:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score40[i] == -3:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-3:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score40[i] == -2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score40[i] == -1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score40[i] == 0:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("0:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score40[i] == 1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score40[i] == 2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score40[i] == 3:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+3:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score40[i] >= 4:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+4 a viac:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)



print("========= cas 50min =========")
hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score50[i] <= -4:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-4 a menej:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score50[i] == -3:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-3:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score50[i] == -2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score50[i] == -1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("-1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score50[i] == 0:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("0:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score50[i] == 1:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+1:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score50[i] == 2:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+2:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score50[i] == 3:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+3:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)

hwins = 0
awins = 0
howins = 0
aowins = 0
for i in range (pocet_riadkov2):
    if score50[i] >= 4:
        if outcome_list[i] == "home win REG":
            hwins = hwins + 1
        if outcome_list[i] == "away win REG":
            awins = awins + 1
        if outcome_list[i] == "away win OT":
            aowins = aowins + 1
        if outcome_list[i] == "home win OT":
            howins = howins + 1
print("+4 a viac:", "domaci", hwins, "domaci pred", howins, "hostia pred", aowins, "hostia", awins)