import sqlite3

conn = sqlite3.connect('python.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                file_name TEXT)")
    conn.commit()

conn = sqlite3.connect('python.db')

fileList = ('information.docx', 'Hello.txt','myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg')

for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (file_name) VALUES (?)", (x,))
            print(x)

conn.close()

