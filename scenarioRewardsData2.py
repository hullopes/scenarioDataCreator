import itertools
import csv

BSs = ['BS1','BS2']
UEs = ['UE1','UE2']
Lks = ['Lh','Lm','Nh','Nm']
wei = [5, 3, 2, 1]
cost_link =[4, 3, 4, 9]
cost_bs = [2, 2, 3, 3]

def getPoints(link):
    sp = link.split('-')
    return wei[Lks.index(sp[0])]

def getDisc(st):
    return 0

##Gerador de cenários para 2x2 com cada UE recebendo 1 melhor link de cada BS
##A saída é:
##[Lm-BS1;Nh-BS2][Nm-BS1;Nm-BS2]
##sendo o primeiro conjunto para o UE1, e o segundo para o UE2...



states = {}

for ue in UEs:
    states[ue] = ue
    states[ue] = []
    for bs in BSs:
        for lk in Lks:
            st = lk + "-" + bs
            states[ue].append(st)

lkbs = {}
for bs in BSs:
    lkbs[bs] = bs
    lkbs[bs] = []
    for lk in Lks:
        st = lk + "-" + bs
        lkbs[bs].append(st)

combLks = list(itertools.product(list(lkbs['BS1']),list(lkbs['BS2'])))
combStdBs = list(set(list(itertools.product(combLks,combLks))))
print(len(combStdBs))
with open('rewards2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for lb in combStdBs:
        st=''
        pt = 0
        for i in lb:
            stin = '['
            for z in i:
                stin = stin + z + ';'
                pt = pt + getPoints(z)
            stin = stin + "]"
            st = st + stin.replace(";]","]")
            pt = pt + getDisc(st)
        writer.writerow([st, pt])