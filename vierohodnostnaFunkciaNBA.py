import csv
import statistics
import math
from scipy.stats import norm
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

input_file = 'vysledky_final2.csv'


# Initialize lists for each category
teamAbbr_list = [None] * 1230
teamPTS_list = [None] * 1230
opptAbbr_list = [None] * 1230
opptPTS_list = [None] * 1230
teamRslt_list = [None] * 1230
teamRsltNum_list = [None] * 1230
teamLoc_list = [None] * 1230
teamPTS1_list = [None] * 1230
teamPTS2_list = [None] * 1230
teamPTS3_list = [None] * 1230
teamPTS4_list = [None] * 1230
teamPTS5_list = [None] * 1230
teamPTS6_list = [None] * 1230
teamPTS7_list = [None] * 1230
teamPTS8_list = [None] * 1230
opptPTS1_list = [None] * 1230
opptPTS2_list = [None] * 1230
opptPTS3_list = [None] * 1230
opptPTS4_list = [None] * 1230
opptPTS5_list = [None] * 1230
opptPTS6_list = [None] * 1230
opptPTS7_list = [None] * 1230
opptPTS8_list = [None] * 1230
# pocet bodov v riadnom hracom case
teamMatchPTS_list = [None] * 1230
opptMatchPTS_list = [None] * 1230
# bodovy rozdiel po i-tej stvrtine
diffPTS1_list = [None] * 1230
diffPTS2_list = [None] * 1230
diffPTS3_list = [None] * 1230
diffPTS4_list = [None] * 1230
diffPTS_list = [None] * 1230

    
with open(input_file, 'r') as infile:
    reader = csv.reader(infile)

    # Read the header row to get the column names
    header = next(reader)

    # Count the number of rows
    num_rows = len(list(reader))

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
        teamAbbr_list[i] = first_row[0]
        teamPTS_list[i] = int(first_row[1])
        opptAbbr_list[i] = first_row[2]
        opptPTS_list[i] = int(first_row[3])
        teamRslt_list[i] = first_row[4]
        teamLoc_list[i] = first_row[5]
        teamPTS1_list[i] = int(first_row[6])
        teamPTS2_list[i] = int(first_row[7])
        teamPTS3_list[i] = int(first_row[8])
        teamPTS4_list[i] = int(first_row[9])
        teamPTS5_list[i] = int(first_row[10])
        teamPTS6_list[i] = int(first_row[11])
        teamPTS7_list[i] = int(first_row[12])
        teamPTS8_list[i] = int(first_row[13])
        opptPTS1_list[i] = int(first_row[14])
        opptPTS2_list[i] = int(first_row[15])
        opptPTS3_list[i] = int(first_row[16])
        opptPTS4_list[i] = int(first_row[17])
        opptPTS5_list[i] = int(first_row[18])
        opptPTS6_list[i] = int(first_row[19])
        opptPTS7_list[i] = int(first_row[20])
        opptPTS8_list[i] = int(first_row[21])
        
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
        if teamRslt_list[i] == "Win":
            num_winsH = num_winsH + 1
        if teamRslt_list[i] == "Loss":
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
    
for i in range(1230):
    # teamRslt 1 ak win
    if (teamRslt_list[i] == "Win"):
        teamRsltNum_list[i] = 1
    if (teamRslt_list[i] == "Loss"):
        teamRsltNum_list[i] = 0
print(sum(teamRsltNum_list), "suma")
print("----------------------------")

alfa = 0.0377
beta = 0.2593
f = 0
for i in range(1230):
    for j in range(3):
        L = ((norm.cdf(((alfa * diffPTS1_list[i] / (math.sqrt(1-((j+1)/4)))) + (beta * (math.sqrt(1-((j+1)/4))))), 0, 1))**(teamRsltNum_list[i]))*((1 - (norm.cdf(((alfa * diffPTS1_list[i] / (math.sqrt(1-((j+1)/4)))) + (beta * (math.sqrt(1-((j+1)/4))))), 0, 1)))**(1 - teamRsltNum_list[i])) 
        f = f + np.log(L)
print(f, "0.0377, 0.2593")

alfa = 0.0377
beta = 0.2594
f = 0
for i in range(1230):
    for j in range(3):
        L = ((norm.cdf(((alfa * diffPTS1_list[i] / (math.sqrt(1-((j+1)/4)))) + (beta * (math.sqrt(1-((j+1)/4))))), 0, 1))**(teamRsltNum_list[i]))*((1 - (norm.cdf(((alfa * diffPTS1_list[i] / (math.sqrt(1-((j+1)/4)))) + (beta * (math.sqrt(1-((j+1)/4))))), 0, 1)))**(1 - teamRsltNum_list[i])) 
        f = f + np.log(L)
print(f, "0.0377, 0.2594")

alfa = 0.0377
beta = 0.2595
f = 0
for i in range(1230):
    for j in range(3):
        L = ((norm.cdf(((alfa * diffPTS1_list[i] / (math.sqrt(1-((j+1)/4)))) + (beta * (math.sqrt(1-((j+1)/4))))), 0, 1))**(teamRsltNum_list[i]))*((1 - (norm.cdf(((alfa * diffPTS1_list[i] / (math.sqrt(1-((j+1)/4)))) + (beta * (math.sqrt(1-((j+1)/4))))), 0, 1)))**(1 - teamRsltNum_list[i])) 
        f = f + np.log(L)
print(f, "0.0377, 0.2595")

sigma = 1 / 0.0377
mi = 0.2594 * sigma
print("sigma:", sigma)
print("mí:", mi)