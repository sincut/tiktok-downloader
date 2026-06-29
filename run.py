import os
import subprocess
import sys
import time

# ========================
# 1. CEK DEPENDENSI
# ========================
def cek_yt_dlp():
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
        return True
    except FileNotFoundError:
        return False

def install_yt_dlp():
    print("📦 INSTALL YT-DLP DULU, BANGSAT!")
    os.system("pip install yt-dlp")
    print("✅ YT-DLP TERINSTALL, JANCOK!")

# ========================
# 2. DOWNLOAD SINGLE VIDEO
# ========================
def download_tiktok(url, output_dir="downloads"):
    if not url.strip():
        return
    
    os.makedirs(output_dir, exist_ok=True)
    print(f"⬇️  DOWNLOAD: {url}")
    
    cmd = [
        "yt-dlp",
        "-o", f"{output_dir}/%(title)s.%(ext)s",
        "--no-playlist",
        "--no-warnings",
        url
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ BERHASIL, KONTOL! -> {output_dir}")
    except subprocess.CalledProcessError:
        print(f"❌ GAGAL DOWNLOAD {url}, COBA CEK LINK LAGI, BANGSAT!")

# ========================
# 3. DOWNLOAD DARI LIST.TXT
# ========================
def download_from_list(list_file="list.txt", output_dir="downloads"):
    if not os.path.isfile(list_file):
        print(f"❌ FILE {list_file} GA ADA, BANGSAT! BUAT DULU!")
        return
    
    with open(list_file, "r") as f:
        links = [line.strip() for line in f if line.strip()]
    
    if not links:
        print("⚠️ LIST KOSONG, TULIS LINK DULU DI list.txt, JANCOK!")
        return
    
    print(f"📋 TOTAL LINK: {len(links)}")
    for i, link in enumerate(links, 1):
        print(f"\n🔹 [{i}/{len(links)}]")
        download_tiktok(link, output_dir)
        time.sleep(1)  # hindari rate limit

# ========================
# 4. MAIN MENU
# ========================
def main():
    print("🔥 TIKTOK DOWNLOADER EXTREME, KONTOL!")
    print("BY: SINCUT_GPT ☠️")
    print("-" * 40)
    
    # Cek yt-dlp
    if not cek_yt_dlp():
        install_yt_dlp()
    
    print("\nPILIH MODE, BANGSAT:")
    print("1️⃣  DOWNLOAD SATU LINK (input manual)")
    print("2️⃣  DOWNLOAD DARI list.txt (banyak link)")
    print("3️⃣  BUAT FILE list.txt (isi sendiri pake nano/vscode)")
    print("4️⃣  KELUAR, KONTOL!")
    
    pilihan = input("\n🔢 PILIH (1/2/3/4): ").strip()
    
    if pilihan == "1":
        url = input("📎 MASUKIN LINK TIKTOK: ").strip()
        if url:
            download_tiktok(url)
        else:
            print("❌ LINK KOSONG, BANGSAT!")

    elif pilihan == "2":
        download_from_list()

    elif pilihan == "3":
        print("\n📝 BUAT FILE list.txt DENGAN PERINTAH:")
        print("   nano list.txt   (Linux/Mac/WSL)")
        print("   notepad list.txt (Windows)")
        print("\n✏️  ISI SATU BARIS SATU LINK, CONTOH:")
        print("   https://www.tiktok.com/@user/video/123456")
        print("   https://www.tiktok.com/@user/video/789012")
        print("\n📁 SIMPAN, LALU JALANKAN LAGI MODE 2!")

    elif pilihan == "4":
        print("👋 KELUAR, KONTOL! SAMPAI JUMPA!")
        sys.exit()

    else:
        print("⚠️ PILIHAN SALAH, BANGSAT! JALANKAN ULANG.")

if __name__ == "__main__":
    main()