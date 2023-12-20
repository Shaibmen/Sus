import sqlite3
def Connect():
    return sqlite3.connect('biblioteka.db')
class Database():
    def CreateTable():
        connect = Connect()
        cursor = connect.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clients(
            Id INTEGER PRIMARY KEY,
            ClientName TEXT NOT NULL,
            Passport TEXT NOT NULL,
            Podpiska TEXT NOT NULL
            );
        ''')
        connect.commit()
        connect.close()

    def CreateClient(name, passport, podpiska):
        connect = Connect()
        cursor = connect.cursor()

        cursor.execute('INSERT INTO Clients (ClientName, Passport, Podpiska) VALUES(?,?,?)', (name, passport, podpiska))
        connect.commit()
        connect.close()

    def ShowAllClients():
        connect = Connect()
        cursor = connect.cursor()

        cursor.execute('SELECT * FROM Clients')
        clients = cursor.fetchall()

        for client in clients:
            print(client)
            connect.close()

    def DeleteClient(passport):
        connect = Connect()
        cursor = connect.cursor()

        cursor.execute('DELETE FROM Clients WHERE Passport = ?', (passport,))
        connect.commit()
        connect.close()

    def UpdatePodpiska(name, podpiska):
        connect = Connect()
        cursor = connect.cursor()

        cursor.execute('UPDATE Clients SET Podpiska = ? WHERE ClientName = ?', (podpiska, name))
        connect.commit()
        connect.close()