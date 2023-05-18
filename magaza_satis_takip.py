class Magaza:
    def __init__(self,magaza_adi=" ",satici_adi=" ",satici_cinsi=" ",satis_miktari=" "):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__satis_miktari = satis_miktari

    def get_magaza_adi(self):
        return self.__magaza_adi

    def get_satici_adi(self):
        return self.__satici_adi

    def get_satici_cinsi(self):
        return self.__satici_cinsi

    def get_satis_miktari(self):
        return self.__satis_miktari

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi

    def set_satis_miktari(self, satis_miktari):
        self.__satis_miktari = satis_miktari

    def magaza_satis_tutar(self, satislar):
        while True:

            magaza = input("satış değerlerini görmek istediğiniz magazanın adi(çıkmak için q basın):")
            if magaza == "q":
                break
            for magaza_adi_bul in satislar:
                if magaza_adi_bul == magaza:
                    kontrol = input(
                        "mağazanın toplam satış değerini görmek için 1'e mağazada satış yapan bir satıcının satış değerini görmek için 2'ye basın(çıkmak için q basın):")

                    if kontrol == "q":
                        break

                    elif kontrol == "1":
                        a = 0
                        for tutar in satislar[magaza]:
                            a += sum(tutar["satis tutarı"])
                        print("satış miktarı:", a)

                    elif kontrol == "2":
                        a = 0
                        satici = input("satici adi:")
                        satici_cinsi = input("saticinin cinsi:")
                        for satici_kontrol in satislar[magaza]:
                            if satici == satici_kontrol["satici adi"] and satici_cinsi == satici_kontrol[
                                "satici cinsi"]:
                                a += sum(satici_kontrol["satis tutarı"])
                        print("satış miktarı:", a)

    def __str__(self, satislar):
        magaza_tutar = {}
        satici_tutar = {}

        for magaza, satislar_magaza in satislar.items():
            magaza_tutar[magaza] = 0
            for satis in satislar_magaza:
                satici = (satis["satici adi"], satis["satici cinsi"])
                satis_tutari = sum(satis["satis tutarı"])
                if satici in satici_tutar:
                    satici_tutar[satici] += satis_tutari
                else:
                    satici_tutar[satici] = satis_tutari
                magaza_tutar[magaza] += satis_tutari

        c = []
        for magaza, magaza_tutari in magaza_tutar.items():
            c.append([magaza, magaza_tutari])
        for satici, satici_tutari in satici_tutar.items():
            c.append([satici, satici_tutari])

        return c









