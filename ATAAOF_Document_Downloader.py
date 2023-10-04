import requests
import os

#OYS [ Öğrenme Yönetim Sistemi ] - Ders Materyalleri TOPLU İndirme#
#Coded by LLCoder -- 04.10.2023 - 07:30#

# Ders adları ve ders ID'leri
dersler = {
    'ATAAOF_inkilapTarihi1': 14170,
    'ATAAOF_CalismaEtik1': 43755,
    'ATAAOF_GorselPrograml1': 46104,
    'ATAAOF_iletisimGiris1': 34080,
    'ATAAOF_internetProg1': 46118,
    'ATAAOF_NesneTabanProg1': 46122
    # Diğer dersler buraya eklenebilir   
}

# Ünite aralığı
baslangic_unite = 1
bitis_unite = 14

# PDF'leri indireceğiniz ana klasörü oluşturun
ana_klasor = 'pdfDokumanlar'
if not os.path.exists(ana_klasor):
    os.makedirs(ana_klasor)

# Her ders için işlem yapın
for ders_adi, ders_id in dersler.items():
    # Ders için ayrı bir klasör oluşturun
    ders_klasoru = os.path.join(ana_klasor, ders_adi)
    if not os.path.exists(ders_klasoru):
        os.makedirs(ders_klasoru)
    
    # Üniteleri indirme işlemi
    for unite in range(baslangic_unite, bitis_unite + 1):
        pdf_url = f'https://oys.ataaof.edu.tr/file/{ders_id}-{unite}.pdf'
        response = requests.get(pdf_url)
        
        if response.status_code == 200:
            with open(os.path.join(ders_klasoru, f'{ders_id}-{unite}.pdf'), 'wb') as f:
                f.write(response.content)
            print(f'{ders_adi} - {ders_id}-{unite}.pdf başarıyla indirildi.')
        else:
            print(f'{ders_adi} - {ders_id}-{unite}.pdf indirilemedi. Durum Kodu: {response.status_code}')
    
    # Özet PDF dosyasını indirme işlemi
    pdf_ozet_url = f'https://oys.ataaof.edu.tr/kisaozetpdf/{ders_id}-kisaozet.pdf'
    response = requests.get(pdf_ozet_url)
    
    if response.status_code == 200:
        with open(os.path.join(ders_klasoru, f'{ders_id}-kisaozet.pdf'), 'wb') as f:
            f.write(response.content)
        print(f'{ders_adi} - {ders_id}-kisaozet.pdf başarıyla indirildi.')
    else:
        print(f'{ders_adi} - {ders_id}-kisaozet.pdf indirilemedi. Durum Kodu: {response.status_code}')
