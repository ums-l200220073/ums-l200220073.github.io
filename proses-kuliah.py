from metaflow import FlowSpec, step

class InformatikaCourseFlow(FlowSpec):
    
    @step
    def start(self):
        # Langkah awal proses kuliah
        print("Memulai proses kuliah di Informatika.")
        self.next(self.bayar_spp)
    
    @step
    def bayar_spp(self):
        # Tahap pembayaran SPP
        print("Membayar SPP untuk semester ini.")
        # Misal: status pembayaran sukses
        self.spp_paid = True
        self.next(self.pilih_matakuliah)
    
    @step
    def pilih_matakuliah(self):
        # Tahap memilih mata kuliah
        if self.spp_paid:
            print("Memilih mata kuliah untuk semester ini.")
            self.matakuliah = ["Struktur Data", "Algoritma", "Pemrograman Lanjut"]
        else:
            print("SPP belum dibayar. Tidak bisa memilih mata kuliah.")
            self.matakuliah = []
        self.next(self.ikuti_kuliah)
    
    @step
    def ikuti_kuliah(self):
        # Tahap mengikuti perkuliahan
        if self.matakuliah:
            print(f"Mengikuti kuliah untuk matakuliah: {', '.join(self.matakuliah)}.")
            # Misal semua perkuliahan diikuti
            self.attended_classes = True
        else:
            print("Tidak ada mata kuliah yang diikuti.")
            self.attended_classes = False
        self.next(self.ujian)
    
    @step
    def ujian(self):
        # Tahap ujian
        if self.attended_classes:
            print("Mengikuti ujian akhir.")
            # Misal nilai ujian
            self.nilai_ujian = {"Struktur Data": 80, "Algoritma": 85, "Pemrograman Lanjut": 90}
        else:
            print("Tidak mengikuti ujian karena tidak ada kuliah yang diikuti.")
            self.nilai_ujian = {}
        self.next(self.hitung_nilai_akhir)
    
    @step
    def hitung_nilai_akhir(self):
        # Tahap menghitung nilai akhir
        if self.nilai_ujian:
            self.nilai_akhir = sum(self.nilai_ujian.values()) / len(self.nilai_ujian)
            print(f"Nilai akhir semester ini: {self.nilai_akhir}")
        else:
            print("Tidak ada nilai ujian yang bisa dihitung.")
            self.nilai_akhir = None
        self.next(self.end)
    
    @step
    def end(self):
        # Akhir proses
        print("Proses kuliah selesai.")
        if self.nilai_akhir:
            print(f"Selamat! Anda selesai dengan nilai akhir: {self.nilai_akhir}")
        else:
            print("Tidak ada nilai yang tercatat.")

# Menjalankan flow
if __name__ == '__main__':
    InformatikaCourseFlow()
