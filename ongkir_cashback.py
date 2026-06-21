total_belanja = int(input("Masukkan total belanja: "))
ongkir = int(input("Masukkan total ongkir: "))
status_member = input("Masukkan status member (Yes/No): ")
hari = input("Masukkan hari: ")

# Ketetntuan Promo Ongkir
if total_belanja >= 400000 :
    diskon_ongkir = 1.0
    print("Anda mendapatkan potongan ongkir 100%")
elif total_belanja >= 250000 :
    diskon_ongkir = 0.75
    print("Anda mendapatkan potongan ongkir 75%")
elif total_belanja >= 150000 :
    diskon_ongkir = 0.5
    print("Anda mendapatkan ongkir 50%")
else :
    diskon_ongkir = 0
    print("Anda tidak mendapatkan ongkir")

total_ongkir = ongkir - (ongkir * diskon_ongkir)
print("Total ongkir adalah: ", total_ongkir, "%")


# ketentuan Cashback
if total_belanja >= 300000 :
    cashback = 10
    print("Anda mendapatkan cashback 10%")
elif total_belanja >= 200000 :
    cashback = 7
    print("Anda mendapatkan cashback 7%")
elif total_belanja >= 100000 :
    cashback = 5
    print("Anda mendapatkan cashback 5%")
else :
    cashback = 0
    print("Anda tidak mendapatkan cashback")

# Aturan Tambahan
if status_member == "yes" :
    cashback_member = 5
    print("Anda mendapatkan tambahan cashback 5%")
else :
    cashback_member = 0
    print("Anda tidak mendapatkan tambahan cashback")

if hari == "sabtu" :
    cashback_hari = 3
    print("Anda mendapatkan tambahan cashback 3%")
else :
    cashback_hari = 0
    print("Anda tidak mendapatkan tambahan cashback")

total_cashback = cashback + cashback_member + cashback_hari
if total_cashback <= 15 :
    print("Anda mendapatkan total cashback: ", total_cashback, "%")
else :
    print("Anda mendapatkan total cashback 15% karena maksimal hanya sampai 15%")
