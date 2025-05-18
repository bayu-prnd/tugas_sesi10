inventaris={}

def tambah_barang():
    nama_barang = input("masukkan nama barang:")
    harga = input("masukkan harga:")
    stock = input("masukkan jumlah stock: ")

    inventaris[nama_barang] = (harga,stock)
    print("barang berhasil ditambahkan")

def tampilkan_barang():
    if not inventaris:
        print("tidak ada barang di inventaris")
    else:
        print("\nDaftar_barang:")
        print(f"{'nama barang':<20}{'harga':<10}{'stock':<10}")
        print("-"*40)
        for nama, (harga,stock) in inventaris.items():
            barang_info = (nama,harga,stock)
            print(f"{barang_info[0]:<20}{barang_info[1]:<10}{barang_info[3]:<10}")

def cari_barang():
    nama_barang = input("masukkan nama barang:")
    if nama_barang in inventaris:
        stock_baru = int(input("masukkan jumlah stock baru:"))
        harga = inventaris[nama_barang[0]]
        inventaris[nama_barang] = (harga, stock_baru)
        print("stock barang telah diperbaharui")
    else:
        print("barang tidakditemukan")

def analisis_data():
    if not inventaris:
        print("dalam inventaris analisis tidak ada barang")
        return
    
    harga_barang = [(nama, info[0])for nama, info in inventaris.items()]
    harga_tertinggi = max(harga_barang,key=lambda x : x[1])
    harga_terendah = min(harga_barang, key = lambda x:x[1])
    total_nilai_stock = sum(harga*stock for harga, stock in inventaris.values())

    print(f"barang dengan harga tertinggi : {harga_tertinggi[0]}-harga:{harga_tertinggi[1]}")
    print(f"barang dengan harga terendah : {harga_terendah[0]}-harga{harga_terendah[1]}")
    print(f"total nilai stock : {total_nilai_stock}")

def main():
    while True:
        print("/nMenu manajemen inventaris barang")
        print("1. Tambah barang baru")
        print("2. tapilkan semua barang")
        print("3. mencari barang")
        print("4. update stock")
        print("5. hapus barang ")
        print("6. analisis data")
        print("7. keluar")

pilihan = input("opsi pilihan(1-7):")

if pilihan =='1':
    tambah_barang()
elif pilihan =='2':
    tampilkan_barang()
elif pilihan =='3':
    cari_barang()
elif pilihan =='4':
    update_stock()
elif pilihan =='5':
    hapus_barang()
elif pilihan =='6':
    analisis_data()
elif pilihan =='7':
    print("program selesai")
    break
else: 
    print("pilihan tidak valid")

if __name__=="__main_":
    main()