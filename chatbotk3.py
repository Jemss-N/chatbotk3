import re

# =========================
# KNOWLEDGE BASE K3
# =========================
K3_DATA = {
    "listrik": {
        "bahaya": "sengatan listrik, korsleting, dan arc flash",
        "apd": "sarung tangan isolasi, sepatu safety, dan helm keselamatan",
        "risiko": "tinggi jika tanpa APD dan SOP"
    },
    "kimia": {
        "bahaya": "keracunan, iritasi kulit, dan kebakaran",
        "apd": "masker, sarung tangan, dan kacamata pelindung",
        "risiko": "sedang hingga tinggi tergantung jenis bahan"
    },
    "ergonomi": {
        "bahaya": "nyeri otot, kelelahan, dan cedera tulang belakang",
        "apd": "kursi ergonomis dan pengaturan posisi kerja",
        "risiko": "sedang jika postur kerja salah"
    },
    "mesin": {
        "bahaya": "terjepit, terpotong, atau tersangkut mesin",
        "apd": "helm, sarung tangan, dan sepatu safety",
        "risiko": "tinggi jika mesin tanpa pelindung"
    }
}

# =========================
# DETEKSI TOPIK
# =========================
def deteksi_topik(teks):
    for topik in K3_DATA:
        if re.search(topik, teks):
            return topik
    return None

# =========================
# CHATBOT RESPONSE
# =========================
def chatbot_k3(user_input):
    teks = user_input.lower()
    topik = deteksi_topik(teks)

    if not topik:
        return (
            "Saya belum memahami konteks bahaya yang dimaksud.\n"
            "Coba jelaskan apakah terkait listrik, kimia, ergonomi, atau mesin."
        )

    data = K3_DATA[topik]

    # Deteksi jenis pertanyaan
    if "bahaya" in teks or "risiko" in teks or "berbahaya" in teks:
        return (
            f"Dalam pekerjaan terkait {topik}, potensi bahayanya adalah "
            f"{data['bahaya']}.\n"
            f"Tingkat risikonya tergolong {data['risiko']}.\n"
            f"Untuk pencegahan, gunakan APD seperti {data['apd']}."
        )

    if "apd" in teks or "pelindung" in teks:
        return (
            f"Untuk pekerjaan {topik}, APD yang disarankan meliputi "
            f"{data['apd']}."
        )

    if "jika" in teks or "kondisi" in teks:
        return (
            f"Berdasarkan kondisi kerja yang kamu sebutkan pada pekerjaan {topik}, "
            f"potensi bahaya adalah {data['bahaya']}.\n"
            f"Risiko dapat diminimalkan dengan penggunaan APD dan mengikuti SOP."
        )

    return (
        f"Pekerjaan di bidang {topik} memiliki potensi bahaya berupa "
        f"{data['bahaya']}.\n"
        f"Pastikan selalu menerapkan K3 sebelum bekerja."
    )

# =========================
# PROGRAM UTAMA
# =========================
def main():
    print("🤖 Chatbot Asisten K3")
    print("Ketik 'keluar' untuk mengakhiri percakapan.\n")

    while True:
        user_input = input("Kamu: ")
        if user_input.lower() == "keluar":
            print("Bot: Tetap utamakan keselamatan kerja 👍")
            break

        response = chatbot_k3(user_input)
        print("Bot:", response)
        print()

if __name__ == "__main__":
    main()
