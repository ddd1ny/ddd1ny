import sys

class poka:
    def __init__(self):
        super().__init__()
        self.poka = ("Досвиданиияяя ! Удачного вам дняя !")
class balans:
    def __init__(self):
        super().__init__()

        self.balanz = 25000

class vashbalans:
    def __init__(self):
        super().__init__()

        self.vash = "С вашего баланса"
class Берете:
    def __init__(self):
        super().__init__()
        self.берет = "Мы вас заинтересовали ? Будете что то брать ?"

class Money:
    def __init__(self):
        super().__init__()
        self.money = "$"

class Pc:
    def __init__(self):
        super().__init__()
        self.memory = 64
        self.vidkarta = 3080
        self.procesor = "i7"


class TV:
    def __init__(self):
        super().__init__()
        self.TV = "4k ,"
        self.tv = "3480x2160"
class Noutbuk:
    def __init__(self):
        super().__init__()
        self.Viduxa= "geforce gtx 1660 ti"
        self.Procisor= "amd ryzen 7"
        self.Ramka= "16 gb"
        self.tb = "1tb"
        self.ekran =  "1920x1080 ," "Full HD"
class Display:
    def __init__(self):
        super().__init__()
        self.resolution = "4k " " 3480x2160 "

class Mobila:
    def __init__(self):
        super().__init__()
        self.RAM = 8
        self.proc = "Qualcomm Snapdragon 8 Gen 3"
        self.Xranilishe = "1 TB"

class Print(Display,Pc,Mobila,Noutbuk,Money,TV,Берете,balans,vashbalans,poka):
    def print_info(self):
        print(f"Ваш баланс {self.balanz} $ \n")
        print("Компьютер :")
        print(f" 4000 {self.money}")
        print(f"Монитор - {self.resolution}")
        print(f"Оперативная память - {self.memory} gb")
        print(f"Процессор - intel core {self.procesor}")
        print(f"Видеокарта - GEFORCE RTX {self.vidkarta}\n")


        print("Телефон :")
        print(f" 500 {self.money}")
        print(f"RAM - {self.RAM}")
        print(f"ХРАНИЛИЩЕ - {self.Xranilishe}")
        print(f"ПРОЦЕССОР - {self.proc}\n")


        print("Ноутбук:")
        print(f"2200 {self.money}")
        print(f"ОЗУ - {self.Ramka}")
        print(f"Хранилище - {self.tb}")
        print(f"Экран - {self.ekran}")
        print(f"Видеокарта - {self.Viduxa}")
        print(f"Проццессор - {self.Procisor}\n")


        print("Тв:")
        print(f" 1000 {self.money}")
        print(f"Разрешение экрана - {self.TV}")
        print(f"Качество - {self.tv}")

        print(f"\n{self.берет}")

        answer = input("")

        if answer  == "Нет":
            print(f"{self.poka}")


        if answer == "Компьютер":
            print(f"\n {self.vash } 4000$")
            self.balanz -= 4000

        if answer == "Телефон":
            print(f"\n {self.vash } 500$")
            self.balanz -= 500

        if answer == "Тв":
            print(f"\n {self.vash} 1000;")
            self.balanz -= 1000

        if answer == "Ноутбук":
            print(f"\n {self.vash }2200$ .")
            self.balanz -= 2200

        asnwir = input("Хотите Узнать баланс ?")
        if asnwir == "Да":
            print(f"Ваш баланс {self.balanz} $")
            print(f"{self.poka}")
        else:
            print(f"{self.poka}")
            sys.exit()




Print = Print()
Print.print_info()

