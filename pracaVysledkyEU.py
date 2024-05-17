import csv
import statistics
import math
from scipy.stats import norm
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

input_file = 'euroleague_final.csv'

# Initialize lists for each category
teamName_list = [None] * 1148
teamPTS_list = [None] * 1148
opptName_list = [None] * 1148
opptPTS_list = [None] * 1148
winner_list = [None] * 1148
teamPTS1_list = [None] * 1148
teamPTS2_list = [None] * 1148
teamPTS3_list = [None] * 1148
teamPTS4_list = [None] * 1148
teamPTSOvertime_list = [None] * 1148
opptPTS1_list = [None] * 1148
opptPTS2_list = [None] * 1148
opptPTS3_list = [None] * 1148
opptPTS4_list = [None] * 1148
opptPTSOvertime_list = [None] * 1148
# pocet bodov v riadnom hracom case
teamMatchPTS_list = [None] * 1148
opptMatchPTS_list = [None] * 1148
# bodovy rozdiel po i-tej stvrtine
diffPTS1_list = [None] * 1148
diffPTS2_list = [None] * 1148
diffPTS3_list = [None] * 1148
diffPTS4_list = [None] * 1148
diffPTS_list = [None] * 1148

with open(input_file, 'r') as infile:
    reader = csv.reader(infile)
    
    # Read the header row to get the column names
    header = next(reader)
    
    # Count the number of rows
    num_rows = len(list(reader))
    print("celkovo zapasov:", num_rows)

    # Go back to the beginning of the file
    infile.seek(0)

    # Skip the header row again
    next(reader, None)
    
    # pre remizy
    num_drawsT = 0
    num_drawsO = 0
    draws = 0
    # vyhry v riadnom hracom case
    wins = 0
    losses = 0
    
    # vyhry do rozhodnutia
    num_winsH = 0
    num_winsA = 0
    
    # polcasove vysledky
    num_HTwinsH = 0
    num_HTwinsA = 0
    num_HTdraws = 0
    
    # kontingencna tabulka
    x_11 = 0
    x_12 = 0
    x_13 = 0
    x_21 = 0
    x_22 = 0
    x_23 = 0
    x_31 = 0
    x_32 = 0
    x_33 = 0
    
    for i in range(num_rows):
        first_row = next(reader)
        # zapisanie info
        teamName_list[i] = first_row[0]
        opptName_list[i] = first_row[1]
        winner_list[i] = first_row[2]
        teamPTS_list[i] = int(first_row[3])
        opptPTS_list[i] = int(first_row[4])
        teamPTS1_list[i] = int(first_row[5])
        opptPTS1_list[i] = int(first_row[6])
        teamPTS2_list[i] = int(first_row[7])
        opptPTS2_list[i] = int(first_row[8])
        teamPTS3_list[i] = int(first_row[9])
        opptPTS3_list[i] = int(first_row[10])
        teamPTS4_list[i] = int(first_row[11])
        opptPTS4_list[i] = int(first_row[12])
        
        # vypocet bodov v zakl. hracej dobe
        teamMatchPTS_list[i] = teamPTS1_list[i] + teamPTS2_list[i] + teamPTS3_list[i] + teamPTS4_list[i]
        opptMatchPTS_list[i] = opptPTS1_list[i] + opptPTS2_list[i] + opptPTS3_list[i] + opptPTS4_list[i]
        
        # remizy domaceho timu a hostujuceho timu
        if teamMatchPTS_list[i] != teamPTS_list[i]:
            num_drawsT = num_drawsT + 1
        if opptMatchPTS_list[i] != opptPTS_list[i]:
            num_drawsO = num_drawsO + 1 
        
        # rozdiel po kazdej stvrtine
        diffPTS1_list[i] = teamPTS1_list[i] - opptPTS1_list[i]
        diffPTS2_list[i] = teamPTS2_list[i] - opptPTS2_list[i]
        diffPTS3_list[i] = teamPTS3_list[i] - opptPTS3_list[i]
        diffPTS4_list[i] = teamPTS4_list[i] - opptPTS4_list[i]
        diffPTS_list[i] = teamMatchPTS_list[i] - opptMatchPTS_list[i]
        
        # pocet remiz celkovo (vsetky tri udaje sa musia rovnat)
        if diffPTS_list[i] == 0:
            draws = draws + 1 
        if diffPTS_list[i] > 0:
            wins = wins + 1
        if diffPTS_list[i] < 0:
            losses = losses + 1
        
        # pocet vitazstiev
        if winner_list[i] == teamName_list[i]:
            num_winsH = num_winsH + 1
        if winner_list[i] == opptName_list[i]:
            num_winsA = num_winsA + 1
            
        # pocet polcasovych vitazstiev
        if diffPTS1_list[i] + diffPTS2_list[i] > 0:
            num_HTwinsH = num_HTwinsH + 1
        if diffPTS1_list[i] + diffPTS2_list[i] < 0:
            num_HTwinsA = num_HTwinsA + 1
        if diffPTS1_list[i] + diffPTS2_list[i] == 0:
            num_HTdraws = num_HTdraws + 1
        
        # kontingencna tabulka
        if (diffPTS1_list[i] + diffPTS2_list[i] > 0) and (diffPTS_list[i] > 0):
            x_11 = x_11 + 1
        if (diffPTS1_list[i] + diffPTS2_list[i] > 0) and (diffPTS_list[i] == 0):
            x_12 = x_12 + 1
        if (diffPTS1_list[i] + diffPTS2_list[i] > 0) and (diffPTS_list[i] < 0):
            x_13 = x_13 + 1
        if (diffPTS1_list[i] + diffPTS2_list[i] == 0) and (diffPTS_list[i] > 0):
            x_21 = x_21 + 1
        if (diffPTS1_list[i] + diffPTS2_list[i] == 0) and (diffPTS_list[i] == 0):
            x_22 = x_22 + 1
        if (diffPTS1_list[i] + diffPTS2_list[i] == 0) and (diffPTS_list[i] < 0):
            x_23 = x_23 + 1
        if (diffPTS1_list[i] + diffPTS2_list[i] < 0) and (diffPTS_list[i] > 0):
            x_31 = x_31 + 1
        if (diffPTS1_list[i] + diffPTS2_list[i] < 0) and (diffPTS_list[i] == 0):
            x_32 = x_32 + 1
        if (diffPTS1_list[i] + diffPTS2_list[i] < 0) and (diffPTS_list[i] < 0):
            x_33 = x_33 + 1
        
print("--------------------")
print("vyhra/vyhra", x_11)
print("vyhra/remiza", x_12)  
print("vyhra/prehra", x_13)  
print("remiza/vyhra", x_21)  
print("remiza/remiza", x_22)  
print("remiza/prehra", x_23)  
print("prehra/vyhra", x_31)  
print("prehra/remiza", x_32)  
print("prehra/prehra", x_33)  
print("--------------------")
print("počet remíz domácich:", num_drawsT)
print("počet remíz hostí:", num_drawsO)
print("počet remíz:", draws)
print("počet víťazstiev domácich v r.h.č.:", wins)
print("počet víťazstiev hostí v r.h.č.:", losses)
print("--------------------")
print("počet víťazstiev domácich:", num_winsH)
print("počet víťazstiev hostí:", num_winsA)
print("--------------------")
print("počet polč. víťazstiev domácich:", num_HTwinsH)
print("počet polč. víťazstiev hostí:", num_HTwinsA)
print("počet polč. remíz:", num_HTdraws)
print("--------------------")

# vypocet pre jednotlive stvrtiny
priemer1 = sum(diffPTS1_list)/len(diffPTS1_list)
print("priemer prva stvrtina:", priemer1)
print("odchylka prva stvrtina:", statistics.stdev(diffPTS1_list))
priemer2 = sum(diffPTS2_list)/len(diffPTS2_list)
print("priemer druha stvrtina:", priemer2)
print("odchylka druha stvrtina:", statistics.stdev(diffPTS2_list))
priemer3 = sum(diffPTS3_list)/len(diffPTS3_list)
print("priemer tretia stvrtina:", priemer3)
print("odchylka tretia stvrtina:", statistics.stdev(diffPTS3_list))
priemer4 = sum(diffPTS4_list)/len(diffPTS4_list)
print("priemer stvrta stvrtina:", priemer4)
print("odchylka stvrta stvrtina:", statistics.stdev(diffPTS4_list))
print("--------------------")
print("priemer celkovo:", sum(diffPTS_list)/len(diffPTS_list))
print("odchylka celkovo:", statistics.stdev(diffPTS_list))
print("--------------------")

# celkovo bodov na jeden zapas
print("priemerný počet bodov domáci:", sum(teamMatchPTS_list)/len(teamMatchPTS_list))
print("odchýlka body domáci:", statistics.stdev(teamMatchPTS_list))
print("priemerný počet bodov hostia:", sum(opptMatchPTS_list)/len(opptMatchPTS_list))
print("odchýlka body hostia:", statistics.stdev(opptMatchPTS_list))
print("priemerný počet bodov na zápas:", (sum(teamMatchPTS_list)+sum(opptMatchPTS_list))/len(teamMatchPTS_list))
print("--------------------")

# vyhry este raz
w = 0
l = 0
for i in range(1148):
    if (teamPTS_list[i] > opptPTS_list[i]):
        w = w + 1
    if (teamPTS_list[i] < opptPTS_list[i]):
        l = l + 1
print(w, "vyhier domaci")
print(l, "vyhier hostia")

# tolko percent zapasov by mali vyhrat domaci
print(norm.cdf((sum(diffPTS_list)/len(diffPTS_list))/statistics.stdev(diffPTS_list), 0, 1), "% zapasov by mali vyhrat domaci")
print("--------------------")

# tabulka pravdepodobnosti
t_1 = 0
t_2 = 1/4
t_3 = 1/2
t_4 = 3/4
t_5 = 9/10
l_1 = -5
l_2 = -3
l_3 = -1
l_4 = 0
l_5 = 1
l_6 = 3
l_7 = 5
l_8 = -7
l_9 = 7
drift = sum(diffPTS_list)/len(diffPTS_list)
sigma2 = statistics.stdev(diffPTS_list) * statistics.stdev(diffPTS_list)
# t = 0
a_1 = (l_4 + ((1-t_1)*drift))/math.sqrt((1-t_1)*sigma2)
# t = 1/4
a_2 = (l_1 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_3 = (l_2 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_4 = (l_3 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_5 = (l_4 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_6 = (l_5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_7 = (l_6 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_8 = (l_7 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_30 = (l_8 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_31 = (l_9 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
# t = 1/2
a_9 = (l_1 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_10 = (l_2 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_11 = (l_3 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_12 = (l_4 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_13 = (l_5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_14 = (l_6 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_15 = (l_7 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_32 = (l_8 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_33 = (l_9 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
# t = 3/4
a_16 = (l_1 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_17 = (l_2 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_18 = (l_3 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_19 = (l_4 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_20 = (l_5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_21 = (l_6 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_22 = (l_7 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_34 = (l_8 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_35 = (l_9 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
# t = 9/10
a_23 = (l_1 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_24 = (l_2 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_25 = (l_3 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_26 = (l_4 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_27 = (l_5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_28 = (l_6 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_29 = (l_7 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_36 = (l_8 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_37 = (l_9 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
print("mi = ", drift, "sigma na druhu =", sigma2)
print(norm.cdf(a_1, 0, 1), "cas nula, skore nula")
print(norm.cdf(a_2, 0, 1), "cas 1/4, skore -5")
print(norm.cdf(a_3, 0, 1), "cas 1/4, skore -3")
print(norm.cdf(a_4, 0, 1), "cas 1/4, skore -1")
print(norm.cdf(a_5, 0, 1), "cas 1/4, skore 0")
print(norm.cdf(a_6, 0, 1), "cas 1/4, skore +1")
print(norm.cdf(a_7, 0, 1), "cas 1/4, skore +3")
print(norm.cdf(a_8, 0, 1), "cas 1/4, skore +5")
print(norm.cdf(a_30, 0, 1), "cas 1/4, skore -7")
print(norm.cdf(a_31, 0, 1), "cas 1/4, skore +7")
print("....................")
print(norm.cdf(a_9, 0, 1), "cas 1/2, skore -5")
print(norm.cdf(a_10, 0, 1), "cas 1/2, skore -3")
print(norm.cdf(a_11, 0, 1), "cas 1/2, skore -1")
print(norm.cdf(a_12, 0, 1), "cas 1/2, skore 0")
print(norm.cdf(a_13, 0, 1), "cas 1/2, skore +1")
print(norm.cdf(a_14, 0, 1), "cas 1/2, skore +3")
print(norm.cdf(a_15, 0, 1), "cas 1/2, skore +5")
print(norm.cdf(a_32, 0, 1), "cas 1/2, skore -7")
print(norm.cdf(a_33, 0, 1), "cas 1/2, skore +7")
print("....................")
print(norm.cdf(a_16, 0, 1), "cas 3/4, skore -5")
print(norm.cdf(a_17, 0, 1), "cas 3/4, skore -3")
print(norm.cdf(a_18, 0, 1), "cas 3/4, skore -1")
print(norm.cdf(a_19, 0, 1), "cas 3/4, skore 0")
print(norm.cdf(a_20, 0, 1), "cas 3/4, skore +1")
print(norm.cdf(a_21, 0, 1), "cas 3/4, skore +3")
print(norm.cdf(a_22, 0, 1), "cas 3/4, skore +5")
print(norm.cdf(a_34, 0, 1), "cas 3/4, skore -7")
print(norm.cdf(a_35, 0, 1), "cas 3/4, skore +7")
print("....................")
print(norm.cdf(a_23, 0, 1), "cas 9/10, skore -5")
print(norm.cdf(a_24, 0, 1), "cas 9/10, skore -3")
print(norm.cdf(a_25, 0, 1), "cas 9/10, skore -1")
print(norm.cdf(a_26, 0, 1), "cas 9/10, skore 0")
print(norm.cdf(a_27, 0, 1), "cas 9/10, skore +1")
print(norm.cdf(a_28, 0, 1), "cas 9/10, skore +3")
print(norm.cdf(a_29, 0, 1), "cas 9/10, skore +5")
print(norm.cdf(a_36, 0, 1), "cas 9/10, skore -7")
print(norm.cdf(a_37, 0, 1), "cas 9/10, skore +7")
print("....................")

# t = 1/4
print("t=1/4")
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i] <= -7:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("-7 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i] >-7 and diffPTS1_list[i]<= -5:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("-5 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i] >-5 and diffPTS1_list[i]<= -3:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("-3 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i] >-3 and diffPTS1_list[i]<= -1:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("-1 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i] >-1 and diffPTS1_list[i]<= 0:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("0 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i] >0 and diffPTS1_list[i]<= 2:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("+1 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i] >2 and diffPTS1_list[i]<= 4:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("+3 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i] >4 and diffPTS1_list[i]<= 6:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("+5 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i] >6:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("+7 a výhry:", var1, var2)
print("--------------------")

# t = 1/2
print("t=1/2")
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i] <= -7:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("-7 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i] >-7 and diffPTS1_list[i]+diffPTS2_list[i]<= -5:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("-5 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i] >-5 and diffPTS1_list[i]+diffPTS2_list[i]<= -3:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("-3 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i] >-3 and diffPTS1_list[i]+diffPTS2_list[i]<= -1:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("-1 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i] >-1 and diffPTS1_list[i]+diffPTS2_list[i]<= 0:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("0 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i] >0 and diffPTS1_list[i]+diffPTS2_list[i]<= 2:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("+1 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i] >2 and diffPTS1_list[i]+diffPTS2_list[i]<= 4:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("+3 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i] >4 and diffPTS1_list[i]+diffPTS2_list[i]<= 6:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("+5 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i] >6:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("+7 a výhry:", var1, var2)
print("--------------------")

# t = 3/4
print("t=3/4")
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i] <= -7:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("-7 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i] >-7 and diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i]<= -5:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("-5 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i] >-5 and diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i]<= -3:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("-3 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i] >-3 and diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i]<= -1:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("-1 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i] >-1 and diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i]<= 0:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("0 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i] >0 and diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i]<= 2:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("+1 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i] >2 and diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i]<= 4:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("+3 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i] >4 and diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i]<=6:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("+5 a výhry:", var1, var2)
var1 = 0
var2 = 0
for i in range(1148):
    if diffPTS1_list[i]+diffPTS2_list[i]+diffPTS3_list[i] >6:
        var1 = var1 + 1
        if diffPTS_list[i] > 0:
            var2 = var2 + 1
print("+7 a výhry:", var1, var2)
print("--------------------")

# vyhry/prehry po predlzeni
var1 = 0
var2 = 0
remizy = [None] * 49
for i in range(1148):
    if diffPTS_list[i] == 0:
        remizy[var1] = i
        var1 = var1 + 1
        if winner_list[i] == teamName_list[i]:
            var2 = var2 + 1
print("z ", var1, " remizovych zapasov vyhrali domaci ", var2)
r1 = 0
r2 = 0 
r3 = 0
r4 = 0
r5 = 0
w_pp_1 = 0
w_pp_2 = 0
w_pp_3 = 0
w_pp_4 = 0
w_pp_5 = 0
for i in range(49):
    if diffPTS4_list[remizy[i]] <= -5:
        r1 = r1 + 1
        if winner_list[i] == teamName_list[i]:
            w_pp_1 = w_pp_1 + 1
    if diffPTS4_list[remizy[i]] <= -1:
        r2 = r2 + 1
        if winner_list[i] == teamName_list[i]:
            w_pp_2 = w_pp_2 + 1
    if diffPTS4_list[remizy[i]] <= 0:
        r3 = r3 + 1
        if winner_list[i] == teamName_list[i]:
            w_pp_3 = w_pp_3 + 1
    if diffPTS4_list[remizy[i]] <= 4:
        r4 = r4 + 1
        if winner_list[i] == teamName_list[i]:
           w_pp_4 = w_pp_4 + 1
    if diffPTS4_list[remizy[i]] < math.inf:
        r5 = r5 + 1
        if winner_list[i] == teamName_list[i]:
            w_pp_5 = w_pp_5 + 1
print("kumulativna postupnost:", r1, r2, r3, r4, r5)
print("z toho vyhry:", w_pp_1, w_pp_2, w_pp_3, w_pp_4, w_pp_5)

# korektura na cele cisla
# t = 0
a_1c1 = (l_4 + 0.5 + ((1-t_1)*drift))/math.sqrt((1-t_1)*sigma2)
a_1c2 = (l_4 - 0.5 + ((1-t_1)*drift))/math.sqrt((1-t_1)*sigma2)
# t = 1/4
a_2c1 = (l_1 + 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_2c2 = (l_1 - 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_3c1 = (l_2 + 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_3c2 = (l_2 - 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_4c1 = (l_3 + 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_4c2 = (l_3 - 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_5c1 = (l_4 + 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_5c2 = (l_4 - 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_6c1 = (l_5 + 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_6c2 = (l_5 - 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_7c1 = (l_6 + 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_7c2 = (l_6 - 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_8c1 = (l_7 + 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_8c2 = (l_7 - 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_30c1 = (l_8 + 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_30c2 = (l_8 - 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_31c1 = (l_9 + 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_31c2 = (l_9 - 0.5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
# t = 1/2
a_9c1 = (l_1 + 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_9c2 = (l_1 - 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_10c1 = (l_2 + 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_10c2 = (l_2 - 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_11c1 = (l_3 + 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_11c2 = (l_3 - 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_12c1 = (l_4 + 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_12c2 = (l_4 - 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_13c1 = (l_5 + 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_13c2 = (l_5 - 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_14c1 = (l_6 + 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_14c2 = (l_6 - 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_15c1 = (l_7 + 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_15c2 = (l_7 - 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_32c1 = (l_8 + 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_32c2 = (l_8 - 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_33c1 = (l_9 + 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_33c2 = (l_9 - 0.5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
# t = 3/4
a_16c1 = (l_1 + 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_16c2 = (l_1 - 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_17c1 = (l_2 + 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_17c2 = (l_2 - 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_18c1 = (l_3 + 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_18c2 = (l_3 - 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_19c1 = (l_4 + 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_19c2 = (l_4 - 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_20c1 = (l_5 + 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_20c2 = (l_5 - 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_21c1 = (l_6 + 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_21c2 = (l_6 - 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_22c1 = (l_7 + 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_22c2 = (l_7 - 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_34c1 = (l_8 + 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_34c2 = (l_8 - 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_35c1 = (l_9 + 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_35c2 = (l_9 - 0.5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
# t = 9/10
a_23c1 = (l_1 + 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_23c2 = (l_1 - 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_24c1 = (l_2 + 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_24c2 = (l_2 - 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_25c1 = (l_3 + 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_25c2 = (l_3 - 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_26c1 = (l_4 + 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_26c2 = (l_4 - 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_27c1 = (l_5 + 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_27c2 = (l_5 - 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_28c1 = (l_6 + 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_28c2 = (l_6 - 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_29c1 = (l_7 + 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_29c2 = (l_7 - 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_36c1 = (l_8 + 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_36c2 = (l_8 - 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_37c1 = (l_9 + 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_37c2 = (l_9 - 0.5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
print("-------------------")
print("po korekture na cele cisla")
print(0.5*norm.cdf(a_1c1, 0, 1)+0.5*norm.cdf(a_1c2, 0, 1), "cas nula, skore nula")
print(0.5*norm.cdf(a_2c1, 0, 1)+0.5*norm.cdf(a_2c2, 0, 1), "cas 1/4, skore -5")
print(0.5*norm.cdf(a_3c1, 0, 1)+0.5*norm.cdf(a_3c2, 0, 1), "cas 1/4, skore -3")
print(0.5*norm.cdf(a_4c1, 0, 1)+0.5*norm.cdf(a_4c2, 0, 1), "cas 1/4, skore -1")
print(0.5*norm.cdf(a_5c1, 0, 1)+0.5*norm.cdf(a_5c2, 0, 1), "cas 1/4, skore 0")
print(0.5*norm.cdf(a_6c1, 0, 1)+0.5*norm.cdf(a_6c2, 0, 1), "cas 1/4, skore +1")
print(0.5*norm.cdf(a_7c1, 0, 1)+0.5*norm.cdf(a_7c2, 0, 1), "cas 1/4, skore +3")
print(0.5*norm.cdf(a_8c1, 0, 1)+0.5*norm.cdf(a_8c2, 0, 1), "cas 1/4, skore +5")
print(0.5*norm.cdf(a_30c1, 0, 1)+0.5*norm.cdf(a_30c2, 0, 1), "cas 1/4, skore -7")
print(0.5*norm.cdf(a_31c1, 0, 1)+0.5*norm.cdf(a_31c2, 0, 1), "cas 1/4, skore +7")
print("....................")
print(0.5*norm.cdf(a_9c1, 0, 1)+0.5*norm.cdf(a_9c2, 0, 1), "cas 1/2, skore -5")
print(0.5*norm.cdf(a_10c1, 0, 1)+0.5*norm.cdf(a_10c2, 0, 1), "cas 1/2, skore -3")
print(0.5*norm.cdf(a_11c1, 0, 1)+0.5*norm.cdf(a_11c2, 0, 1), "cas 1/2, skore -1")
print(0.5*norm.cdf(a_12c1, 0, 1)+0.5*norm.cdf(a_12c2, 0, 1), "cas 1/2, skore 0")
print(0.5*norm.cdf(a_13c1, 0, 1)+0.5*norm.cdf(a_13c2, 0, 1), "cas 1/2, skore +1")
print(0.5*norm.cdf(a_14c1, 0, 1)+0.5*norm.cdf(a_14c2, 0, 1), "cas 1/2, skore +3")
print(0.5*norm.cdf(a_15c1, 0, 1)+0.5*norm.cdf(a_15c2, 0, 1), "cas 1/2, skore +5")
print(0.5*norm.cdf(a_32c1, 0, 1)+0.5*norm.cdf(a_32c2, 0, 1), "cas 1/2, skore -7")
print(0.5*norm.cdf(a_33c1, 0, 1)+0.5*norm.cdf(a_33c2, 0, 1), "cas 1/2, skore +7")
print("....................")
print(0.5*norm.cdf(a_16c1, 0, 1)+0.5*norm.cdf(a_16c2, 0, 1), "cas 3/4, skore -5")
print(0.5*norm.cdf(a_17c1, 0, 1)+0.5*norm.cdf(a_17c2, 0, 1), "cas 3/4, skore -3")
print(0.5*norm.cdf(a_18c1, 0, 1)+0.5*norm.cdf(a_18c2, 0, 1), "cas 3/4, skore -1")
print(0.5*norm.cdf(a_19c1, 0, 1)+0.5*norm.cdf(a_19c2, 0, 1), "cas 3/4, skore 0")
print(0.5*norm.cdf(a_20c1, 0, 1)+0.5*norm.cdf(a_20c2, 0, 1), "cas 3/4, skore +1")
print(0.5*norm.cdf(a_21c1, 0, 1)+0.5*norm.cdf(a_21c2, 0, 1), "cas 3/4, skore +3")
print(0.5*norm.cdf(a_22c1, 0, 1)+0.5*norm.cdf(a_22c2, 0, 1), "cas 3/4, skore +5")
print(0.5*norm.cdf(a_34c1, 0, 1)+0.5*norm.cdf(a_34c2, 0, 1), "cas 3/4, skore -7")
print(0.5*norm.cdf(a_35c1, 0, 1)+0.5*norm.cdf(a_35c2, 0, 1), "cas 3/4, skore +7")
print("....................")
print(0.5*norm.cdf(a_23c1, 0, 1)+0.5*norm.cdf(a_23c2, 0, 1), "cas 9/10, skore -5")
print(0.5*norm.cdf(a_24c1, 0, 1)+0.5*norm.cdf(a_24c2, 0, 1), "cas 9/10, skore -3")
print(0.5*norm.cdf(a_25c1, 0, 1)+0.5*norm.cdf(a_25c2, 0, 1), "cas 9/10, skore -1")
print(0.5*norm.cdf(a_26c1, 0, 1)+0.5*norm.cdf(a_26c2, 0, 1), "cas 9/10, skore 0")
print(0.5*norm.cdf(a_27c1, 0, 1)+0.5*norm.cdf(a_27c2, 0, 1), "cas 9/10, skore +1")
print(0.5*norm.cdf(a_28c1, 0, 1)+0.5*norm.cdf(a_28c2, 0, 1), "cas 9/10, skore +3")
print(0.5*norm.cdf(a_29c1, 0, 1)+0.5*norm.cdf(a_29c2, 0, 1), "cas 9/10, skore +5")
print(0.5*norm.cdf(a_36c1, 0, 1)+0.5*norm.cdf(a_36c2, 0, 1), "cas 9/10, skore -7")
print(0.5*norm.cdf(a_37c1, 0, 1)+0.5*norm.cdf(a_37c2, 0, 1), "cas 9/10, skore +7")
print("....................")

# overme normalne rozdelenie
print("QQ plots")
# Create Q-Q plot
plt.figure(figsize=(12.5, 7.5))
stats.probplot(diffPTS1_list, dist="norm", plot=plt)
plt.title('Q-Q graf bodových rozdielov v 1. štvrtine - Euroliga', fontsize=25)
plt.xlabel('kvantily normálneho rozdelenia', fontsize=15)
plt.ylabel('hodnoty skóre', fontsize=15)
plt.show()
print("....................")

# korelacia vysledkov jednotlivych stvrtin
# Calculate the Pearson correlation coefficient
print("KOR. KOEFICIENTY")
n = len(diffPTS1_list)
#
correlation_coefficient12 = np.corrcoef(diffPTS1_list, diffPTS2_list)[0, 1]
standard_error12 = np.sqrt((1 - correlation_coefficient12**2) / (n - 2))
print("korelacny koeficient 1 a 2:", correlation_coefficient12, "chyba:", standard_error12)
#
correlation_coefficient13 = np.corrcoef(diffPTS1_list, diffPTS3_list)[0, 1]
standard_error13 = np.sqrt((1 - correlation_coefficient13**2) / (n - 2))
print("korelacny koeficient 1 a 3:", correlation_coefficient13, "chyba:", standard_error13)
#
correlation_coefficient14 = np.corrcoef(diffPTS1_list, diffPTS4_list)[0, 1]
standard_error14 = np.sqrt((1 - correlation_coefficient14**2) / (n - 2))
print("korelacny koeficient 1 a 4:", correlation_coefficient14, "chyba:", standard_error14)
#
correlation_coefficient23 = np.corrcoef(diffPTS2_list, diffPTS3_list)[0, 1]
standard_error23 = np.sqrt((1 - correlation_coefficient23**2) / (n - 2))
print("korelacny koeficient 2 a 3:", correlation_coefficient23, "chyba:", standard_error23)
#
correlation_coefficient24 = np.corrcoef(diffPTS2_list, diffPTS4_list)[0, 1]
standard_error24 = np.sqrt((1 - correlation_coefficient24**2) / (n - 2))
print("korelacny koeficient 2 a 4:", correlation_coefficient24, "chyba:", standard_error24)
#
correlation_coefficient34 = np.corrcoef(diffPTS3_list, diffPTS4_list)[0, 1]
standard_error34 = np.sqrt((1 - correlation_coefficient34**2) / (n - 2))
print("korelacny koeficient 3 a 4:", correlation_coefficient34, "chyba:", standard_error34)

# korelacny koeficient medzi stvrtinami a vysledkom
# v zakladnej hracej dobe
cor1 = np.corrcoef(diffPTS1_list, diffPTS_list)[0, 1]
standard_error1 = np.sqrt((1 - cor1**2) / (n - 2))
print("kor. stvrtina 1:", cor1, "chyba:", standard_error1)
#
cor2 = np.corrcoef(diffPTS2_list, diffPTS_list)[0, 1]
standard_error2 = np.sqrt((1 - cor2**2) / (n - 2))
print("kor. stvrtina 2:", cor2, "chyba:", standard_error2)
#
cor3 = np.corrcoef(diffPTS3_list, diffPTS_list)[0, 1]
standard_error3 = np.sqrt((1 - cor3**2) / (n - 2))
print("kor. stvrtina 3:", cor3, "chyba:", standard_error3)
#
cor4 = np.corrcoef(diffPTS4_list, diffPTS_list)[0, 1]
standard_error4 = np.sqrt((1 - cor4**2) / (n - 2))
print("kor. stvrtina 4:", cor4, "chyba:", standard_error4)

# tabulka pravdepodobnosti
# pomocou metody max. vierohodnosti a odhadu parametrov
print("------------------------------")
print("pomocou odhadu parametrov")
t_1 = 0
t_2 = 1/4
t_3 = 1/2
t_4 = 3/4
t_5 = 9/10
l_1 = -5
l_2 = -3
l_3 = -1
l_4 = 0
l_5 = 1
l_6 = 3
l_7 = 5
l_8 = -7
l_9 = 7
drift = 9.491990846681922
sigma2 = 22.88329519450801 ** 2
# t = 0
a_1 = (l_4 + ((1-t_1)*drift))/math.sqrt((1-t_1)*sigma2)
# t = 1/4
a_2 = (l_1 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_3 = (l_2 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_4 = (l_3 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_5 = (l_4 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_6 = (l_5 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_7 = (l_6 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_8 = (l_7 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_30 = (l_8 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
a_31 = (l_9 + ((1-t_2)*drift))/math.sqrt((1-t_2)*sigma2)
# t = 1/2
a_9 = (l_1 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_10 = (l_2 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_11 = (l_3 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_12 = (l_4 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_13 = (l_5 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_14 = (l_6 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_15 = (l_7 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_32 = (l_8 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
a_33 = (l_9 + ((1-t_3)*drift))/math.sqrt((1-t_3)*sigma2)
# t = 3/4
a_16 = (l_1 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_17 = (l_2 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_18 = (l_3 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_19 = (l_4 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_20 = (l_5 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_21 = (l_6 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_22 = (l_7 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_34 = (l_8 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
a_35 = (l_9 + ((1-t_4)*drift))/math.sqrt((1-t_4)*sigma2)
# t = 9/10
a_23 = (l_1 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_24 = (l_2 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_25 = (l_3 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_26 = (l_4 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_27 = (l_5 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_28 = (l_6 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_29 = (l_7 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_36 = (l_8 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
a_37 = (l_9 + ((1-t_5)*drift))/math.sqrt((1-t_5)*sigma2)
print("mi = ", drift, "sigma na druhu =", sigma2)
print(norm.cdf(a_1, 0, 1), "cas nula, skore nula")
print(norm.cdf(a_2, 0, 1), "cas 1/4, skore -5")
print(norm.cdf(a_3, 0, 1), "cas 1/4, skore -3")
print(norm.cdf(a_4, 0, 1), "cas 1/4, skore -1")
print(norm.cdf(a_5, 0, 1), "cas 1/4, skore 0")
print(norm.cdf(a_6, 0, 1), "cas 1/4, skore +1")
print(norm.cdf(a_7, 0, 1), "cas 1/4, skore +3")
print(norm.cdf(a_8, 0, 1), "cas 1/4, skore +5")
print(norm.cdf(a_30, 0, 1), "cas 1/4, skore -7")
print(norm.cdf(a_31, 0, 1), "cas 1/4, skore +7")
print("....................")
print(norm.cdf(a_9, 0, 1), "cas 1/2, skore -5")
print(norm.cdf(a_10, 0, 1), "cas 1/2, skore -3")
print(norm.cdf(a_11, 0, 1), "cas 1/2, skore -1")
print(norm.cdf(a_12, 0, 1), "cas 1/2, skore 0")
print(norm.cdf(a_13, 0, 1), "cas 1/2, skore +1")
print(norm.cdf(a_14, 0, 1), "cas 1/2, skore +3")
print(norm.cdf(a_15, 0, 1), "cas 1/2, skore +5")
print(norm.cdf(a_32, 0, 1), "cas 1/2, skore -7")
print(norm.cdf(a_33, 0, 1), "cas 1/2, skore +7")
print("....................")
print(norm.cdf(a_16, 0, 1), "cas 3/4, skore -5")
print(norm.cdf(a_17, 0, 1), "cas 3/4, skore -3")
print(norm.cdf(a_18, 0, 1), "cas 3/4, skore -1")
print(norm.cdf(a_19, 0, 1), "cas 3/4, skore 0")
print(norm.cdf(a_20, 0, 1), "cas 3/4, skore +1")
print(norm.cdf(a_21, 0, 1), "cas 3/4, skore +3")
print(norm.cdf(a_22, 0, 1), "cas 3/4, skore +5")
print(norm.cdf(a_34, 0, 1), "cas 3/4, skore -7")
print(norm.cdf(a_35, 0, 1), "cas 3/4, skore +7")
print("....................")
print(norm.cdf(a_23, 0, 1), "cas 9/10, skore -5")
print(norm.cdf(a_24, 0, 1), "cas 9/10, skore -3")
print(norm.cdf(a_25, 0, 1), "cas 9/10, skore -1")
print(norm.cdf(a_26, 0, 1), "cas 9/10, skore 0")
print(norm.cdf(a_27, 0, 1), "cas 9/10, skore +1")
print(norm.cdf(a_28, 0, 1), "cas 9/10, skore +3")
print(norm.cdf(a_29, 0, 1), "cas 9/10, skore +5")
print(norm.cdf(a_36, 0, 1), "cas 9/10, skore -7")
print(norm.cdf(a_37, 0, 1), "cas 9/10, skore +7")
print("....................")