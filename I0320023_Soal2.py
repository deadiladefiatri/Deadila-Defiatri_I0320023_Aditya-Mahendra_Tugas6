print ("PROGRAM MENGHITUNG NILAI RATA - RATA")
print()
x = int(input("Banyaknya Data : "))
data = []
jumlah = 0

for i in range(0, x):
    nilai = int(input("Nilai ujian ke-%d : " % (i+1)))
    jumlah += nilai

rata2 = jumlah / x
print("Nilai Rata-rata  = %0.2f" % rata2)
