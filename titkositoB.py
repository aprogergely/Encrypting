class encoder:
    def __init__(self, file):
    
        self.file=file
        kulcs = ["Ő","á","f","ü","G","A","Z","v",".","o","h","L","E","O","r","?","a","!","U","D","b","p","q","I","Q","J",",","Y","É","ö","Ü","x","j","S","P","g","u","R","Ö","M","é","Ó","ó","m","W",":","n","y"," ","z","C","e","H","s","ű","F","Ű","T","Á","N","K","c","B","í","t","d","k","(","X","w","ú","l","ő","Ú","i",")","Í","V"]
        #betuk=set()
        f = open("file.txt", "r")
        eredeti = f.read()
        f.close()
        titkositott=open("file.txt", "w")
        szamsor = []


        for i in eredeti:
            j = 0
            success = False
            while j < len(kulcs):
                if (i == kulcs[j]):
                    szamsor.append(j)
                    success = True
                    j+=1
                else:
                    if j == (len(kulcs)-1):
                        if success == False:
                            print("Ismeretlen karakter!")
                            break
                    j+=1

        l=0
        eredmeny=0
        for k in szamsor:
            eredmeny=eredmeny+(k*pow(97,l))
            l+=1

        titkositott.write(str(eredmeny))

        titkositott.close()
    def start(self):
        self.window.mainloop()
