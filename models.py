import random

def calculate_score(mhs):
    """Menghitung skor prioritas beasiswa (Weighted Scoring)[cite: 48]."""
    score_ipk = (mhs["ipk"] / 4.0) * 100
    score_pendapatan = max(0, (15_000_000 - mhs["penghasilan"]) / 15_000_000) * 100
    score_tanggungan = min(5, mhs["tanggungan"]) * 20
    score_prestasi = min(3, mhs["prestasi"]) * 33.33
    
    total_skor = (score_ipk * 0.4) + (score_pendapatan * 0.3) + (score_tanggungan * 0.2) + (score_prestasi * 0.1)
    return round(total_skor, 2)

def generate_student_identity():
    """Menghasilkan kombinasi nama acak dan NIM kustom[cite: 14, 46]."""
    nama_depan = ["Andi", "Budi", "Candra", "Dedi", "Eko", "Fajar", "Gita", "Hendra", "Indah", "Joko", 
                  "Kevin", "Lestari", "Mega", "Nugroho", "Putri", "Rian", "Siti", "Taufik", "Utami", "Wawan"]
    nama_belakang = ["Pratama", "Santoso", "Wijaya", "Kusuma", "Hidayat", "Saputra", "Wibowo", "Setiawan", "Utomo", "Siregar"]
    
    nama_lengkap = f"{random.choice(nama_depan)} {random.choice(nama_belakang)}"
    dua_digit_belakang = f"{random.randint(0, 99):02d}"
    nim_kustom = f"2502029{dua_digit_belakang}"
    
    return nim_kustom, nama_lengkap