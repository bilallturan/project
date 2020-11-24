# BilalTuran 20191132038

sifreleme = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm9876543210')

while True:
    a = input("Çıkmak İçin 0'a basınız, veya devam ediniz:")
    if a == "0":
        print("program sonlandırılıyor")
        break

    def rot13(yazı):
        return yazı.translate(rot13trans)
    def main():
        veri = input("Değer giriniz:")

        print(veri)
        print(rot13(veri))


    if __name__ == "__main__":
        main()


