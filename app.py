import time
from views.dashboard_component import render_dashboard

# Simulasi State Awal (Sedang Loading)
app_state = {"items": [], "is_loading": True}

def update_state(new_data):
    app_state["items"] = new_data
    app_state["is_loading"] = False

if __name__ == "__main__":
    # 1. KONDISI SAAT DATA SEDANG LOADING
    print("[LOG] Mengambil data dari server...")
    render_dashboard(app_state["items"], app_state["is_loading"])
    
    print("\n" + "="*30 + "\n") # Pembatas biar rapi
    
    # Simulasi jeda waktu proses loading backend
    time.sleep(1) 
    
    # 2. KONDISI SAAT DATA SUDAH TAMPIL
    mock_data = [{"id": 101, "name": "Produk A"}, {"id": 102, "name": "Produk B"}]
    print("[LOG] Data berhasil diterima!")
    update_state(mock_data)
    
    render_dashboard(app_state["items"], app_state["is_loading"])