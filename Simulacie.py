import numpy as np
import random

def simulacia_hokejoveho_zapasu(stav, lmbda, k, t):
    cas = 0
    while True:
        # Generovanie času do ďalšieho gólu pomocou Weibullovho rozdelenia
        cas_do_golu = np.random.weibull(k) * lmbda
        
        # Aktualizácia času
        cas = cas + cas_do_golu
        
        # Ak je čas väčší ako limit t, končíme simuláciu
        if (cas >= t):
            #print("Časový limit bol dosiahnutý.")
            return(stav)
        
        # Výber tímu, ktorý skóroval
        pH = 0.52
        pA = 1 - pH
        tim = random.choices(['A', 'H'], weights=[pA, pH])[0]
        if (tim == "A"):
            stav = stav - 1
        if (tim == "H"):
            stav = stav + 1
        
        # Výpis gólu a času
        #print(f"Čas: {cas:.2f}, Gol: {tim}, Stav: {stav}")
        
        # Zmena parametrov
        if (np.abs(stav) >= 4):
            lmbda = lmbda4
            k = k4
        if (np.abs(stav) == 3):
            lmbda = lmbda3
            k = k3
        if (np.abs(stav) == 2):
            lmbda = lmbda2
            k = k2
        if (np.abs(stav) == 1):
            lmbda = lmbda1
            k = k1
        if (stav == 0):
            lmbda = lmbda0
            k = k0
            
        
# Parametre simulácie
lmbda0 = 663.5 # Parameter lambda pre Weibullovo rozdelenie
lmbda1 = 572.8
lmbda2 = 522.4
lmbda3 = 463.2
lmbda4 = 453.6
k4 = 1.1856       # Parameter k pre Weibullovo rozdelenie
k3 = 1.1177
k2 = 1.0772
k1 = 1.1115
k0 = 1.0691
t1 = 3480         # Časový limit v minútach
t2 = 3360           #4. minúta zápasu
t3 = 3240           #6min
t4 = 3120           #8min
t5 = 3000           #10min
t6 = 2880           #12min
t7 = 2880           #14min
t8 = 2640           #16min
t9 = 2520           #18min
t10 = 2400          #20min
t11 = 2280          #22min
t12 = 2160          #24min
t13 = 2040          #26min
t14 = 1920          #28min
t15 = 1800          #30min
t16 = 1680          #32min
t17 = 1560          #34min
t18 = 1440          #36min
t19 = 1320          #38min
t20 = 1200          #40min
t21 = 1080          #42min
t22 = 960           #44min
t23 = 840           #46min
t24 = 720           #48min
t25 = 600           #50min
t26 = 480           #52min
t27 = 360           #54min
t28 = 240           #56min
t29 = 120           #58min

def spustenie_simulacie(stav, cas, k, lmbda):
    # Spustenie simulácie
    wins = 0
    draws = 0
    losses = 0
    for i in range (10000):
        vysledok = simulacia_hokejoveho_zapasu(stav, lmbda, k, cas)
        if vysledok < 0:
            losses = losses + 1
        elif vysledok == 0:
            draws = draws + 1
        elif vysledok > 0:
            wins = wins + 1
        #print(f"Výsledok simulácie {i+1}: {wins} - {draws} - {losses}")
    print(f"Čas: {cas} Stav: {stav}")
    print(wins, " - ", draws, " - ", losses)

#for i in range(1, 30):
    #print(f"spustenie_simulacie(-2, t{i}, k2, lmbda2)")

spustenie_simulacie(-2, t1, k2, lmbda2)
spustenie_simulacie(-2, t2, k2, lmbda2)
spustenie_simulacie(-2, t3, k2, lmbda2)
spustenie_simulacie(-2, t4, k2, lmbda2)
spustenie_simulacie(-2, t5, k2, lmbda2)
spustenie_simulacie(-2, t6, k2, lmbda2)
spustenie_simulacie(-2, t7, k2, lmbda2)
spustenie_simulacie(-2, t8, k2, lmbda2)
spustenie_simulacie(-2, t9, k2, lmbda2)
spustenie_simulacie(-2, t10, k2, lmbda2)
spustenie_simulacie(-2, t11, k2, lmbda2)
spustenie_simulacie(-2, t12, k2, lmbda2)
spustenie_simulacie(-2, t13, k2, lmbda2)
spustenie_simulacie(-2, t14, k2, lmbda2)
spustenie_simulacie(-2, t15, k2, lmbda2)
spustenie_simulacie(-2, t16, k2, lmbda2)
spustenie_simulacie(-2, t17, k2, lmbda2)
spustenie_simulacie(-2, t18, k2, lmbda2)
spustenie_simulacie(-2, t19, k2, lmbda2)
spustenie_simulacie(-2, t20, k2, lmbda2)
spustenie_simulacie(-2, t21, k2, lmbda2)
spustenie_simulacie(-2, t22, k2, lmbda2)
spustenie_simulacie(-2, t23, k2, lmbda2)
spustenie_simulacie(-2, t24, k2, lmbda2)
spustenie_simulacie(-2, t25, k2, lmbda2)
spustenie_simulacie(-2, t26, k2, lmbda2)
spustenie_simulacie(-2, t27, k2, lmbda2)
spustenie_simulacie(-2, t28, k2, lmbda2)
spustenie_simulacie(-2, t29, k2, lmbda2)
