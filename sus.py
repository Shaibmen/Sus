import sqlite3
import sys
from Database import Database

def Connect():
    return sqlite3.connect('biblioteka.db')

class RegistrationUser():
    
    def registration():
        name = ""
        passport = ""
        podpiska = ""
        while True:
            name = str(input("введите имя: "))
            passport = int(input("введите номер паспорта(посление 6 цифр): "))
            podpiska = int(input("оформить подписку на чтение книг.\n 1. 3 месяца\n 2. 6 месяцев. \n 3. 9 месяцев. \n 4. 1 год\n"))
            match podpiska:
                case 1:
                    podpiska = "3 месяца"
                case 2:
                    podpiska = "6 месяцев"
                case 3:
                    podpiska = "9 месяцев"
                case 4:
                    podpiska = "1 год"
            break
        Database.CreateClient(name, passport, podpiska)
        print("регистрация успешна!")
        Zapusk.main()

class AdminUser():
    def AdminData():
        password = "adminlox"
        passowrdAdm = input("введите пароль: ")
        if passowrdAdm == password:
            AdminUser.AdminPanel()
        else:
            Zapusk.main()

    def AdminPanel():
        while True:
            choose = int(input("Панелька админа:\n1. Показать всех клиентов \n2. Поменять подписку клиенту\n3. Удалить клиента \n4. Выйти\n"))
            match choose:
                case 1:
                    Database.ShowAllClients()
                case 2:
                    name = input("введите имя клиента ")
                    newpodpiska = input("Выберите подписку: \n 1. 3 месяца\n 2. 6 месяцев. \n 3. 9 месяцев. \n 4. 1 год\n")
                    match newpodpiska:
                        case "1":
                            podpiska = "3 месяца"
                        case "2":
                            podpiska = "6 месяца"
                        case "3":
                            podpiska = "9 месяцев"
                        case "4":
                            podpiska = "1 год"
                    Database.UpdatePodpiska(name, podpiska)
                    print("обновление завершено")
                case 3:
                    passport = input("введите номер паспорта клиента: ")
                    Database.DeleteClient(passport)
                    print("удаление завершено")
                case 4:
                    return 0
        


class Zapusk():
    def main():
        Database.CreateTable()
        choose = int(input("\'Читальня\' \n-----------------------\n1.Зарегистрироваться\n2.Панель Админа\n3.Выйти\n"))
        match choose:
            case 1:
                RegistrationUser.registration()
            case 2:
                AdminUser.AdminData()
            case 3:
                print('Bye Bye!')
Zapusk.main()