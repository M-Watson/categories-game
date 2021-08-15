import sqlite3
import random
import pandas as pd


def get_random_list():
    con = sqlite3.connect("data/categories.db")
    df = pd.read_sql_query("SELECT * from originals", con)
    con.close()

    random_list = []
    for i in range(13):
        number = random.randint(0,len(df))
        while number in random_list:
            new_number = random.randint(0,len(df))
            number = new_number
        random_list.append(number)

    '''
    print(random_list)
    con = sqlite3.connect('data//categories.db')
    cur = con.cursor()
    s = cur.execute(select_all)
    '''
    selected = []
    selected_full = []
    for n in random_list:
        #select_n = f'''SELECT * FROM originals where i={n};'''
        select_n_content = df['content'].iloc[n]
        select_n_full = df.iloc[n]
        selected_full.append(select_n_full)
        selected.append(select_n_content)
    return[selected,selected_full]
