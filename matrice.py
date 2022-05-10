from random import randint

P1 = [["----" for x in range(10)] for x in range(10)]
ship_size = [2,3,3,4,5]

def random_mat(m):
    
    for i in (ship_size):
        res = False
        pos = randint(0,1)
        if pos == 0:  #verticale
            while res == False:
                x = randint(0,len(m[0])-1)
                y = randint(0,len(m)-i-1)
                for k in range(0,i):
                    if m[y+k][x] == "----":
                        res = True
                    else:
                        res = False
            for j in range(0,i):
                m[y+j][x] = "ship"
        else : #horizontal
            while res == False:
                x = randint(0,len(m[0])-i-1)
                y = randint(0,len(m)-1)
                for k in range(0,i):
                    if m[y][x+k] == "----":
                        res = True
                    else:
                        res = False
            for j in range(0,i):
                m[y][x+j] = "ship"    
    return(m)
         

def show_mat(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(f"{m[j][i]}", end=" ")
        print("\n")
    print("\n")

show_mat(random_mat(P1))
