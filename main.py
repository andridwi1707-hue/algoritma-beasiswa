import models
import pengujian
from struktur_data import MaxHeapPriorityQueue

def create_mahasiswa():
    print("\n--- Tambah Data Mahasiswa Baru (Create) [cite: 61] ---")
    nim = input("Masukkan NIM: ")
    for mhs in pengujian.DATABASE_MAHASISWA:
        if mhs["nim"] == nim:
            print("❌ Gagal: Mahasiswa dengan NIM tersebut sudah terdaftar!")
            return
            
    nama = input("Masukkan Nama: ")
    ipk = float(input("Masukkan IPK (0.00 - 4.00): "))
    penghasilan = int(input("Masukkan Penghasilan Orang Tua (Rp): "))
    tanggungan = int(input("Masukkan Jumlah Tanggungan: "))
    prestasi = int(input("Masukkan Jumlah Prestasi: "))
    
    mhs_baru = {"nim": nim, "nama": nama, "ipk": ipk, "penghasilan": penghasilan, "tanggungan": tanggungan, "prestasi": prestasi, "status_bantuan": "Layak"}
    mhs_baru["skor_akhir"] = models.calculate_score(mhs_baru)
    pengujian.DATABASE_MAHASISWA.append(mhs_baru)
    print("✅ Data mahasiswa berhasil ditambahkan!")

def read_mahasiswa():
    print("\n--- Daftar Seluruh Mahasiswa di Database (Read) [cite: 61] ---")
    if not pengujian.DATABASE_MAHASISWA:
        print("Database kosong.")
        return
        
    print("-" * 95)
    print(f"{'No':<5}{'NIM':<12}{'Nama':<22}{'IPK':<8}{'Penghasilan':<15}{'Tanggungan':<12}{'Skor':<10}")
    print("-" * 95)
    
    for idx, mhs in enumerate(pengujian.DATABASE_MAHASISWA, 1):
        print(f"{idx:<5}{mhs['nim']:<12}{mhs['nama']:<22}{mhs['ipk']:<8}"
              f"Rp {mhs['penghasilan']:<12,}{mhs['tanggungan']:<12}{mhs['skor_akhir']:<10}")
    
    print("-" * 95)
    print(f"Total data saat ini: {len(pengujian.DATABASE_MAHASISWA)} mahasiswa.")

def update_mahasiswa():
    print("\n--- Ubah Data Mahasiswa (Update) [cite: 62] ---")
    nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
    for mhs in pengujian.DATABASE_MAHASISWA:
        if mhs["nim"] == nim:
            nama_baru = input(f"Nama baru [{mhs['nama']}]: ")
            if nama_baru: mhs["nama"] = nama_baru
            ipk_baru = input(f"IPK baru [{mhs['ipk']}]: ")
            if ipk_baru: mhs["ipk"] = float(ipk_baru)
            mhs["skor_akhir"] = models.calculate_score(mhs)
            print("✅ Data mahasiswa berhasil diperbarui!")
            return
    print("❌ Mahasiswa dengan NIM tersebut tidak ditemukan.")

def delete_mahasiswa():
    print("\n--- Hapus Data Mahasiswa (Delete) [cite: 62] ---")
    nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
    for idx, mhs in enumerate(pengujian.DATABASE_MAHASISWA):
        if mhs["nim"] == nim:
            pengujian.DATABASE_MAHASISWA.pop(idx)
            print(f"✅ Mahasiswa dengan NIM {nim} berhasil dihapus.")
            return
    print("❌ Mahasiswa dengan NIM tersebut tidak ditemukan.")

def saring_penerima_beasiswa():
    print("\n--- Proses Seleksi Penerima Beasiswa (Max-Heap) [cite: 47] ---")
    if not pengujian.DATABASE_MAHASISWA:
        print("❌ Gagal: Tidak ada data di database.")
        return
        
    try:
        kuota = int(input(f"Masukkan kuota beasiswa (Maksimal {len(pengujian.DATABASE_MAHASISWA)}): "))
    except ValueError:
        print("❌ Masukkan angka valid.")
        return
        
    pq = MaxHeapPriorityQueue()
    for mhs in pengujian.DATABASE_MAHASISWA: 
        pq.insert(mhs)
        
    print(f"\n🎉 HASIL KEPUTUSAN: {min(kuota, len(pengujian.DATABASE_MAHASISWA))} Mahasiswa Prioritas Tertinggi[cite: 64]:")
    print("-" * 90)
    print(f"{'No':<5}{'NIM':<12}{'Nama':<22}{'IPK':<8}{'Skor Akhir':<10}")
    print("-" * 90)
    for i in range(1, kuota + 1):
        pemenang = pq.extract_max()
        if not pemenang: 
            break
        print(f"{i:<5}{pemenang['nim']:<12}{pemenang['nama']:<22}{pemenang['ipk']:<8}{pemenang['skor_akhir']:<10}")
    print("-" * 90)

def main():
    pengujian.generate_initial_data(10) # Data awal standar [cite: 61]
    while True:
        print("\n==================================================")
        print("   SISTEM MANAJEMEN & SELEKSI BEASISWA (TOPIK 7)   ")
        print("==================================================")
        print("[1] Lihat Semua Data Mahasiswa (Read)")
        print("[2] Tambah Mahasiswa Baru (Create)")
        print("[3] Ubah Data Mahasiswa (Update)")
        print("[4] Hapus Data Mahasiswa (Delete)")
        print("[5] Jalankan Proses Seleksi Beasiswa (Heap/PQ)")
        print("[6] Isi Data Masal & Jalankan Analisis Algoritma")
        print("[0] Keluar Aplikasi")
        print("==================================================")
        
        pilihan = input("Pilih Menu: ")
        if pilihan == "1": read_mahasiswa()
        elif pilihan == "2": create_mahasiswa()
        elif pilihan == "3": update_mahasiswa()
        elif pilihan == "4": delete_mahasiswa()
        elif pilihan == "5": saring_penerima_beasiswa()
        elif pilihan == "6": pengujian.run_interactive_experiments()
        elif pilihan == "0": break

if __name__ == "__main__":
    main()