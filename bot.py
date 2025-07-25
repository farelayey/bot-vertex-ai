import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import time
import os

# --- Konfigurasi Otomatis dari Lingkungan GitHub ---
# Kode ini akan otomatis mengambil ID Proyek dari lingkungan GitHub Actions
# Anda hanya perlu menggantinya jika menjalankan secara lokal.
PROJECT_ID = "bot-gambar-otomatis" 
LOCATION = "us-central1" # Lokasi ini seringkali memiliki ketersediaan model yang baik

# Inisialisasi Vertex AI
try:
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    print(f"✅ Vertex AI berhasil diinisialisasi untuk proyek {PROJECT_ID}")
except Exception as e:
    print(f"❌ Gagal inisialisasi Vertex AI: {e}")
    exit() # Hentikan skrip jika inisialisasi gagal

# Memuat model Imagen
print("🔄 Memuat model Imagen...")
model = ImageGenerationModel.from_pretrained("imagegeneration@005")
print("✅ Model Imagen berhasil dimuat.")

# --- Daftar Prompt (Ide Gambar) ---
# Anda bisa menambahkan atau mengubah daftar ini sesuka Anda!
list_of_prompts = [
    "Seekor rubah oranye sedang membaca buku di bawah pohon rindang, gaya kartun Ghibli",
    "Pemandangan kota Jakarta di masa depan dengan mobil terbang dan gedung pencakar langit ramah lingkungan",
    "Close-up foto secangkir kopi latte art dengan motif batik di atasnya"
]

# --- Logika Utama Bot ---
print("\n--- Memulai Proses Pembuatan Gambar ---")
file_counter = int(time.time()) # Menggunakan waktu saat ini agar nama file unik

for prompt in list_of_prompts:
    try:
        print(f"\n⏳ Membuat gambar untuk prompt: '{prompt}'...")
        
        # Mengirim permintaan ke API Imagen
        images = model.generate_images(
            prompt=prompt,
            number_of_images=1,
            aspect_ratio="1:1", # 1:1 untuk persegi, 16:9 untuk landscape
            safety_filter_level="block_some"
        )
        
        # Menyimpan gambar
        file_name = f"gambar_{file_counter}.png"
        images[0].save(location=file_name)
        
        print(f"✅ Gambar berhasil disimpan sebagai {file_name}")
        file_counter += 1
        
    except Exception as e:
        print(f"❌ Gagal membuat gambar untuk prompt ini. Error: {e}")
        
    # Beri jeda 10 detik antar permintaan agar tidak membebani sistem
    print("... jeda 10 detik ...")
    time.sleep(10)

print("\n🎉 Semua prompt telah selesai diproses. Bot selesai bekerja.")