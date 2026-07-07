import time
import random
import models
import algoritma

DATABASE_MAHASISWA = []

def generate_initial_data(size=10):
    """Script pembangkit data otomatis untuk pengujian[cite: 61, 72]."""
    global DATABASE_MAHASISWA
    DATABASE_MAHASISWA = []
    
    for _ in range(size):
        nim, nama = models.generate_student_identity()
        mahasiswa = {
            "nim": nim, "nama": nama,
            "ipk": round(random.uniform(2.5, 4.0), 2),
            "penghasilan": random.randint(1_500_000, 10_000_000),
            "tanggungan": random.randint(1, 5),
            "prestasi": random.randint(0, 3),
            "status_bantuan": "Layak"
        }
        mahasiswa["skor_akhir"] = models.calculate_score(mahasiswa)
        DATABASE_MAHASISWA.append(mahasiswa)

def run_interactive_experiments():
    """Menguji performa pada 4 skala data dengan 5x pengulangan[cite: 57, 59]."""
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

    print(f"\nGenerasi {size} data secara otomatis...")
    generate_initial_data(size)
    
    print(f"\nMengukur performa algoritma pada skala {size} data (5x pengulangan)[cite: 57]...")
    print("-" * 65)
    
    t_select = []
    for i in range(1, 6):
        s = time.time()
        _ = algoritma.selection_sort(DATABASE_MAHASISWA)
        durasi = (time.time() - s) * 1000
        t_select.append(durasi)
        print(f"  > Selection Sort Uji {i}: {durasi:.2f} ms")
        
    print("")
    t_merge = []
    for i in range(1, 6):
        s = time.time()
        _ = algoritma.merge_sort(DATABASE_MAHASISWA)
        durasi = (time.time() - s) * 1000
        t_merge.append(durasi)
        print(f"  > Merge Sort Uji {i}    : {durasi:.2f} ms")
        
    print("-" * 65)
    print(f"📈 RATA-RATA EKSEKUSI DATA ({size} OBJEK)[cite: 57]:")
    print(f"   * Selection Sort : {sum(t_select)/5:.4f} ms")
    print(f"   * Merge Sort     : {sum(t_merge)/5:.4f} ms")
    print("-" * 65)
    print(f"✅ Berhasil! {size} data tersimpan di database utama.")