import random

# Simulasikan data dari database
users = [{"id": 1, "name": "Admin"}, {"id": 2, "name": "User"}]

def get_users():
    # Menghasilkan angka acak antara 1 sampai 10
    # Jika angka ganjil, anggap server sibuk (simulasi error)
    if random.randint(1, 10) % 2 != 0:
        return {"status": "error", "message": "Server sedang sibuk. Silakan coba beberapa saat lagi."}
    
    # Jika angka genap, return data sukses
    return {"status": "success", "data": users}