__author__="kvda"

class myClass():
    def myFunc(self):
        print("Program transpose Matriks")
        print("---")
        barisInp = input("Masukkan jumlah baris : ")
        kolomInp = input("Masukkan jumlah kolom : ")
        print("")

        matriks1 = []

        offset = 0
        
        print("kvda-creator")
        print("---")
        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                Amatriks = input("Masukkan angka untuk baris {0} kolom {1} : ".format(offset+1,offset2+1))
                matriks1.append(Amatriks)
                offset2+=1
            offset+=1
        print("---")
        print("Matriks anda : ")
        print("---")
        offset = 0
        offsetMatriks = 0
        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                print(int(matriks1[offsetMatriks]),end=" ")
                offsetMatriks+=1
                offset2+=1
            print(" ")
            offset+=1
        print("---")
        print("")
        
        print("Hasil dari transpose matriks anda : ")
        print("---")

        if(kolomInp=="2" and barisInp=="2"):
            newBarisInp = kolomInp
            offset = 0
            offsetMatriks = 0
            while offset<int(newBarisInp):
                offset2 = 0
                print(int(matriks1[offsetMatriks]),int(matriks1[offsetMatriks+2]))
                offsetMatriks+=1
                offset2+=1
                offset+=1
            print("---")
        elif(kolomInp=="3"):
            newBarisInp = kolomInp
            offset = 0
            offsetMatriks = 0
            while offset<int(newBarisInp):
                offset2 = 0
                print(int(matriks1[offsetMatriks]),int(matriks1[offsetMatriks+3]))
                offsetMatriks+=1
                offset2+=1
                offset+=1
            print("---")
        elif(barisInp=="3"):
            newBarisInp = kolomInp
            offset = 0
            offsetMatriks = 0
            while offset<int(newBarisInp):
                print(int(matriks1[offsetMatriks]),int(matriks1[offsetMatriks+2]),int(matriks1[offsetMatriks+4]))
                offsetMatriks+=1
                offset+=1
            print("---")
         
if __name__ == '__main__':
    myClass().myFunc()