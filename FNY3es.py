from z3 import * 

#import itertools 

c = [Bool('c%s' % (i)) for i in range(55)] 

 

#c[0]=1 S, c[1 ]=1 e2, c[2 ]=1 e4, c[3 ]=1 e5, c[4 ]=1 b1, c[5 ]=1 b2, c[6 ]=1 b3, c[7 ]=1 z1, c[8 ]=1 x, c[9 ]=1 g 

#          c[10]=S e2, c[11]=S e4, c[12]=S e5, c[13]=S b1, c[14]=S b2, c[15]=S b3, c[16]=S z1, c[17]=S x, c[18]=S g  

#                      c[19]=e2e4, c[20]=e2e5, c[21]=e2b1, c[22]=e2b2, c[23]=e2b3, c[24]=e2z1, c[25]=e2x, c[26]=e2g,

#                                  c[27]=e4e5, c[28]=e4b1, c[29]=e4b2, c[30]=e4b3, c[31]=e4z1, c[32]=e4x, c[33]=e4g   

#                                              c[34]=e5b1, c[35]=e5b2, c[36]=e5b3, c[37]=e5z1, c[38]=e5x, c[39]=e5g, 

#                                                          c[40]=b1b2, c[41]=b1b3, c[42]=b1z1, c[43]=b1x, c[44]=b1g,

#                                                                      c[45]=b2b3, c[46]=b2z1, c[47]=b2x, c[48]=b2g,
                                                                                                                       
#                                                                                  c[49]=b3z1, c[50]=b3x, c[51]=b3g
 
#                                                                                              c[52]=z1x, c[53]=z1g

#                                                                                                         c[54]=xg

#  parity function
#  break up long input lists in two smaller lists

def MXor(ls): #solver,
    if len(ls) == 1:
        return ls[0]
    elif len(ls) == 2:
        return Xor(ls[0], ls[1])
    elif len(ls) == 3:
        return Xor(ls[0], Xor(ls[1], ls[2]))
    elif len(ls) == 4:
        #  this symmetric form is much faster than the chained forms
        return Xor(Xor(ls[0], ls[1]), Xor(ls[2], ls[3]))
    else:
        cut_len = len(ls) // 2
        return Xor(MXor(ls[:cut_len]), MXor(ls[cut_len:]))


s = Solver() # create a solver s 

#implement SUSY
#s.add(And(c[0]==True,c[10]==True, c[11]==True, c[12]==True,c[13]==True,c[14]==True,c[15]==True,c[16]==True,c[17]==True,c[18]==True))
#implement not close to susyness
s.add(Not(And(c[10]==True, c[11]==True, c[12]==True,c[16]==True,c[17]==True,c[18]==True)))

#B1_pqrs projectors
#pqrs=0000
#N16s=0
#N16bars=0
B1_0000=And(c[21],c[42],MXor([c[40],c[41],c[42]]),c[43])
B1_0000_n10=And(B1_0000,c[40],c[44])#chirality phase (b1)(b2)
B1_0000_n5bar=And(B1_0000,c[40],Not(c[44]))#
B1_0000_n10bar=And(B1_0000,Not(c[40]),c[44])#
B1_0000_n5=And(B1_0000,Not(c[40]),Not(c[44]))#
# c[44] b1 g
#0010
B1_0010=And(MXor([c[21],c[20]]),MXor([c[42],c[37]]),MXor([c[40],c[41],c[42],c[3],c[34],c[35],c[36],c[37]]),MXor([c[43],c[38]]))
B1_0010_n10=And(B1_0010,MXor([True,c[40],c[34],c[35],c[3]]),Xor(c[44],c[39])) #chirality phase (b1+e5)(b2+e5)
B1_0010_n5bar=And(B1_0010,MXor([True,c[40],c[34],c[35],c[3]]),Not(Xor(c[44],c[39])))
B1_0010_n10bar=And(B1_0010,Not(MXor([True,c[40],c[34],c[35],c[3]])),Xor(c[44],c[39])) 
B1_0010_n5=And(B1_0010,Not(MXor([True,c[40],c[34],c[35],c[3]])),Not(Xor(c[44],c[39])))

#0100
B1_0100=And(MXor([c[21],c[19]]),MXor([c[42],c[31]]),MXor([c[40],c[41],c[42],c[2],c[28],c[29],c[30],c[31]]),MXor([c[43],c[32]]))
B1_0100_n10=And(B1_0100,MXor([True,c[40],c[29]]),Xor(c[44],c[33])) #chirality phase (b1+e4)(b2)
B1_0100_n5bar=And(B1_0100,MXor([True,c[40],c[29]]),Not(Xor(c[44],c[33])))
B1_0100_n10bar=And(B1_0100,Not(MXor([True,c[40],c[29]])),Xor(c[44],c[33]))
B1_0100_n5=And(B1_0100,Not(MXor([True,c[40],c[29]])),Not(Xor(c[44],c[33])))

#0110
B1_0110=And(MXor([c[21],c[19],c[20]]),MXor([c[42],c[31],c[37]]),\
    MXor([c[40],c[41],c[42],c[2],c[3],c[28],c[29],c[30],c[31],c[34],c[35],c[36],c[37]]),MXor([c[43],c[32],c[38]]))
B1_0110_n10=And(B1_0110,MXor([True,c[40],c[29],c[3],c[34],c[35]]),MXor([c[44],c[33],c[39]])) #chirality phase (b1+e4+e5)(b2+e5)
B1_0110_n5bar=And(B1_0110,MXor([True,c[40],c[29],c[3],c[34],c[35]]),Not(MXor([c[44],c[33],c[39]])))
B1_0110_n10bar=And(B1_0110,Not(MXor([True,c[40],c[29],c[3],c[34],c[35]])),MXor([c[44],c[33],c[39]]))
B1_0110_n5=And(B1_0110,Not(MXor([True,c[40],c[29],c[3],c[34],c[35]])),Not(MXor([c[44],c[33],c[39]])))

#s.add(Sum([If(projBools[i],1,0) for i in range(len(projBools))]) >= 6)

#B2
#pqrs=0000
B2_0000=And(c[29],c[46],MXor([c[40],c[45],c[46]]),c[47])
B2_0000_n10=And(B2_0000,c[40],c[48])#chirality phase (b1)(b2)
B2_0000_n5bar=And(B2_0000,c[40],Not(c[48]))
B2_0000_n10bar=And(B2_0000,Not(c[40]),c[48])
B2_0000_n5=And(B2_0000,Not(c[40]),Not(c[48]))

#c[48] b2g
#0010
B2_0010=And(MXor([c[29],c[27]]),MXor([c[46],c[37]]),MXor([c[40],c[45],c[46],c[3],c[34],c[35],c[36],c[37]]),MXor([c[47],c[38]]))
B2_0010_n10=And(B2_0010,MXor([True,c[40],c[34],c[35],c[3]]),Xor(c[48],c[39])) #chirality phase (b2+e5)(b1+e5)
B2_0010_n5bar=And(B2_0010,MXor([True,c[40],c[34],c[35],c[3]]),Not(Xor(c[48],c[39])))
B2_0010_n10bar=And(B2_0010,Not(MXor([True,c[40],c[34],c[35],c[3]])),Xor(c[48],c[39]))
B2_0010_n5=And(B2_0010,Not(MXor([True,c[40],c[34],c[35],c[3]])),Not(Xor(c[48],c[39])))

#0100
B2_0100=And(MXor([c[29],c[19]]),MXor([c[46],c[24]]),MXor([c[40],c[45],c[46],c[1],c[21],c[22],c[23],c[24]]),MXor([c[47],c[25]]))
B2_0100_n10=And(B2_0100,MXor([True,c[40],c[21]]),Xor(c[48],c[26])) #chirality phase (b2+e2)(b1)
B2_0100_n5bar=And(B2_0100,MXor([True,c[40],c[21]]),Not(Xor(c[48],c[26])))
B2_0100_n10bar=And(B2_0100,Not(MXor([True,c[40],c[21]])),Xor(c[48],c[26]))
B2_0100_n5=And(B2_0100,Not(MXor([True,c[40],c[21]])),Not(Xor(c[48],c[26])))

#0110
B2_0110=And(MXor([c[29],c[19],c[27]]),MXor([c[46],c[24],c[37]]),\
    MXor([c[40],c[45],c[46],c[1],c[3],c[21],c[22],c[23],c[24],c[34],c[35],c[36],c[37]]),MXor([c[47],c[25],c[38]]))
B2_0110_n10=And(B2_0110,MXor([True,c[40],c[21],c[3],c[20],c[34],c[35]]),MXor([c[48],c[26],c[39]])) #chirality phase (b2+e2+e5)(b1+e5)
B2_0110_n5bar=And(B2_0110,MXor([True,c[40],c[21],c[3],c[20],c[34],c[35]]),Not(MXor([c[48],c[26],c[39]])))
B2_0110_n10bar=And(B2_0110,Not(MXor([True,c[40],c[21],c[3],c[20],c[34],c[35]])),MXor([c[48],c[26],c[39]]))
B2_0110_n5=And(B2_0110,Not(MXor([True,c[40],c[21],c[3],c[20],c[34],c[35]])),Not(MXor([c[48],c[26],c[39]])))

# define 4 B3 projectors 

#pqrs=0000
B3_0000=And(c[36],c[49],MXor([c[41],c[45],c[49]]),c[50])
B3_0000_n10=And(B3_0000,c[41],c[51])#chirality phase (b1)(b3)
B3_0000_n5bar=And(B3_0000,c[41],Not(c[51]))
B3_0000_n10bar=And(B3_0000,Not(c[41]),c[51])
B3_0000_n5=And(B3_0000,Not(c[41]),Not(c[51]))

#c[51] b3g
#0001
B3_0001=And(MXor([c[36],c[27]]),MXor([c[49],c[37]]),MXor([c[41],c[45],c[49],c[2],c[28],c[29],c[30],c[31]]),MXor([c[50],c[32]]))
B3_0001_n10=And(B3_0001,MXor([True,c[41],c[2],c[30],c[28]]),Xor(c[51],c[33])) #chirality phase (b3+e4)(b1+e4)
B3_0001_n5bar=And(B3_0001,MXor([True,c[41],c[2],c[30],c[28]]),Not(Xor(c[51],c[33])))
B3_0001_n10bar=And(B3_0001,Not(MXor([True,c[41],c[2],c[30],c[28]])),Xor(c[51],c[33]))
B3_0001_n5=And(B3_0001,Not(MXor([True,c[41],c[2],c[30],c[28]])),Not(Xor(c[51],c[33])))

#0100
B3_0100=And(MXor([c[36],c[20]]),MXor([c[49],c[24]]),MXor([c[41],c[45],c[49],c[1],c[21],c[22],c[23],c[24]]),MXor([c[50],c[25]]))
B3_0100_n10=And(B3_0100,MXor([True,c[41],c[21]]),Xor(c[51],c[26])) #chirality phase (b3+e2)(b1)
B3_0100_n5bar=And(B3_0100,MXor([True,c[41],c[21]]),Not(Xor(c[51],c[26])))
B3_0100_n10bar=And(B3_0100,Not(MXor([True,c[41],c[21]])),Xor(c[51],c[26]))
B3_0100_n5=And(B3_0100,Not(MXor([True,c[41],c[21]])),Not(Xor(c[51],c[26])))

#0101
B3_0101=And(MXor([c[36],c[20],c[27]]),MXor([c[49],c[24],c[37]]),\
    MXor([c[41],c[45],c[49],c[2],c[1],c[28],c[29],c[30],c[31],c[21],c[22],c[23],c[24]]),MXor([c[50],c[25],c[32]]))
B3_0101_n10=And(B3_0101,MXor([True,c[41],c[21],c[28],c[30],c[2],c[19]]),MXor([c[51],c[26],c[33]])) #chirality phase (b3+e2+e4)(b1+e4)
B3_0101_n5bar=And(B3_0101,MXor([True,c[41],c[21],c[28],c[30],c[2],c[19]]),Not(MXor([c[51],c[26],c[33]])))
B3_0101_n10bar=And(B3_0101,Not(MXor([True,c[41],c[21],c[28],c[30],c[2],c[19]])),MXor([c[51],c[26],c[33]]))
B3_0101_n5=And(B3_0101,Not(MXor([True,c[41],c[21],c[28],c[30],c[2],c[19]])),Not(MXor([c[51],c[26],c[33]])))

n10s=[B1_0000_n10,B1_0010_n10,B1_0100_n10,B1_0110_n10,\
        B2_0000_n10,B2_0010_n10,B2_0100_n10,B2_0110_n10,\
        B3_0000_n10,B3_0001_n10,B3_0100_n10,B3_0101_n10] 

n5bars= [B1_0000_n5bar,B1_0010_n5bar,B1_0100_n5bar,B1_0110_n5bar,\
        B2_0000_n5bar,B2_0010_n5bar,B2_0100_n5bar,B2_0110_n5bar,\
        B3_0000_n5bar,B3_0001_n5bar,B3_0100_n5bar,B3_0101_n5bar]

n10bars=[B1_0000_n10bar,B1_0010_n10bar,B1_0100_n10bar,B1_0110_n10bar,\
        B2_0000_n10bar,B2_0010_n10bar,B2_0100_n10bar,B2_0110_n10bar,\
        B3_0000_n10bar,B3_0001_n10bar,B3_0100_n10bar,B3_0101_n10bar] 

n5s=[B1_0000_n5,B1_0010_n5,B1_0100_n5,B1_0110_n5,\
        B2_0000_n5,B2_0010_n5,B2_0100_n5,B2_0110_n5,\
        B3_0000_n5,B3_0001_n5,B3_0100_n5,B3_0101_n5]

#s.add(Sum([If(projBools[i],1,0) for i in range(len(projBools))]) >= 6)
#print(N16s)
s.add(Sum([If(n10s[i],1,0) for i in range(len(n10s))])-Sum([If(n10bars[i],1,0) for i in range(len(n10bars))]) == 3) 
s.add(Sum([If(n5bars[i],1,0) for i in range(len(n5bars))])-Sum([If(n5s[i],1,0) for i in range(len(n5s))]) == 3) 

s.add(Sum([If(n10bars[i],1,0) for i in range(len(n10bars))]) >= 1) 

#VECTORIALS V1_pqrs projectors
#pqrs=0000
#NHs=0
V1_0000=And(MXor([True,c[10],c[21],c[25]]),MXor([True,c[16],c[42],c[52]]),MXor([True, c[0],c[13],c[14],c[15],c[16],\
    c[40],c[41],c[42],c[8],c[43],c[47],c[50],c[52]]),MXor([True,c[17],c[43],c[8]]))

V1_0000_5v=And(V1_0000,MXor([True,c[14],c[40],c[47]]),MXor([c[18],c[44],c[54]]))#chirality phase (S+b1+x)(b2)
V1_0000_5barv=And(V1_0000,MXor([True,c[14],c[40],c[47]]),Not(MXor([c[18],c[44],c[54]])))

#0010
V1_0010=And(MXor([True,c[10],c[21],c[25],c[20]]),MXor([True,c[16],c[42],c[52],c[37]]),MXor([True, c[0],c[13],c[14],c[15],c[16],\
    c[40],c[41],c[42],c[8],c[43],c[47],c[50],c[52],\
    c[3],c[34],c[35],c[36],c[37]]),MXor([True,c[17],c[43],c[8],c[38]]))

V1_0010_5v=And(V1_0010,MXor([True,c[14],c[40],c[47],c[35],c[12],c[34],c[38],c[3]]),MXor([c[18],c[44],c[54],c[39]]))#chirality phase (S+b1+x+e5)(b2+e5)
V1_0010_5barv=And(V1_0010,MXor([True,c[14],c[40],c[47],c[35],c[12],c[34],c[38],c[3]]),Not(MXor([c[18],c[44],c[54],c[39]])))

#0100
V1_0100=And(MXor([True,c[10],c[21],c[25],c[19]]),MXor([True,c[16],c[42],c[52],c[31]]),MXor([True, c[0],c[13],c[14],c[15],c[16],\
    c[40],c[41],c[42],c[8],c[43],c[47],c[50],c[52],\
    c[2],c[28],c[29],c[30],c[31]]),MXor([True,c[17],c[43],c[8],c[32]]))

V1_0100_5v=And(V1_0100,MXor([True,c[14],c[40],c[47],c[29]]),MXor([c[18],c[44],c[54],c[33]]))#chirality phase (S+b1+x+e5)(b2+e5)
V1_0100_5barv=And(V1_0100,MXor([True,c[14],c[40],c[47],c[29]]),Not(MXor([c[18],c[44],c[54],c[33]])))

#0110
V1_0110=And(MXor([True,c[10],c[21],c[25],c[20],c[19]]),MXor([True,c[16],c[42],c[52],c[31],c[37]]),MXor([True, c[0],c[13],c[14],c[15],c[16],\
    c[40],c[41],c[42],c[8],c[43],c[47],c[50],c[52],\
    c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]]),MXor([True,c[17],c[43],c[8],c[38],c[32]]))

V1_0110_5v=And(V1_0110,MXor([c[14],c[40],c[47],c[24],c[35],c[12],c[34],c[38],c[27],c[3]]),MXor([c[18],c[44],c[54],c[39]]))#chirality phase (S+b1+x+e5)(b2+e5)
V1_0110_5barv=And(V1_0110,MXor([c[14],c[40],c[47],c[24],c[35],c[12],c[34],c[38],c[27],c[3]]),Not(MXor([c[18],c[44],c[54],c[33],c[39]])))


#V2
#pqrs=0000
V2_0000=And(MXor([True,c[11],c[29],c[32]]),MXor([True,c[16],c[46],c[52]]),MXor([True, c[0],c[13],c[14],c[15],c[16],\
    c[40],c[45],c[46],c[8],c[43],c[47],c[50],c[52]]),MXor([c[17],c[47],c[8]]))

V2_0000_5v=And(V2_0000,MXor([True,c[13],c[40],c[43]]),MXor([c[18],c[48],c[54]]))
V2_0000_5barv=And(V2_0000,MXor([True,c[13],c[40],c[43]]),MXor([True,c[18],c[48],c[54]]))
#V2_0000_16=And(B2_0000,c[40])#chirality phase (b1)(b2)

#0010
V2_0010=And(MXor([True,c[11],c[29],c[32],c[27]]),MXor([True,c[16],c[46],c[52],c[37]]),MXor([True, c[0],c[13],c[14],c[15],c[16],\
    c[40],c[45],c[46],c[8],c[43],c[47],c[50],c[52],c[3],c[34],c[35],c[36],c[37]]),MXor([c[17],c[47],c[8],c[38]]))

V2_0010_5v=And(V2_0010,MXor([True,c[13],c[40],c[43],c[34],c[12],c[35],c[38],c[3]]),MXor([c[18],c[48],c[54],c[39]]))
V2_0010_5barv=And(V2_0010,MXor([True,c[13],c[40],c[43],c[34],c[12],c[35],c[38],c[3]]),MXor([True,c[18],c[48],c[54],c[39]]))

#0100
V2_0100=And(MXor([True,c[11],c[29],c[32],c[19]]),MXor([True,c[16],c[46],c[52],c[24]]),MXor([True, c[0],c[13],c[14],c[15],c[16],\
    c[40],c[45],c[46],c[8],c[43],c[47],c[50],c[52],c[1],c[21],c[22],c[23],c[24]]),MXor([c[17],c[47],c[8],c[25]]))

V2_0100_5v=And(V2_0100,MXor([True,c[13],c[40],c[43],c[21]]),MXor([c[18],c[48],c[54],c[26]]))
V2_0100_5barv=And(V2_0100,MXor([True,c[13],c[40],c[43],c[21]]),MXor([True,c[18],c[48],c[54],c[26]]))

#0110
V2_0110=And(MXor([True,c[11],c[29],c[32],c[19],c[27]]),MXor([c[46],c[52],c[24],c[37]]),\
    MXor([c[40],c[45],c[46],c[8],c[43],c[47],c[50],c[52],c[2],c[3],c[28],c[29],c[30],c[31],c[34],c[35],c[36],c[37]]),MXor([c[47],c[8],c[25],c[38]]))

V2_0110_5v=And(V2_0110,MXor([c[13],c[40],c[43],c[21],c[34],c[12],c[35],c[38],c[3],c[20]]),MXor([c[18],c[48],c[54],c[26],c[39]]))
V2_0110_5barv=And(V2_0110,MXor([c[13],c[40],c[43],c[21],c[34],c[12],c[35],c[38],c[3],c[20]]),MXor([True,c[18],c[48],c[54],c[26],c[39]]))

# define 4 V3 projectors 

#pqrs=0000
V3_0000=And(MXor([True,c[12],c[36],c[38]]),MXor([True,c[16],c[49],c[52]]),MXor([c[0],c[13],c[14],c[15],c[16],\
    c[41],c[45],c[49],c[8],c[43],c[47],c[50],c[52]]),MXor([True,c[17],c[50],c[8]]))

V3_0000_5v=And(V3_0000,MXor([True,c[13],c[41],c[43]]),MXor([True,c[18],c[51],c[54]]))
V3_0000_5barv=And(V3_0000,MXor([True,c[13],c[41],c[43]]),MXor([c[18],c[51],c[54]]))

#0001
V3_0001=And(MXor([True,c[12],c[36],c[38],c[27]]),MXor([True,c[16],c[49],c[52],c[37]]),MXor([c[0],c[13],c[14],c[15],c[16],\
    c[41],c[45],c[49],c[8],c[43],c[47],c[50],c[52],c[2],c[28],c[29],c[30],c[31]]),MXor([True,c[17],c[50],c[8],c[32]]))

V3_0001_5v=And(V3_0001,MXor([True,c[13],c[41],c[43],c[28],c[11],c[30],c[32],c[2]]),MXor([True,c[18],c[51],c[54],c[33]]))
V3_0001_5barv=And(V3_0001,MXor([True,c[13],c[41],c[43],c[28],c[11],c[30],c[32],c[2]]),MXor([c[18],c[51],c[54],c[33]]))

#0100
V3_0100=And(MXor([True,c[12],c[36],c[38],c[19]]),MXor([True,c[16],c[49],c[52],c[24]]),MXor([c[0],c[13],c[14],c[15],c[16],\
    c[41],c[45],c[49],c[8],c[43],c[47],c[50],c[52],c[1],c[21],c[22],c[23],c[24]]),MXor([True,c[17],c[50],c[8],c[25]]))

V3_0100_5v=And(V3_0100,MXor([True,c[13],c[41],c[43],c[21]]),MXor([True,c[18],c[51],c[54],c[26]]))
V3_0100_5barv=And(V3_0100,MXor([True,c[13],c[41],c[43],c[21]]),MXor([c[18],c[51],c[54],c[26]]))

#0101
V3_0101=And(MXor([c[29],c[38],c[19],c[27]]),MXor([c[46],c[52],c[24],c[37]]),\
    MXor([c[41],c[45],c[49],c[8],c[43],c[47],c[50],c[52],c[2],c[3],c[28],c[29],c[30],c[31],c[34],c[35],c[36],c[37]]),MXor([c[50],c[8],c[25],c[32]]))

V3_0101=And(MXor([True,c[12],c[36],c[38],c[19],c[27]]),MXor([True,c[16],c[49],c[52],c[24],c[37]]),MXor([c[0],c[13],c[14],c[15],c[16],\
    c[41],c[45],c[49],c[8],c[43],c[47],c[50],c[52],c[1],c[21],c[22],c[23],c[24],\
    c[2],c[28],c[29],c[30],c[31]]),MXor([True,c[17],c[50],c[8],c[25],c[32]]))

V3_0101_5v=And(V3_0101,MXor([True,c[13],c[41],c[43],c[21],c[28],c[11],c[30],c[32],c[2]]),MXor([True,c[18],c[51],c[54],c[26],c[33]]))
V3_0101_5barv=And(V3_0101,MXor([True,c[13],c[41],c[43],c[21],c[28],c[11],c[30],c[32],c[19],c[2]]),MXor([c[18],c[51],c[54],c[26],c[33]]))

n5vs=   [V1_0000_5v,V1_0010_5v,V1_0100_5v,V1_0110_5v,\
        V2_0000_5v,V2_0010_5v,V2_0100_5v,V2_0110_5v,\
        V3_0000_5v,V3_0001_5v,V3_0100_5v,V3_0101_5v]

n5barvs=   [V1_0000_5barv,V1_0010_5barv,V1_0100_5barv,V1_0110_5barv,\
        V2_0000_5barv,V2_0010_5barv,V2_0100_5barv,V2_0110_5barv,\
        V3_0000_5barv,V3_0001_5barv,V3_0100_5barv,V3_0101_5barv]            


#Higgs constraints- not necessary(?) since untwisted higgs...
#s.add(Sum([If(n5vs[i],1,0) for i in range(len(n5vs))]) >= 1)      
#s.add(Sum([If(n5barvs[i],1,0) for i in range(len(n5barvs))]) >= 1)     

#TACHYONS
#Vectorials
#e2 { }, projs: S,e4,e5,z1,z2,x,b1,g,
#y1w6  oscillator case
y1e2=And(Not(c[10]),Not(c[19]),Not(c[20]),Not(c[24]),Not(MXor([c[1],c[21],c[22],c[23],c[24]])),Not(c[25]),Not(c[21]),c[26])
#w1w3,...
w1e2=And(Not(c[10]),Not(c[19]),Not(c[20]),Not(c[24]),Not(MXor([c[1],c[21],c[22],c[23],c[24]])),Not(c[25]),Not(c[21]),Not(c[26]))
#y3y6
y3e2=And(Not(c[10]),Not(c[19]),Not(c[20]),Not(c[24]),Not(MXor([c[1],c[21],c[22],c[23],c[24]])),Not(c[25]),c[21],c[26])
#ybar4...
y4e2=And(Not(c[10]),c[19],Not(c[20]),Not(c[24]),Not(MXor([c[1],c[21],c[22],c[23],c[24]])),Not(c[25]),c[21],Not(c[26]))
#y5...
y5e2=And(Not(c[10]),Not(c[19]),c[20],Not(c[24]),Not(MXor([c[1],c[21],c[22],c[23],c[24]])),Not(c[25]),c[21],Not(c[26]))

#y6w6e2=And(Not(c[19]),Not(c[20]),Not(c[24]),Not(MXor([c[1],c[21],c[22],c[23],c[24]])),Not(c[25]),c[21],c[26])
#psi,eta1
#psie2=And(Not(c[10]),Not(c[19]),Not(c[20]),Not(c[24]),Not(MXor([c[1],c[21],c[22],c[23],c[24]])),c[25],c[21],c[26])
#eta23
#eta23e2=And(Not(c[10]),Not(c[19]),Not(c[20]),Not(c[24]),Not(MXor([c[1],c[21],c[22],c[23],c[24]])),c[25],Not(c[21]),c[26])
#phi12
#phi1e2=And(Not(c[10]),Not(c[19]),Not(c[20]),c[24],Not(MXor([c[1],c[21],c[22],c[23],c[24]])),Not(c[25]),Not(c[21]),c[26])
#phi34
phi3e2=And(Not(c[10]),Not(c[19]),Not(c[20]),c[24],Not(MXor([c[1],c[21],c[22],c[23],c[24]])),Not(c[25]),Not(c[21]),Not(c[26]))
#phi58
phi5e2=And(Not(c[10]),Not(c[19]),Not(c[20]),Not(c[24]),MXor([c[1],c[21],c[22],c[23],c[24]]),Not(c[25]),Not(c[21]),Not(c[26]))
#phi67
#phi6e2=And(Not(c[10]),Not(c[19]),Not(c[20]),Not(c[24]),MXor([c[1],c[21],c[22],c[23],c[24]]),Not(c[25]),Not(c[21]),c[26])

s.add(And(Not(y1e2),Not(y3e2),Not(y4e2),Not(y5e2),Not(phi5e2),Not(phi3e2)))

#e4 { }, projs: S,e2,e5,z1,z2,x,b2,g
#y1w1 oscillator case
y1e4=And(Not(c[11]),Not(c[19]),Not(c[27]),Not(c[31]),Not(MXor([c[2],c[28],c[29],c[30],c[31]])),Not(c[32]),c[29],c[33])
#y2
y2e4=And(Not(c[11]),c[19],Not(c[27]),Not(c[31]),Not(MXor([c[2],c[28],c[29],c[30],c[31]])),Not(c[32]),c[29],Not(c[33]))
#y3 (w3 same as y1w1)
y3e4=And(Not(c[11]),Not(c[19]),Not(c[27]),Not(c[31]),Not(MXor([c[2],c[28],c[29],c[30],c[31]])),Not(c[32]),Not(c[29]),c[33])
#y5
y5e4=And(Not(c[11]),Not(c[19]),c[27],Not(c[31]),Not(MXor([c[2],c[28],c[29],c[30],c[31]])),Not(c[32]),Not(c[29]),Not(c[33]))
#y6 same as...
#psi,eta2
#psie4=And(Not(c[11]),Not(c[19]),Not(c[27]),Not(c[31]),Not(MXor([c[2],c[28],c[29],c[30],c[31]])),c[32],c[29],c[33])
#eta13
#eta13e4=And(Not(c[11]),Not(c[19]),Not(c[27]),Not(c[31]),Not(MXor([c[2],c[28],c[29],c[30],c[31]])),c[32],Not(c[29]),c[33])
#phi12
#phi1e4=And(Not(c[11]),Not(c[19]),Not(c[27]),c[31],Not(MXor([c[2],c[28],c[29],c[30],c[31]])),Not(c[32]),Not(c[29]),c[33])
#phi34
phi3e4=And(Not(c[11]),Not(c[19]),Not(c[27]),c[31],Not(MXor([c[2],c[28],c[29],c[30],c[31]])),Not(c[32]),Not(c[29]),Not(c[33]))
#phi58
phi5e4=And(Not(c[11]),Not(c[19]),Not(c[27]),Not(c[31]),MXor([c[2],c[28],c[29],c[30],c[31]]),Not(c[32]),Not(c[29]),Not(c[33]))
#phi58
#phi6e4=And(Not(c[11]),Not(c[19]),Not(c[27]),Not(c[31]),MXor([c[2],c[28],c[29],c[30],c[31]]),Not(c[32]),Not(c[29]),c[33])

s.add(And(Not(y1e4),Not(y2e4),Not(y3e4),Not(y5e4),Not(phi5e4),Not(phi3e4)))

#e5 { }, projs: e2,e4,z1,z2,x,b3,g
#y1w1 oscillator case
y1e5=And(Not(c[12]),Not(c[20]),Not(c[27]),Not(c[37]),Not(MXor([c[3],c[34],c[35],c[36],c[37]])),Not(c[38]),c[36],c[39])
#y2
y2e5=And(Not(c[12]),c[20],Not(c[27]),Not(c[37]),Not(MXor([c[3],c[34],c[35],c[36],c[37]])),Not(c[38]),c[36],Not(c[39]))
#y3 (w3 same as y1w1)
#y3e5=And(Not(c[20]),Not(c[27]),Not(c[37]),Not(MXor([c[3],c[34],c[35],c[36],c[37]])),Not(c[38]),c[36])
#y4
y4e5=And(Not(c[12]),Not(c[20]),c[27],Not(c[37]),Not(MXor([c[3],c[34],c[35],c[36],c[37]])),Not(c[38]),c[36],Not(c[39]))
#y6
y6e5=And(Not(c[12]),Not(c[20]),Not(c[27]),Not(c[37]),Not(MXor([c[3],c[34],c[35],c[36],c[37]])),Not(c[38]),Not(c[36]),c[39])
#psi,eta3
#psie5=And(Not(c[12]),Not(c[20]),Not(c[27]),Not(c[37]),Not(MXor([c[3],c[34],c[35],c[36],c[37]])),c[38],c[36],c[39])
#eta12
#eta23e5=And(Not(c[12]),Not(c[20]),Not(c[27]),Not(c[37]),Not(MXor([c[3],c[34],c[35],c[36],c[37]])),c[38],Not(c[36]),c[39])
#phi12
#phi1e5=And(Not(c[12]),Not(c[20]),Not(c[27]),c[37],Not(MXor([c[3],c[34],c[35],c[36],c[37]])),Not(c[38]),Not(c[36]),c[39])
#phi34
phi3e5=And(Not(c[12]),Not(c[20]),Not(c[27]),c[37],Not(MXor([c[3],c[34],c[35],c[36],c[37]])),Not(c[38]),Not(c[36]),Not(c[39]))
#phi58
phi5e5=And(Not(c[12]),Not(c[20]),Not(c[27]),Not(c[37]),MXor([c[3],c[34],c[35],c[36],c[37]]),Not(c[38]),Not(c[36]))
#phi67
#phi6e5=And(Not(c[12]),Not(c[20]),Not(c[27]),Not(c[37]),MXor([c[3],c[34],c[35],c[36],c[37]]),Not(c[38]),c[36])

s.add(And(Not(y1e5),Not(y2e5),Not(y4e5),Not(y6e5),Not(phi5e5),Not(phi3e5)))

#e2+e4
#yw not y5w5
e2e4yw=And(Not(MXor([True,c[10],c[11]])),Not(Xor(c[20],c[27])),Not(Xor(c[24],c[31])),\
    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31]])),Not(Xor(c[25],c[32])),Xor(c[26],c[33]))
    
e2e4yw5=And(Not(MXor([True,c[10],c[11]])),Xor(c[20],c[27]),Not(Xor(c[24],c[31])),\
    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31]])),Not(Xor(c[25],c[32])),Not(Xor(c[26],c[33])))

#e2e4psieta=And(Not(MXor([True,c[10],c[11]])),Not(Xor(c[20],c[27])),Not(Xor(c[24],c[31])),\
#    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31]])),Xor(c[25],c[32]),Xor(c[26],c[33]))

#e2e4phi1=And(Not(MXor([True,c[10],c[11]])),Not(Xor(c[20],c[27])),Xor(c[24],c[31]),\
#    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31]])),Not(Xor(c[25],c[32])),Xor(c[26],c[33]))

e2e4phi3=And(Not(MXor([True,c[10],c[11]])),Not(Xor(c[20],c[27])),Xor(c[24],c[31]),\
    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31]])),Not(Xor(c[25],c[32])),Not(Xor(c[26],c[33])))

e2e4phi5=And(Not(MXor([True,c[10],c[11]])),Not(Xor(c[20],c[27])),Not(Xor(c[24],c[31])),\
    MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31]]),Not(Xor(c[25],c[32])),Not(Xor(c[26],c[33])))

#e2e4phi6=And(Not(MXor([True,c[10],c[11]])),Not(Xor(c[20],c[27])),Not(Xor(c[24],c[31])),\
#    MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31]]),Not(Xor(c[25],c[32])),Xor(c[26],c[33]))

s.add(And(Not(e2e4yw),Not(e2e4yw5),Not(e2e4phi5),Not(e2e4phi3)))

#e2+e5
#yw not y4w4
e2e5yw=And(Not(MXor([True,c[10],c[12]])),Not(Xor(c[19],c[27])),Not(Xor(c[24],c[37])),\
    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[3],c[34],c[35],c[36],c[37]])),Not(Xor(c[25],c[38])),Xor(c[26],c[39]))
    
e2e5yw4=And(Not(MXor([True,c[10],c[12]])),Xor(c[19],c[27]),Not(Xor(c[24],c[37])),\
    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[3],c[34],c[35],c[36],c[37]])),Not(Xor(c[25],c[38])),Not(Xor(c[26],c[39])))

#e2e5psieta=And(Not(MXor([True,c[10],c[12]])),Not(Xor(c[19],c[27])),Not(Xor(c[24],c[37])),\
    #Not(MXor([c[1],c[21],c[22],c[23],c[24],c[3],c[34],c[35],c[36],c[37]])),Xor(c[25],c[38]),Xor(c[26],c[39]))

#e2e5phi1=And(Not(MXor([True,c[10],c[12]])),Not(Xor(c[19],c[27])),Xor(c[24],c[37]),\
#    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[3],c[34],c[35],c[36],c[37]])),Not(Xor(c[25],c[38])),Xor(c[26],c[39]))

e2e5phi3=And(Not(MXor([True,c[10],c[12]])),Not(Xor(c[19],c[27])),Xor(c[24],c[37]),\
    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[3],c[34],c[35],c[36],c[37]])),Not(Xor(c[25],c[38])),Not(Xor(c[26],c[39])))

e2e5phi5=And(Not(MXor([True,c[10],c[12]])),Not(Xor(c[19],c[27])),Not(Xor(c[24],c[37])),\
    MXor([c[1],c[21],c[22],c[23],c[24],c[3],c[34],c[35],c[36],c[37]]),Not(Xor(c[25],c[38])),Not(Xor(c[26],c[39])))

#e2e5phi6=And(Not(MXor([True,c[10],c[12]])),Not(Xor(c[19],c[27])),Not(Xor(c[24],c[37])),\
#    MXor([c[1],c[21],c[22],c[23],c[24],c[3],c[34],c[35],c[36],c[37]]),Not(Xor(c[25],c[38])),Xor(c[26],c[39]))

s.add(And(Not(e2e5yw),Not(e2e5yw4),Not(e2e5phi5),Not(e2e5phi3)))

#e4+e5
#yw not y2w2
e4e5yw=And(Not(MXor([True,c[11],c[12]])),Not(Xor(c[19],c[20])),Not(Xor(c[31],c[37])),\
    Not(MXor([c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]])),Not(Xor(c[32],c[38])),Xor(c[33],c[39]))
    
e4e5yw2=And(Not(MXor([True,c[11],c[12]])),Xor(c[19],c[20]),Not(Xor(c[31],c[37])),\
    Not(MXor([c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]])),Not(Xor(c[32],c[38])),Not(Xor(c[33],c[39])))

#e4e5psieta=And(Not(MXor([True,c[11],c[12]])),Not(Xor(c[19],c[20])),Not(Xor(c[31],c[37])),\
    #Not(MXor([c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]])),Xor(c[32],c[38]),Xor(c[33],c[39]))

#e4e5phi1=And(Not(MXor([True,c[11],c[12]])),Not(Xor(c[19],c[20])),Xor(c[31],c[37]),\
    #Not(MXor([c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]])),Not(Xor(c[32],c[38])),Xor(c[33],c[39]))

e4e5phi3=And(Not(MXor([True,c[11],c[12]])),Not(Xor(c[19],c[20])),Xor(c[31],c[37]),\
    Not(MXor([c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]])),Not(Xor(c[32],c[38])),Not(Xor(c[33],c[39])))

e4e5phi5=And(Not(MXor([True,c[11],c[12]])),Not(Xor(c[19],c[20])),Not(Xor(c[31],c[37])),\
    MXor([c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]]),Not(Xor(c[32],c[38])),Not(Xor(c[33],c[39])))

#e4e5phi6=And(Not(MXor([True,c[11],c[12]])),Not(Xor(c[19],c[20])),Not(Xor(c[31],c[37])),\
    #MXor([c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]]),Not(Xor(c[32],c[38])),Xor(c[33],c[39]))

s.add(And(Not(e4e5yw),Not(e4e5yw2),Not(e4e5phi5),Not(e4e5phi3)))

#e2+e4+e5
#yw
e245yw=And(Not(MXor([c[10],c[11],c[12]])),Not(MXor([c[24],c[31],c[37]])),\
    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]])),\
        Not(MXor([c[25],c[32],c[38]])),Not(MXor([c[26],c[33],c[39]])))

#e245psieta=And(Not(MXor([c[10],c[11],c[12]])),Not(MXor([c[24],c[31],c[37]])),\
    #Not(MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]])),\
        #MXor([c[25],c[32],c[38]]),MXor([c[26],c[33],c[39]]))

#e245phi1=And(Not(MXor([c[10],c[11],c[12]])),MXor([c[24],c[31],c[37]]),\
    #Not(MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]])),\
        #Not(MXor([c[25],c[32],c[38]])),MXor([c[26],c[33],c[39]]))

e245phi3=And(Not(MXor([c[10],c[11],c[12]])),MXor([c[24],c[31],c[37]]),\
    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]])),\
        Not(MXor([c[25],c[32],c[38]])),Not(MXor([c[26],c[33],c[39]])))

e245phi5=And(Not(MXor([c[10],c[11],c[12]])),Not(MXor([c[24],c[31],c[37]])),\
    MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]]),\
        Not(MXor([c[25],c[32],c[38]])),Not(MXor([c[26],c[33],c[39]])))

#e245phi6=And(Not(MXor([c[10],c[11],c[12]])),Not(MXor([c[24],c[31],c[37]])),\
    #Not(MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37]])),\
        #Not(MXor([c[25],c[32],c[38]])),MXor([c[26],c[33],c[39]]))

s.add(And(Not(e245yw),Not(e245phi5),Not(e245phi3)))

#Spinorials
#z1, projs: S,e2,e4,e5,z2,x,b1,b2,b3 - z2 is redundant it seems
z1T=And(Not(c[16]),Not(c[24]),Not(c[31]),Not(c[37]),Not(MXor([c[42],c[46],c[49]])),Not(c[52]),Not(c[42]),Not(c[46]),Not(c[49]))

#z2, projs: S,e2,e4,e5,z1,x,b1,b2,b3- i'll just do b1 
z2T=And(Not(MXor([c[0],c[13],c[14],c[15],c[16]])),Not(MXor([c[1],c[21],c[22],c[23],c[24]])),Not(MXor([c[2],c[28],c[29],c[30],c[31]])),\
    Not(MXor([c[3],c[34],c[35],c[36],c[37]])),Not(MXor([c[42],c[46],c[49]])),Not(MXor([True,c[8],c[43],c[47],c[50],c[52]])),Not(MXor([c[40],c[41],c[42]])))

#2g+x, just b1 not b2 and b3..?
ggxT=And(Not(c[17]),Not(c[25]),Not(c[32]),Not(c[38]),Not(Xor(True,c[8])),Not(MXor([c[43],c[47],c[50],c[54]])),Not(c[43]))

#2g+x+z1
ggxz1T=And(Not(MXor([True,c[17],c[16]])),Not(MXor([c[25],c[24]])),Not(MXor([c[32],c[31]])),Not(MXor([c[38],c[37]])),\
    Not(MXor([True,c[8],c[52]])),Not(MXor([c[43],c[42]])))

#2g+x+z2
ggxz2T=And(Not(MXor([True,c[17],c[0],c[13],c[14],c[15],c[16]])),Not(MXor([c[25],c[1],c[21],c[22],c[23],c[24]])),\
    Not(MXor([c[32],c[2],c[28],c[29],c[30],c[31]])),\
    Not(MXor([c[38],c[3],c[34],c[35],c[36],c[37]])),Not(MXor([c[43],c[47],c[50],c[52]])),Not(MXor([c[43],c[40],c[41],c[42]])))

#2g+x+z1+z2
ggxz1z2T=And(Not(MXor([c[17],c[0],c[13],c[14],c[15]])),Not(MXor([c[25],c[1],c[21],c[22],c[23]])),Not(MXor([c[32],c[2],c[28],c[29],c[30]])),\
    Not(MXor([c[38],c[3],c[34],c[35],c[36]])),Not(MXor([c[43],c[47],c[50]])),Not(MXor([c[43],c[40],c[41]])))

s.add(And(Not(z1T),Not(z2T),Not(ggxT),Not(ggxz1T),Not(ggxz2T),Not(ggxz1z2T)))

#e2+z1, b1...
e2z1=And(Xor(c[10],c[16]),Not(Xor(c[19],c[31])),Not(Xor(c[20],c[37])),\
    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[42],c[46],c[49]])),Not(Xor(c[25],c[52])),Not(MXor([True,c[21],c[42]])))

#e2+z2
e2z2=And(MXor([c[10],c[0],c[13],c[14],c[15],c[16]]),Not(MXor([c[19],c[2],c[28],c[29],c[30],c[31]])),\
    Not(MXor([c[20],c[3],c[34],c[35],c[36],c[37]])),Not(MXor([c[24],c[42],c[46],c[49]])),\
        Not(MXor([c[25],True,c[8],c[43],c[47],c[50],c[52]])),Not(MXor([True,c[21],c[40],c[41],c[42]])))

#e2+2g+x
ggxz1z2_e2=MXor([c[25],c[24],c[1],c[21],c[22],c[23],c[24],c[43],c[47],c[50]])
e2x=And(Xor(c[10],c[17]),Not(Xor(c[19],c[32])),Not(Xor(c[20],c[38])),Not(MXor([c[25],True,c[8]])),\
    Not(MXor([True,c[21],c[43]])),Not(ggxz1z2_e2))

#e2+2g+x+z1
e2ggxz1=And(Not(MXor([c[10],c[17],c[16]])),Not(MXor([c[19],c[32],c[31]])),Not(MXor([c[20],c[38],c[37]])),\
    Not(MXor([c[21],c[42],c[43]])),Not(MXor([c[25],True,c[8],c[52]])))

#e2+2g+x+z2
ggxz1_e2=MXor([True,c[25],c[24],c[43],c[47],c[50],c[42],c[46],c[49]])
e2ggxz2=And(Not(MXor([c[10],c[17],c[0],c[13],c[14],c[15],c[16]])),Not(MXor([c[19],c[32],c[2],c[28],c[29],c[30],c[31]])),\
    Not(MXor([c[20],c[38],c[3],c[34],c[35],c[36],c[37]])),Not(MXor([c[25],c[43],c[47],c[50],c[52]])),\
        Not(MXor([True,c[21],c[40],c[41],c[42],c[43]])),Not(ggxz1_e2))

#e2+2g+x+z1+z2
e2ggxz1z2=And(Not(MXor([True,c[10],c[17],c[0],c[13],c[14],c[15]])),Not(MXor([c[19],c[32],c[2],c[28],c[29],c[30]])),\
    Not(MXor([c[20],c[38],c[3],c[34],c[35],c[36]])),Not(MXor([c[25],c[43],c[47],c[50]])),\
        Not(MXor([True,c[21],c[40],c[41],c[43]])))

s.add(And(Not(e2z1),Not(e2z2),Not(e2x),Not(e2ggxz1),Not(e2ggxz2),Not(e2ggxz1z2)))

#e4+z1 - b2...
e4z1=And(Xor(c[11],c[16]),Not(Xor(c[19],c[24])),Not(Xor(c[27],c[37])),\
    Not(MXor([c[2],c[28],c[29],c[30],c[31],c[42],c[46],c[49]])),\
        Not(Xor(c[32],c[52])),Not(MXor([True,c[29],c[46]])))

#e4+z2
e4z2=And(MXor([c[11],c[0],c[13],c[14],c[15],c[16]]),Not(MXor([c[19],c[1],c[21],c[22],c[23],c[24]])),\
    Not(MXor([c[27],c[3],c[34],c[35],c[36],c[37]])),\
    Not(MXor([c[31],c[42],c[46],c[49]])),Not(MXor([c[32],True,c[8],c[43],c[47],c[50],c[52]])),\
        Not(MXor([True,c[29],c[40],c[45],c[46]])))

#e4+2g+x
ggxz1z2_e4=MXor([c[32],c[31],c[2],c[28],c[29],c[30],c[31],c[43],c[47],c[50]])
e4x=And(Xor(c[11],c[17]),Not(Xor(c[19],c[25])),Not(Xor(c[27],c[38])),Not(MXor([True,c[32],c[8]])),\
    Not(MXor([True,c[29],c[47]])),Not(ggxz1z2_e4))

#e4+2g+x+z1
e4ggxz1=And(Not(MXor([c[11],c[17],c[16]])),Not(MXor([c[19],c[25],c[24]])),Not(MXor([c[27],c[38],c[37]])),\
    Not(MXor([c[29],c[46],c[47]])),Not(MXor([c[32],True,c[8],c[52]])))

#e4+2g+x+z2
ggxz1_e4=MXor([True,c[32],c[31],c[43],c[47],c[50],c[42],c[46],c[49]])
e4ggxz2=And(Not(MXor([c[11],c[17],c[0],c[13],c[14],c[15],c[16]])),Not(MXor([c[19],c[25],c[1],c[21],c[22],c[23],c[24]])),\
    Not(MXor([c[27],c[38],c[3],c[34],c[35],c[36],c[37]])),Not(MXor([c[29],c[40],c[45],c[46],c[47]])),\
        Not(MXor([c[32],c[43],c[47],c[50],c[52]])),Not(ggxz1_e4))

#e4+2g+x+z1+z2
e4ggxz1z2=And(Not(MXor([True,c[11],c[17],c[0],c[13],c[14],c[15]])),Not(MXor([c[19],c[25],c[1],c[21],c[22],c[23]])),\
    Not(MXor([c[27],c[38],c[3],c[34],c[35],c[36]])),Not(MXor([c[32],c[43],c[47],c[50]])),Not(MXor([True,c[29],c[40],c[45],c[47]])))

s.add(And(Not(e4z1),Not(e4z2),Not(e4x),Not(e4ggxz1),Not(e4ggxz2),Not(e4ggxz1z2)))

#e5+z1, b3 is a proj...
e5z1=And(Xor(c[12],c[16]),Not(Xor(c[20],c[24])),Not(Xor(c[27],c[31])),\
    Not(MXor([c[3],c[34],c[35],c[36],c[37],c[42],c[46],c[49]])),Not(Xor(c[38],c[52])),Not(MXor([True,c[36],c[49]])))

#e5+z2
e5z2=And(MXor([c[12],c[0],c[13],c[14],c[15],c[16]]),Not(MXor([c[20],c[1],c[21],c[22],c[23],c[24]])),\
    Not(MXor([c[27],c[2],c[28],c[29],c[30],c[31]])),\
    Not(MXor([c[37],c[42],c[46],c[49]])),Not(MXor([c[38],True,c[8],c[43],c[47],c[50],c[52]])),Not(MXor([True,c[36],c[41],c[45],c[49]])))

#e5+2g+x
ggxz1z2_e5=MXor([c[38],c[3],c[34],c[35],c[36],c[43],c[47],c[50]])
e5x=And(Xor(c[12],c[17]),Not(Xor(c[20],c[32])),Not(Xor(c[27],c[32])),Not(MXor([True,c[38],c[8]])),\
    Not(ggxz1z2_e5),Not(MXor([True,c[36],c[50]])))

#e5+2g+x+z1
ggxz2_e5=MXor([c[38],c[3],c[34],c[35],c[36],c[37],c[43],c[47],c[50],c[42],c[46],c[49]])
e5ggxz1=And(Not(MXor([c[12],c[17],c[16]])),Not(MXor([c[20],c[25],c[24]])),Not(MXor([c[27],c[32],c[31]])),\
    Not(MXor([c[38],True,c[8],c[52]])),Not(MXor([c[36],c[49],c[50]])),Not(ggxz2_e5))

#e5+2g+x+z2
ggxz1_e5=MXor([True,c[38],c[37],c[43],c[47],c[50],c[42],c[46],c[49]])
e5ggxz2=And(Not(MXor([c[12],c[17],c[0],c[13],c[14],c[15],c[16]])),Not(MXor([c[20],c[25],c[1],c[21],c[22],c[23],c[24]])),\
    Not(MXor([c[27],c[32],c[2],c[28],c[29],c[30],c[31]])),Not(MXor([c[38],c[43],c[47],c[50],c[52]])),\
        Not(MXor([c[36],c[41],c[45],c[49],c[50]])),Not(ggxz1_e5))

#e5+2g+x+z1+z2
e5ggxz1z2=And(Not(MXor([True,c[12],c[17],c[0],c[13],c[14],c[15]])),Not(MXor([c[20],c[25],c[1],c[21],c[22],c[23]])),\
    Not(MXor([c[27],c[32],c[2],c[28],c[29],c[30]])),Not(MXor([c[38],c[43],c[47],c[50]])),\
        Not(MXor([True,c[36],c[41],c[45],c[50]])))

s.add(And(Not(e5z1),Not(e5z2),Not(e5x),Not(e5ggxz1),Not(e5ggxz2),Not(e5ggxz1z2)))

#e2+e4+z1
e2e4z1=And(Not(MXor([c[10],c[11],c[16]])),Not(MXor([c[20],c[27],c[37]])),Not(MXor([c[25],c[32],c[52]])),\
    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[42],c[46],c[49]])))

#e2+e4+z2
e2e4z2=And(Not(MXor([c[10],c[11],c[0],c[13],c[14],c[15],c[16]])),Not(MXor([c[20],c[27],c[3],c[34],c[35],c[36],c[37]])),\
    Not(MXor([c[25],c[32],True,c[8],c[43],c[47],c[50],c[52]])),Not(MXor([c[24],c[31],c[42],c[46],c[49]])))

#e2+e4+2g+x
ggxz1z2_e24=MXor([c[25],c[32],c[1],c[21],c[22],c[23],c[2],c[28],c[29],c[30],c[43],c[47],c[50]])
e2e4x=And(Not(MXor([c[10],c[11],c[17]])),Not(MXor([c[20],c[27],c[38]])),Not(MXor([c[25],c[32],True,c[8]])),Not(ggxz1z2_e24))

#e2+e4+2g+x+z1
ggxz2_e24=MXor([True,c[25],c[32],c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[43],c[47],c[50],c[42],c[46],c[49]])
e24ggxz1=And(Not(MXor([True,c[10],c[11],c[17],c[16]])),Not(MXor([c[20],c[27],c[38],c[37]])),\
             Not(MXor([c[25],c[32],True,c[8],c[52]])),Not(ggxz2_e24))

#e2+e4+2g+x+z2
ggxz1_e24=MXor([True,c[25],c[32],c[24],c[31],c[43],c[47],c[50],c[42],c[46],c[49]])
e24ggxz2=And(Not(MXor([True,c[10],c[11],c[17],c[0],c[13],c[14],c[15],c[16]])),Not(MXor([c[20],c[27],c[38],c[3],c[34],c[35],c[36],c[37]])),\
    Not(MXor([c[25],c[32],c[43],c[47],c[50],c[52]])),Not(ggxz1_e24))

#e2+e4+2g+x+z1z2
e24ggxz1z2=And(Not(MXor([c[10],c[11],c[17],c[0],c[13],c[14],c[15]])),Not(MXor([c[20],c[27],c[38],c[3],c[34],c[35],c[36]])),\
    Not(MXor([c[25],c[32],c[43],c[47],c[50]])))

s.add(And(Not(e2e4z1),Not(e2e4z2),Not(e2e4x),Not(e24ggxz1),Not(e24ggxz2),Not(e24ggxz1z2)))

#e2+e5+z1
e2e5z1=And(Not(MXor([c[10],c[12],c[16]])),Not(MXor([c[19],c[27],c[31]])),Not(MXor([c[25],c[38],c[52]])),\
    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[3],c[34],c[35],c[36],c[37],c[42],c[46],c[49]])))

#e2+e5+z2
e2e5z2=And(Not(MXor([c[10],c[12],c[0],c[13],c[14],c[15],c[16]])),Not(MXor([c[19],c[27],c[2],c[28],c[29],c[30],c[31]])),\
    Not(MXor([c[25],c[38],True,c[8],c[43],c[47],c[50],c[52]])),Not(MXor([c[24],c[37],c[42],c[46],c[49]])))

#e2+e5+2g+x
ggxz1z2_e25=MXor([c[25],c[38],c[1],c[21],c[22],c[23],c[3],c[34],c[35],c[36],c[43],c[47],c[50]])
e2e5x=And(Not(MXor([c[10],c[12],c[17]])),Not(MXor([c[19],c[27],c[32]])),Not(MXor([c[25],c[38],c[8],True])),Not(ggxz1z2_e25))

#e2+e5+2g+x+z1
ggxz2_e25=MXor([True,c[25],c[38],c[1],c[21],c[22],c[23],c[24],c[3],c[34],c[35],c[36],c[37],c[43],c[47],c[50],c[42],c[46],c[49]])
e25ggxz1=And(Not(MXor([True,c[10],c[12],c[17],c[16]])),Not(MXor([c[19],c[27],c[32],c[31]])),Not(MXor([c[25],c[38],True,c[8],c[52]])),Not(ggxz2_e25))

#e2+e5+2g+x+z2
ggxz1_e25=MXor([True,c[25],c[38],c[24],c[37],c[43],c[47],c[50],c[42],c[46],c[49]])
e25ggxz2=And(Not(MXor([True,c[10],c[12],c[17],c[0],c[13],c[14],c[15],c[16]])),Not(MXor([c[19],c[27],c[32],c[2],c[28],c[29],c[30],c[31]])),\
    Not(MXor([c[25],c[38],c[43],c[47],c[50],c[52]])),Not(ggxz1_e25))

#e2+e5+2g+x+z1+z2
e25ggxz1z2=And(Not(MXor([c[10],c[12],c[17],c[0],c[13],c[14],c[15]])),Not(MXor([c[19],c[27],c[32],c[2],c[28],c[29],c[30]])),\
    Not(MXor([c[25],c[38],c[43],c[47],c[50]])))

s.add(And(Not(e2e5z1),Not(e2e5z2),Not(e2e5x),Not(e25ggxz1),Not(e25ggxz2),Not(e25ggxz1z2)))

#e4+e5+z1
e4e5z1=And(Not(MXor([c[11],c[12],c[16]])),Not(MXor([c[19],c[20],c[24]])),Not(MXor([c[32],c[38],c[52]])),\
    Not(MXor([c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37],c[42],c[46],c[49]])))

#e4+e5+z2
e4e5z2=And(Not(MXor([c[11],c[12],c[0],c[13],c[14],c[15],c[16]])),Not(MXor([c[19],c[20],c[1],c[21],c[22],c[23],c[24]])),\
    Not(MXor([c[32],c[38],True,c[8],c[43],c[47],c[50],c[52]])),Not(MXor([c[31],c[37],c[42],c[46],c[49]])))

#e4+e5+2g+x
ggxz1z2_e45=MXor([c[32],c[38],c[2],c[28],c[29],c[30],c[3],c[34],c[35],c[36],c[43],c[47],c[50]])
e4e5x=And(Not(MXor([c[11],c[12],c[17]])),Not(MXor([c[19],c[20],c[25]])),Not(MXor([c[32],c[38],True,c[8]])),Not(ggxz1z2_e45))

#e4+e5+2g+x+z1
ggxz2_e45=MXor([True,c[32],c[38],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37],c[43],c[47],c[50],c[42],c[46],c[49]])
e45ggxz1=And(Not(MXor([True,c[11],c[12],c[17],c[16]])),Not(MXor([c[19],c[20],c[25],c[24]])),\
    Not(MXor([c[32],c[38],True,c[8],c[52]])),Not(ggxz2_e45))

#e4+e5+2g+x+z2
ggxz1_e45=MXor([True,c[32],c[38],c[31],c[37],c[43],c[47],c[50],c[42],c[46],c[49]])
e45ggxz2=And(Not(MXor([True,c[11],c[12],c[17],c[0],c[13],c[14],c[15],c[16]])),\
    Not(MXor([c[19],c[20],c[25],c[1],c[21],c[22],c[23],c[24]])),\
    Not(MXor([c[32],c[38],c[43],c[47],c[50],c[52]])),Not(ggxz1_e45))

#e4+e5+2g+x+z1+z2
e45ggxz1z2=And(Not(MXor([c[11],c[12],c[17],c[0],c[13],c[14],c[15]])),Not(MXor([c[19],c[20],c[25],c[1],c[21],c[22],c[23]])),\
    Not(MXor([c[32],c[38],c[43],c[47],c[50]])))

s.add(And(Not(e4e5z1),Not(e4e5z2),Not(e4e5x),Not(e45ggxz1),Not(e45ggxz2),Not(e45ggxz1z2)))

#e2+e4+e5+z1
e2e4e5z1=And(MXor([c[10],c[11],c[12],c[16]]),Not(MXor([c[25],c[32],c[38],c[52]])),\
    Not(MXor([c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37],c[42],c[46],c[49]])))

#e2+e4+e5+z2
e2e4e5z2=And(MXor([c[10],c[11],c[12],c[0],c[13],c[14],c[15],c[16]]),Not(MXor([c[25],c[32],c[38],True,c[8],c[43],c[47],c[50],c[52]])),\
    Not(MXor([c[24],c[31],c[37],c[42],c[46],c[49]])))

#e2+e4+e5+2g+x
ggxz1z2_e245=MXor([c[25],c[32],c[38],c[24],c[31],c[37],c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],\
    c[3],c[34],c[35],c[36],c[37],c[43],c[47],c[50]])
e2e4e5x=And(MXor([c[10],c[11],c[12],c[17]]),Not(MXor([c[25],c[32],c[38],True,c[8]])),Not(ggxz1z2_e245))

#e2+e4+e5+2g+x+z1
ggxz2_e245=MXor([c[25],c[32],c[38],c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],\
    c[3],c[34],c[35],c[36],c[37],c[43],c[47],c[50],c[42],c[46],c[49]])
e245ggxz1=And(Not(MXor([c[10],c[11],c[12],c[17],c[16]])),Not(MXor([c[25],c[32],c[38],True,c[8],c[52]])),Not(ggxz2_e245))

#e2+e4+e5+2g+x+z2
ggxz1_e245=MXor([True,c[25],c[32],c[38],c[24],c[31],c[37],c[43],c[47],c[50],c[42],c[46],c[49]])
e245ggxz2=And(Not(MXor([c[10],c[11],c[12],c[17],c[0],c[13],c[14],c[15],c[16]])),\
    Not(MXor([c[25],c[32],c[38],c[43],c[47],c[50],c[52]])),Not(ggxz1_e245))

#e2+e4+e5+2g+x+z1+z2
e245ggxz1z2=And(Not(MXor([True,c[10],c[11],c[12],c[17],c[0],c[13],c[14],c[15]])),\
    Not(MXor([c[25],c[32],c[38],c[43],c[47],c[50]])))

s.add(And(Not(e2e4e5z1),Not(e2e4e5z2),Not(e2e4e5x),Not(e245ggxz1),Not(e245ggxz2),Not(e245ggxz1z2)))

#e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x {}
#y2w2
e136y2=And(Not(MXor([True,c[0],c[10],c[11],c[12],c[13],c[14],c[15],c[17]])),MXor([c[10],True,c[1],c[19],c[20],c[21],c[22],c[23],c[25]]),\
    Not(MXor([c[11],True,c[2],c[19],c[27],c[28],c[29],c[30],c[32]])),Not(MXor([c[12],True,c[3],c[20],c[27],c[34],c[35],c[36],c[38]])),\
    Not(MXor([c[17],c[25],c[32],c[38],c[43],c[47],c[50],c[8]])),Not(MXor([c[16],c[24],c[31],c[37],c[42],c[46],c[49],c[52]])),
    Not(MXor([c[0],c[13],c[14],c[15],c[16],c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37],\
        c[42],c[46],c[49],True,c[8],c[43],c[47],c[50],c[52]])))
#y4w4
e136y4=And(Not(MXor([True,c[0],c[10],c[11],c[12],c[13],c[14],c[15],c[17]])),Not(MXor([c[10],True,c[1],c[19],c[20],c[21],c[22],c[23],c[25]])),\
    MXor([c[11],True,c[2],c[19],c[27],c[28],c[29],c[30],c[32]]),Not(MXor([c[12],True,c[3],c[20],c[27],c[34],c[35],c[36],c[38]])),\
    Not(MXor([c[17],c[25],c[32],c[38],c[43],c[47],c[50],c[8]])),Not(MXor([c[16],c[24],c[31],c[37],c[42],c[46],c[49],c[52]])),
    Not(MXor([c[0],c[13],c[14],c[15],c[16],c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37],\
        c[42],c[46],c[49],True,c[8],c[43],c[47],c[50],c[52]])))
#y5w5
e136y5=And(Not(MXor([True,c[0],c[10],c[11],c[12],c[13],c[14],c[15],c[17]])),Not(MXor([c[10],True,c[1],c[19],c[20],c[21],c[22],c[23],c[25]])),\
    Not(MXor([c[11],True,c[2],c[19],c[27],c[28],c[29],c[30],c[32]])),MXor([c[12],True,c[3],c[20],c[27],c[34],c[35],c[36],c[38]]),\
    Not(MXor([c[17],c[25],c[32],c[38],c[43],c[47],c[50],c[8]])),Not(MXor([c[16],c[24],c[31],c[37],c[42],c[46],c[49],c[52]])),
    Not(MXor([c[0],c[13],c[14],c[15],c[16],c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37],\
        c[42],c[46],c[49],True,c[8],c[43],c[47],c[50],c[52]])))
#psi12345eta123
e136psi=And(Not(MXor([True,c[0],c[10],c[11],c[12],c[13],c[14],c[15],c[17]])),Not(MXor([c[10],True,c[1],c[19],c[20],c[21],c[22],c[23],c[25]])),\
    Not(MXor([c[11],True,c[2],c[19],c[27],c[28],c[29],c[30],c[32]])),Not(MXor([c[12],True,c[3],c[20],c[27],c[34],c[35],c[36],c[38]])),\
    MXor([c[17],c[25],c[32],c[38],c[43],c[47],c[50],c[8]]),Not(MXor([c[16],c[24],c[31],c[37],c[42],c[46],c[49],c[52]])),
    Not(MXor([c[0],c[13],c[14],c[15],c[16],c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37],\
        c[42],c[46],c[49],c[8],c[43],c[47],c[50],c[52]])))
#phi34
e136phi3=And(Not(MXor([True,c[0],c[10],c[11],c[12],c[13],c[14],c[15],c[17]])),Not(MXor([c[10],True,c[1],c[19],c[20],c[21],c[22],c[23],c[25]])),\
    Not(MXor([c[11],True,c[2],c[19],c[27],c[28],c[29],c[30],c[32]])),Not(MXor([c[12],True,c[3],c[20],c[27],c[34],c[35],c[36],c[38]])),\
    Not(MXor([c[17],c[25],c[32],c[38],c[43],c[47],c[50],c[8]])),MXor([c[16],c[24],c[31],c[37],c[42],c[46],c[49],c[52]]),
    Not(MXor([c[0],c[13],c[14],c[15],c[16],c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37],\
        c[42],c[46],c[49],True,c[8],c[43],c[47],c[50],c[52]])))
#phi5678
e136phi5=And(Not(MXor([True,c[0],c[10],c[11],c[12],c[13],c[14],c[15],c[17]])),Not(MXor([c[10],True,c[1],c[19],c[20],c[21],c[22],c[23],c[25]])),\
    Not(MXor([c[11],True,c[2],c[19],c[27],c[28],c[29],c[30],c[32]])),Not(MXor([c[12],True,c[3],c[20],c[27],c[34],c[35],c[36],c[38]])),\
    Not(MXor([c[17],c[25],c[32],c[38],c[43],c[47],c[50],c[8]])),Not(MXor([c[16],c[24],c[31],c[37],c[42],c[46],c[49],c[52]])),
    MXor([c[0],c[13],c[14],c[15],c[16],c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],c[3],c[34],c[35],c[36],c[37],\
        c[42],c[46],c[49],True,c[8],c[43],c[47],c[50],c[52]]))

s.add(And(Not(e136y2),Not(e136y4),Not(e136y5),Not(e136phi3),Not(e136psi),Not(e136phi5)))

#e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x +z1

e136z1=And(Not(MXor([c[0],c[10],c[11],c[12],c[13],c[14],c[15],c[17],c[16]])),Not(MXor([True,c[10],c[1],c[19],c[20],c[21],c[22],c[23],c[25],c[24]])),\
    Not(MXor([c[11],True,c[2],c[19],c[27],c[28],c[29],c[30],c[32],c[31]])),Not(MXor([c[12],True,c[3],c[20],c[27],c[34],c[35],c[36],c[38],c[37]])),\
    Not(MXor([c[17],c[25],c[32],c[38],c[43],c[47],c[50],c[8],c[52]])),
    Not(MXor([c[0],c[13],c[14],c[15],c[16],c[1],c[21],c[22],c[23],c[24],c[2],c[28],c[29],c[30],c[31],\
        c[3],c[34],c[35],c[36],c[37],True,c[8],c[43],c[47],c[50],c[52]])))

#e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x +z2
e136z2=And(Not(MXor([c[10],c[11],c[12],c[16],c[17]])),Not(MXor([c[10],True,c[19],c[20],c[24],c[25]])),\
    Not(MXor([c[11],True,c[19],c[27],c[31],c[32]])),Not(MXor([c[12],True,c[20],c[27],c[37],c[38]])),\
    Not(MXor([True,c[17],c[25],c[32],c[38],c[52]])),Not(MXor([c[16],c[24],c[31],c[37],c[52]])))

#e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x +2g+x
e136ggx=And(Not(MXor([c[0],c[10],c[11],c[12],c[13],c[14],c[15]])),Not(MXor([c[10],True,c[1],c[19],c[20],c[21],c[22],c[23]])),\
    Not(MXor([c[11],c[19],True,c[2],c[27],c[28],c[29],c[30]])),Not(MXor([c[12],c[20],c[27],True,c[3],c[34],c[35],c[36]])),\
    Not(MXor([c[17],c[25],c[32],c[38],c[43],c[47],c[50]])),\
    Not(MXor([c[0],c[13],c[14],c[15],c[17],c[1],c[21],c[22],c[23],c[25],c[2],c[28],c[29],c[30],c[32],\
        c[3],c[34],c[35],c[36],c[38],c[43],c[47],c[50]])))

#e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x +2g+x+z1
e136ggxz1=And(Not(MXor([c[0],c[10],c[11],c[12],c[13],c[14],c[15],c[16],True])),\
    Not(MXor([c[10],True,c[1],c[19],c[20],c[21],c[22],c[23],c[24]])),\
    Not(MXor([c[11],c[19],True,c[2],c[27],c[28],c[29],c[30],c[31]])),\
    Not(MXor([c[12],c[20],c[27],True,c[3],c[34],c[35],c[36],c[37]])),\
    Not(MXor([c[17],c[25],c[32],c[38],True,c[43],c[47],c[50],c[52]])),\
    Not(MXor([c[0],c[13],c[14],c[15],c[16],c[17],c[1],c[21],c[22],c[23],c[24],c[25],\
              c[2],c[28],c[29],c[30],c[31],c[32],c[3],c[34],c[35],c[36],c[37],c[38],c[43],c[47],c[50],c[52],c[54]]))) 

#e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x +2g+x+z2
e136ggxz2=And(Not(MXor([True,c[10],c[11],c[12],c[16]])),Not(MXor([True,c[10],c[19],c[20],c[24]])),\
    Not(MXor([c[11],True,c[19],c[27],c[31]])),Not(MXor([c[12],True,c[20],c[27],c[37]])),\
    Not(MXor([c[8],c[17],c[25],c[32],c[38],c[52]])),Not(MXor([c[8],c[17],c[16],c[25],c[24],c[32],c[31],c[38],c[37],c[52]])))

#e1+e3+e6=S+e2+e4+e5+b1+b2+b3+x +2g+x+z1+z2
e136ggxz1z2=And(Not(MXor([c[10],c[11],c[12]])),Not(MXor([c[10],True,c[19],c[20]])),\
    Not(MXor([c[11],True,c[19],c[27]])),Not(MXor([c[12],True,c[20],c[27]])),\
    Not(MXor([c[8],c[17],c[25],c[32],c[38]]))) 

s.add(And(Not(e136z1),Not(e136z2),Not(e136ggx),Not(e136ggxz1),Not(e136ggxz2),Not(e136ggxz1z2)))

#g (3,3) { }
#y2w2
gamma2=And(Not(c[18]),c[26],Not(c[33]),Not(c[39]),Not(MXor([c[9],c[44],c[48],c[51],c[54]])))
#y4w4
gamma4=And(Not(c[18]),Not(c[26]),c[33],Not(c[39]),Not(MXor([c[9],c[44],c[48],c[51],c[54]])))
#y5w5
gamma5=And(Not(c[18]),Not(c[26]),Not(c[33]),c[39],Not(MXor([c[9],c[44],c[48],c[51],c[54]])))
#phi3458 (2g+x+z1+z2 projector needs adding? )
gammaPhi=And(Not(c[18]),Not(c[26]),Not(c[33]),Not(c[39]),MXor([c[9],c[44],c[48],c[51],c[54]]))
#other oscill possibilities
gammaElse=And(Not(c[18]),Not(c[26]),Not(c[33]),Not(c[39]),Not(MXor([c[9],c[44],c[48],c[51],c[54]])))

#x+g (3,3) { }  x+3g same conditions... checked 2g+z1+z2...
#y2w2
gx1=And(Not(MXor([True,c[17],c[18]])),MXor([c[25],c[26]]),Not(MXor([c[32],c[33]])),\
           Not(MXor([c[38],c[39]])),Not(MXor([True,c[54],c[43],c[47],c[50],c[44],c[48],c[51]])))
#y4w4
gx2=And(Not(MXor([True,c[17],c[18]])),Not(MXor([c[25],c[26]])),MXor([c[32],c[33]]),\
           Not(MXor([c[38],c[39]])),Not(MXor([True,c[54],c[43],c[47],c[50],c[44],c[48],c[51]])))
#y5w5
gx3=And(Not(MXor([True,c[17],c[18]])),Not(MXor([c[25],c[26]])),Not(MXor([c[32],c[33]])),\
           MXor([c[38],c[39]]),Not(MXor([True,c[54],c[43],c[47],c[50],c[44],c[48],c[51]])))
#phi? - covered all oscills I think
gx4=And(Not(MXor([True,c[17],c[18]])),Not(MXor([c[25],c[26]])),Not(MXor([c[32],c[33]])),\
           Not(MXor([c[38],c[39]])),MXor([True,c[54],c[43],c[47],c[50],c[44],c[48],c[51]]))


#g+z1 (3,5) - one complex R oscill (2g+x+z2 is a projector)
#any
##print("g+z1 S proj:", )
gz1=And(MXor([c[18],c[16]]),Not(MXor([c[26],c[24]])),Not(MXor([c[33],c[31]])),Not(MXor([c[33],c[31]])),Not(MXor([c[39],c[37]])),\
     Not(MXor([True,c[9],c[42],c[46],c[49],c[44],c[48],c[51],c[52],c[53],c[54]])))
    
#g+z2 (3,5) - one complex R oscill (2g+x+z1 is a projector)
#any
gz2=And(Not(MXor([True,c[18],c[0],c[13],c[14],c[15],c[16]])),Not(MXor([c[26],c[1],c[21],c[22],c[23],c[24]])),\
    Not(MXor([c[33],c[2],c[28],c[29],c[30],c[31]])),Not(MXor([c[39],c[3],c[34],c[35],c[36],c[37]])), \
    Not(MXor([c[8],c[54],c[43],c[47],c[50],c[52],c[53],c[42],c[46],c[49]])))

#1+b1+b2+b3+x+3g = z1+z2+x+3g=y36,y1w6,w13,psi,eta=1/2, phi1267=1/2,phi3458 (3,7)
z1z2x3g=And(MXor([c[0],c[13],c[14],c[15],c[17],c[18]]),Not(MXor([c[1],c[21],c[22],c[23],c[25],c[26]])),\
    Not(MXor([c[2],c[28],c[29],c[30],c[32],c[33]])),Not(MXor([c[3],c[34],c[35],c[36],c[38],c[39]])))

s.add(And(Not(gamma2),Not(gamma4),Not(gamma5),Not(gammaPhi),Not(gammaElse),Not(gx1),Not(gx2),Not(gx3),Not(gx4),Not(gz1),Not(gz2),Not(z1z2x3g)))

print(s.check()) 

import timeit
import json 
import sys
start = timeit.default_timer()
#from time import time
#t1 = time()



while s.check() == sat: 
#for i in range(10):
    m = s.model () 
    
    if not m: 

        break 
    f = open('FNY3esLONG.txt','a') 
    #finds 15389 in 1 hour
    old_stdout = sys.stdout  #  store the default system handler to be able to restore it 

    sys.stdout = f 
    #t2 = time()
    #elapsed = t2 - t1
    #print(elapsed) # Print elapsed time
    Boolm=[m[c[i]] for i in range(55)]
    print(Boolm)
    """
    BCm=[]
    for item in Boolm:
        #print(type(item))
        if type(item)==BoolRef:
            if item.sexpr()=='true':
                BCm.append(1)
            else:
                BCm.append(0)
        else:
            BCm.append(1)
    #BCm=[ 1 if item.sexpr()=='true' else 0 for item in Boolm]

    print(BCm)"""
    #print(type(modl))
    
    f.close() 

    sys.stdout=old_stdout 
    
    #print(sorted ([(d, m[d]) for d in m], key = lambda x: str(x[0]))) 
    #print(sorted ([(m[d]) for d in m], key = lambda x: str(x[0]))) 

    s.add(Not(And([v() == m[v] for v in m]))) 

stop = timeit.default_timer()
print("Time:", stop - start)
 