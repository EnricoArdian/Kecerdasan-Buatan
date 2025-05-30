print("soal 1")
#memberikan/konversi int pada t meskipun t adalah integer tetapi akan terbaca string pada input.
t = int(input("Masukan Jumlah: "))
#perulangan dengan (1,t+1) untuk mebaca barisan pertama sampai nilai input t,+1 supaya terbaca sampai angka yang di input.
for i in range(1,t+1):
#print i dikali oleh kode emote supaya memunculkan emote dan mendapatkan baris yang bertambah mulai dari 1 sampai dengan t.
    print(i * "\U0001F601")
