# Buatlah sebuah program yang dapat membandingkan 2 buah file teks dan kemudian
# menampilkan perbedaan antar kedua teks per barisnya jika ada perbedaaan! 
def perbandingan(cek_1,cek_2):
    with open(cek_1, 'r') as file1:
        baris_1 = file1.readlines()
    with open(cek_2, 'r') as file2:
        baris_2= file2.readlines()
    a=len(baris_1)
    b=len(baris_2)
    if a<b:
        for i in range(b):
            if baris_1[i]!=baris_2[i]:
                print ("beda di line", i+1)
                print ("file pertama: ", baris_1[i].strip())
                print ("file kedua: ", baris_2[i].strip())
    else:
        for j in range(a):
            if baris_1[j]!=baris_2[j]:
                print ("beda di line", j+1)
                print ("file pertama: ", baris_1[j].strip())
                print ("file kedua: ", baris_2[j].strip())
                                          
cek_1 = input("masukan nama file pertama: ")
cek_2 = input("masukan nama file kedua: ")
perbandingan(cek_1,cek_2)
