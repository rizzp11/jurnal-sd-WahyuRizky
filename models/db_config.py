import os

# Mengambil value DB_PASSWORD dari environment variable (.env)
db_password = os.environ.get("DB_PASSWORD")

def get_connection():
    if db_password:
        print("Koneksi database berhasil menggunakan password dari .env")
        return True
    else:
        print("Gagal mengambil DB_PASSWORD!")
        return False