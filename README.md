# Chatbot Gemini Sederhana (Flask + Google Gemini API)

Proyek ini adalah chatbot web sederhana menggunakan [Flask](https://flask.palletsprojects.com/) dan Google Gemini API (`gemini-2.0-flash`). Anda dapat mengirim pesan ke AI dan mendapatkan balasan secara real-time melalui web.

## Fitur
- Chatbot AI berbasis Google Gemini API
- Antarmuka web sederhana dan modern (HTML + CSS terpisah)
- Mudah dijalankan secara lokal

## Struktur Folder
```
GEMINI/
│
├── google_ai.py
├── API_KEY.txt
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Cara Instalasi & Menjalankan

1. **Clone/download** repositori ini.
2. **Buat file `API_KEY.txt`** di folder utama, isi dengan API key Gemini Anda (hanya baris pertama).
3. **Install dependencies**:
    ```
    pip install flask requests
    ```
4. **Jalankan aplikasi**:
    ```
    python google_ai.py
    ```
5. **Buka browser** ke [http://127.0.0.1:5000/](http://127.0.0.1:5000/) untuk mulai chat.

## Konfigurasi API Key
- Dapatkan API key dari Google AI Studio atau Google Cloud Console.
- Simpan API key di file `API_KEY.txt` (tanpa spasi/enter tambahan).

## Kustomisasi
- Edit tampilan di `templates/index.html` dan `static/style.css`.
- Ubah logika chatbot di fungsi `chat_with_gemini` pada `google_ai.py`.

## Lisensi
Proyek ini untuk pembelajaran dan non-komersial.
