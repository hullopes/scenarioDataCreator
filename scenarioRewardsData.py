import itertools
import csv

BSs = ['BS1','BS2']
UEs = ['UE1','UE2']
Lks = ['Lh','Lm','Nh','Nm']
hei = [5, 3, 2, 1]
custo_link =[4, 3, 4, 9]
custo_bs = [2, 2, 3, 3]

states = {}

for ue in UEs:
    states[ue] = ue
    states[ue] = []
    for bs in BSs:
        for lk in Lks:
            st = ue + "-" + lk + "-" + bs
            states[ue].append(st)

lista = list(itertools.product(states['UE1'],states['UE2']))

print(lista)

print(len(lista))

lista2 = list(set(lista))
print(len(lista2))


def getPoints(item):
    points =0;
    elks = []
    ebs = []
    for i in item:
        lk = i[4:6]
        bs = i[7:10]
        points = points + hei[Lks.index(lk)]
        if lk in elks and bs in ebs:
            points = points - custo_link[Lks.index(lk)]
        else:
            if bs in ebs:
                points = points - custo_bs[Lks.index(lk)]
        elks.append(lk)
        ebs.append(bs)
    return points


with open('rewards.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    cont = 1
    for i in lista:
        st=''
        pt = getPoints(i)
        for y in i:
            sti="("+y+")"
            if st != sti:
                st = st+sti
        writer.writerow([st, pt])
        cont=cont+1

