import sqlite3
import pytz
import time
from datetime import datetime

def reg_user(id, refka):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(""" CREATE TABLE IF NOT EXISTS black_list (
            id BIGINT,
            stat
            ) """)
    db.commit()

    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id BIGINT,
        prokladka,
        finish_stat
        ) """)
    db.commit()

    sql.execute(f"SELECT id FROM user_time WHERE id ='{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?,?)", (id,time.time(),'0'))
        db.commit()


#Новое
def get_data_tag(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    a = sql.execute(f"SELECT prokladka FROM user_time  WHERE id = '{id}'").fetchone()[0]
    return a


def update_status(user_id,n):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    try:
        status_all = int(sql.execute(f"SELECT finish_stat FROM user_time WHERE id = '{user_id}'").fetchall()[0][0])
        if status_all < n:
            sql.execute(f"UPDATE user_time SET finish_stat = '{n}'  WHERE id = '{user_id}'")
            db.commit()

    except Exception as ex:
        print("Произошла ошибка:", ex, "юзер:" , user_id)



def change_all():
    print('Заблокирована функция. Необходимо раскомитить код')
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET finish_stat = '1000'")
    db.commit()



def info_members(): # Количество челов, запустивших бота
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    all = sql.execute(f"SELECT COUNT(*) FROM user_time ").fetchone()[0]

    a0 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '0'").fetchone()[0]
    a1 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '1'").fetchone()[0]
    a2 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '2'").fetchone()[0]
    a3 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '3'").fetchone()[0]
    a4 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '4'").fetchone()[0]
    a5 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '5'").fetchone()[0]
    a6 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '6'").fetchone()[0]
    a7 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '7'").fetchone()[0]
    a8 = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE finish_stat = '8'").fetchone()[0]


    return [a0,a1,a2,a3,a4,a5,a6,a7,a8,all]




def get_stat(): # Количество челов, запустивших бота
    env = []
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    data = sql.execute(f'SELECT DISTINCT prokladka FROM user_time').fetchall()

    for d in data:
        i = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE prokladka = "{d[0]}"').fetchone()[0]
        env.append([d[0],i])

    return env

def get_my_link(user_name):
    print('Поиск')
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    i = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE prokladka = "{user_name}"').fetchone()[0]
    return i



def get_connt_stat(n): # Количество челов, запустивших бота
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    i = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE prokladka = "{n}"').fetchone()[0]
    return i



def change_status(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET finish_stat = '1' WHERE id = '{id}'")
    db.commit()


def change_prokladka(id, p):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET prokladka = '{p}' WHERE id = '{id}'")
    db.commit()

def add_black(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(f"SELECT id FROM black_list WHERE id = '{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO black_list VALUES (?,?)", (int(id), '0'))
        sql.execute(f"INSERT INTO black_list VALUES (?,?)", (str(id), '0'))
        db.commit()

def get_username(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    q = (sql.execute(f"SELECT prokladka FROM user_time WHERE id = '{id}'").fetchone())[0]
    return q



def cheak_black(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT id FROM black_list WHERE id = '{id}'")
    if sql.fetchone() is None: #Список пуст, разрешает
        return 0
    else: #Запрещаем
        return 1