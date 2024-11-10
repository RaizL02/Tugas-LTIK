#Nama: lUTHFIL HADI SURYA PANGESTU
#NIM: 2401208
#KELAS: RPL 1A

password_benar= "Latihan"

# Maksimum percobaan
percobaan = 3

# Menu login
def login():
    # Password yang benar
    password_benar = "Latihan"
    percobaan = 3
    print("Menu Login")
    
    for attempt in range(percobaan):
        password = input("Masukkan password: ")
        
        if password == password_benar:
            print("Login berhasil!")
            return 
        else:
            print("Password salah!")
    
    print("Anda telah mencapai batas percobaan. Keluar dari menu login.")

# Memanggil fungsi login
login()