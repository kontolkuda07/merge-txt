import os

# Meminta input dari pengguna
folder_path = input("Masukkan folder: ").strip()
output_file = input("Nama output file: ").strip()

# Pastikan folder valid
if not os.path.isdir(folder_path):
    print("Folder tidak ditemukan. Pastikan path sudah benar!")
else:
    # Membuka file output untuk menulis hasil gabungan
    with open(output_file, "w", encoding="utf-8") as outfile:
        # Loop melalui semua file di folder
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):  # Hanya memproses file .txt
                file_path = os.path.join(folder_path, filename)
                
                with open(file_path, "r", encoding="utf-8") as infile:
                    outfile.write(f"\n=== {filename} ===\n")  # Menambahkan nama file sebagai header
                    outfile.write(infile.read())  # Menulis isi file ke hasil gabungan
                    outfile.write("\n\n")  # Menambahkan baris kosong sebagai pemisah
        
    print(f"Semua file .txt telah digabungkan ke dalam '{output_file}'")
