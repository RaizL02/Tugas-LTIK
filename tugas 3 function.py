#Nama: lUTHFIL HADI SURYA PANGESTU
#NIM: 2401208
#KELAS: RPL 1A

def hitung_selisih(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
    total_detik_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    total_detik_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai
    
    selisih_detik = total_detik_selesai - total_detik_mulai
    
    jam = selisih_detik // 3600
    menit = (selisih_detik % 3600) // 60
    detik = selisih_detik % 60
    
    return jam, menit, detik

jam_mulai = int(input("Jam mulai: "))
menit_mulai = int(input("Menit mulai: "))
detik_mulai = int(input("Detik mulai: "))

jam_selesai = int(input("Jam selesai: "))
menit_selesai = int(input("Menit selesai: "))
detik_selesai = int(input("Detik selesai: "))

jam, menit, detik = hitung_selisih(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai)

print(f"Selisih: {jam} jam - {menit} menit - {detik} detik")