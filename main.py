import pandas as pd
from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

    
hast_soz = { #hastane sözlüğü tanımlanıyor 
"Personel Numarası": ["1", "2", "1", "2", "3", "1", "2", "3", "", "", ""],
"Hasta Numarası": ["", "", "", "", "", "", "", "", "1", "2", "3"],
"İsim": ["Seray", "Yağmur", "Damla", "Gökmen", "Emin", "Numan", "Mert", "Ada", "Renas", "Batuhan", "Seçil"],
"Soyisim":["Fırıncıoğulları","Fırıncıoğulları","Fırıncıoğulları","Gezgin","Fırıncıoğulları","Nevşioğulları","Özdemir","Ay","Taş","Parıltı","Taş" ],
"Departman": ["Güvenlik", "Temizlik Görevlisi", "Doktor", "Doktor", "Doktor", "Hemşire", "Hemşire", "Hemşire", "", "", ""],
"Maaş": [4000, 4000, 8000, 4000, 7500, 6000, 5000, 7500, "", "", ""],
"Uzmanlık": ["", "", "İç Hastalıkları", "Estetik Ve Plastik Cerrahisi", "Kardiyoloji", "", "", "", "", "", ""],
"Deneyim Yılı": ["", "", 3, 15, 2, "", "", "", "", "", ""],
"Hastane": ["", "", "İzmir Şehir Hastanesi", "Özel Ekin Hastanesi", "Defne Devlet Hastanesi", "Hatay Devlet Hastanesi", "İzmir Bakırçay Hastanesi", "Marmaris Devlet Hastanesi", "", "", ""],
"Güncel Maaş": ["", "", "", 84000, "", "", 9800, 25000, "", "", ""],
"Sertifika": ["", "", "", "", "", "Eğitim", "Ameliyat", "Psikiyatri", "", "", ""],
"Çalışma Saati": ["", "", "", "", "", 33, 24, 35, "", "", ""],
"Doğum Tarihi": ["", "", "", "", "", "", "", "", "27/08/1989", "13/05/2004", "11/07/2005"],
"Hastalık": ["", "", "", "", "", "", "", "", "Çölyak", "Herpes Enfeksiyonu", "HIV"],
"Tedavi": ["", "", "", "", "", "", "", "", "Yok", "İlaç", "İlaç"],
"Tedavi Süresi": ["", "", "", "", "", "", "", "", "Ömür Boyu", "10 Gün", "Ömür Boyu"]
}

df = pd.DataFrame(hast_soz) #hastane sözlüğünün dataframei oluşturuluyor
df = df.replace("", "0").fillna(0) #sütunda olan verinin değeri yoksa 0 yazdırılıyor

personeller = [] #personel ve hastaların bilgilerini tutan listeler atanıyor
hastalar = []

for i, satir in df.iterrows(): #döngü ile df verilerini satır satır gezer

    if satir["Personel Numarası"] != "0": #personele ait bilgileri değişkenlere atar
        isim = satir["İsim"]
        soyisim = satir["Soyisim"]

        if satir["Departman"] == "Doktor": #gezilen satırda departman değişkeni görürse doktorun bilgilerini doktor listesine atar
            doktor = Doktor(satir["Personel Numarası"], isim, soyisim, satir["Departman"], int(satir["Maaş"]), satir["Uzmanlık"], int(satir["Deneyim Yılı"]), satir["Hastane"])
            personeller.append(doktor)

        elif satir["Departman"] == "Hemşire": #doktor personeliyle aynı işlevi gören kod bloğu
            hemsire = Hemsire(satir["Personel Numarası"], isim, soyisim, satir["Departman"], int(satir["Maaş"]), int(satir["Çalışma Saati"]), satir["Sertifika"], satir["Hastane"])
            personeller.append(hemsire)

        else:
            personel = Personel(satir["Personel Numarası"], isim, soyisim, satir["Departman"], int(satir["Maaş"])) #departman satırında doktor veya hemşire yoksa çalıaşcak kod bloğu
            personeller.append(personel)

    if satir["Hasta Numarası"] != "0": #hasta bilgilerini değişkene atar
        isim= satir["İsim"]
        soyisim = satir["Soyisim"]
        hasta = Hasta(satir["Hasta Numarası"], isim, soyisim, satir["Doğum Tarihi"], satir["Hastalık"], satir["Tedavi"])
        hastalar.append(hasta) #hasta bilgileri hastalar listesine ekleniyor


yeni_soz = {
    "Personel Numarası": [p.get_personel_no() for p in personeller] + ["0"] * len(hastalar), #personeller listesinden personel numaraları çağırılıp numaralar yazılıyor hastalar listesinde personel numarası olmadığı için 0 yazılıyor
    "Hasta Numarası": ["0"] * len(personeller) + [h.get_hasta_no() for h in hastalar], 
    "İsim": [f"{p.get_ad()}" for p in personeller] + [f"{h.get_ad()} " for h in hastalar],
    "Soyisim": [p.get_soyad() for p in personeller] + [h.get_soyad() for h in hastalar],
    "Departman": [p.get_departman() for p in personeller] + ["0"] * len(hastalar),
    "Maaş": [p.get_maas() for p in personeller] + ["0"] * len(hastalar),
    "Uzmanlık": [p.get_uzmanlik() if isinstance(p, Doktor) else "0" for p in personeller] + ["0"] * len(hastalar),
    "Deneyim Yılı": [p.get_deneyim_yili() if isinstance(p, Doktor) else "0" for p in personeller] + ["0"] * len(hastalar),
    "Hastane": [p.get_hastane() if isinstance(p, (Doktor, Hemsire)) else "0" for p in personeller] + ["0"] * len(hastalar),
    "Güncel Maaş": [row["Güncel Maaş"] for index, row in df.iterrows() if row["Personel Numarası"] != "0"] + ["0"] * len(hastalar),
    "Sertifika": [p.get_sertifika() if isinstance(p, Hemsire) else "0" for p in personeller] + ["0"] * len(hastalar),
    "Çalışma Saati": [p.get_calisma_saati() if isinstance(p, Hemsire) else "0" for p in personeller] + ["0"] * len(hastalar),
    "Doğum Tarihi": ["0"] * len(personeller) + [h.get_dogum_tarihi() for h in hastalar],
    "Hastalık": ["0"] * len(personeller) + [h.get_hastalik() for h in hastalar],
    "Tedavi": ["0"] * len(personeller) + [h.get_tedavi() for h in hastalar],
    "Tedavi Süresi": ["0"] * len(personeller) + [row["Tedavi Süresi"] for index, row in df.iterrows() if row["Hasta Numarası"] != "0"]
}

print(df)

df["Doğum Tarihi"] = pd.to_datetime(df["Doğum Tarihi"], format='%d/%m/%Y', errors='coerce') #hstaların doğum tarihleri gün ay yıl formatına dönüştürülüyor
_90_sonrasi = df[(df["Doğum Tarihi"] >= "01-01-1990") & (df["Hasta Numarası"] != 0)] #hastanın doğum tarifi 1990dan büyükse ekrana yazdırılıyor
print("Doğum tarihi 1990 ve sonrası olan hastalar:")
print(_90_sonrasi)
print("\n")

doktorlar = df[df["Departman"] == "Doktor"] #doktor departmanındaki bilgilere bakılır
uzmanlik_grup = doktorlar.groupby("Uzmanlık").size() #uzmanlıklarına göre doktorlar gruplandırılıp boyutu hesaplanıyor
print("Uzmanlık alanlarına göre doktor sayısı:")
print(uzmanlik_grup)
print("\n")

df["Deneyim Yılı"] = df["Deneyim Yılı"].replace("", 0).astype(int) #deneyim yılında boş değerlere 0 verir ve değerleri integera dönüştürür
deneyimli_doktorlar = doktorlar[doktorlar["Deneyim Yılı"] > 5] #5 yıldan fazla deneyimi olanlar doktorlar listesine atanır
print("5 yıldan fazla deneyime sahip doktor sayısı:", len(deneyimli_doktorlar)) #listenin uzunluğu ekrana verilir
print("\n")

df["Maaş"] = df["Maaş"].replace("", 0).astype(int) #maaş sütunundaki boş değerlere 0 verir ve değerleri integera dönüştürür
maasi_yuksek_personel = df[df["Maaş"] > 7000] #7000den fazla maaşı alan personeller listeye atanır ve ekrana yazdırılır
print("Maaşı 7000 TL üzerinde olan personeller:")
print(maasi_yuksek_personel)
print("\n")


sorted_df = df.sort_values("İsim") #sorted komutu ile isimler alfabetik olarak sıralanır ve ekrana yazdırılır
print("Alfabetik olarak sıralanmış DataFrame:")
print(sorted_df)
print("\n")

yeni_df = df[["İsim", "Soyisim","Departman", "Maaş", "Uzmanlık", "Deneyim Yılı", "Hastalık", "Tedavi"]] #belirli değişkenlerden oluşan yeni data ekrana verilir
print("Yeni DataFrame:")
print(yeni_df)

       
