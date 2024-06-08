class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi


    def set_hasta_no(self, hasta_no):
        self.__hasta_no = hasta_no
    def get_hasta_no(self):
        return self.__hasta_no
    

    def set_ad(self, ad):
        self.__ad = ad
    def get_ad(self):
        return self.__ad
    
    
    def set_soyad(self, soyad):
        self.__soyad = soyad
    def get_soyad(self):
        return self.__soyad


    def set_dogum_tarihi(self, dogum_tarihi):
        self.__dogum_tarihi = dogum_tarihi
    def get_dogum_tarihi(self):
        return self.__dogum_tarihi


    def set_hastalik(self, hastalik):
        self.__hastalik = hastalik
    def get_hastalik(self):
        return self.__hastalik


    def set_tedavi(self, tedavi):
        self.__tedavi = tedavi
    def get_tedavi(self):
        return self.__tedavi
    


    def tedavi_suresi_hesapla(self):
       
        tedavi_sureleri = {
            'HIV':'Ömür boyu',
            'ÇÖLYAK':'Ömür boyu',
            'REFLÜ':'15 yıl',
            'HERPES ENFEKSİYONU':'10 gün',
            'GRİBAL ENFEKSİYON': '7 gün',
            'AKCİĞER ENFEKSİYONU':'10 gün',
            'ZATÜRRE': '14 gün',
            'KIRIK': '30 gün',
            'COVID-19': '15 gün',
            'KALP AMELİYATI': '21 gün'
            
        }

        if self.__hastalik in tedavi_sureleri:
            return tedavi_sureleri[self.__hastalik]
        else:
            return "Bilinmeyen hastalık. Tedavi süresi hesaplanamıyor."

    def __str__(self):
        return f"Hasta No: {self.__hasta_no}, Ad: {self.__ad}, Soyad: {self.__soyad}, Doğum Tarihi: {self.__dogum_tarihi}, Hastalık: {self.__hastalik}, Tedavi: {self.__tedavi}"
    
