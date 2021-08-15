import sqlite3
import pandas as pd


def set_up_table():
    create_command = '''CREATE TABLE IF NOT EXISTS originals (
                            i INTEGER,
                            original_set_number INTEGER,
                            content
                            );'''

    con = sqlite3.connect('data//categories.db')
    cur = con.cursor()
    cur.execute(create_command)
    con.commit()



    data = pd.read_csv('data//categories.csv')

    for i in range(len(data)):
        original_set_number = data['original_set_number'].iloc[i]
        content = data['content'].iloc[i].replace("'","")

        insert_command = f"""INSERT INTO originals
                            (i,original_set_number,content)
                            VALUES ('{i}','{original_set_number}','{content}');"""
        cur.execute(insert_command)
        con.commit()




    con.close()
    return()

def create_current():
        create_command = '''CREATE TABLE IF NOT EXISTS current (
                                i INTEGER,
                                original_set_number INTEGER,
                                content
                                );'''

        con = sqlite3.connect('data//categories.db')
        cur = con.cursor()
        cur.execute(create_command)
        con.commit()


create_current()
