# scenarioDataCreator
Python data creator for MDP algorithm

##
Used to create csv files for MDP

### Parameters:
 #####-Basestations
```
BSs = ['BS1','BS2']
```
#####-User Equipments
```
UEs = ['UE1','UE2']
```
#####-Tipe of links, i.e., the quality of the alingned beans
```
Lks = ['Lh','Lm','Nh','Nm']
```
  - Lh: LOS_high
  - Lm: LOS_medium
  - Nh: nLOS_high
  - Nm: nLOS_medium
#####-The weight of the link reward
```
wei = [5, 3, 2, 1]
```
#####-Cost over same BS-Link allocation
```
cost_link =[4, 3, 4, 9]
```
#####-Cost over same BS allocation (with different links/beams)
```
cost_bs = [2, 2, 3, 3]
```


