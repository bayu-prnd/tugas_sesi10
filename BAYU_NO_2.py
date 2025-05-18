data_mahasiswa={}

def tambah_data():
    NIM = input("Masukkan NIM:")
    NAMA= input("Masukkan Nama:")
    JURUSAN= input("Masukkan Jurusan:")
    IPK= input("Masukkan IPK:")

    data_mahasiswa[NIM]= {'Nama': NAMA, 'Jurusan':JURUSAN, 'IPK':IPK}
    print("Data mahasiswa berhasil ditambahkan.")

def tampilan_data():
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa")
    else:
        for NIM, info in data_mahasiswa.items():
            mahasiswa_info = (NIM, info['Nama'], info['Jurusan'], info['IPK'])
            print(f"NIM:{mahasiswa_info[0]}, Nama:{mahasiswa_info[1]}, Jurusan:{mahasiswa_info[2]}, IPK:{mahasiswa_info[3]}")

def cari_data():
    NIM=input("Masukkan NIM yang akan dicari:")
    if NIM in data_mahasiswa:
        info = data_mahasiswa[NIM]
        mahasiswa_info = (NIM, info['Nama'], info['Jurusan'], info['IPK'])
        print(f"NIM:{mahasiswa_info[0]}, Nama:{mahasiswa_info[1]}, Jurusan:{mahasiswa_info[2]}, IPK:{mahasiswa_info[3]}")
    else:
        print("Data mahasiswa tidak ditemukan.")


def hapus_data():
    NIM = input("Masukkan NIM yang akan dihapus:")
    if NIM in data_mahasiswa:
        del data_mahasiswa[NIM]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Data mahasiswa tidak ditemukan.")

def main():
    while True:
        print("\nMenu pengelolaan data mahasiswa")
        print("1. Tambahkan data mahasiswa yang baru")
        print("2. Tambilkan semua data mahasiswa")
        print("3. Cari darta mahasiswa berdasarkan dengann NIP")
        print("4. Menghapus data mahasiswa berdasarkan NIM")
        print("5. Kelular")

        pilihan = input("pilih menu opsi (1-10):")


        if pilihan =='1':
            tambah_data()
        elif pilihan =='2':
            tampilan_data()
        elif pilihan =='3':
            cari_data()
        elif pilihan =='4':
            hapus_data()
        elif pilihan =='5':
            print("Program telah selesai")
            break
        else:
            print("pilihan tidak valid, silahkan untuk dicoba lagi")
    if __name__ == "_main_":
        main()

