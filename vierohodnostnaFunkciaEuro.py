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
teamRsltNum_list = [None] * 1148
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
        
        # rozdiel po kazdej stvrtine
        diffPTS1_list[i] = teamPTS1_list[i] - opptPTS1_list[i]
        diffPTS2_list[i] = teamPTS2_list[i] - opptPTS2_list[i]
        diffPTS3_list[i] = teamPTS3_list[i] - opptPTS3_list[i]
        diffPTS4_list[i] = teamPTS4_list[i] - opptPTS4_list[i]
        diffPTS_list[i] = teamMatchPTS_list[i] - opptMatchPTS_list[i]
        
        for i in range(1148):
            # teamRslt 1 ak win
            if (winner_list[i] == teamName_list[i]):
                teamRsltNum_list[i] = 1
            if (winner_list[i] == opptName_list[i]):
                teamRsltNum_list[i] = 0
print(sum(teamRsltNum_list), "suma")
print("----------------------------")

alfa = 0.0437
beta = 0.4147
f = 0
for i in range(1148):
    for j in range(3):
        L = ((norm.cdf(((alfa * diffPTS1_list[i] / (math.sqrt(1-((j+1)/4)))) + (beta * (math.sqrt(1-((j+1)/4))))), 0, 1))**(teamRsltNum_list[i]))*((1 - (norm.cdf(((alfa * diffPTS1_list[i] / (math.sqrt(1-((j+1)/4)))) + (beta * (math.sqrt(1-((j+1)/4))))), 0, 1)))**(1 - teamRsltNum_list[i])) 
        f = f + np.log(L)
print(f, "0.0437, 0.4147")

alfa = 0.0437
beta = 0.4148
f = 0
for i in range(1148):
    for j in range(3):
        L = ((norm.cdf(((alfa * diffPTS1_list[i] / (math.sqrt(1-((j+1)/4)))) + (beta * (math.sqrt(1-((j+1)/4))))), 0, 1))**(teamRsltNum_list[i]))*((1 - (norm.cdf(((alfa * diffPTS1_list[i] / (math.sqrt(1-((j+1)/4)))) + (beta * (math.sqrt(1-((j+1)/4))))), 0, 1)))**(1 - teamRsltNum_list[i])) 
        f = f + np.log(L)
print(f, "0.0437, 0.4148")

alfa = 0.0437
beta = 0.4149
f = 0
for i in range(1148):
    for j in range(3):
        L = ((norm.cdf(((alfa * diffPTS1_list[i] / (math.sqrt(1-((j+1)/4)))) + (beta * (math.sqrt(1-((j+1)/4))))), 0, 1))**(teamRsltNum_list[i]))*((1 - (norm.cdf(((alfa * diffPTS1_list[i] / (math.sqrt(1-((j+1)/4)))) + (beta * (math.sqrt(1-((j+1)/4))))), 0, 1)))**(1 - teamRsltNum_list[i])) 
        f = f + np.log(L)
print(f, "0.0437, 0.4149")

sigma = 1 / 0.0437
mi = 0.4148 * sigma
print("sigma:", sigma)
print("mí:", mi)
        

