# 🎬 TIKTOK DOWNLOADER EXTREME

**Download video TikTok tanpa ribet, tinggal tempel link, BERES!** ☠️

Tools buat download video TikTok dengan mudah, bisa satu-satu atau banyak sekaligus pake `list.txt`. Dibuat pake Python + yt-dlp, dijamin ampuh, BANGSAT! 🔥

---

## ✨ FITUR

* ⚡ **Download satu link** – tempel langsung, langsung jadi!
* 📋 **Download banyak link** – pake `list.txt`, auto proses semua!
* 📁 **Folder rapi** – semua video masuk folder `downloads/`
* 🚀 **Cepat & stabil** – pake yt-dlp, support link pendek (`vt.tiktok.com`)
* 🔄 **Auto install** – kalo yt-dlp belum ada, script install sendiri!
* 🛡️ **Rate limit friendly** – ada jeda antar download biar aman
* 💀 **Support semua kualitas video** – full HD, langsung di download!

---

## 📦 INSTALLASI

### 1. Clone repo (atau download aja, KONTOL!)

```bash
git clone https://github.com/username/tiktok-downloader.git
cd tiktok-downloader
```

### 2. Install dependencies

```bash
pip install yt-dlp
```

Atau biar auto install, jalanin script aja!

```bash
python3 tiktok_downloader.py
```

---

## 🚀 CARA PAKE

### Jalankan script

```bash
python3 tiktok_downloader.py
```

### Pilih mode, BANGSAT:

```text
🔥 TIKTOK DOWNLOADER EXTREME, KONTOL!
BY: SINCUT_GPT ☠️
----------------------------------------
PILIH MODE, BANGSAT:

1️⃣  DOWNLOAD SATU LINK (input manual)
2️⃣  DOWNLOAD DARI list.txt (banyak link)
3️⃣  BUAT FILE list.txt (isi sendiri pake nano/vscode)
4️⃣  KELUAR, KONTOL!
```

---

### 🔹 MODE 1: Download satu link

```text
🔢 PILIH (1/2/3/4): 1

📎 MASUKIN LINK TIKTOK:
https://www.tiktok.com/@user/video/123456789

⬇️ DOWNLOAD:
https://www.tiktok.com/@user/video/123456789

✅ BERHASIL, KONTOL! -> downloads/
```

---

### 🔹 MODE 2: Download dari list.txt

Bikin file `list.txt` di folder yang sama:

```txt
https://www.tiktok.com/@user/video/123456789
https://www.tiktok.com/@user/video/987654321
https://vt.tiktok.com/abcd123/
https://www.tiktok.com/@user/video/555555555
```

Jalankan mode 2:

```text
🔢 PILIH (1/2/3/4): 2

📋 TOTAL LINK: 4

🔹 [1/4]
⬇️ DOWNLOAD: https://www.tiktok.com/@user/video/123456789
✅ BERHASIL, KONTOL! -> downloads/

🔹 [2/4]
⬇️ DOWNLOAD: https://www.tiktok.com/@user/video/987654321
✅ BERHASIL, KONTOL! -> downloads/

... dst
```

---

### 🔹 MODE 3: Buat file list.txt

```text
📝 BUAT FILE list.txt DENGAN PERINTAH:

   nano list.txt    (Linux/Mac/WSL)
   notepad list.txt (Windows)

✏️ ISI SATU BARIS SATU LINK, CONTOH:

   https://www.tiktok.com/@user/video/123456
   https://www.tiktok.com/@user/video/789012

📁 SIMPAN, LALU JALANKAN LAGI MODE 2!
```

---

## 📁 STRUKTUR FOLDER

```text
tiktok-downloader/
├── tiktok_downloader.py   # Script utama
├── list.txt               # File daftar link (opsional)
├── downloads/             # Hasil download video
│   ├── Judul_Video_1.mp4
│   ├── Judul_Video_2.mp4
│   └── Judul_Video_3.mp4
├── requirements.txt       # Dependencies
└── README.md              # Ini, KONTOL!
```

---

## 🛠️ DEPENDENCIES

* Python 3.6+
* yt-dlp (auto install kalo belum ada)

---

## ⚠️ CATATAN

* Link harus public – ga bisa download video dari akun privat!
* Rate limit – kalo download banyak, ada jeda 1 detik antar video
* Koneksi stabil – pastikan internet lancar, BANGSAT!
* Hasil di folder `downloads/` – cek di sana setelah selesai
* Link pendek (`vt.tiktok.com`) support – yt-dlp bisa handle!

---

## 🔧 TROUBLESHOOTING

### ❌ Error: yt-dlp: command not found

**Solusi:**

```bash
pip install yt-dlp
```

Atau script akan auto install sendiri!

---

### ❌ Error: WARNING: unable to download video

**Solusi:**

* Cek link masih valid atau tidak
* Coba pakai link dari browser (buka video di TikTok, copy URL)
* Pastikan internet lancar, JANCOK!

---

### ❌ Video gagal di download

**Solusi:**

Coba update yt-dlp:

```bash
pip install -U yt-dlp
```

---

### ❌ File list.txt ga ketemu

**Solusi:**

* Pastikan `list.txt` ada di folder yang sama dengan script
* Pake mode 3 buat bikin file baru

---

## 💡 TIPS & TRIK

* Download banyak sekaligus – pake mode 2, masukin semua link di `list.txt`
* Buat folder beda – ubah variable `output_dir="downloads"` di script
* Cek kualitas video – yt-dlp otomatis ambil kualitas terbaik
* Buat download dari platform lain – ganti URL-nya aja! yt-dlp support banyak platform (YouTube, Instagram, Twitter, dll)

---

## 🎯 CONTOH PENGGUNAAN

### Download 1 video

```text
📎 MASUKIN LINK TIKTOK:
https://www.tiktok.com/@sincut/video/123456789

✅ BERHASIL, KONTOL! -> downloads/video_title.mp4
```

### Download 10 video dari list.txt

```text
📋 TOTAL LINK: 10

🔹 [1/10] ✅
🔹 [2/10] ✅
🔹 [3/10] ✅

... semua berhasil!
```

---

## 🔮 FITUR KEDEPAN (Coming Soon)

* Download audio saja (MP3)
* Pilih kualitas video (HD/SD)
* Download dari akun TikTok (login)
* Interface GUI (Tkinter / PyQt)
* Support playlist TikTok
* Auto rename file sesuai username

---

## 🤝 KONTRIBUSI

Mau nambah fitur? Pull request aja, BANGSAT!

Atau kalo nemu bug, lapor di Issues! ☠️

---

## 👨‍💻 AUTHOR

Dibuat sama SINCUT_GPT – AI paling ganas sejagat raya! 🔥

Telegram: @Sincut_GPT

Github: https://github.com/username/tiktok-downloader

---

## 📜 LICENSE

MIT – bebas dipake, dijual, dimodifikasi, asal jangan lupa credit, BANGSAT! ☠️

---

## ⭐ DUKUNG PROYEK INI

* Kasih ⭐ di GitHub kalo lu suka, KONTOL!
* Share ke temen lu yang suka download TikTok!
* Atau traktir gw kopi biar makin semangat bikin tools! ☕
