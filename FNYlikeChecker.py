#from z3 import * 
import random
#import itertools 

def createGSO():

    lsModel=[random.choice([0,1]) for i in range(55)]
    return lsModel

def createSUSYGSO():
    lsModel=[2 for i in range(55)]
    susyphases=[0,10,11,12,13,14,15,16,17,18]
    for i in range(55):
        if i in susyphases:
            lsModel[i]=1
        else:
            lsModel[i]=random.choice([0,1])
            
    return lsModel

#implement SUSY
def checkNotSUSY(c):
    NonSUSY=False
    if c[10]+c[11]+c[12]+c[16]+c[17]+c[18]<6:
        NonSUSY=True
    return NonSUSY

def checkSUSY(c):
    Susy=False
    if c[0]==True and c[10]==True and c[11]==True and c[12]==True and c[13]==True and c[14]==True and c[15]==True and c[16]==True and c[17]==True and c[18]==True:
        Susy=True
    return Susy

def Gens3(c):
    n10s=0
    n10bar=0
    n5s=0
    n5bar=0
    #B1_pqrs projectors
    #pqrs=0000
    if c[21]==1 and c[42]==1 and (c[40]+c[41]+c[42])%2==1 and c[43]==1:
        if c[40]==1 and c[44]==1:#chirality phase (b1)(b2)
            n10s+=1
            #print("n10 from b1")
        elif c[40]==1 and c[44]==0:
            n5bar+=1
            #print("n5bar from b1")
        elif c[40]==0 and c[44]==1:
            n10bar+=1
            #print("n10bar from b1")
        elif c[40]==0 and c[44]==0:
            n5s+=1
            #print("n5 from b1")
    
    #0010
    if (c[21]+c[20])%2==1 and (c[42]+c[37])%2==1 and (c[40]+c[41]+c[42]+c[3]+c[34]+c[35]+c[36]+c[37])%2==1 and (c[43]+c[38])%2==1:

        if (1+c[40]+c[34]+c[35]+c[3])%2==1 and (c[44]+c[39])%2==1: #chirality phase (b1+e5)(b2+e5)
            n10s+=1
            #print("n10 from b1+e5")
        elif (1+c[40]+c[34]+c[35]+c[3])%2==1 and (c[44]+c[39])%2==0:
            n5bar+=1
            #print("n5bar from b1+e5")
        elif (1+c[40]+c[34]+c[35]+c[3])%2==0 and (c[44]+c[39])%2==1: 
            n10bar+=1
            #print("n10bar from b1+e5")
        elif (1+c[40]+c[34]+c[35]+c[3])%2==0 and (c[44]+c[39])%2==0:
            n5s+=1
            #print("n5 from b1+e5")

    #0100
    if (c[21]+c[19])%2==1 and (c[42]+c[31])%2==1 and (c[40]+c[41]+c[42]+c[2]+c[28]+c[29]+c[30]+c[31])%2==1 and (c[43]+c[32])%2==1:
        if (1+c[40]+c[29])%2==1 and (c[44]+c[33])%2==1: #chirality phase (b1+e4)(b2)
            n10s+=1
            #print("n10 from b1+e4")
        elif (1+c[40]+c[29])%2==1 and (c[44]+c[33])%2==0:
            n5bar+=1
            #print("n5bar from b1+e4")
        elif (1+c[40]+c[29])%2==0 and (c[44]+c[33])%2==1:
            n10bar+=1
            #print("n10bar from b1+e4")
        elif (1+c[40]+c[29])%2==0 and (c[44]+c[33])%2==0:
            n5s+=1
            #print("n5 from b1+e4")

    #0110
    if (c[21]+c[19]+c[20])%2==1 and (c[42]+c[31]+c[37])%2==1 and \
        (c[40]+c[41]+c[42]+c[2]+c[3]+c[28]+c[29]+c[30]+c[31]+c[34]+c[35]+c[36]+c[37])%2==1 and (c[43]+c[32]+c[38])%2==1:
        if (1+c[40]+c[29]+c[3]+c[34]+c[35])%2==1 and (c[44]+c[33]+c[39])%2==1: #chirality phase (b1+e4+e5)(b2+e5)
            n10s+=1
            #print("n10 from b1+e4+e5")
        elif (1+c[40]+c[29]+c[3]+c[34]+c[35])%2==1 and (c[44]+c[33]+c[39])%2==0:
            n5bar+=1
            #print("n5bar from b1+e4+e5")
        elif (1+c[40]+c[29]+c[3]+c[34]+c[35])%2==0 and (c[44]+c[33]+c[39])%2==1:
            n10bar+=1
            #print("n10bar from b1+e4+e5")
        elif (1+c[40]+c[29]+c[3]+c[34]+c[35])%2==0 and (c[44]+c[33]+c[39])%2==0:
            n5s+=1
            #print("n5 from b1+e4+e5")

    #B2
    #pqrs=0000
    if c[29]==1 and c[46]==1 and (c[40]+c[45]+c[46])%2==1 and c[47]==1:
        if c[40]==1 and c[48]==1:#chirality phase (b1)(b2)
            n10s+=1
            #print("n10 from b2")
        elif c[40]==1 and c[48]==0:
            n5bar+=1
            #print("n5bar from b2")
        elif c[40]==0 and c[48]==1:
            n10bar+=1
            #print("n10bar from b2")
        elif c[40]==0 and c[48]==0:
            n5s+=1
            #print("n5 from b2")

    #c[48] b2g
    #0010
    if (c[29]+c[27])%2==1 and (c[46]+c[37])%2==1 and (c[40]+c[45]+c[46]+c[3]+c[34]+c[35]+c[36]+c[37])%2==1 and (c[47]+c[38])%2==1:
        if (1+c[40]+c[34]+c[35]+c[3])%2==1 and (c[48]+c[39])%2==1: #chirality phase (b2+e5)(b1+e5)
            n10s+=1
            #print("n10 from b2+e5")
        elif (1+c[40]+c[34]+c[35]+c[3])%2==1 and (c[48]+c[39])%2==0:
            n5bar+=1
            #print("n5bar from b2+e5")
        elif (1+c[40]+c[34]+c[35]+c[3])%2==0 and (c[48]+c[39])%2==1:
            n10bar+=1
            #print("n10bar from b2+e5")
        elif (1+c[40]+c[34]+c[35]+c[3])%2==0 and (c[48]+c[39])%2==0:
            n5s+=1
            #print("n5 from b2+e5")

    #0100
    if (c[29]+c[19])%2==1 and (c[46]+c[24])%2==1 and (c[40]+c[45]+c[46]+c[1]+c[21]+c[22]+c[23]+c[24])%2==1 and (c[47]+c[25])%2==1:
        if (1+c[40]+c[21])%2==1 and (c[48]+c[26])%2==1: #chirality phase (b2+e2)(b1)
            n10s+=1
            #print("n10 from b2+e2")
        elif (1+c[40]+c[21])%2==1 and (c[48]+c[26])%2==0:
            n5bar+=1
            #print("n5bar from b2+e2")
        elif (1+c[40]+c[21])%2==0 and (c[48]+c[26])%2==1:
            n10bar+=1
            #print("n10bar from b2+e2")
        elif (1+c[40]+c[21])%2==0 and (c[48]+c[26])%2==0:
            n5s+=1
            #print("n5 from b2+e2")

    #0110
    if (c[29]+c[19]+c[27])%2==1 and (c[46]+c[24]+c[37])%2==1 and \
        (c[40]+c[45]+c[46]+c[1]+c[3]+c[21]+c[22]+c[23]+c[24]+c[34]+c[35]+c[36]+c[37])%2==1 and (c[47]+c[25]+c[38])%2==1:
        if (1+c[40]+c[21]+c[3]+c[20]+c[34]+c[35])%2==1 and (c[48]+c[26]+c[39])%2==1: #chirality phase (b2+e2+e5)(b1+e5)
            n10s+=1
            #print("n10 from b2+e2+e5")
        elif (1+c[40]+c[21]+c[3]+c[20]+c[34]+c[35])%2 and (c[48]+c[26]+c[39])%2==0:
            n5bar+=1
            #print("n5bar from b2+e2+e5")
        elif (1+c[40]+c[21]+c[3]+c[20]+c[34]+c[35])%2==0 and (c[48]+c[26]+c[39])%2==1:
            n10bar+=1
            #print("n10bar from b2+e2+e5")
        elif (1+c[40]+c[21]+c[3]+c[20]+c[34]+c[35])%2==0 and (c[48]+c[26]+c[39])%2==0:
            n5s+=1
            #print("n5 from b2+e2+e5")

    # define 4 B3 projectors 

    #pqrs=0000
    if c[36]==1 and c[49]==1 and (c[41]+c[45]+c[49])%2==1 and c[50]==1:

        if c[41]==1 and c[51]==1: #chirality phase (b1)(b3)
            n10s+=1
            #print("n10 from b3")
        elif c[41]==1 and c[51]==0:
            n5bar+=1
            #print("n5bar from b3")
        elif c[41]==0 and c[51]==1:
            n10bar+=1
            #print("n10bar from b3")
        elif c[41]==0 and c[51]==0:
            n5s+=1
            #print("n5 from b3")

    #c[51] b3g
    #0001
    if (c[36]+c[27])%2==1 and (c[49]+c[37])%2==1 and (c[41]+c[45]+c[49]+c[2]+c[28]+c[29]+c[30]+c[31])%2==1 and (c[50]+c[32])%2==1:
        if (1+c[41]+c[2]+c[30]+c[28])%2==1 and (c[51]+c[33])%2==1: #chirality phase (b3+e4)(b1+e4)
            n10s+=1
            #print("n10 from b3+e4")
        elif (1+c[41]+c[2]+c[30]+c[28])%2==1 and (c[51]+c[33])%2==0:
            n5bar+=1
            #print("n5bar from b3+e4")
        elif (1+c[41]+c[2]+c[30]+c[28])%2==0 and (c[51]+c[33])%2==1:
            n10bar+=1
            #print("n10bar from b3+e4")
        elif (1+c[41]+c[2]+c[30]+c[28])%2==0 and (c[51]+c[33])%2==0:
            n5s+=1
            #print("n5 from b3+e4")

    #0100
    if (c[36]+c[20])%2==1 and (c[49]+c[24])%2==1 and (c[41]+c[45]+c[49]+c[1]+c[21]+c[22]+c[23]+c[24])%2==1 and (c[50]+c[25])%2==1:

        if (1+c[41]+c[21])%2==1 and (c[51]+c[26])%2==1: #chirality phase (b3+e2)(b1)
            n10s+=1
            #print("n10 from b3+e2")
        elif (1+c[41]+c[21])%2==1 and (c[51]+c[26])%2==0:
            n5bar+=1
            #print("n5bar from b3+e2")
        elif (1+c[41]+c[21])%2==0 and (c[51]+c[26])%2==1:
            n10bar+=1
            #print("n10bar from b3+e2")
        elif (1+c[41]+c[21])%2==0 and (c[51]+c[26])%2==0:
            n5s+=1
            #print("n5 from b3+e2")

    #0101
    if (c[36]+c[20]+c[27])%2==1 and (c[49]+c[24]+c[37])%2==1 and \
        (c[41]+c[45]+c[49]+c[2]+c[1]+c[28]+c[29]+c[30]+c[31]+c[21]+c[22]+c[23]+c[24])%2==1 and (c[50]+c[25]+c[32])%2==1:
        if (1+c[41]+c[21]+c[28]+c[30]+c[2]+c[19])%2==1 and (c[51]+c[26]+c[33])%2==1: #chirality phase (b3+e2+e4)(b1+e4)
            n10s+=1
            #print("n10 from b3+e2+e4")
        elif (1+c[41]+c[21]+c[28]+c[30]+c[2]+c[19])%2==1 and (c[51]+c[26]+c[33])%2==0:
            n5bar+=1
            #print("n5bar from b3+e2+e4")
        elif (1+c[41]+c[21]+c[28]+c[30]+c[2]+c[19])%2==0 and (c[51]+c[26]+c[33])%2==1:
            n10bar+=1
            #print("n10bar from b3+e2+e4")
        elif (1+c[41]+c[21]+c[28]+c[30]+c[2]+c[19])%2==0 and (c[51]+c[26]+c[33])%2==0:
            n5s+=1
            #print("n5 from b3+e2+e4")

    return [n10s,n5bar,n10bar,n5s]

def vects(c):
    NHs=0
    v5=0
    v5bar=0
    #VECTORIALS V1_pqrs projectors
    #pqrs=0000

    if (1+c[10]+c[21]+c[25])%2==1 and (1+c[16]+c[42]+c[52])%2==1 and (1 + c[0]+c[13]+c[14]+c[15]+c[16]+\
        c[40]+c[41]+c[42]+c[8]+c[43]+c[47]+c[50]+c[52])%2==1 and (1+c[17]+c[43]+c[8])%2==0:
        if (1+c[14]+c[40]+c[47])%2==1 and (c[18]+c[44]+c[54])%2==1:#chirality phase (S+b1+x)(b2):
            v5+=1
        elif (1+c[14]+c[40]+c[47])%2==1 and (c[18]+c[44]+c[54])%2==0:
            v5bar+=1

    #0010
    if (1+c[10]+c[21]+c[25]+c[20])%2==1 and (1+c[16]+c[42]+c[52]+c[37])%2==1 and (1+ c[0]+c[13]+c[14]+c[15]+c[16]+\
        c[40]+c[41]+c[42]+c[8]+c[43]+c[47]+c[50]+c[52]+c[3]+c[34]+c[35]+c[36]+c[37])%2==1 \
            and (1+c[17]+c[43]+c[8]+c[38])%2==0:

        if (1+c[14]+c[40]+c[47]+c[35]+c[12]+c[34]+c[38]+c[3])%2==1 and (c[18]+c[44]+c[54]+c[39])%2==1:#chirality phase (S+b1+x+e5)(b2+e5)
            v5+=1
        if (1+c[14]+c[40]+c[47]+c[35]+c[12]+c[34]+c[38]+c[3])%2==1 and (c[18]+c[44]+c[54]+c[39])%2==0:
            v5bar+=1

    #0100
    if (1+c[10]+c[21]+c[25]+c[19])%2==1 and (1+c[16]+c[42]+c[52]+c[31])%2==1 and \
        (1+ c[0]+c[13]+c[14]+c[15]+c[16]+c[40]+c[41]+c[42]+c[8]+c[43]+c[47]+c[50]+c[52]+c[2]+c[28]+c[29]+c[30]+c[31])%2==1 and \
            (1+c[17]+c[43]+c[8]+c[32])%2==0:

        if (1+c[14]+c[40]+c[47]+c[29])%2==1 and (c[18]+c[44]+c[54]+c[33])%2==1:#chirality phase (S+b1+x+e5)(b2+e5)
            v5+=1
        if (1+c[14]+c[40]+c[47]+c[29])%2==1 and (c[18]+c[44]+c[54]+c[33])%2==0:
            v5bar+=1

    #0110
    if (1+c[10]+c[21]+c[25]+c[20]+c[19])%2==1 and (1+c[16]+c[42]+c[52]+c[31]+c[37])%2==1 and \
        (1+ c[0]+c[13]+c[14]+c[15]+c[16]+c[40]+c[41]+c[42]+c[8]+c[43]+c[47]+c[50]+c[52]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2==1 and \
        (1+c[17]+c[43]+c[8]+c[38]+c[32])%2==0:

        if (c[14]+c[40]+c[47]+c[24]+c[35]+c[12]+c[34]+c[38]+c[27]+c[3])%2==1 and (c[18]+c[44]+c[54]+c[39])%2==1:#chirality phase (S+b1+x+e5)(b2+e5)
            v5+=1
        if (c[14]+c[40]+c[47]+c[24]+c[35]+c[12]+c[34]+c[38]+c[27]+c[3])%2==1 and (c[18]+c[44]+c[54]+c[33]+c[39])%2==0:
            v5bar+=1


    #V2
    #pqrs=0000
    if (1+c[11]+c[29]+c[32])%2==1 and (1+c[16]+c[46]+c[52])%2==1 and (1+ c[0]+c[13]+c[14]+c[15]+c[16]+\
        c[40]+c[45]+c[46]+c[8]+c[43]+c[47]+c[50]+c[52])%2==1 and (c[17]+c[47]+c[8])%2==0:

        if (1+c[13]+c[40]+c[43])%2==1 and (c[18]+c[48]+c[54])%2==1:
            v5+=1
        if (1+c[13]+c[40]+c[43])%2==1 and (1+c[18]+c[48]+c[54])%2==1:
            v5bar+=1

    #V2_0000_16=And(000,c[40])#chirality phase (b1)(b2)

    #0010
    if (1+c[11]+c[29]+c[32]+c[27])%2==1 and (1+c[16]+c[46]+c[52]+c[37])%2==1 and (1+ c[0]+c[13]+c[14]+c[15]+c[16]+\
        c[40]+c[45]+c[46]+c[8]+c[43]+c[47]+c[50]+c[52]+c[3]+c[34]+c[35]+c[36]+c[37])%2==1 and (c[17]+c[47]+c[8]+c[38])%2==0:

        if (1+c[13]+c[40]+c[43]+c[34]+c[12]+c[35]+c[38]+c[3])%2==1 and (c[18]+c[48]+c[54]+c[39])%2==1:
            v5+=1
        if (1+c[13]+c[40]+c[43]+c[34]+c[12]+c[35]+c[38]+c[3])%2==1 and (1+c[18]+c[48]+c[54]+c[39])%2==1:
            v5bar+=1

    #0100
    if (1+c[11]+c[29]+c[32]+c[19])%2==1 and (1+c[16]+c[46]+c[52]+c[24])%2==1 and (1+ c[0]+c[13]+c[14]+c[15]+c[16]+\
        c[40]+c[45]+c[46]+c[8]+c[43]+c[47]+c[50]+c[52]+c[1]+c[21]+c[22]+c[23]+c[24])%2==1 and (c[17]+c[47]+c[8]+c[25])%2==0:

        if (1+c[13]+c[40]+c[43]+c[21])%2==1 and (c[18]+c[48]+c[54]+c[26])%2==1:
            v5+=1
        if (1+c[13]+c[40]+c[43]+c[21])%2==1 and (1+c[18]+c[48]+c[54]+c[26])%2==1:
            v5bar+=1

    #0110
    if (1+c[11]+c[29]+c[32]+c[19]+c[27])%2==1 and (c[46]+c[52]+c[24]+c[37])%2==1 and \
        (c[40]+c[45]+c[46]+c[8]+c[43]+c[47]+c[50]+c[52]+c[2]+c[3]+c[28]+c[29]+c[30]+c[31]+c[34]+c[35]+c[36]+c[37])%2==1 and \
            (c[47]+c[8]+c[25]+c[38])%2==0:


        if (c[13]+c[40]+c[43]+c[21]+c[34]+c[12]+c[35]+c[38]+c[3]+c[20])%2==1 and (c[18]+c[48]+c[54]+c[26]+c[39])==1:
            v5+=1
        if (c[13]+c[40]+c[43]+c[21]+c[34]+c[12]+c[35]+c[38]+c[3]+c[20])%2==1 and (1+c[18]+c[48]+c[54]+c[26]+c[39])==1:
            v5bar+=1

    # define 4 V3 projectors 

    #pqrs=0000
    if (1+c[12]+c[36]+c[38])%2==1 and (1+c[16]+c[49]+c[52])%2==1 and (c[0]+c[13]+c[14]+c[15]+c[16]+\
        c[41]+c[45]+c[49]+c[8]+c[43]+c[47]+c[50]+c[52])%2==1 and (1+c[17]+c[50]+c[8])%2==0:

        if (1+c[13]+c[41]+c[43])%2==1 and (1+c[18]+c[51]+c[54])%2==1:
            v5+=1
        if (1+c[13]+c[41]+c[43])%2==1 and (c[18]+c[51]+c[54])%2==1:
            v5bar+=1

    #0001
    if (1+c[12]+c[36]+c[38]+c[27])%2==1 and (1+c[16]+c[49]+c[52]+c[37])%2==1 and (c[0]+c[13]+c[14]+c[15]+c[16]+\
        c[41]+c[45]+c[49]+c[8]+c[43]+c[47]+c[50]+c[52]+c[2]+c[28]+c[29]+c[30]+c[31])%2==1 and (1+c[17]+c[50]+c[8]+c[32])%2==0:

        if (1+c[13]+c[41]+c[43]+c[28]+c[11]+c[30]+c[32]+c[2])%2==1 and (1+c[18]+c[51]+c[54]+c[33])%2==1:
            v5+=1
        if (1+c[13]+c[41]+c[43]+c[28]+c[11]+c[30]+c[32]+c[2])%2==1 and (c[18]+c[51]+c[54]+c[33])%2==1:
            v5bar+=1

    #0100
    if (1+c[12]+c[36]+c[38]+c[19])%2==1 and (1+c[16]+c[49]+c[52]+c[24])%2==1 and (c[0]+c[13]+c[14]+c[15]+c[16]+\
        c[41]+c[45]+c[49]+c[8]+c[43]+c[47]+c[50]+c[52]+c[1]+c[21]+c[22]+c[23]+c[24])%2==1 and (1+c[17]+c[50]+c[8]+c[25])%2==1:

        if (1+c[13]+c[41]+c[43]+c[21])%2==1 and (1+c[18]+c[51]+c[54]+c[26])%2==1:
            v5+=1
        if (1+c[13]+c[41]+c[43]+c[21])%2==1 and (c[18]+c[51]+c[54]+c[26])%2==1:
            v5bar+=1

    #0101
    

    if (1+c[12]+c[36]+c[38]+c[19]+c[27])%2==1 and (1+c[16]+c[49]+c[52]+c[24]+c[37])%2==1 and (c[0]+c[13]+c[14]+c[15]+c[16]+\
        c[41]+c[45]+c[49]+c[8]+c[43]+c[47]+c[50]+c[52]+c[1]+c[21]+c[22]+c[23]+c[24]+\
        c[2]+c[28]+c[29]+c[30]+c[31])%2==1 and (1+c[17]+c[50]+c[8]+c[25]+c[32])%2==0:

        if (1+c[13]+c[41]+c[43]+c[21]+c[28]+c[11]+c[30]+c[32]+c[2])%2==1 and (1+c[18]+c[51]+c[54]+c[26]+c[33])%2==1:
            v5+=1
        if (1+c[13]+c[41]+c[43]+c[21]+c[28]+c[11]+c[30]+c[32]+c[19]+c[2])%2==1 and (c[18]+c[51]+c[54]+c[26]+c[33])%2==1:
            v5bar+=1

    return [v5,v5bar]          


#TACHYONS
def tachs(c):
    tachy=False
    #Vectorials
    #e2 { }, projs: S,e4,e5,z1,z2,x,b1,g,
    #y1w6  oscillator case
    if c[10]==0 and c[19]==0 and c[20]==0 and c[24]==0 and (c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and c[25]==0 and c[21]==0 and c[26]==1:
        tachy=True 
        #print("e2 y1w6 tach")
    #w1w3,...
    if c[10]==0 and c[19]==0 and c[20]==0 and c[24]==0 and (c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and c[25]==0 and c[21]==0 and c[26]==0:
        tachy=True 
        #print("e2 w1w3 tach")
    #y3y6
    if c[10]==0 and c[19]==0 and c[20]==0 and c[24]==0 and (c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and c[25]==0 and c[21]==1 and c[26]==0:
        tachy=True 
        #print("e2 y3y6 tach")
    #ybar4...
    if c[10]==0 and c[19]==1 and c[20]==0 and c[24]==0 and (c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and c[25]==0 and c[21]==1 and c[26]==0:
        tachy=True 
        #print("e2 ybar4 tach")
    #y5...
    if c[10]==0 and c[19]==0 and c[20]==1 and c[24]==0 and (c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and c[25]==0 and c[21]==1 and c[26]==0:
        tachy=True 
        #print("e2 y5 tach")

    #y6w6e2=And(c[19])%2 and c[20])%2 and c[24])%2 and (c[1]+c[21]+c[22]+c[23]+c[24])%2 and c[25])%2 and c[21]+c[26])
    #psi,eta1
    #psie2=And(c[10])%2 and c[19])%2 and c[20])%2 and c[24])%2 and (c[1]+c[21]+c[22]+c[23]+c[24])%2 and c[25]+c[21]+c[26])
    #eta23
    #eta23e2=And(c[10])%2 and c[19])%2 and c[20])%2 and c[24])%2 and (c[1]+c[21]+c[22]+c[23]+c[24])%2 and c[25]+c[21])%2 and c[26])
    #phi12
    #phi1e2=And(c[10])%2 and c[19])%2 and c[20])%2 and c[24]+(c[1]+c[21]+c[22]+c[23]+c[24])%2 and c[25])%2 and c[21])%2 and c[26])
    #phi34
    if c[10]==0 and c[19]==0 and c[20]==0 and c[24]==1 and (c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and c[25]==0 and c[21]==0 and c[26]==0:
        tachy=True 
        #print("e2 phi34 tach")
    #phi58
    if c[10]==0 and c[19]==0 and c[20]==0 and c[24]==0 and (c[1]+c[21]+c[22]+c[23]+c[24])%2==1 and c[25]==0 and c[21]==0 and c[26]==0:
        tachy=True 
        #print("e2 phi58 tach")
    #phi67
    #phi6e2=And(c[10])%2 and c[19])%2 and c[20])%2 and c[24])%2 and (c[1]+c[21]+c[22]+c[23]+c[24])%2 and c[25])%2 and c[21])%2 and c[26])


    #e4 { }, projs: S,e2,e5,z1,z2,x,b2,g
    #y1w1 oscillator case
    if c[11]==0 and c[19]==0 and c[27]==0 and c[31]==0 and (c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and c[32]==0 and c[29]==1 and c[33]==1:
        tachy=True 
        #print("e4 y1w1 tach")
    #y2
    if c[11]==0 and c[19]==1 and c[27]==0 and c[31]==0 and (c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and c[32]==0 and c[29]==1 and c[33]==0:
        tachy=True 
        #print("e4 y2 tach")
    #y3 (w3 same as y1w1)
    if c[11]==0 and c[19]==0 and c[27]==0 and c[31]==0 and (c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and c[32]==0 and c[29]==0 and c[33]==1:
        tachy=True 
        #print("e4 y3 tach")
    #y5
    if c[11]==0 and c[19]==0 and c[27]==1 and c[31]==0 and (c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and c[32]==0 and c[29]==1 and c[33]==0:
        tachy=True 
        #print("e4 y5 tach")
    #y6 same as...
    #psi,eta2
    #psie4=And(c[11])%2 and c[19])%2 and c[27])%2 and c[31])%2 and (c[2]+c[28]+c[29]+c[30]+c[31])%2 and c[32]+c[29]+c[33])
    #eta13
    #eta13e4=And(c[11])%2 and c[19])%2 and c[27])%2 and c[31])%2 and (c[2]+c[28]+c[29]+c[30]+c[31])%2 and c[32]+c[29])%2 and c[33])
    #phi12
    #phi1e4=And(c[11])%2 and c[19])%2 and c[27])%2 and c[31]+(c[2]+c[28]+c[29]+c[30]+c[31])%2 and c[32])%2 and c[29])%2 and c[33])
    #phi34
    if c[11]==0 and c[19]==0 and c[27]==0 and c[31]==1 and (c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and c[32]==0 and c[29]==0 and c[33]==0:
        tachy=True 
        #print("e4 phi34 tach")
    #phi58
    if c[11]==0 and c[19]==0 and c[27]==0 and c[31]==0 and (c[2]+c[28]+c[29]+c[30]+c[31])%2==1 and c[32]==0 and c[29]==0 and c[33]==0:
        tachy=True 
        #print("e4 phi58 tach")
    #phi58
    #phi6e4=And(c[11])%2 and c[19])%2 and c[27])%2 and c[31])%2 and (c[2]+c[28]+c[29]+c[30]+c[31])%2 and c[32])%2 and c[29])%2 and c[33])

    #e5 { }, projs: e2,e4,z1,z2,x,b3,g
    #y1w1 oscillator case
    if c[12]==0 and c[20]==0 and c[27]==0 and c[37]==0 and (c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and c[38]==0 and c[36]==1 and c[39]==0:
        tachy=True 
        #print("e5 y1w1 tach")
    #y2
    if c[12]==0 and c[20]==1 and c[27]==0 and c[37]==0 and (c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and c[38]==0 and c[36]==1 and c[39]==0:
        tachy=True 
        #print("e5 y2 tach")
    #y3 (w3 same as y1w1)
    #y3e5=And(c[20])%2 and c[27])%2 and c[37])%2 and (c[3]+c[34]+c[35]+c[36]+c[37])%2 and c[38])%2 and c[36])
    #y4
    if c[12]==0 and c[20]==0 and c[27]==1 and c[37]==0 and (c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and c[38]==0 and c[36]==1 and c[39]==0:
        tachy=True 
        #print("e5 y4 tach")
    #y6
    if c[12]==0 and c[20]==0 and c[27]==0 and c[37]==0 and (c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and c[38]==0 and c[36]==0 and c[39]==1:
        tachy=True 
        #print("e5 y6 tach")
    #psi,eta3
    #psie5=And(c[12])%2 and c[20])%2 and c[27])%2 and c[37])%2 and (c[3]+c[34]+c[35]+c[36]+c[37])%2 and c[38]+c[36]+c[39])
    #eta12
    #eta23e5=And(c[12])%2 and c[20])%2 and c[27])%2 and c[37])%2 and (c[3]+c[34]+c[35]+c[36]+c[37])%2 and c[38]+c[36])%2 and c[39])
    #phi12
    #phi1e5=And(c[12])%2 and c[20])%2 and c[27])%2 and c[37]+(c[3]+c[34]+c[35]+c[36]+c[37])%2 and c[38])%2 and c[36])%2 and c[39])
    #phi34
    if c[12]==0 and c[20]==0 and c[27]==0 and c[37]==1 and (c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and c[38]==0 and c[36]==0 and c[39]==0:
        tachy=True 
        #print("e5 phi34 tach")
    #phi58
    if c[12]==0 and c[20]==0 and c[27]==0 and c[37]==0 and (c[3]+c[34]+c[35]+c[36]+c[37])%2==1 and c[38]==0 and c[36]==0 and c[39]==0:
        tachy=True 
        #print("e5 phi58 tach")
    #phi67
    #phi6e5=And(c[12])%2 and c[20])%2 and c[27])%2 and c[37])%2 and (c[3]+c[34]+c[35]+c[36]+c[37])%2 and c[38])%2 and c[36])


    #e2+e4
    #yw not y5w5
    if (1+c[10]+c[11])%2==0 and (c[20]+c[27])==0 and (c[24]+c[31])%2==0 and \
        (c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and (c[25]+c[32])%2==0 and (c[26]+c[33])%2==1:
        tachy=True 
        #print("e2+e4 yw tach")
    #y5w5
    if (1+c[10]+c[11])%2==0 and (c[20]+c[27])%2==1 and (c[24]+c[31])%2==0 and \
        (c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and (c[25]+c[32])%2==0 and (c[26]+c[33])%2==0:
        tachy=True 
        #print("e2+e4 y5w5 tach")

    #e2e4psieta=And((1+c[10]+c[11])%2 and (c[20]+c[27])%2 and (c[24]+c[31])%2 and \
    #    (c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31])%2 and (c[25]+c[32])%2 and (c[26]+c[33])

    #e2e4phi1=And((1+c[10]+c[11])%2 and (c[20]+c[27])%2 and (c[24]+c[31])%2 and \
    #    (c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31])%2 and (c[25]+c[32])%2 and (c[26]+c[33])

    if (1+c[10]+c[11])%2==0 and (c[20]+c[27])%2==0 and (c[24]+c[31])%2==1 and \
    (c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and (c[25]+c[32])%2==0 and (c[26]+c[33])%2==0:
        tachy=True 
        #print("e2+e4 phi34 tach")

    if (1+c[10]+c[11])%2==0 and (c[20]+c[27])%2==0 and (c[24]+c[31])%2==0 and \
    (c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31])%2==1 and (c[25]+c[32])%2==0 and (c[26]+c[33])%2==0:
        tachy=True 
        #print("e2+e4 phi58 tach")

    #e2e4phi6=And((1+c[10]+c[11])%2 and (c[20]+c[27])%2 and (c[24]+c[31])%2 and \
    #    (c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31])%2 and (c[25]+c[32])%2 and (c[26]+c[33])

    #e2+e5
    #yw not y4w4
    if (1+c[10]+c[12])%2==0 and (c[19]+c[27])%2==0 and (c[24]+c[37])%2==0 and \
    (c[1]+c[21]+c[22]+c[23]+c[24]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and (c[25]+c[38])%2==0 and (c[26]+c[39])%2==1:
        tachy=True 
        #print("e2+e5 yw tach")
    
    if (1+c[10]+c[12])%2==0 and (c[19]+c[27])%2==1 and (c[24]+c[37])%2==0 and \
        (c[1]+c[21]+c[22]+c[23]+c[24]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and (c[25]+c[38])%2==0 and (c[26]+c[39])%2==0:
        tachy=True 
        #print("e2+e5 y4w4 tach")

    #e2e5psieta=And((1+c[10]+c[12])%2 and (c[19]+c[27])%2 and (c[24]+c[37])%2 and \
    #(c[1]+c[21]+c[22]+c[23]+c[24]+c[3]+c[34]+c[35]+c[36]+c[37])%2 and (c[25]+c[38])%2 and (c[26]+c[39])

    #e2e5phi1=And((1+c[10]+c[12])%2 and (c[19]+c[27])%2 and (c[24]+c[37])%2 and \
    #    (c[1]+c[21]+c[22]+c[23]+c[24]+c[3]+c[34]+c[35]+c[36]+c[37])%2 and (c[25]+c[38])%2 and (c[26]+c[39])

    if (1+c[10]+c[12])%2==0 and (c[19]+c[27])%2==0 and (c[24]+c[37])%2==1 and \
        (c[1]+c[21]+c[22]+c[23]+c[24]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and (c[25]+c[38])%2==0 and (c[26]+c[39])%2==0:
        tachy=True 
        #print("e2+e5 phi34 tach")

    if (1+c[10]+c[12])%2==0 and (c[19]+c[27])%2==0 and (c[24]+c[37])%2==0 and \
        (c[1]+c[21]+c[22]+c[23]+c[24]+c[3]+c[34]+c[35]+c[36]+c[37])%2==1 and (c[25]+c[38])%2==0 and (c[26]+c[39])%2==0:
        tachy=True 
        #print("e2+e5 phi58 tach")

    #e2e5phi6=And((1+c[10]+c[12])%2 and (c[19]+c[27])%2 and (c[24]+c[37])%2 and \
    #    (c[1]+c[21]+c[22]+c[23]+c[24]+c[3]+c[34]+c[35]+c[36]+c[37])%2 and (c[25]+c[38])%2 and (c[26]+c[39])

    #e4+e5
    #yw not y2w2
    if (1+c[11]+c[12])%2==0 and (c[19]+c[20])%2==0 and (c[31]+c[37])%2==0 and \
        (c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and (c[32]+c[38])%2==0 and (c[33]+c[39])%2==1:
        tachy=True 
        #print("e4+e5 yw tach")
        
    if (1+c[11]+c[12])%2==0 and (c[19]+c[20])%2==1 and (c[31]+c[37])%2==0 and \
        (c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and (c[32]+c[38])%2==0 and (c[33]+c[39])%2==0:
        tachy=True 
        #print("e4+e5 yw2 tach")

    #e4e5psieta=And((1+c[11]+c[12])%2 and (c[19]+c[20])%2 and (c[31]+c[37])%2 and \
        #(c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2 and (c[32]+c[38])%2 and (c[33]+c[39])

    #e4e5phi1=And((1+c[11]+c[12])%2 and (c[19]+c[20])%2 and (c[31]+c[37])%2 and \
        #(c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2 and (c[32]+c[38])%2 and (c[33]+c[39])

    if (1+c[11]+c[12])%2==0 and (c[19]+c[20])%2==0 and (c[31]+c[37])%2==1 and \
        (c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and (c[32]+c[38])%2==0 and (c[33]+c[39])%2==0:
        tachy=True 
        #print("e4+e5 phi34 tach")

    if (1+c[11]+c[12])%2==0 and (c[19]+c[20])%2==0 and (c[31]+c[37])%2==0 and \
        (c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2==1 and (c[32]+c[38])%2==0 and (c[33]+c[39])%2==0:
        tachy=True 
        #print("e4+e5 phi58 tach")

    #e4e5phi6=And((1+c[11]+c[12])%2 and (c[19]+c[20])%2 and (c[31]+c[37])%2 and \
        #(c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2 and (c[32]+c[38])%2 and (c[33]+c[39])

    #e2+e4+e5
    #yw
    if (c[10]+c[11]+c[12])%2==0 and (c[24]+c[31]+c[37])%2==0 and \
        (c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and \
        (c[25]+c[32]+c[38])%2==0 and (c[26]+c[33]+c[39])%2==0:
        tachy=True 
        #print("e2+e4+e5 yw tach")

    #e245psieta=And((c[10]+c[11]+c[12])%2 and (c[24]+c[31]+c[37])%2 and \
        #(c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2 and \
            #(c[25]+c[32]+c[38])%2 and (c[26]+c[33]+c[39])

    #e245phi1=And((c[10]+c[11]+c[12])%2 and (c[24]+c[31]+c[37])%2 and \
        #(c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2 and \
            #(c[25]+c[32]+c[38])%2 and (c[26]+c[33]+c[39])

    if (c[10]+c[11]+c[12])%2==0 and (c[24]+c[31]+c[37])%2==1 and \
        (c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and \
        (c[25]+c[32]+c[38])%2==0 and (c[26]+c[33]+c[39])%2==0:
        tachy=True 
        #print("e2+e4+e5 phi34 tach")

    if (c[10]+c[11]+c[12])%2==0 and (c[24]+c[31]+c[37])%2==0 and \
        (c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2==1 and \
        (c[25]+c[32]+c[38])%2==0 and (c[26]+c[33]+c[39])%2==0:
        tachy=True 
        #print("e2+e4+e5 phi58 tach")

    #e245phi6=And((c[10]+c[11]+c[12])%2 and (c[24]+c[31]+c[37])%2 and \
        #(c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37])%2 and \
            #(c[25]+c[32]+c[38])%2 and (c[26]+c[33]+c[39])

    #Spinorials
    #z1, projs: S,e2,e4,e5,z2,x,b1,b2,b3 - z2 is redundant it seems
    if c[16]==0 and c[24]==0 and c[31]==0 and c[37]==0 and (c[42]+c[46]+c[49])%2==0 and c[52]==0 and c[42]==0 and c[46]==0 and c[49]==0:
        tachy=True 
        #print("z1 tach")

    #z2, projs: S,e2,e4,e5,z1,x,b1,b2,b3- i'll just do b1 
    if (c[0]+c[13]+c[14]+c[15]+c[16])%2==0 and (c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and (c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and \
        (c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and (c[42]+c[46]+c[49])%2==0 and (c[8]+c[43]+c[47]+c[50]+c[52])%2==0 and (c[40]+c[41]+c[42])%2==0:
        tachy=True 
        #print("z2 tach")

    #2g+x, just b1 not b2 and b3..?
    if c[17]==0 and c[25]==0 and c[32]==0 and c[38]==0 and (1+c[8])%2==0 and (c[43]+c[47]+c[50]+c[54])%2==0 and c[43]==0:
        tachy=True 
        #print("2g+x tach")

    #2g+x+z1
    if (1+c[17]+c[16])%2==0 and (c[25]+c[24])%2==0 and (c[32]+c[31])%2==0 and (c[38]+c[37])%2==0 and \
        (c[8]+c[52])%2==0 and (c[43]+c[42])%2==0:
        tachy=True 
        #print("2g+x+z1 tach")

    #2g+x+z2
       
    if (1+c[17]+c[0]+c[13]+c[14]+c[15]+c[16])%2==0 and (c[25]+c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and \
        (c[32]+c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and \
        (c[38]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and (c[43]+c[47]+c[50]+c[52])%2==0 and (c[43]+c[40]+c[41]+c[42])%2==0:
        tachy=True 
        #print("2g+x+z2 tach")

    #2g+x+z1+z2
    if (c[17]+c[0]+c[13]+c[14]+c[15])%2==0 and (c[25]+c[1]+c[21]+c[22]+c[23])%2==0 and (c[32]+c[2]+c[28]+c[29]+c[30])%2==0 and \
        (c[38]+c[3]+c[34]+c[35]+c[36])%2==0 and (c[43]+c[47]+c[50])%2==0 and (c[43]+c[40]+c[41])%2==0:
        tachy=True 
        #print("2g+x+z1+z2 tach")

    #e2+z1, b1...
    if (c[10]+c[16])%2==1 and (c[19]+c[31])%2==0 and (c[20]+c[37])%2==0 and \
        (c[1]+c[21]+c[22]+c[23]+c[24]+c[42]+c[46]+c[49])%2==0 and (c[25]+c[52])%2==0 and (1+c[21]+c[42])%2==0:
        tachy=True 
        #print("e2+z1 tach")

    #e2+z2
    if (c[10]+c[0]+c[13]+c[14]+c[15]+c[16])%2==1 and (c[19]+c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and \
        (c[20]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and (c[24]+c[42]+c[46]+c[49])%2==0 and \
            (c[25]+c[8]+c[43]+c[47]+c[50]+c[52])%2==0 and (1+c[21]+c[40]+c[41]+c[42])%2==0:
        tachy=True 
        #print("e2+z2 tach")

    #e2+2g+x
    ggxz1z2_e2=(c[25]+c[24]+c[1]+c[21]+c[22]+c[23]+c[24]+c[43]+c[47]+c[50])%2
    if (c[10]+c[17])%2==1 and (c[19]+c[32])%2==0 and (c[20]+c[38])%2==0 and (c[25]+c[8])%2==1 and \
        (1+c[21]+c[43])%2==0 and ggxz1z2_e2==0:
        tachy=True 
        #print("e2+2g+x tach")

    #e2+2g+x+z1
    if (c[10]+c[17]+c[16])%2==0 and (c[19]+c[32]+c[31])%2==0 and (c[20]+c[38]+c[37])%2==0 and \
        (c[21]+c[42]+c[43])%2==0 and (c[25]+c[8]+c[52])%2==1:
        tachy=True 
        #print("e2+2g+x+z1 tach")

    #e2+2g+x+z2
    if (c[10]+c[17]+c[0]+c[13]+c[14]+c[15]+c[16])%2==0 and (c[19]+c[32]+c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and \
        (c[20]+c[38]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and (c[25]+1+c[43]+c[47]+c[50]+c[52])%2==0 and \
        (1+c[21]+c[40]+c[41]+c[42]+c[43])%2==0:
        tachy=True 
        #print("e2+2g+x+z2 tach")

    #e2+2g+x+z1+z2
    if (1+c[10]+c[17]+c[0]+c[13]+c[14]+c[15])%2==0 and (c[19]+c[32]+c[2]+c[28]+c[29]+c[30])%2==0 and \
        (c[20]+c[38]+c[3]+c[34]+c[35]+c[36])%2==0 and (c[25]+c[43]+c[47]+c[50])%2==0 and \
        (1+c[21]+c[40]+c[41]+c[43])%2==0:
        tachy=True 
        #print("e2+2g+x+z1+z2 tach")

    #e4+z1 - b2...
    if (c[11]+c[16])%2==1 and (c[19]+c[24])%2==0 and (c[27]+c[37])%2==0 and \
        (c[2]+c[28]+c[29]+c[30]+c[31]+c[42]+c[46]+c[49])%2==0 and \
        (c[32]+c[52])%2==0 and (1+c[29]+c[46])%2==0:
        tachy=True 
        #print("e4+z1 tach")

    #e4+z2
    if (c[11]+c[0]+c[13]+c[14]+c[15]+c[16])%2==1 and (c[19]+c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and \
        (c[27]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and \
        (c[31]+c[42]+c[46]+c[49])%2==0 and (c[32]+c[8]+c[43]+c[47]+c[50]+c[52])%2==0 and \
            (1+c[29]+c[40]+c[45]+c[46])%2==0:
        tachy=True 
        #print("e4+z2 tach")

    #e4+2g+x
    ggxz1z2_e4=(c[32]+c[31]+c[2]+c[28]+c[29]+c[30]+c[31]+c[43]+c[47]+c[50])%2
    if (c[11]+c[17])%2==1 and (c[19]+c[25])%2==0 and (c[27]+c[38])%2==0 and (c[32]+1+c[8])%2==0 and \
        (1+c[29]+c[47])%2==0 and ggxz1z2_e4==0:
        tachy=True 
        #print("e4+2g+x tach")

    #e4+2g+x+z1
    if (c[11]+c[17]+c[16])%2==0 and (c[19]+c[25]+c[24])%2==0 and (c[27]+c[38]+c[37])%2==0 and \
        (c[29]+c[46]+c[47])%2==0 and (c[32]+1+c[8]+c[52])%2==0:
        tachy=True 
        #print("e4+2g+x+z1 tach")

    #e4+2g+x+z2
    if (c[11]+c[17]+c[0]+c[13]+c[14]+c[15]+c[16])%2==0 and (c[19]+c[25]+c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and \
        (c[27]+c[38]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and (c[29]+c[40]+c[45]+c[46]+c[47])%2==0 and \
        (c[32]+1+c[43]+c[47]+c[50]+c[52])%2==0:
        tachy=True 
        #print("e4+2g+x+z2 tach")

    #e4+2g+x+z1+z2
    if (1+c[11]+c[17]+c[0]+c[13]+c[14]+c[15])%2==0 and (c[19]+c[25]+c[1]+c[21]+c[22]+c[23])%2==0 and \
        (c[27]+c[38]+c[3]+c[34]+c[35]+c[36])%2==0 and (c[32]+c[43]+c[47]+c[50])%2==0 and (1+c[29]+c[40]+c[45]+c[47])%2==0:
        tachy=True 
        #print("e4+2g+x+z1+z2 tach")

    #e5+z1, b3 is a proj...
    if (c[12]+c[16])%2==1 and (c[20]+c[24])%2==0 and (c[27]+c[31])%2==0 and \
        (c[3]+c[34]+c[35]+c[36]+c[37]+c[42]+c[46]+c[49])%2==0 and (c[38]+c[52])%2==0 and (1+c[36]+c[49])%2==0:
        tachy=True 
        #print("e5+z1 tach")

    #e5+z2
    if (c[12]+c[0]+c[13]+c[14]+c[15]+c[16])%2==1 and (c[20]+c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and \
        (c[27]+c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and \
        (c[37]+c[42]+c[46]+c[49])%2==0 and (c[38]+c[8]+c[43]+c[47]+c[50]+c[52])%2==0 and (1+c[36]+c[41]+c[45]+c[49])%2==0:
        tachy=True 
        #print("e5+z2 tach")

    #e5+2g+x
    ggxz1z2_e5=(c[38]+c[3]+c[34]+c[35]+c[36]+c[43]+c[47]+c[50])%2
    if (c[12]+c[17])%2==1 and (c[20]+c[32])%2==0 and (c[27]+c[32])%2==0 and (c[38]+c[8])%2==1 and \
        ggxz1z2_e5==0 and (1+c[36]+c[50])%2==0:
        tachy=True 
        #print("e5+2g+x tach")

    #e5+2g+x+z1
    ggxz2_e5=(c[38]+c[3]+c[34]+c[35]+c[36]+c[37]+c[43]+c[47]+c[50]+c[42]+c[46]+c[49])%2
    if (c[12]+c[17]+c[16])%2==0 and (c[20]+c[25]+c[24])%2==0 and (c[27]+c[32]+c[31])%2==0 and \
        (c[38]+c[8]+c[52])%2==1 and (c[36]+c[49]+c[50])%2==0 and ggxz2_e5==0:
        tachy=True 
        #print("e5+2g+x+z1 tach")

    #e5+2g+x+z2
    ggxz1_e5=(c[38]+c[37]+c[43]+c[47]+c[50]+c[42]+c[46]+c[49])%2
    if (c[12]+c[17]+c[0]+c[13]+c[14]+c[15]+c[16])%2==0 and (c[20]+c[25]+c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and \
        (c[27]+c[32]+c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and (c[38]+1+c[43]+c[47]+c[50]+c[52])%2==0 and \
        (c[36]+c[41]+c[45]+c[49]+c[50])%2==0 and ggxz1_e5==0:
        tachy=True 
        #print("e5+2g+x+z2 tach")

    #e5+2g+x+z1+z2
    if (1+c[12]+c[17]+c[0]+c[13]+c[14]+c[15])%2==0 and (c[20]+c[25]+c[1]+c[21]+c[22]+c[23])%2==0 and \
        (c[27]+c[32]+c[2]+c[28]+c[29]+c[30])%2==0 and (c[38]+c[43]+c[47]+c[50])%2==0 and \
        (1+c[36]+c[41]+c[45]+c[50])%2==0:
        tachy=True 
        #print("e5+2g+x+z1+z2 tach")

    #e2+e4+z1
    if (c[10]+c[11]+c[16])%2==0 and (c[20]+c[27]+c[37])%2==0 and (c[25]+c[32]+c[52])%2==0 and \
        (c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[42]+c[46]+c[49])%2==0:
        tachy=True 
        #print("e2+e4+z1 tach")

    #e2+e4+z2
    if (c[10]+c[11]+c[0]+c[13]+c[14]+c[15]+c[16])%2==0 and (c[20]+c[27]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and \
        (c[25]+c[32]+c[8]+c[43]+c[47]+c[50]+c[52])%2==1 and (c[24]+c[31]+c[42]+c[46]+c[49])%2==0:
        tachy=True 
        #print("e2+e4+z2 tach")

    #e2+e4+2g+x
    ggxz1z2_e24=(c[25]+c[32]+c[1]+c[21]+c[22]+c[23]+c[2]+c[28]+c[29]+c[30]+c[43]+c[47]+c[50])%2
    if (c[10]+c[11]+c[17])%2==0 and (c[20]+c[27]+c[38])%2==0 and (c[25]+c[32]+c[8])%2==0 and ggxz1z2_e24==0:
        tachy=True 
        #print("e2+e4+2g+x tach")

    #e2+e4+2g+x+z1
    
    ggxz2_e24=(1+c[25]+c[32]+c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[43]+c[47]+c[50]+c[42]+c[46]+c[49])%2
    if (1+c[10]+c[11]+c[17]+c[16])%2==0 and (c[20]+c[27]+c[38]+c[37])%2==0 and \
        (c[25]+c[32]+c[8]+c[52])%2==1 and ggxz2_e24==0:
        tachy=True 
        #print("e2+e4+2g+x+z1 tach")

    #e2+e4+2g+x+z2
    
    #print("S phase: ",(1+c[10]+c[11]+c[17]+c[0]+c[13]+c[14]+c[15]+c[16])%2)
    #print("e5 phase: ", (c[20]+c[27]+c[38]+c[3]+c[34]+c[35]+c[36]+c[37])%2)
    #print("x phase:", (c[25]+c[32]+c[43]+c[47]+c[50]+c[52])%2)
    #print("ggxz1 e24: ", (1+c[25]+c[32]+c[24]+c[31]+c[43]+c[47]+c[50]+c[42]+c[46]+c[49])%2)
    ggxz1_e24=(1+c[25]+c[32]+c[24]+c[31]+c[43]+c[47]+c[50]+c[42]+c[46]+c[49])%2
    if (1+c[10]+c[11]+c[17]+c[0]+c[13]+c[14]+c[15]+c[16])%2==0 and (c[20]+c[27]+c[38]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and \
        (c[25]+c[32]+c[43]+c[47]+c[50]+c[52])%2==0 and ggxz1_e24==0:
        tachy=True 
        #print("e2+e4+2g+x+z2 tach")
        

    #e2+e4+2g+x+z1z2
    #print("x proj: ", (c[25]+c[32]+c[43]+c[47]+c[50])%2)
    #print("S proj: ", (c[10]+c[11]+c[17]+c[0]+c[13]+c[14]+c[15])%2)
    #print("e5 proj: ", (c[20]+c[27]+c[38]+c[3]+c[34]+c[35]+c[36])%2)
    if (c[10]+c[11]+c[17]+c[0]+c[13]+c[14]+c[15])%2==0 and (c[20]+c[27]+c[38]+c[3]+c[34]+c[35]+c[36])%2==0 and \
        (c[25]+c[32]+c[43]+c[47]+c[50])%2==0:
        tachy=True 
        #print("e2+e4+2g+x+z1+z2 tach")

    #e2+e5+z1
    if (c[10]+c[12]+c[16])%2==0 and (c[19]+c[27]+c[31])%2==0 and (c[25]+c[38]+c[52])%2==0 and \
        (c[1]+c[21]+c[22]+c[23]+c[24]+c[3]+c[34]+c[35]+c[36]+c[37]+c[42]+c[46]+c[49])%2==0:
        tachy=True 
        #print("e2+e5+z1 tach")

    #e2+e5+z2
    if (c[10]+c[12]+c[0]+c[13]+c[14]+c[15]+c[16])%2==0 and (c[19]+c[27]+c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and \
        (c[25]+c[38]+c[8]+c[43]+c[47]+c[50]+c[52])%2==0 and (c[24]+c[37]+c[42]+c[46]+c[49])%2==0:
        tachy=True 
        #print("e2+e5+z2 tach")

    #e2+e5+2g+x
    
    ggxz1z2_e25=(c[25]+c[38]+c[1]+c[21]+c[22]+c[23]+c[3]+c[34]+c[35]+c[36]+c[43]+c[47]+c[50])%2
    ##print("e25ggx S proj: ", (c[10]+c[12]+c[17])%2)
    ##print("e25ggx e4 proj: ", (c[19]+c[27]+c[32])%2)
    ##print("e25ggx x proj: ", (c[25]+c[38]+1+c[8])%2)
    ##print("e25ggx ggxz1z2 proj: ", ggxz1z2_e25)
    if (c[10]+c[12]+c[17])%2==0 and (c[19]+c[27]+c[32])%2==0 and (c[25]+c[38]+1+c[8])%2==0 and ggxz1z2_e25==0:
        tachy=True 
        #print("e2+e5+2g+x tach")

    #e2+e5+2g+x+z1
    ggxz2_e25=(1+c[25]+c[38]+c[1]+c[21]+c[22]+c[23]+c[24]+c[3]+c[34]+c[35]+c[36]+c[37]+c[43]+c[47]+c[50]+c[42]+c[46]+c[49])%2
    if (1+c[10]+c[12]+c[17]+c[16])%2==0 and (c[19]+c[27]+c[32]+c[31])%2==0 and (c[25]+c[38]+1+c[8]+c[52])%2==0 and \
        (c[25]+c[38]+c[1]+c[21]+c[22]+c[23]+c[24]+c[3]+c[34]+c[35]+c[36]+c[37]+c[43]+c[47]+c[50]+c[42]+c[46]+c[49])%2==0 and ggxz2_e25==0:
        tachy=True 
        #print("e2+e5+2g+x+z1 tach")

    #e2+e5+2g+x+z2
    ggxz1_e25=(1+c[32]+c[38]+c[31]+c[37]+c[43]+c[47]+c[50]+c[42]+c[46]+c[49])%2
    if (1+c[10]+c[12]+c[17]+c[0]+c[13]+c[14]+c[15]+c[16])%2==0 and (c[19]+c[27]+c[32]+c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and \
        (c[25]+c[38]+1+c[43]+c[47]+c[50]+c[52])%2==0 and ggxz1_e25==0:
        tachy=True 
        #print("e2+e5+2g+x+z2 tach")

    #e2+e5+2g+x+z1+z2
        
    if (c[10]+c[12]+c[17]+c[0]+c[13]+c[14]+c[15])%2==0 and (c[19]+c[27]+c[32]+c[2]+c[28]+c[29]+c[30])%2==0 and \
        (c[25]+c[38]+c[43]+c[47]+c[50])%2==0:
        tachy=True 
        #print("e2+e5+2g+x+z2 tach")

    #e4+e5+z1
    if (c[11]+c[12]+c[16])%2==0 and (c[19]+c[20]+c[24])%2==0 and (c[32]+c[38]+c[52])%2==0 and \
        (c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37]+c[42]+c[46]+c[49])%2==0:
        tachy=True 
        #print("e4+e5+z1 tach")

    #e4+e5+z2
    if (c[11]+c[12]+c[0]+c[13]+c[14]+c[15]+c[16])%2==0 and (c[19]+c[20]+c[1]+c[28]+c[29]+c[30]+c[31])%2==0 and \
        (c[32]+c[38]+1+c[8]+c[43]+c[47]+c[50]+c[52])%2==0 and (c[31]+c[37]+c[42]+c[46]+c[49])%2==0:
        tachy=True 
        #print("e4+e5+z2 tach")

    #e4+e5+2g+x
    ggxz1z2_e45=(c[32]+c[38]+c[2]+c[28]+c[29]+c[30]+c[3]+c[34]+c[35]+c[36]+c[43]+c[47]+c[50])%2
    if (c[11]+c[12]+c[17])%2==0 and (c[19]+c[20]+c[25])%2==0 and (c[32]+c[38]+1+c[8])%2==0 and ggxz1z2_e45==0:
        tachy=True 
        #print("e4+e5+2g+x tach")

    #e4+e5+2g+x+z1
    ggxz2_e45=(1+c[32]+c[38]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37]+c[43]+c[47]+c[50]+c[42]+c[46]+c[49])%2
    if (1+c[11]+c[12]+c[17]+c[16])%2==0 and (c[19]+c[20]+c[25]+c[24])%2==0 and \
        (c[32]+c[38]+1+c[8]+c[52])%2==0 and ggxz2_e45==0:
        tachy=True 
        #print("e4+e5+2g+x+z1 tach")

    #e4+e5+2g+x+z2
    
    ggxz1_e45=(1+c[32]+c[38]+c[31]+c[37]+c[43]+c[47]+c[50]+c[42]+c[46]+c[49])%2
    if (1+c[11]+c[12]+c[17]+c[0]+c[13]+c[14]+c[15]+c[16])%2==0 and \
        (c[19]+c[20]+c[25]+c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and \
        (c[32]+c[38]+c[43]+c[47]+c[50]+c[52])%2==0 and ggxz1_e45==0:
        tachy=True 
        #print("e4+e5+2g+x+z2 tach")
    
    
    #e4+e5+2g+x+z1+z2
    if (c[11]+c[12]+c[17]+c[0]+c[13]+c[14]+c[15])%2==0 and (c[19]+c[20]+c[25]+c[1]+c[21]+c[22]+c[23])%2==0 and \
        (c[32]+c[38]+c[43]+c[47]+c[50])%2==0:
        tachy=True 
        #print("e4+e5+2g+x+z1+z2 tach")

    #e2+e4+e5+z1
    if (c[10]+c[11]+c[12]+c[16])%2==1 and (c[25]+c[32]+c[38]+c[52])%2==0 and \
        (c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37]+c[42]+c[46]+c[49])%2==0:
        tachy=True 
        #print("e2+e4+e5+z1 tach")

    #e2+e4+e5+z2
    #print("S phase for e2e4e5z2: ", (c[10]+c[11]+c[12]+c[0]+c[13]+c[14]+c[15]+c[16])%2)
    #print("x phase for e2e4e5z2: ", (c[25]+c[32]+c[38]+c[8]+c[43]+c[47]+c[50]+c[52])%2)
    #print("z1 phase for e2e4e5z2: ", (c[24]+c[31]+c[37]+c[42]+c[46]+c[49])%2)
    
    if (c[10]+c[11]+c[12]+c[0]+c[13]+c[14]+c[15]+c[16])%2==1 and (1+c[25]+c[32]+c[38]+c[8]+c[43]+c[47]+c[50]+c[52])%2==0 and \
        (c[24]+c[31]+c[37]+c[42]+c[46]+c[49])%2==0: # -1 in x phase  from flipping x b1/b2/b3 phase...probably a bug in other places too :( when x z2 used 
        tachy=True 
        #print("e2+e4+e5+z2 tach")

    #e2+e4+e5+2g+x
    ggxz1z2_e245=(c[25]+c[32]+c[38]+c[24]+c[31]+c[37]+c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+\
        c[3]+c[34]+c[35]+c[36]+c[37]+c[43]+c[47]+c[50])%2
    if (c[10]+c[11]+c[12]+c[17])%2==1 and (c[25]+c[32]+c[38]+1+c[8])%2==0 and ggxz1z2_e245==0:
        tachy=True 
        #print("e2+e4+e5+2g+x tach")

    #e2+e4+e5+2g+x+z1
    ggxz2_e245=(c[25]+c[32]+c[38]+c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+\
        c[3]+c[34]+c[35]+c[36]+c[37]+c[43]+c[47]+c[50]+c[42]+c[46]+c[49])%2
    if (c[10]+c[11]+c[12]+c[17]+c[16])%2==0 and (c[25]+c[32]+c[38]+1+c[8]+c[52])%2==0 and ggxz2_e245==0:
        tachy=True 
        #print("e2+e4+e5+2g+x+z1 tach")

    #e2+e4+e5+2g+x+z2
    ggxz1_e245=(1+c[25]+c[32]+c[38]+c[24]+c[31]+c[37]+c[43]+c[47]+c[50]+c[42]+c[46]+c[49])%2
    if (c[10]+c[11]+c[12]+c[17]+c[0]+c[13]+c[14]+c[15]+c[16])%2==0 and \
        (c[25]+c[32]+c[38]+1+c[43]+c[47]+c[50]+c[52])%2==0 and ggxz1_e245==0:
        tachy=True 
        #print("e2+e4+e5+2g+x+z2 tach")
    
    
    #e2+e4+e5+2g+x+z1+z2
    #print("S proj: ", (1+c[10]+c[11]+c[12]+c[17]+c[0]+c[13]+c[14]+c[15])%2)
    #print("x proj: ", (c[25]+c[32]+c[38]+c[43]+c[47]+c[50])%2)
    if (1+c[10]+c[11]+c[12]+c[17]+c[0]+c[13]+c[14]+c[15])%2==0 and \
        (c[25]+c[32]+c[38]+c[43]+c[47]+c[50])%2==0:
        tachy=True 
        #print("e2+e4+e5+2g+x+z1+z2 tach")

    #e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x {}
    #y2w2
    if (1+c[0]+c[10]+c[11]+c[12]+c[13]+c[14]+c[15]+c[17])%2==0 and (c[10]+1+c[1]+c[19]+c[20]+c[21]+c[22]+c[23]+c[25])%2==1 and \
        (c[11]+1+c[2]+c[19]+c[27]+c[28]+c[29]+c[30]+c[32])%2==0 and (c[12]+1+c[3]+c[20]+c[27]+c[34]+c[35]+c[36]+c[38])%2==0 and \
        (c[17]+c[25]+c[32]+c[38]+c[43]+c[47]+c[50]+1+c[8])%2==0 and (c[16]+c[24]+c[31]+c[37]+c[42]+c[46]+c[49]+c[52])%2==0 and \
        (c[0]+c[13]+c[14]+c[15]+c[16]+c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37]+\
            c[42]+c[46]+c[49]+c[8]+c[43]+c[47]+c[50]+c[52])%2==0:
        tachy=True 
        #print("e1+e3+e6 yw2 tach")

    #y4w4
    if (1+c[0]+c[10]+c[11]+c[12]+c[13]+c[14]+c[15]+c[17])%2==0 and (c[10]+1+c[1]+c[19]+c[20]+c[21]+c[22]+c[23]+c[25])%2==0 and \
        (c[11]+1+c[2]+c[19]+c[27]+c[28]+c[29]+c[30]+c[32])%2==1 and (c[12]+1+c[3]+c[20]+c[27]+c[34]+c[35]+c[36]+c[38])%2==0 and \
        (c[17]+c[25]+c[32]+c[38]+c[43]+c[47]+c[50]+1+c[8])%2==0 and (c[16]+c[24]+c[31]+c[37]+c[42]+c[46]+c[49]+c[52])%2==0 and \
        (c[0]+c[13]+c[14]+c[15]+c[16]+c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37]+\
            c[42]+c[46]+c[49]+c[8]+c[43]+c[47]+c[50]+c[52])%2==0:
        tachy=True 
        #print("e1+e3+e6 yw4 tach")

    #y5w5
    if (1+c[0]+c[10]+c[11]+c[12]+c[13]+c[14]+c[15]+c[17])%2==0 and (c[10]+1+c[1]+c[19]+c[20]+c[21]+c[22]+c[23]+c[25])%2==0 and \
        (c[11]+1+c[2]+c[19]+c[27]+c[28]+c[29]+c[30]+c[32])%2==0 and (c[12]+1+c[3]+c[20]+c[27]+c[34]+c[35]+c[36]+c[38])%2==1 and \
        (c[17]+c[25]+c[32]+c[38]+c[43]+c[47]+c[50]+1+c[8])%2==0 and (c[16]+c[24]+c[31]+c[37]+c[42]+c[46]+c[49]+c[52])%2==0 and \
        (c[0]+c[13]+c[14]+c[15]+c[16]+c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37]+\
            c[42]+c[46]+c[49]+c[8]+c[43]+c[47]+c[50]+c[52])%2==0:
        tachy=True 
        #print("e1+e3+e6 yw5 tach")

    #psi12345eta123
    #if (1+c[0]+c[10]+c[11]+c[12]+c[13]+c[14]+c[15]+c[17])%2 and (c[10]+1+c[1]+c[19]+c[20]+c[21]+c[22]+c[23]+c[25])%2 and \
    #    (c[11]+1+c[2]+c[19]+c[27]+c[28]+c[29]+c[30]+c[32])%2 and (c[12]+1+c[3]+c[20]+c[27]+c[34]+c[35]+c[36]+c[38])%2 and \
    #    (c[17]+c[25]+c[32]+c[38]+c[43]+c[47]+c[50]+c[8])%2 and (c[16]+c[24]+c[31]+c[37]+c[42]+c[46]+c[49]+c[52])%2 and 
    #    (c[0]+c[13]+c[14]+c[15]+c[16]+c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37]+\
    #        c[42]+c[46]+c[49]+c[8]+c[43]+c[47]+c[50]+c[52])
    #phi34
    if (1+c[0]+c[10]+c[11]+c[12]+c[13]+c[14]+c[15]+c[17])%2==0 and (c[10]+1+c[1]+c[19]+c[20]+c[21]+c[22]+c[23]+c[25])%2==0 and \
        (c[11]+1+c[2]+c[19]+c[27]+c[28]+c[29]+c[30]+c[32])%2==0 and (c[12]+1+c[3]+c[20]+c[27]+c[34]+c[35]+c[36]+c[38])%2==0 and \
        (c[17]+c[25]+c[32]+c[38]+c[43]+c[47]+c[50]+1+c[8])%2==0 and (c[16]+c[24]+c[31]+c[37]+c[42]+c[46]+c[49]+c[52])%2==1 and \
        (c[0]+c[13]+c[14]+c[15]+c[16]+c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37]+\
            c[42]+c[46]+c[49]+c[8]+c[43]+c[47]+c[50]+c[52])%2==0:
        tachy=True 
        #print("e1+e3+e6 phi34 tach")
    #phi58
    if (1+c[0]+c[10]+c[11]+c[12]+c[13]+c[14]+c[15]+c[17])%2==0 and (c[10]+1+c[1]+c[19]+c[20]+c[21]+c[22]+c[23]+c[25])%2==0 and \
        (c[11]+1+c[2]+c[19]+c[27]+c[28]+c[29]+c[30]+c[32])%2==0 and (c[12]+1+c[3]+c[20]+c[27]+c[34]+c[35]+c[36]+c[38])%2==0 and \
        (c[17]+c[25]+c[32]+c[38]+c[43]+c[47]+c[50]+1+c[8])%2==0 and (c[16]+c[24]+c[31]+c[37]+c[42]+c[46]+c[49]+c[52])%2==0 and \
        (c[0]+c[13]+c[14]+c[15]+c[16]+c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+c[3]+c[34]+c[35]+c[36]+c[37]+\
            c[42]+c[46]+c[49]+c[8]+c[43]+c[47]+c[50]+c[52])%2==1:
        tachy=True 
        #print("e1+e3+e6 phi58 tach")

    #e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x +z1
    #print("e136z1 projs")
    #print("S:", (c[0]+c[10]+c[11]+c[12]+c[13]+c[14]+c[15]+c[17]+c[16])%2)
    #print("e2:", (1+c[10]+c[1]+c[19]+c[20]+c[21]+c[22]+c[23]+c[25]+c[24])%2)
    #print("e4:", (1+c[11]+c[2]+c[19]+c[27]+c[28]+c[29]+c[30]+c[32]+c[31])%2)
    #print("e5:", (1+c[12]+c[3]+c[20]+c[27]+c[34]+c[35]+c[36]+c[38]+c[37])%2)
    #print("x probably:", (c[17]+c[25]+c[32]+c[38]+c[43]+c[47]+c[50]+c[8]+c[52])%2)
    #print("z2:", (c[0]+c[13]+c[14]+c[15]+c[16]+c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+\
            #c[3]+c[34]+c[35]+c[36]+c[37]+c[8]+1+c[43]+c[47]+c[50]+c[52])%2)
    
    if (c[0]+c[10]+c[11]+c[12]+c[13]+c[14]+c[15]+c[17]+c[16])%2==0 and (c[10]+c[1]+c[19]+c[20]+c[21]+c[22]+c[23]+c[25]+c[24])%2==1 and \
        (c[11]+c[2]+c[19]+c[27]+c[28]+c[29]+c[30]+c[32]+c[31])%2==1 and (c[12]+c[3]+c[20]+c[27]+c[34]+c[35]+c[36]+c[38]+c[37])%2==1 and \
        (c[17]+c[25]+c[32]+c[38]+c[43]+c[47]+c[50]+c[8]+c[52])%2==0 and \
        (c[0]+c[13]+c[14]+c[15]+c[16]+c[1]+c[21]+c[22]+c[23]+c[24]+c[2]+c[28]+c[29]+c[30]+c[31]+\
            c[3]+c[34]+c[35]+c[36]+c[37]+c[8]+1+c[43]+c[47]+c[50]+c[52])%2==0:
        tachy=True 
        #print("e1+e3+e6 +z1 tach")

    #e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x +z2
    if (c[10]+c[11]+c[12]+c[16]+c[17])%2==0 and (c[10]+1+c[19]+c[20]+c[24]+c[25])%2==0 and \
        (c[11]+1+c[19]+c[27]+c[31]+c[32])%2==0 and (c[12]+1+c[20]+c[27]+c[37]+c[38])%2==0 and \
        (1+c[17]+c[25]+c[32]+c[38]+c[52])%2==0 and (c[16]+c[24]+c[31]+c[37]+c[52])%2==0:
        tachy=True 
        #print("e1+e3+e6 +z2 tach")

    #e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x +2g+x
    if (c[0]+c[10]+c[11]+c[12]+c[13]+c[14]+c[15])%2==0 and (c[10]+1+c[1]+c[19]+c[20]+c[21]+c[22]+c[23])%2==0 and \
        (c[11]+c[19]+1+c[2]+c[27]+c[28]+c[29]+c[30])%2==0 and (c[12]+c[20]+c[27]+1+c[3]+c[34]+c[35]+c[36])%2==0 and \
        (c[17]+c[25]+c[32]+c[38]+1+c[43]+c[47]+c[50])%2==0 and \
        (c[0]+c[13]+c[14]+c[15]+c[17]+c[1]+c[21]+c[22]+c[23]+c[25]+c[2]+c[28]+c[29]+c[30]+c[32]+\
            c[3]+c[34]+c[35]+c[36]+c[38]+c[43]+c[47]+c[50])%2==0:
        tachy=True 
        #print("e1+e3+e6 +2g+x tach")

    #e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x +2g+x+z1
    #print("e136ggxz1 projs")
    #print("S:", (c[0]+c[10]+c[11]+c[12]+c[13]+c[14]+c[15]+c[16]+1)%2)
    #print("e2:", (c[10]+1+c[1]+c[19]+c[20]+c[21]+c[22]+c[23]+c[24])%2)
    #print("e4:", (c[11]+c[19]+1+c[2]+c[27]+c[28]+c[29]+c[30]+c[31])%2)
    #print("e5:", (c[12]+c[20]+c[27]+1+c[3]+c[34]+c[35]+c[36]+c[37])%2)
    #print("x probably:", (c[17]+c[25]+c[32]+c[38]+1+c[43]+c[47]+c[50]+c[52])%2)
    #print("2g+x+z2:", (c[0]+c[13]+c[14]+c[15]+c[16]+c[17]+c[1]+c[21]+c[22]+c[23]+c[24]+c[25]+\
                #c[2]+c[28]+c[29]+c[30]+c[31]+c[32]+c[3]+c[34]+c[35]+c[36]+c[37]+c[38]+c[43]+c[47]+c[50]+c[52]+c[54])%2)
    if (c[0]+c[10]+c[11]+c[12]+c[13]+c[14]+c[15]+c[16]+1)%2==0 and \
        (c[10]+1+c[1]+c[19]+c[20]+c[21]+c[22]+c[23]+c[24])%2==0 and \
        (c[11]+c[19]+1+c[2]+c[27]+c[28]+c[29]+c[30]+c[31])%2==0 and \
        (c[12]+c[20]+c[27]+1+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and \
        (c[17]+c[25]+c[32]+c[38]+1+c[43]+c[47]+c[50]+c[52])%2==0 and \
        (c[0]+c[13]+c[14]+c[15]+c[16]+c[17]+c[1]+c[21]+c[22]+c[23]+c[24]+c[25]+\
         c[2]+c[28]+c[29]+c[30]+c[31]+c[32]+c[3]+c[34]+c[35]+c[36]+c[37]+c[38]+\
             c[43]+c[47]+c[50]+c[52]+c[54])%2==0:
        tachy=True 
        #print("e1+e3+e6 +2g+x+z1 tach")

    #e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x +2g+x+z2
    #print("e136 + z2+ 2g+x:")
    #print("S:", (1+c[10]+c[11]+c[12]+c[16])%2)
    #print("e2:", (1+c[10]+c[19]+c[20]+c[24])%2)
    #print("e4:", (c[11]+1+c[19]+c[27]+c[31])%2)
    #print("e5:", (c[12]+1+c[20]+c[27]+c[37])%2)
    #print("x probably:", (c[8]+c[17]+c[25]+c[32]+c[38]+c[52])%2)
    #print("2g+x+z2:", (c[8]+c[17]+c[16]+c[25]+c[24]+c[32]+c[31]+c[38]+c[37]+c[52])%2)
    
    if (1+c[10]+c[11]+c[12]+c[16])%2==0 and (1+c[10]+c[19]+c[20]+c[24])%2==0 and \
        (c[11]+1+c[19]+c[27]+c[31])%2==0 and (c[12]+1+c[20]+c[27]+c[37])%2==0 and \
        (c[8]+c[17]+c[25]+c[32]+c[38]+c[52])%2==0 and (c[8]+c[17]+c[16]+c[25]+c[24]+c[32]+c[31]+c[38]+c[37]+c[52])%2==0:
        tachy=True 
        #print("e1+e3+e6 +2g+x+z2 tach")

    #e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x +2g+x+z1+z2
    
    
    if (c[10]+c[11]+c[12])%2==0 and (c[10]+1+c[19]+c[20])%2==0 and \
        (c[11]+1+c[19]+c[27])%2==0 and (c[12]+1+c[20]+c[27])%2==0 and \
        (1+c[8]+c[17]+c[25]+c[32]+c[38])%2==0:
        tachy=True 
        print("e1+e3+e6 +2g+x+z1+z2 tach")

    #g (3,3) { } (note : 2g+x+z1+z2 is a projector)
    #y2w2
    if c[18]==0 and c[26]==1 and c[33]==0 and c[39]==0 and (c[9]+c[44]+c[48]+c[51]+c[54])%2==0:
        tachy=True 
        #print("g yw2 tach")
    #y4w4
    if c[18]==0 and c[26]==0 and c[33]==1 and c[39]==0 and (c[9]+c[44]+c[48]+c[51]+c[54])%2==0:
        tachy=True 
        #print("g yw4 tach")
    #y5w5
    if c[18]==0 and c[26]==0 and c[33]==0 and c[39]==1 and (c[9]+c[44]+c[48]+c[51]+c[54])%2==0:
        tachy=True 
        #print("g yw5 tach")
    #phi3458 
    if c[18]==0 and c[26]==0 and c[33]==0 and c[39]==0 and (c[9]+c[44]+c[48]+c[51]+c[54])%2==1:
        tachy=True 
        #print("g phi3458 tach")

    #other oscill possibilities - inc. 2 complex oscills
    if c[18]==0 and c[26]==0 and c[33]==0 and c[39]==0 and (c[9]+c[44]+c[48]+c[51]+c[54])%2==0:
        tachy=True 
        #print("g other tach")
    
    #x+g (3,3) { }  x+3g same conditions... checked 2g+z1+z2...
    #y2w2
    if (1+c[17]+c[18])%2==0 and (c[25]+c[26])%2==1 and (c[32]+c[33])%2==0 and (c[38]+c[39])%2==0 and \
        (1+c[54]+c[43]+c[47]+c[50]+c[44]+c[48]+c[51])%2==0:
        tachy=True
    if (1+c[17]+c[18])%2==0 and (c[25]+c[26])%2==0 and (c[32]+c[33])%2==1 and (c[38]+c[39])%2==0 and \
        (1+c[54]+c[43]+c[47]+c[50]+c[44]+c[48]+c[51])%2==0:
        tachy=True
    if (1+c[17]+c[18])%2==0 and (c[25]+c[26])%2==0 and (c[32]+c[33])%2==0 and (c[38]+c[39])%2==1 and \
        (1+c[54]+c[43]+c[47]+c[50]+c[44]+c[48]+c[51])%2==0:
        tachy=True
    if (1+c[17]+c[18])%2==0 and (c[25]+c[26])%2==0 and (c[32]+c[33])%2==0 and (c[38]+c[39])%2==0 and \
        (1+c[54]+c[43]+c[47]+c[50]+c[44]+c[48]+c[51])%2==1:
        tachy=True

    
    #g+z1 (3,5) - one complex R oscill (2g+x+z2 is a projector)
    #any
    ##print("g+z1 S proj:", )
    if (1+c[18]+c[16])%2==0 and (c[26]+c[24])%2==0 and (c[33]+c[31])%2==0 and (c[39]+c[37])%2==0 and (1+c[9]+c[42]+c[46]+c[49]+c[44]+c[48]+c[51]+c[52]+c[53]+c[54])%2==0:
        tachy=True 
        #print("g+z1 tach")
    #g+z2 (3,5) - one complex R oscill (2g+x+z1 is a projector)
    #any
    if (1+c[18]+c[0]+c[13]+c[14]+c[15]+c[16])==0 and (c[26]+c[1]+c[21]+c[22]+c[23]+c[24])%2==0 and \
        (c[33]+c[2]+c[28]+c[29]+c[30]+c[31])%2==0 and (c[39]+c[3]+c[34]+c[35]+c[36]+c[37])%2==0 and \
            (c[8]+c[54]+c[43]+c[47]+c[50]+c[52]+c[53]+c[42]+c[46]+c[49])%2==0:
        tachy=True 
        #print("g+z2 tach")

    #1+b1+b2+b3+x+3g = z1+z2+x+3g=y36,y1w6,w13,psi,eta=1/2, phi1267=1/2,phi3458 (3,7)
    if (c[0]+c[13]+c[14]+c[15]+c[17]+c[18])%2==1 and (c[1]+c[21]+c[22]+c[23]+c[25]+c[26])%2==0 and \
        (c[2]+c[28]+c[29]+c[30]+c[32]+c[33])%2==0 and (c[3]+c[34]+c[35]+c[36]+c[38]+c[39])%2==0:
        tachy=True 
        #print("1+b1+b2+b3+x+3g tach")

    #3gamma - basically same as gamma....
    
    return tachy

fromSMT60=[True, True, False, True, None, None, None, None, False, True, True, True, True, False, True, False, True, True, False, False, False, True, None, False, False, True, False, False, False, True, True, False, False, True, False, False, True, False, False, False, True, True, True, True, False, True, True, True, True, True, True, True, False, None, False]
def BooltoInt(lsb):
    lsb[9]=True
    return [1 if item is True else 0 for item in lsb]

fromSMT60ls=BooltoInt(fromSMT60)
GSOmodel=[1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0]
##print("c[42] is:", GSOmodel[42])



import numpy as np

InputBasisFile = "basisFNY3es.txt" 

with open(InputBasisFile, "r") as InBasis:
     Basis = np.loadtxt(InBasis)
NumBas = Basis.shape[0]

def BProd(B1,B2):
   BP = 0.5*np.dot(B1[0:20],B2[0:20]) - 0.5*np.dot(B1[20:32],B2[20:32]) - np.dot(B1[32:48],B2[32:48])
   return BP
# Dot product of basis vectors
BP = np.zeros((NumBas,NumBas))
for i in range(NumBas):
    for k in range(NumBas):
        BP[i][k] = BProd(Basis[i],Basis[k])

def CreateGSOMat(ls1):
    matrix=np.zeros((11,11))
    
    matrix[0][0] = 1 #still applies?
    ls=[np.real(np.around(np.exp(1j*np.pi*x))) for x in ls1]
    #print(ls1)
    #print(ls)
    matrix[0][1]=ls[0]
    matrix[0][2]=ls[1]
    matrix[0][3]=ls[2]
    matrix[0][4]=ls[3]
    matrix[0][5]=ls[4]
    matrix[0][6]=ls[5]
    matrix[0][7]=ls[6]
    matrix[0][8]=ls[7]
    matrix[0][9]=ls[8]
    matrix[0][10]=ls[9]
    matrix[1][2]=ls[10]
    matrix[1][3]=ls[11]
    matrix[1][4]=ls[12]
    matrix[1][5]=ls[13]
    matrix[1][6]=ls[14]
    matrix[1][7]=ls[15]
    matrix[1][8]=ls[16]
    matrix[1][9]=ls[17]
    matrix[1][10]=ls[18]
    matrix[2][3]=ls[19]
    matrix[2][4]=ls[20]
    matrix[2][5]=ls[21]
    matrix[2][6]=ls[22]
    matrix[2][7]=ls[23]
    matrix[2][8]=ls[24]
    matrix[2][9]=ls[25]
    matrix[2][10]=ls[26]
    matrix[3][4]=ls[27]
    matrix[3][5]=ls[28]
    matrix[3][6]=ls[29]
    matrix[3][7]=ls[30]
    matrix[3][8]=ls[31]
    matrix[3][9]=ls[32]
    matrix[3][10]=ls[33]
    matrix[4][5]=ls[34]
    matrix[4][6]=ls[35]
    matrix[4][7]=ls[36]
    matrix[4][8]=ls[37]
    matrix[4][9]=ls[38]
    matrix[4][10]=ls[39]
    matrix[5][6]=ls[40]
    matrix[5][7]=ls[41]
    matrix[5][8]=ls[42]
    matrix[5][9]=ls[43]
    matrix[5][10]=ls[44]
    matrix[6][7]=ls[45]
    matrix[6][8]=ls[46]
    matrix[6][9]=ls[47]
    matrix[6][10]=ls[48]
    matrix[7][8]=ls[49]
    matrix[7][9]=ls[50]
    matrix[7][10]=ls[51]
    matrix[8][9]=ls[52]
    matrix[8][10]= ls[53]*1j
    matrix[9][10]=ls[54]
    
                
    #fix lower triangle 
    for i in range(0,11):
        for j in range(1,11):
            if (j>i):
                #matrix[i][j]=random.choice([-1,1])
                matrix[j][i]=np.real(np.around(np.exp(1j*np.pi*BP[i][j]/2)))*matrix[i][j]
            else:
                pass
    
    #fix diagonal
    for i in range(0,11):    
        matrix[i][i] = -np.real(np.around(np.exp(1j*np.pi*BP[i][i]/4))*matrix[i][0])
    #print("g.1 BP is:", BP[10][0])
    
    
    return matrix
mod1=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0]


def RandClass():
    countr=0
    tachfree=0
    for i in range(10000000000):
        #modl=createSUSYGSO()
        modl=createGSO()
        #susyphases=[0,10,11,12,13,14,15,16,17,18]
        notSUSY=checkNotSUSY(modl)
        if notSUSY==True:
        
            ##print(modl)
            tach=tachs(modl)
            if tach is False:
                tachfree+=1
                ###print("no tachs")
                gens=Gens3(modl)
                ##print(gens)
                if gens[0]-gens[2]==3 and gens[1]-gens[3]==3:
                    print("no susy, no tachs and 3 gen")
                    #print(modl)
                    if gens[2]>=1:#heavy higgs
                        #vecs=vects(modl)
                        #if vecs[0]>=1 and vecs[1]>=1:#light higgs
                        countr+=1
                            
        else: #probs susy
            pass
    #examp=[1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    #tachE=tachs(examp)
    #if tachE is False:
        
        ##print("no tachs")
        #gensE=Gens3(examp)
        ##print(gens)
        #if gensE[0]-gensE[2]==3 and gensE[1]-gensE[3]==3:
            ##print("no tachs and 3 gen for examp")
            #if gensE[2]>=1:#heavy higgs
                #vecsE=vects(examp)
                #if vecsE[0]>=1 and vecsE[1]>=1:#light higgs
                    #print("works for examp")
    return [tachfree,countr]

import timeit

start = timeit.default_timer()
#print(Gens3(GSOmodel))
#print(tachs(mod1))
#print(fromSMT60ls)
print(RandClass()) # Nonsusy: 10^8 in 20331.131143477003 secs=5.6 hours with no models found
stop = timeit.default_timer()
print("Time:", stop - start)


 