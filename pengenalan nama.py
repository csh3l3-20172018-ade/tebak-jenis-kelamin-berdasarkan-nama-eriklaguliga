#Fikri Attamami Laguliga
#KELAS IF 39-14
#1301150028

#fungsi dari def/fungsi cek_perempuan ini adalah sebagai fungsi cek per karakter dimana fungsi ini akan melakukan looping banyaknya karankter ditandai dengan (len(a)) dan melakukan pengecekan
#karakter yang di cek disini adalah a,u,e,i,t,dan l. Ketika inputan program memenuhi syarat tersebut maka akan melakukan count terhadap banyaknya karakter yang memenuhi syarat
def cek_perempuan(a):
    d = 0
    for i in a[0]:#maksud dari a[0] adalah kita mengambil nama pertama untuk dicek
        if(i == 'a'):
            d=d+1
        elif(i =='u'):
            d=d+1
        elif(i=='e'):
            d=d+1
        elif(i=='t'):
            d=d+1
        elif(i=='l'):
            d=d+1
    return d
#fungsi dari def/fungsi cek_laki ini adalah sebagai fungsi cek per karakter dimana fungsi ini akan melakukan looping banyaknya karankter ditandai dengan (len(a)) dan melakukan pengecekan
#karakter yang di cek disini adalah b,d,dan o. Ketika inputan program memenuhi syarat tersebut maka akan melakukan count terhadap banyaknya karakter yang memenuhi syarat
def cek_laki(a):
    d = 0
    for i in (a[0]):#maksud dari a[0] adalah kita mengambil nama pertama untuk dicek
        if (i == 'b'):
            d = d + 1
        elif (i == 'd'):
            d = d + 1
        elif (i == 'o'):
            d = d + 1
    return d
#pada tahap ini user dapat melakukan inputan nama yang akan dicek dengan memanggil fungsi cek_perempuan dan cek_laki yang akan disimpan divariabel prob_cewek dan prob_laki
nama = input("masukkan nama :")
temp = nama.split() #disi nama akan dipisahkan berdasarkan spasinya
prob_cewek = cek_perempuan(temp)
prob_laki = cek_laki(temp)
#ketika inputan sudah diproses di fungsi prob_cewek dan prob_laki maka hasil perhitungan akan dibandingkan. ketika hasil count problaki lebih besar dari pada perempuan makan dia laki-laki begitu juga sebaliknya
if(prob_laki>prob_cewek):
    print("laki-laki")
elif(prob_laki<prob_cewek):
    print("perempuan")

print(prob_laki)
print(prob_cewek)
