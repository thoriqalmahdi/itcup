# Input data
K = int(input())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
N = int(input())
B = list(map(int, input().split()))

# Inisialisasi variabel biaya minimum dengan nilai tak terhingga
min_biaya = float('inf')

# Fungsi untuk mencari biaya minimum untuk memindahkan ayam ke kandang yang berbeda
def cari_biaya_minimal(kandang, ayam):
    biaya_minimal = float('inf')
    for k in range(K):
        if k != kandang:
            biaya = P[k] * ayam + C[k]
            biaya_minimal = min(biaya_minimal, biaya)
    return biaya_minimal

# Fungsi untuk mencari biaya total minimum untuk memindahkan semua ayam ke kandang yang berbeda
def cari_biaya_total_minimal():
    # Inisialisasi variabel total biaya dengan nilai 0
    total_biaya = 0
    
    # Loop untuk setiap kandang
    for k in range(K):
        # Inisialisasi variabel jumlah ayam pada kandang dengan nilai 0
        ayam_pada_kandang = 0
        
        # Loop untuk setiap ayam pada kandang
        for i in range(N):
            if B[i] == k + 1:
                ayam_pada_kandang += 1
            else:
                # Jika kandang sudah penuh, cari biaya minimum untuk memindahkan ayam ke kandang yang berbeda
                if ayam_pada_kandang == P[k]:
                    biaya_minimal = cari_biaya_minimal(k, ayam_pada_kandang)
                    total_biaya += biaya_minimal
                    ayam_pada_kandang = 0
                
                # Tambah jumlah ayam pada kandang
                ayam_pada_kandang += 1
        
        # Jika masih ada ayam pada kandang, cari biaya minimum untuk memindahkan ayam ke kandang yang berbeda
        if ayam_pada_kandang > 0:
            biaya_minimal = cari_biaya_minimal(k, ayam_pada_kandang)
            total_biaya += biaya_minimal
    
    return total_biaya

# Cari biaya total minimum untuk memindahkan semua ayam ke kandang yang berbeda
min_biaya = cari_biaya_total_minimal()

# Output hasil pencarian biaya minimum
print(min_biaya)
