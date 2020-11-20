import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear_screen()
    print(">>>Silahkan Pilih<<<")
    print("1. Kue Keju Rp. 6000 (25 Kue)")
    print("2. Kue Coklat Rp. 3500 (35 Kue)")
    print("3. Keluar")
    pilih = input("Pilih menu> ")

    if(pilih == "1"):
        kue_keju()
    elif(pilih == "2"):
        kue_coklat()
    elif(pilih == "3"):
        print("Terimakasih sudah menggunakan aplikasi ini")
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    menu()

def kue_keju():
    harga_kue_keju = 6000
    clear_screen()
    print("---Kue Keju---")
    print("Promo:")
    print("Diskon 10% pembelian 4-15 kue keju")
    print("Diskon 15% pembelian 16-25 kue keju")
    jumlah = int(input("Jumlah kue keju> "))
    if(jumlah >= 0 and jumlah <= 3):
        harga = harga_kue_keju*jumlah
        print("Total: Rp.", harga)
    elif(jumlah >= 4 and jumlah <= 15):
        diskon = int((harga_kue_keju*jumlah)*10/100)
        harga = int((harga_kue_keju*jumlah)-diskon)
        print("Diskon. Rp.", diskon)
        print("Total: Rp.", harga)
    elif(jumlah >= 16 and jumlah <= 25):
        diskon = int((harga_kue_keju*jumlah)*15/100)
        harga = int((harga_kue_keju*jumlah)-diskon)
        print("Diskon. Rp.", diskon)
        print("Total: Rp.", harga)
    else:
        print("Jumlah tidak tersedia")
        input("Tekan Enter untuk mengulang...")
        kue_keju()
    bayar = int(input("Bayar> "))
    if(bayar >= harga):
        print("Kembalian: Rp.", bayar-harga)
    else:
        print("Uang tidak cukup")
        input("Tekan Enter untuk mengulang...")
        kue_keju()
    back_to_menu()

def kue_coklat():
    harga_kue_coklat = 3500
    clear_screen()
    print("---Kue Coklat---")
    print("Promo:")
    print("Diskon 7% pembelian 5-20 kue coklat")
    print("Diskon 12% pembelian 21-35 kue coklat")
    jumlah = int(input("Jumlah kue coklat> "))
    if(jumlah >= 0 and jumlah <= 4):
        harga = harga_kue_coklat*jumlah
        print("Total: Rp.", harga)
    elif(jumlah >= 5 and jumlah <= 20):
        diskon = int((harga_kue_coklat*jumlah)*7/100)
        harga = int((harga_kue_coklat*jumlah)-diskon)
        print("Diskon. Rp.", diskon)
        print("Total: Rp.", harga)
    elif(jumlah >= 21 and jumlah <= 35):
        diskon = int((harga_kue_coklat*jumlah)*12/100)
        harga = int((harga_kue_coklat*jumlah)-diskon)
        print("Diskon. Rp.", diskon)
        print("Total: Rp.", harga)
    else:
        print("Jumlah tidak tersedia")
        input("Tekan Enter untuk mengulang...")
        kue_keju()
    bayar = int(input("Bayar> "))
    if(bayar >= harga):
        print("Kembalian: Rp.", bayar-harga)
    else:
        print("Uang tidak cukup")
        input("Tekan Enter untuk mengulang...")
        kue_keju()
    back_to_menu()

if __name__ == "__main__":
    while True:
        menu()