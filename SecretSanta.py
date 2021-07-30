import random

santalist = open("List.txt","rt")
mainpool = []
dictmainpool = {}

bannedpair = {}

for line in santalist:
    mainpool.append(line.split()[0])
    dictmainpool[line.split()[0]] = len(mainpool)-1
    if(len(line.split()) > 1):
        bannedpair[len(mainpool)-1] = line.split()[1]

for ban in bannedpair:
    bannedpair[ban] =  dictmainpool[bannedpair[ban]]

temppool = list(range(len(mainpool)))
goodshuffle = False

while not(goodshuffle):
    random.shuffle(temppool)

    giftpair = []
    goodshuffle = True
    
    for x in range(len(temppool)):
        if x == (len(temppool)-1):
            pair = temppool[0]
        else:
            pair = temppool[x+1]

        if temppool[x] in bannedpair:
            if bannedpair[temppool[x]] == pair:
                goodshuffle = False
                
        pair = mainpool[temppool[x]] + ' ' + mainpool[pair]
        giftpair.append(pair)

for pair in giftpair:
    santa = pair.split()[0]
    child = pair.split()[1]
    temp_file = open(santa+".txt","w+")
    temp_file.write(child)
    temp_file.close()

santalist.close()
