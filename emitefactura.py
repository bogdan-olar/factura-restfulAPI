
class Factura:

    def __init__(self, serie, numar, data, client_id, delegat_id ) -> None:
            self.serie = serie
            self.numar = numar
            self.data = data
            self.client_id = client_id
            self.delegat_id = delegat_id
        
class BunuriServicii:

    def __init__(self, denumire, cantitate, fel, pret_bucata, cota_tva, numar_factura ) -> None:
        self.denumire = denumire
        self.cantitate = cantitate
        self.fel = fel
        self.pret_bucata = pret_bucata
        self.cota_tva = cota_tva
        self.numar_factura = numar_factura
