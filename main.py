# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Вставляем данные в таблицу
import sqlite3
import time
def connection():
    connection = sqlite3.connect('shows.db')
    print('Соединение с БД прошло успешно')
    return connection
def add_group(connection):
    BandName = str(input('Название группы: '))
    Year = str(input('Год создания группы: '))
    Country = str(input('Страна группы: '))
    Place = str(input('Позиция в чартах: '))
    query = """
     INSERT INTO Band (BandName, Year, Country, Place)
     VALUES (?, ?, ?, ?);
     """
    cursor = connection.cursor()
    cursor.execute(query, (BandName, Year, Country, Place))
    connection.commit()
    connection.close()
def search_playlist_by_group(connection):
    group=str(input('Название группы:'))
    cursor=connection.cursor()
    cursor.execute(" SELECT * FROM Repertuar WHERE Grouppa=?",(group,))
    records=cursor.fetchall()
    print("Репертуар группы "+group+":")
    print('----------')
    count=0
    for row in records:
        count=count+1
        print(str(count)+". "+row[0])
    print('----------')
    connection.commit()
    connection.close()
def search_groupInfo(connection):
    Name=str(input('Название группы:'))
    cursor=connection.cursor()
    cursor.execute("SELECT *FROM Band WHERE BandName=?",(Name,))
    records=cursor.fetchall()
    print('----------')
    print("Название группы: "+records[0][0]+'\n'+"Год основания группы: "+records[0][1]+'\n'+"Страна: "+ records[0][2]+'\n'+"Позиция в чарте: "+ str(records[0][3]))
    print('----------')
    cursor.execute("SELECT *FROM Squad WHERE GroupName=?",(Name,))
    records=cursor.fetchall()
    print("Состав участников и информация о них:")
    print('----------')
    count=0
    for row in records:
        count=count+1
        print(str(count)+". "+row[0] + '\n'+"Роль:"+row[1]+". Возраст:"+str(row[2]))
        print('----------')
    print('----------')
    connection.commit()
    connection.close()
def delete_member(connection):
    Band=str(input("Введите название группы, из которой хотите удалить участника:"))
    Name=str(input("Введите ФИО участника, которого хотите удалить:"))
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Squad WHERE FIO=? AND GroupName=?",(Name,Band))
    print("Участник группы "+Band+" "+Name+" был успешно удален")
    connection.commit()
    connection.close()
def edit_place(connection):
    Band=str(input("Введите название группы, у которой хотите изменить позицию в чартах:"))
    NewPlace=int(input("Введите новую позицию группы в чарте:"))
    print("Новое место в чарте у группы " + Band+" "+str(NewPlace))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Band WHERE BandName=?",(Band,))
    record=cursor.fetchall()
    for row in record:
        OldPlace=int(row[3])
    cursor.execute("UPDATE Band set Place=Place+1 WHERE Place>=? AND Place<=?",(NewPlace,OldPlace))
    cursor.execute("UPDATE Band set Place=? WHERE BandName=?",(NewPlace,Band))
    connection.commit()
    connection.close()
def search_top_group_info(connection):
    print('----------')
    print("Репетуар лучшей группы в чартах")
    print('----------')
    cursor = connection.cursor()
    cursor.execute("SELECT *FROM Band WHERE Place=1")
    record=cursor.fetchall()
    count=0
    for row in record:
        BandName=str(row[0])
    cursor.execute("SELECT Name FROM Repertuar WHERE Grouppa=?",(BandName,))
    Tracks=cursor.fetchall()
    print("На данный момент чарт возглавляет группа "+BandName+", в ее репертуар входят песни:")
    for row in Tracks:
        count=count+1
        print(str(count)+". "+row[0])
    print('----------')
    connection.commit()
    connection.close()
def search_info_by_song(connection):
    cursor=connection.cursor()
    print('----------')
    print("Вы находитесь в меню поиска информации о песне, перед вами список песен всех групп, введите название песни, информацию о которой, вы хотели бы узнать")
    print('----------')
    cursor.execute("SELECT *FROM Repertuar")
    lists=cursor.fetchall()
    counter=0
    for row in lists:
        counter=counter+1
        print(str(counter)+". "+row[0]+" Группа:"+row[1])
    print('----------')
    TrackName=str(input("Название песни: "))
    cursor.execute("SELECT *FROM Repertuar WHERE Name=?",(TrackName,))
    record=cursor.fetchall()
    for row in record:
        print("Название песни: "+row[0]+". Группа: "+row[1]+". Автор: "+row[2]+" Год выхода: "+str(row[3])+". Композитор: "+row[4])
    counter=0
    connection.commit()
    connection.close()
def print_report_Topthree(connection):
    print("Отчет о топ-3 группах в чарте на сегодня:")
    print('----------')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM Band WHERE Place=1")
    record=cursor.fetchall()
    for row in record:
        print("Чарт возглавляет группа $"+row[0]+"$!!!!")
    cursor.execute("SELECT * FROM Band WHERE Place=2")
    record = cursor.fetchall()
    for row in record:
        print("На втором месте чарта располагается группа $" + row[0] + "$!!!!")
    cursor.execute("SELECT * FROM Band WHERE Place=3")
    record = cursor.fetchall()
    for row in record:
        print("Тройку чарта замыкает группа  $" + row[0] + "$!!!!")
    print('----------')
    connection.commit()
    connection.close()
def print_report_gastroli(connection):
    print('----------')
    print("Информация о запланированных гастролях музыкальных групп:")
    cursor=connection.cursor()
    cursor.execute("SELECT Grouppa FROM Gastroli")
    records=cursor.fetchall()
    for row in records:
        print("Группа "+row[0]+" планирует в этом году концерт")
        cursor.execute("SELECT *FROM Gastroli WHERE Grouppa=?",(row[0],))
        gastroli_info=cursor.fetchall()
        for inform in gastroli_info:
            print("Название программы: "+inform[0]+". Локация: "+inform[2]+". Дата: "+str(inform[3])+" Время концерта: "+str(inform[4])+" - "+str(inform[5])+" Цена билетов: "+ str(inform[6]))
        cursor.execute("SELECT *FROM Repertuar WHERE Grouppa=?",(row[0],))
        count=1
        repertuar_info=cursor.fetchall()
        print("Программа:")
        for repertuar in repertuar_info:
            print(str(count)+". "+repertuar[0]+". Автор: "+repertuar[2])
            count=count+1
        print('----------')
    connection.commit()
    connection.close()

def console_picture():
    print("                **    **  ********  **        **            **      ")
    print("               **    **  ********  **        **         **     **   ")
    print("              ********  **        **        **         **      **  ")
    print("             ********  ********  **        **         **      **  ")
    print("            **    **  **        **        **         **      **  ")
    print("           **    **  ********  ********  ********    **    **   ")
    print("          **    **  ********  ********  ********       **      ")

def menu():
    operation = int(input('Введите номер операции\n'
                          '0.Выход\n'
                          '1.Добавить новую Группу\n'
                          '2.Найти песни по Группе\n'
                          '3.Информация о группе\n'
                          '4.Удалить исполнителя из группы\n'
                          '5.Изменить место в хит-параде\n'
                          '6.Репертуар лучшей группы в хит-параде\n'
                          '7.Информация о песне\n'
                          '8.Топ-3 хит-парада отчет\n'
                          '9.Гастроли отчет\n'
                          'Операция:'))
    if operation == 0:
        return 0
    if operation == 1:
        add_group(connection())
        menu()
    if operation == 2:
        search_playlist_by_group(connection())
        menu()
    if operation == 3:
        search_groupInfo(connection())
        menu()
    if operation == 4:
        delete_member(connection())
        menu()
    if operation == 5:
        edit_place(connection())
        menu()
    if operation == 6:
        search_top_group_info(connection())
        menu()
    if operation == 7:
        search_info_by_song(connection())
        menu()
    if operation == 8:
        print_report_Topthree(connection())
        menu()
    if operation == 9:
        print_report_gastroli(connection())
        menu()

console_picture()
menu()