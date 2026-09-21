# 🏄 Panduan Setup — Pancoran Slide Festival 2026

## File yang Ada
| File | Fungsi |
|------|--------|
| `index.html` | Form pendaftaran peserta |
| `Code.gs` | Backend Google Apps Script |
| `SETUP_GUIDE.md` | Panduan ini |

---

## Langkah 1 — Buat Google Spreadsheet
1. Buka [sheets.google.com](https://sheets.google.com)
2. Buat spreadsheet baru → beri nama **"Pendaftaran PSF 2026"**
3. Salin **ID spreadsheet** dari URL:
   ```
   https://docs.google.com/spreadsheets/d/[INI_ADALAH_ID_NYA]/edit
   ```

---

## Langkah 2 — Buat Folder Google Drive
1. Buka [drive.google.com](https://drive.google.com)
2. Buat folder baru → beri nama **"Bukti Bayar PSF 2026"**
3. Klik kanan folder → **Share** → ubah akses menjadi **"Anyone with the link"**
4. Salin **ID folder** dari URL:
   ```
   https://drive.google.com/drive/folders/[INI_ADALAH_ID_NYA]
   ```

---

## Langkah 3 — Deploy Google Apps Script
1. Buka [script.google.com](https://script.google.com) → **New project**
2. Paste seluruh isi file `Code.gs`
3. Ganti dua baris CONFIG:
   ```javascript
   const SPREADSHEET_ID  = 'ID_spreadsheet_Anda_dari_langkah_1';
   const DRIVE_FOLDER_ID = 'ID_folder_Drive_Anda_dari_langkah_2';
   ```
4. Klik **Deploy → New deployment**
5. Pilih type: **Web app**
6. Execute as: **Me**
7. Who has access: **Anyone**
8. Klik **Deploy** → izinkan akses → **Copy** URL yang muncul

---

## Langkah 4 — Hubungkan Form
1. Buka `index.html` dengan teks editor
2. Cari baris:
   ```javascript
   const SCRIPT_URL = 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE';
   ```
3. Ganti dengan URL dari langkah 3:
   ```javascript
   const SCRIPT_URL = 'https://script.google.com/macros/s/xxxxx/exec';
   ```
4. Simpan file

---

## Langkah 5 — Isi Data Pembayaran
Di `index.html`, cari dan ganti placeholder berikut:
```html
[NAMA BANK]         → contoh: BCA
[NOMOR REKENING]    → contoh: 1234567890
[NAMA PEMILIK]      → contoh: Pancoran Group
[Gambar QRIS di sini] → ganti dengan tag <img src="qris.png" ...>
```

---

## Langkah 6 — Ganti Logo (Opsional)
Di `index.html`, cari:
```html
<div class="hero-logo-placeholder">🏄</div>
```
Ganti dengan:
```html
<img class="hero-logo" src="logo.png" alt="Logo"/>
```

---

## Test Form
- Buka `index.html` di browser
- Isi form → submit
- Cek Google Sheets → data harus muncul
- Cek folder Drive → file bukti bayar harus ada

---

## Catatan Penting
- File upload maks. **5 MB**
- Format yang diterima: **JPG, PNG, PDF**
- Rekening Pembayaran: **Bank BCA 2646 677 677 a.n. Srono Perkasa Sejahtera**
- Nomor WA Contact Person Konfirmasi: **0813 3728 031**
