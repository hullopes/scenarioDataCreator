import itertools
import csv

Reward = {}

def read_file():
    #read rewards file and save it to a variable
    with open('rewards.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            Reward[row[0]] = float(row[1]) if row[1] != 'None' else None

read_file()

#print(Reward)
#print(len(Reward))
with open('transitions.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for k, v in Reward.items():
        #print("Code : {0}, Value : {1}".format(k, v))
        #getting link, bs and ue
        k2 = k.replace(")(", "-")
        k2=k2.replace("(", "")
        k2=k2.replace(")","")
        k3 = k2.split('-')
        s1 = k
        act = "[(" + k3[0] + "->" + k3[1] + "<-" + k3[2] + ")-(" + k3[3] + "->" + k3[4] + "<-" + k3[5] + ")]"
        s2 = k
        p=0.0
        if v >= 7.0:
            #st=st+",[("+k3[0]+"->"+k3[1]+"<-"+k3[2]+")-("+k3[3]+"->"+k3[4]+"<-"+k3[5]+")]"
            #st=st+","+k+",0.8"
            p=0.8
        elif v < 7.0 and v >= 5.0:
            #st = st + ",[(" + k3[0] + "->" + k3[1] + "<-" + k3[2] + ")-(" + k3[3] + "->" + k3[4] + "<-" + k3[5] + ")]"
            #st = st + "," + k + ",0.5"
            p=0.5
        elif v < 5.0 and v >= 1.2:
            #st = st + ",[(" + k3[0] + "->" + k3[1] + "<-" + k3[2] + ")-(" + k3[3] + "->" + k3[4] + "<-" + k3[5] + ")]"
            #st = st + "," + k + ",0.2"
            p=0.2
        else:
            #st = st + ",[(" + k3[0] + "->" + k3[1] + "<-" + k3[2] + ")-(" + k3[3] + "->" + k3[4] + "<-" + k3[5] + ")]"
            #st = st + "," + k + ",0.1"
            p=0.1
        #print(st)
        writer.writerow([s1, act, s2, p])