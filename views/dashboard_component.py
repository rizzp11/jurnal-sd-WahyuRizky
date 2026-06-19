def render_dashboard(data_list, is_loading):
    print("--- DASHBOARD APLIKASI ---")
    
    # Jika is_loading bernilai True, tampilkan teks Mohon Tunggu
    if is_loading:
        print("Mohon Tunggu...")
    else:
        if not data_list:
            print("[!] Data Kosong. Silakan sinkronisasi dengan Backend.")
        else:
            for item in data_list:
                print(f"- Item ID: {item['id']} | Nama: {item['name']}")