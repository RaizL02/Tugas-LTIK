#Nama: lUTHFIL HADI SURYA PANGESTU
#NIM: 2401208
#KELAS: RPL 1A

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

N = int(input("Masukkan jumlah bilangan Fibonacci yang ingin ditampilkan: "))
hasil = fibonacci(N)
print("Deret Fibonacci:", hasil)