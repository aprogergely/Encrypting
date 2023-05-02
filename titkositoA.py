import random

class encoder:
    def __init__(self, file):
    
        self.file=file
        kulcs = ["Ő","á","f","ü","G","A","Z","v",".","o","h","L","E","O","r","?","a","!","U","D","b","p","q","I","Q","J",",","Y","É","ö","Ü","x","j","S","P","g","u","R","Ö","M","é","Ó","ó","m","W",":","n","y"," ","z","C","e","H","s","ű","F","Ű","T","Á","N","K","c","B","í","t","d","k","(","X","w","ú","l","ő","Ú","i",")","Í","V"]
        #betuk=set()
        f = open(file, "r")
        eredeti = f.read()
        f.close()
        titkositott=open(file, "w")
        randomszam = random.randint(0,len(kulcs))
        titkositott.write(kulcs[randomszam])

        #for i in eredeti:
        #    betuk.add(i)

        #for j in betuk:
        #    k = 0
        #    while k < len(kulcs):
        #        if (j == kulcs[k]):
        #            k+=1
        #        else:
        #            k+=1

        for l in eredeti:
            k = 0
            success = False
            while k < len(kulcs):
                if (l == kulcs[k]):
                    if (randomszam+k) > len(kulcs):
                        titkositott.write(kulcs[(randomszam+k-len(kulcs))])
                        success = True
                    else:
                        titkositott.write(kulcs[(randomszam+k)])
                        success = True
                    k+=1
                else:
                    if k == (len(kulcs)-1):
                        if success == False:
                            titkositott.write(l)
                    k+=1

        titkositott.close()
    def start(self):
        self.window.mainloop()
