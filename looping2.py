print("soal 2")
#memberikan/konversi int pada t meskipun t adalah integer tetapi akan terbaca string pada input.
t = int(input("Masukan jumlah: "))
#perulangan dengan (1,t+1) untuk mebaca barisan pertama sampai nilai input t.+1 supaya terbaca sampai angka yang di input.
for i in range(1,t+1):
#print (t-i+1) dikali dengan kode emoji.(t-i+1) digunakan untuk mendapatkan bentuk segitiga yang di inginkan,
#contohnya jika menginput jumlah 10 maka akan di input 10-1+1 hingga menghasilkan tetap 10 dan berulang dilakukan pada baris berikutnya
  print((t-i+1) * "\U0001F601" )
