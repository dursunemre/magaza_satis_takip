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

def main():
    satislar = {}
    while True:
        satis = Magaza(magaza_adi=" ",satici_adi=" ",satici_cinsi=" ",satis_miktari=" ")

        satis.set_magaza_adi(input("satis yapilan magazanin adi:"))

        satis.set_satici_adi(input("satis yapilan saticinin adi:"))

        satis.set_satici_cinsi(input("satis yapilan saticinin cinsi:"))

        satis.set_satis_miktari(int(input("satis miktari:")))

        magaza = satis.get_magaza_adi()
        ad = satis.get_satici_adi()
        cins = satis.get_satici_cinsi()
        tutar = satis.get_satis_miktari()

        if magaza in satislar:
            for kayit in satislar[magaza]:
                if kayit['satici adi'] == ad and kayit['satici cinsi'] == cins:
                    kayit['satis tutarı'].append(tutar)
                    break
                else:
                    satislar[magaza].append({'satici adi': ad, 'satici cinsi': cins, 'satis tutarı': [tutar]})
        else:
            satislar[magaza] = [{'satici adi': ad, 'satici cinsi': cins, 'satis tutarı': [tutar]}]

        a = input("çıkmak için k devam için l basın:")
        if a not in ["k", "l"]:
            a = input("lütfen geçerli bir deger girin:")
        if a == "k":
            break

        while True:

            a = input("belirli bir mağaza/satıcı satış tutarı değeri için k'ye , toplam satış tutarları için l'ye, çıkmak için q basın")
            if a == "k":
                satis.magaza_satis_tutar(satislar)
            elif a == "l":
                print("magaza adı-çalışan bilgisi , satış tutarı\n",'\n'.join([' '.join([str(item) for item in row]) for row in satis.__str__(satislar)]))
            elif a == "q":
                break









