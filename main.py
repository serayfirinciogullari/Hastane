import sys
import pandas as pd
from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

tercih=input("1-)Kayıtlı verileri göster\n2-)Veri gir")

if tercih=="1":
    
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

       
elif tercih=="2": #kullanıcı veri girişi yapmak isterse  

    while True:
        print("\n")
        print("1-)Personel\n2-)Doktor\n3-)Hemşire\n4-)Hasta\n")
        secim=input("Bilgilerini gireceğiniz kişinin bulunduğu kategoriyi seçiniz (Giriş yapmak istemiyorsanız 0'a basınız..!)")

        if secim=="1": #personel girişi yapılacaksa

            for i in range(50):
                isim =input(f"{i+1}. personelin ismini giriniz:").upper() #bilgiler büyük küçük harfe duyarsızlaştırılıyor ve gerekli bilgiler alınıyor
                soyisim=input(f"{i+1}. personelin soyismini giriniz:").upper()
                departman=input(f"{i+1}. personelin departmanını giriniz:").upper()
                maas=input(f"{i+1}. personelin maaşını giriniz:").upper()

                personel=Personel(i+1,isim,soyisim,departman,maas) #personel sınıfından bir nesne oluşturuluyor

                with open ("hastaneBilgileri.txt","a+",encoding="utf-8") as dosya:  
                    dosya.write(f"personel={i+1},{isim},{soyisim},{departman},{maas}") #nesne dosyaya yazdırılıyor
                    dosya.write("\n")  
                    
    
                sor = input("Personel girişi yapmaya devam etmek istiyor musunuz? (E(evet) H(hayır))\n") #girişe devam edip etmeme tercihi sunuluyor

                if sor.lower() == "e":
                    continue
                elif sor.lower() == "h":
                    break
                else:
                    print("Hatalı giriş yaptınız lütfen tekrar tuşa basınız. (E(evet) H(hayır) A(ana menü))")

            if sor.lower() == "h": 
                continue
                
            
        elif secim=="2": #doktor girişi yapılacaksa
            for i in range(50):
                
                isim =input(f"{i+1}. doktorun ismini giriniz:").upper() #bilgiler büyük küçük harfe duyarsızlaştırılıyopr
                soyisim=input(f"{i+1}. doktorun soyismini giriniz:").upper()
                departman=input(f"{i+1}. doktorun departmanını giriniz:").upper()
                maas=int(input(f"{i+1}. doktorun maaşını giriniz:"))
                uzmanlık=input(f"{i+1}. doktorun uzmanlık alanını giriniz:")
                deneyim_yılı=int(input(f"{i+1}. doktorun deneyim yılını giriniz:"))
                hastane=input(f"{i+1}. doktorun görev aldığını hastaneyi giriniz:").upper()

                doktor=Doktor(i+1,isim,soyisim,departman,maas,uzmanlık,deneyim_yılı,hastane) #personel sınıfından kalıtılan doktor sınıfının nesnesi üretiliyor
 
                
                with open ("hastaneBilgileri.txt","a+",encoding="utf-8") as dosya: #türkçe karakterlere duyarlı şekilde dosyaya yazdıırlıyor
                    dosya.write(f"doktor={i+1},{isim},{soyisim},{departman},{maas},{uzmanlık},{deneyim_yılı},{hastane},")
                    dosya.write("\n")

                secim2=input("Doktorun maaşını arttırmak ister misiniz?(Evet(E veya h) Hayır(H veya h))") #doktorun maaşını artırma soruluyor

                if secim2=="E" or "e":
                    yeni_maas=doktor.maas_arttir() #maaş artırılacasksa maas_artir fonskiyonu çağırılıyor
                    
                    with open ("hastaneBilgileri.txt","a+",encoding="utf-8") as dosya:   #yeni maaş dosyaya yazdırılılıyor
                        dosya.write(f"YENİ MAAŞ= {yeni_maas}")
                        dosya.write("\n")
                
                elif secim2=="H" or "h":
                    print("Bilgiler dosyaya yazılıyor...")
                
                else:
                    print("Hatalı tuşa bastınız...")
    
                print("Bilgiler dosyaya başarıyla yazıldı...")

                sor = input("Doktor girişi yapmaya devam etmek istiyor musunuz? (E(evet) H(hayır))\n")

                if sor.lower() == "e":
                    continue
                elif sor.lower() == "h":
                    break
                else:
                    print("Hatalı giriş yaptınız lütfen tekrar tuşa basınız. (E(evet) H(hayır) A(ana menü))")

            if sor.lower() == "h":
                continue

        elif secim=="3": #hemşire girişi yapılacaksa
            for i in range(50):
                
                isim =input(f"{i+1}. hemşirenin ismini giriniz:").upper() #veriler duyarsızlaştırılıyor
                soyisim=input(f"{i+1}. hemşirenin soyismini giriniz:").upper()
                departman=input(f"{i+1}. hemşirenin departmanını giriniz:").upper()
                maas=int(input(f"{i+1}. hemşirenin maaşını giriniz:"))
                çalışma_saati=int(input(f"{i+1}. hemşirenin haftalık çalışma saatini giriniz:"))
                sertifika=input(f"{i+1}. hemşirenin sertifikasını giriniz:").upper()
                hastane=input(f"{i+1}. hemşirenin görev aldığını hastaneyi giriniz:").upper()

                hemşire=Hemsire(i+1,isim,soyisim,departman,maas,çalışma_saati,sertifika,hastane)

                with open ("hastaneBilgileri.txt","a+",encoding="utf-8") as dosya:

                    dosya.write(f"hemşire={i+1},{isim},{soyisim},{departman},{maas},{çalışma_saati},{sertifika},{hastane},") #bilgiler yazdırılıyor
                    dosya.write("\n")
                
                secim2=input("Hemşirenin maaşını arttırmak ister misiniz?(Evet(E veya h) Hayır(H veya h))")
 
                if secim2=="E" or "e": 

                    yeni_maas=hemşire.maas_arttir() #maaş artırma fonksiyonu çağırılıp dosyaya yazdırılıyor
                    with open ("hastaneBilgileri.txt","a+",encoding="utf-8") as dosya:  
                        dosya.write(f"YENİ MAAŞ= {yeni_maas}")
                        dosya.write("\n")
                
                elif secim2=="H" or "h":
                    print("Bilgiler dosyaya yazılıyor...")
                
                else:
                    print("Hatalı tuşa bastınız...")
    
                print("Bilgiler dosyaya başarıyla yazıldı...")

                sor = input("Hemşire girişi yapmaya devam etmek istiyor musunuz? (E(evet) H(hayır))\n")

                if sor.lower() == "e":
                    continue
                elif sor.lower() == "h":
                    break
                
                else:
                    print("Hatalı giriş yaptınız lütfen tekrar tuşa basınız. (E(evet) H(hayır) A(ana menü))")

            if sor.lower() == "h":
                continue


        elif secim=="4": #hasta giirşi olacaska
                for i in range(50):
                    
                    isim =input(f"{i+1}. hastanın ismini giriniz:").upper()
                    soyisim=input(f"{i+1}. hastanın soyismini giriniz:").upper()
                    doğum_tarihi=input(f"{i+1}.hastanın doğum tarihini giriniz:").upper()
                    print("-HIV\n-ÇÖLYAK-REFLÜ\n-KIRK-KALP AMELİYATI\n-GRİBAL ENFEKSİYON\n-HERPES ENFEKSİYONU\n-AKCİĞER ENFEKSİYONU\n-ZATÜRRE\n-COVID-19").upper()
                    hastalık=input(f"{i+1}. hastanın hastalığını giriniz:").upper()
                    tedavi=input(f"{i+1}. hastanın tedavisini giriniz:").upper()

                    hasta=Hasta(i+1,isim,soyisim,doğum_tarihi,hastalık,tedavi)
                    tedav_suresi=hasta.tedavi_suresi_hesapla() #tedavi süresini hesaplayan fonksiyon çağırılıypr

                    with open ("hastaneBilgileri.txt","a+",encoding="utf-8") as dosya:    
                        dosya.write(f"hasta={i+1},{isim},{soyisim},{doğum_tarihi},{hastalık},{tedavi},{tedav_suresi}") #hasta bilgileri dosyaya yazdırılıyor
                        dosya.write("\n")

                    sor = input("Hasta girişi yapmaya devam etmek istiyor musunuz? (E(evet) H(hayır) M(ana menü))\n")

                    if sor.lower() == "e":
                        continue
                    elif sor.lower() == "h":
                        break
                    elif sor.lower() == "m":
                        break
                    else:
                        print("Hatalı giriş yaptınız lütfen tekrar tuşa basınız. (E(evet) H(hayır) M(ana menü))")

                if sor.lower() == "m":
                    continue

        elif secim==0:
            print("Programdan çıkış yapılıyor...")
            break

        else:
            print("Yanlış tuşa bastınız...")



