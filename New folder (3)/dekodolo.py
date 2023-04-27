import random

kulcs = ["Ő","á","f","ü","G","A","Z","v",".","o","h","L","E","O","r","?","a","!","U","D","b","p","q","I","Q","J",",","Y","É","ö","Ü","x","j","S","P","g","u","R","Ö","M","é","Ó","ó","m","W",":","n","y"," ","z","C","e","H","s","ű","F","Ű","T","Á","N","K","c","B","í","t","d","k","(","X","w","ú","l","ő","Ú","i",")","Í","V"]
#betuk=set()
f = open("file.txt", "r")
eredeti = f.read()
f.close()
dekodolt=open("file.txt", "w")
offset = 0

k = 0
while k < len(kulcs):
    if kulcs[k]==eredeti[0]:
        offset=k
    k+=1

eredeti=eredeti[1:]

for l in eredeti:
    if l != 0:
        k = 0
        while k < len(kulcs):
            if (l == kulcs[k]):
                if (k-offset<0):
                    dekodolt.write(kulcs[(k-offset+len(kulcs))])
                    #dekodolt.write(" ")
                else:
                    dekodolt.write(kulcs[(k-offset)])
                k+=1
            else:
                k+=1

dekodolt.close()
