import random

def functionN():
    for i in range(1,w):
        for j in range(1,h):
            if p[i][j]!='':
                if p[i-1][j]=='':
                    p[i][j]+=1
                if p[i-1][j+1]=='':
                    p[i][j]+=1
                if p[i][j-1]=='':

                    p[i][j]+=1
                if p[i][j+1]=='':
                    p[i][j]+=1
                if p[i+1][j-1]=='':
                    p[i][j]+=1
                if p[i+1][j]=='':
                    p[i][j]+=1
                if p[i+1][j+1]=='':
                    p[i][j]+=1
   
w= int( input("Δώσε πλάτος: ") )
h= int ( input("Δώσε ύψος: ") )
b= int ( input("Πόσες βόμβες;: ") )

p = [[int(0) for x in range(w+1)] for y in range(h+1)]
for i in range (b):
    p[random.randint(1,w)][random.randint(1,h)] = '*'
                
                
functionN()

for i in range (1,w
                ):
    print(p[i])
