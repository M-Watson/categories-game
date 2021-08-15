from flask import Flask
from flask import render_template,request,redirect

import sqlite3
import pandas as pd

import randomSelect as rs






app = Flask(__name__)


#@app.route('/hello/<name>')

@app.route('/',methods=['GET','POST'])
def hello(name=None):
    con = sqlite3.connect("data/categories.db")
    df = pd.read_sql_query("SELECT * from current", con)
    contents = []
    for n in range(len(df['content'])):
        #select_n = f'''SELECT * FROM originals where i={n};'''
        select_n_content = df['content'].iloc[n]
        contents.append(select_n_content)



    if request.form.get('SEND'):
        cur = con.cursor()
        delete_command = '''DELETE FROM current;'''
        cur.execute(delete_command)
        con.commit()
        contents,full = rs.get_random_list()


        for v in range(len(full)):
            i = full[v]['i']
            original_set_number = full[v]['original_set_number']

            content = full[v]['content']
            cur = con.cursor()
            insert_command = f"""INSERT INTO current
                                (i,original_set_number,content)
                                VALUES ('{i}','{original_set_number}','{content}');"""
            cur.execute(insert_command)
            con.commit()

        df = pd.read_sql_query("SELECT * from current", con)
        contents = []
        for n in range(len(df['content'])):
            #select_n = f'''SELECT * FROM originals where i={n};'''
            select_n_content = df['content'].iloc[n]
            contents.append(select_n_content)

        return(render_template('hello.html', len = len(contents), contents = contents))



    return(render_template('hello.html', len = len(contents), contents = contents))


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8080)
