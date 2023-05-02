import math

class decoder:
    def __init__(self, file):
    
        self.file=file
        kulcs = ["Ő","á","f","ü","G","A","Z","v",".","o","h","L","E","O","r","?","a","!","U","D","b","p","q","I","Q","J",",","Y","É","ö","Ü","x","j","S","P","g","u","R","Ö","M","é","Ó","ó","m","W",":","n","y"," ","z","C","e","H","s","ű","F","Ű","T","Á","N","K","c","B","í","t","d","k","(","X","w","ú","l","ő","Ú","i",")","Í","V"]
        #betuk=set()
        f = open(file, "r")
        eredeti = int(f.read())
        f.close()
        dekodolt=open(file, "w")
        szamok=[]


        while eredeti>0:
            i=0
            while pow(97,i) < eredeti:
                i+=1
            i-=1
            j=math.floor(eredeti/pow(97,i))
            szamok.insert(0,j)
            eredeti=eredeti-(j*pow(97,i))

        for k in szamok:
            dekodolt.write(kulcs[k])

        dekodolt.close()
    def start(self):
        self.window.mainloop()
