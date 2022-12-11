import streamlit as st
from streamlit_option_menu import option_menu

# navigasi sidebar
with st.sidebar :
    selected = option_menu( 'Perhitungan Analisis Proksimat',
    ['Menghitung Kadar Air',
    'Menghitung Kadar Abu',
    'Menghitung Kadar Protein',
    'Menghitung Kadar Karbohidrat',
    'Menghitung Kadar Lemak'],
    default_index=0)


if (selected == 'Menghitung Kadar Air'):
    st.title('''
    Menghitung Kadar Air dengan Metode Thermogravimetri
    Perhitungan Kadar Air Wet Basis
    ''')

    Wo = st.number_input ('Masukkan Berat Botol Kosong', format="%0.4f")
    Wa = st.number_input ('Masukkan Berat Sampel Sebelum Pengovenan', format="%0.4f")
    Wb = st.number_input ('Masukkan Berat Botol yang Berisi Sampel Setelah Pengovenan', format="%0.4f")
    hitung = st.button ('Hitung Kadar Air Wet Basis')

    if hitung:
        hitung = ((Wa-(Wb-Wo))/Wa)*100
        st.success(f'Kadar Air Wet Basis adalah {hitung} %')

if (selected == 'Menghitung Kadar Abu'):
    st.title('''
    Menghitung Kadar Abu dengan Metode Gravimetri
    Perhitungan Kadar Abu Wet Basis
    ''')

    Wo = st.number_input ('Masukkan Berat Krus Kosong', format="%0.4f")
    Wa = st.number_input ('Masukkan Berat Sampel Sebelum Pengabuan', format="%0.4f")
    Wb = st.number_input ('Masukkan Berat Krus yang Berisi Sampel Setelah Pengabuan', format="%0.4f")
    hitung = st.button ('Hitung Kadar Abu Wet Basis')

    if hitung:
        hitung = ((Wb-Wo)/Wa)*100
        st.success(f'Kadar Air Wet Basis adalah {hitung} %')

if (selected == 'Menghitung Kadar Protein'):
    st.title('''
    Menghitung Kadar Protein dengan Metode Mikrokjeldahl
    Perhitungan Kadar Protein Kasar
    ''')

    Titrasi = st.number_input ('Masukkan titrat yang digunakan pada titrasi sampel (mL)', format="%0.2f")
    Blanko = st.number_input ('Masukkan titrat yang digunakan pada titrasi blanko (mL)', format="%0.2f")
    Normalitas_titrat = st.number_input ('Masukkan normalitas larutan baku yang digunakan (N)', format="%0.4f")
    Faktor_pengenceran = st.number_input('Masukkan faktor pengenceran', format="%0.2f")
    Faktor_konversi = st.number_input('Masukkan faktor konversi protein', format="%0.2f")
    Berat_bahan = st.number_input ('Masukkan berat sampel yang digunakan (gram)', format="%0.4f")
    konversi_protein = st.button ('Hitung Kadar Protein Kasar')

    if konversi_protein:
        Nitrogen = (((Titrasi-Blanko)*Normalitas_titrat*14.008*Faktor_pengenceran)/Berat_bahan*1000)*100
        konversi_protein = Nitrogen*Faktor_konversi
        st.success(f'Kadar kadar protein kasar pada sampel adalah {konversi_protein} %')

if (selected == 'Menghitung Kadar Karbohidrat'):
    st.title('''
    Menghitung Kadar Karbohidrat dengan Metode Luff Schoorl
    Perhitungan Kadar Karbohidrat Wet Basis
    ''')
    col1, col2, col3 = st.columns(3)
    with col1:
        Titrasi = st.number_input ('Masukkan titrat yang digunakan pada titrasi sampel (mL)', format="%0.2f")
    with col2:
        Blanko = st.number_input ('Masukkan titrat yang digunakan pada titrasi blanko (mL)', format="%0.2f")
    with col3:
        Normalitas = st.number_input ('Masukkan normalitas natrium tiosulfat yang digunakan pada titrasi (N)', format="%0.4f")
    konversi_titran = st.button ('Hitung Volume Tio 0,1 N')

    if konversi_titran:
       Titran = (Blanko-Titrasi)*(Normalitas/0.1)
       st.success(f'Volume Tio 0,1 N adalah {Titran} %')

    col1, col2, col3 = st.columns(3)
    with col1:
        tio_satu = st.number_input ('Masukkan rentang atas volume natrium tiosulfat 0,1 N yang ada pada tabel konversi Luff Schoorl', format="%0.4f")
    with col2:
        mg_gula_satu = st.number_input ('Masukkan rentang atas berat gula yang ada pada tabel konversi Luff Schoorl (mg)', format="%0.4f")
    with col3:
        tio_dua = st.number_input ('Masukkan rentang bawah volume natrium tiosulfat 0,1 N yang ada pada tabel konversi Luff Schoorl', format="%0.4f")
    with col1:
        mg_gula_dua = st.number_input ('Masukkan rentang bawah berat gula yang ada pada tabel konversi Luff Schoorl (mg)', format="%0.4f")
    with col2:
        mg_bahan = st.number_input ('Masukkan barat bahan yang digunakan (mg)', format="%0.4f")
    with col3:
        Faktor_pengenceran = st.number_input('Masukkan faktor pengenceran', format="%0.2f")
    konversi_karbohidrat = st.button ('Hitung Kadar Karbohidrat')

    if konversi_karbohidrat:
        Titran = (Blanko-Titrasi)*(Normalitas/0.1)
        mg_gula_Titran = mg_gula_satu + ((mg_gula_dua-mg_gula_satu)/(tio_dua-tio_satu)) * (Titran-tio_satu)
        Karbohidrat = ((mg_gula_Titran/mg_bahan)*0.9*Faktor_pengenceran)*100
        st.success(f'Kadar kadar protein kasar pada sampel adalah {Karbohidrat} %')

if (selected == 'Menghitung Kadar Lemak'):
    st.title('''
    Menghitung Kadar Lemak dengan Metode Soxhlet
    Perhitungan Kadar Lemak Wet Basis
    ''')

    A = st.number_input ('Masukkan berat labu kosong', format="%0.4f")
    B = st.number_input ('Masukkan berat labu yang berisi sisa pelarut yang mengandung lipid', format="%0.4f")
    Berat_sampel = st.number_input ('Masukkan Berat Sampel', format="%0.4f")
    hitung = st.button ('Hitung Kadar Lemak Wet Basis')

    if hitung:
        hitung = ((B-A)/Berat_sampel)*100
        st.success(f'Kadar Lemak Wet Basis adalah {hitung} %')