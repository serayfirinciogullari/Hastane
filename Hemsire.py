from Personel import Personel

class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane


    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati
    def get_calisma_saati(self):
        return self.__calisma_saati
    

    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika
    def get_sertifika(self):
        return self.__sertifika
    

    def set_hastane(self, hastane):
        self.__hastane = hastane
    def get_hastane(self):
        return self.__hastane


    def maas_arttir(self):
        if 0 < self.__calisma_saati <= 20:
            self._Personel__maas = self._Personel__maas
        elif 20 < self.__calisma_saati <= 30:
            self._Personel__maas = self._Personel__maas + self.__calisma_saati * 200
        elif self.__calisma_saati > 30:
            self._Personel__maas = self._Personel__maas + self.__calisma_saati * 500
        return self._Personel__maas

    def __str__(self):
        return f"Hemşire No: {self.get_personel_no()}, Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Departman: {self.get_departman()}, Maaş: {self.get_maas()}, Çalışma Saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastane: {self.__hastane}"

   