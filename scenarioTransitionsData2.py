import csv
import random

Lks = ['Lh','Lm','Nh','Nm']
wei = [5, 3, 2, 1]

Reward = {}

def read_file():
    #read rewards file and save it to a variable
    with open('rewards2.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            Reward[row[0]] = float(row[1]) if row[1] != 'None' else None

read_file()

#print(Reward)
#print(len(Reward))

def sortS2(Reward):
    k = list(Reward.items())
    i = random.randint(0, len(Reward))
    print(i)
    num = k[i][0]
    print(num)

    return k[i][0]


def getAct(k3):
    bs = ''
    lk = ''
    act = '['
    if Lks.index(k3[0]) <= Lks.index(k3[2]):
        act = act + "("+k3[0]+"<-"+k3[1]+")"
        bs = k3[1]
        lk = k3[0]
    else:
        bs = k3[3]
        lk = k3[2]
        act = act + "("+k3[2]+"<-" + k3[3] + ")"

    if Lks.index(k3[4]) <= Lks.index(k3[6]):
        if k3[5] == bs and k3[4] == lk:
            act = act + "("+k3[6]+"<-" + k3[7] + ")"
        else:
            act = act + "("+k3[4]+"<-" + k3[5] + ")"
    else:
        if k3[7] == bs and k3[6] == lk:
            act = act + "("+k3[4]+"<-" + k3[5] + ")"
        else:
            act = act + "("+k3[6]+"<-" + k3[7] + ")"

    return act + ']'


with open('transitions2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for k, v in Reward.items():
        #print("Code : {0}, Value : {1}".format(k, v))
        #getting link, bs and ue
        k2 = k.replace("][", "-")
        k2=k2.replace("[", "")
        k2=k2.replace("]","")
        k2 = k2.replace(";", "-")
        k3 = k2.split('-')
        s1 = k
        act = getAct(k3)
        #act = "[(" + k3[0] + "->" + k3[1] + "<-" + k3[2] + ")-(" + k3[3] + "->" + k3[4] + "<-" + k3[5] + ")]"
        s2 = k
        p=0.0
        if v >= 7.0:
            p=0.8
        elif v < 7.0 and v >= 5.0:
            p=0.5
        elif v < 5.0 and v >= 1.2:
            p=0.2
        else:
            p=0.1
        #print(st)
        writer.writerow([s1, act, s2, p])
        #generating n aleatory s2 output
        n=5
        sort_s2 = sortS2(Reward)
        writer.writerow([s1, act, sort_s2, 0.1])