import time
import random

# ==========================================
# 1. MODUL PENYIMPANAN DATA & UTILITAS
# ==========================================
DATABASE_MAHASISWA = []

def calculate_score(mhs):
    """Menghitung skor prioritas beasiswa (Weighted Scoring)."""
    score_ipk = (mhs["ipk"] / 4.0) * 100
    score_pendapatan = max(0, (15_000_000 - mhs["penghasilan"]) / 15_000_000) * 100
    score_tanggungan = min(5, mhs["tanggungan"]) * 20
    score_prestasi = min(3, mhs["prestasi"]) * 33.33
    
    total_skor = (score_ipk * 0.4) + (score_pendapatan * 0.3) + (score_tanggungan * 0.2) + (score_prestasi * 0.1)
    return round(total_skor, 2)

def generate_student_identity():
    """Menghasilkan kombinasi nama acak dan NIM awalan 2502029 dengan 2 digit belakang acak."""
    nama_depan = ["Andi", "Budi", "Candra", "Dedi", "Eko", "Fajar", "Gita", "Hendra", "Indah", "Joko", 
                  "Kevin", "Lestari", "Mega", "Nugroho", "Putri", "Rian", "Siti", "Taufik", "Utami", "Wawan"]
    nama_belakang = ["Pratama", "Santoso", "Wijaya", "Kusuma", "Hidayat", "Saputra", "Wibowo", "Setiawan", "Utomo", "Siregar"]
    
    nama_lengkap = f"{random.choice(nama_depan)} {random.choice(nama_belakang)}"
    dua_digit_belakang = f"{random.randint(0, 99):02d}"
    nim_kustom = f"2502029{dua_digit_belakang}"
    
    return nim_kustom, nama_lengkap

def generate_initial_data(size=10):
    """Menghasilkan data otomatis untuk diisi ke database utama."""
    global DATABASE_MAHASISWA
    DATABASE_MAHASISWA = []
    
    for _ in range(size):
        nim, nama = generate_student_identity()
        mahasiswa = {
            "nim": nim, "nama": nama,
            "ipk": round(random.uniform(2.5, 4.0), 2),
            "penghasilan": random.randint(1_500_000, 10_000_000),
            "tanggungan": random.randint(1, 5),
            "prestasi": random.randint(0, 3),
            "status_bantuan": "Layak"
        }
        mahasiswa["skor_akhir"] = calculate_score(mahasiswa)
        DATABASE_MAHASISWA.append(mahasiswa)


# ==========================================
# 2. FITUR CRUD (CREATE, READ, UPDATE, DELETE)
# ==========================================
def create_mahasiswa():
    print("\n--- Tambah Data Mahasiswa Baru ---")
    nim = input("Masukkan NIM: ")
    for mhs in DATABASE_MAHASISWA:
        if mhs["nim"] == nim:
            print("❌ Gagal: Mahasiswa dengan NIM tersebut sudah terdaftar!")
            return
            
    nama = input("Masukkan Nama: ")
    ipk = float(input("Masukkan IPK (0.00 - 4.00): "))
    penghasilan = int(input("Masukkan Penghasilan Orang Tua (Rp): "))
    tanggungan = int(input("Masukkan Jumlah Tanggungan: "))
    prestasi = int(input("Masukkan Jumlah Prestasi: "))
    
    mhs_baru = {"nim": nim, "nama": nama, "ipk": ipk, "penghasilan": penghasilan, "tanggungan": tanggungan, "prestasi": prestasi, "status_bantuan": "Layak"}
    mhs_baru["skor_akhir"] = calculate_score(mhs_baru)
    DATABASE_MAHASISWA.append(mhs_baru)
    print("✅ Data mahasiswa berhasil ditambahkan!")

def read_mahasiswa():
    """[PERBAIKAN] Menampilkan SELURUH data mahasiswa tanpa ada yang disembunyikan."""
    print("\n--- Daftar Seluruh Mahasiswa di Database ---")
    if not DATABASE_MAHASISWA:
        print("Database kosong.")
        return
        
    print("-" * 95)
    print(f"{'No':<5}{'NIM':<12}{'Nama':<22}{'IPK':<8}{'Penghasilan':<15}{'Tanggungan':<12}{'Skor':<10}")
    print("-" * 95)
    
    # Menampilkan semua data tanpa menggunakan slice limit lagi
    for idx, mhs in enumerate(DATABASE_MAHASISWA, 1):
        print(f"{idx:<5}{mhs['nim']:<12}{mhs['nama']:<22}{mhs['ipk']:<8}"
              f"Rp {mhs['penghasilan']:<12,}{mhs['tanggungan']:<12}{mhs['skor_akhir']:<10}")
    
    print("-" * 95)
    print(f"Total data saat ini: {len(DATABASE_MAHASISWA)} mahasiswa.")

def update_mahasiswa():
    print("\n--- Ubah Data Mahasiswa ---")
    nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
    for mhs in DATABASE_MAHASISWA:
        if mhs["nim"] == nim:
            nama_baru = input(f"Nama baru [{mhs['nama']}]: ")
            if nama_baru: mhs["nama"] = nama_baru
            ipk_baru = input(f"IPK baru [{mhs['ipk']}]: ")
            if ipk_baru: mhs["ipk"] = float(ipk_baru)
            mhs["skor_akhir"] = calculate_score(mhs)
            print("✅ Data mahasiswa berhasil diperbarui!")
            return
    print("❌ Mahasiswa dengan NIM tersebut tidak ditemukan.")

def delete_mahasiswa():
    print("\n--- Hapus Data Mahasiswa ---")
    nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
    for idx, mhs in enumerate(DATABASE_MAHASISWA):
        if mhs["nim"] == nim:
            DATABASE_MAHASISWA.pop(idx)
            print(f"✅ Mahasiswa dengan NIM {nim} berhasil dihapus.")
            return
    print("❌ Mahasiswa dengan NIM tersebut tidak ditemukan.")


# ==========================================
# 3. ALGORITMA SORTING & PRIORITY QUEUE
# ==========================================
def selection_sort(arr):
    data = list(arr)
    n = len(data)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if data[j]["skor_akhir"] > data[max_idx]["skor_akhir"]: max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]
    return data

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["skor_akhir"] >= right[j]["skor_akhir"]: result.append(left[i]); i += 1
        else: result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

class MaxHeapPriorityQueue:
    def __init__(self): self.heap = []
    def insert(self, mhs):
        self.heap.append(mhs)
        self._heapify_up(len(self.heap) - 1)
    def extract_max(self):
        if not self.heap: return None
        if len(self.heap) == 1: return self.heap.pop()
        max_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_item
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index]["skor_akhir"] > self.heap[parent]["skor_akhir"]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)
    def _heapify_down(self, index):
        left, right, largest = 2*index + 1, 2*index + 2, index
        if left < len(self.heap) and self.heap[left]["skor_akhir"] > self.heap[largest]["skor_akhir"]: largest = left
        if right < len(self.heap) and self.heap[right]["skor_akhir"] > self.heap[largest]["skor_akhir"]: largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)


# ==========================================
# 4. MODUL PENGUJIAN SKALA BESAR
# ==========================================
def run_interactive_experiments():
    """Mengizinkan user memilih skala pengujian dan langsung memasukkannya ke database utama."""
    print("\n=== MENU PENGUJIAN DATA MASAL (EKSPERIMEN) ===")
    print("[1] Uji & Isi dengan 100 Data")
    print("[2] Uji & Isi dengan 500 Data")
    print("[3] Uji & Isi dengan 1.000 Data")
    print("[4] Uji & Isi dengan 5.000 Data")
    
    pilihan = input("Pilih skala data pengujian: ")
    if pilihan == "1": size = 100
    elif pilihan == "2": size = 500
    elif pilihan == "3": size = 1000
    elif pilihan == "4": size = 5000
    else:
        print("❌ Pilihan tidak valid.")
        return

    print(f"\nGenerasi {size} data dengan NIM 2502029xx secara otomatis...")
    generate_initial_data(size)
    
    print(f"\nMengukur performa komputasi algoritma pada skala {size} data (5x pengulangan)...")
    print("-" * 65)
    
    t_select = []
    for i in range(1, 6):
        s = time.time()
        _ = selection_sort(DATABASE_MAHASISWA)
        durasi = (time.time() - s) * 1000
        t_select.append(durasi)
        print(f"  > Selection Sort Uji {i}: {durasi:.2f} ms")
        
    print("")
    t_merge = []
    for i in range(1, 6):
        s = time.time()
        _ = merge_sort(DATABASE_MAHASISWA)
        durasi = (time.time() - s) * 1000
        t_merge.append(durasi)
        print(f"  > Merge Sort Uji {i}    : {durasi:.2f} ms")
        
    print("-" * 65)
    print(f"📈 RATA-RATA EKSEKUSI DATA ({size} OBJEK):")
    print(f"   * Selection Sort : {sum(t_select)/5:.4f} ms")
    print(f"   * Merge Sort     : {sum(t_merge)/5:.4f} ms")
    print("-" * 65)
    print(f"✅ Berhasil! {size} data sekarang tersimpan di database utama.")
    print("Master bisa memilih Menu [1] untuk melihat SEMUA data tersebut.")


# ==========================================
# 5. SELEKSI PENERIMA (PRIORITY QUEUE)
# ==========================================
def saring_penerima_beasiswa():
    print("\n--- Proses Seleksi Penerima Beasiswa (Priority Queue) ---")
    if not DATABASE_MAHASISWA:
        print("❌ Gagal: Tidak ada data di database.")
        return
        
    try:
        kuota = int(input(f"Masukkan kuota beasiswa (Maksimal {len(DATABASE_MAHASISWA)}): "))
    except ValueError:
        print("❌ Masukkan angka valid.")
        return
        
    pq = MaxHeapPriorityQueue()
    for mhs in DATABASE_MAHASISWA: pq.insert(mhs)
        
    print(f"\n🎉 HASIL KEPUTUSAN: {min(kuota, len(DATABASE_MAHASISWA))} Mahasiswa Prioritas Tertinggi:")
    print("-" * 90)
    print(f"{'No':<5}{'NIM':<12}{'Nama':<22}{'IPK':<8}{'Skor Akhir':<10}")
    print("-" * 90)
    for i in range(1, kuota + 1):
        pemenang = pq.extract_max()
        if not pemenang: break
        print(f"{i:<5}{pemenang['nim']:<12}{pemenang['nama']:<22}{pemenang['ipk']:<8}{pemenang['skor_akhir']:<10}")
    print("-" * 90)


# ==========================================
# 6. MENU UTAMA INTERAKTIF
# ==========================================
def main_menu():
    generate_initial_data(10) # Default awal: 10 data
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
        elif pilihan == "6": run_interactive_experiments()
        elif pilihan == "0": break

if __name__ == "__main__":
    main_menu()