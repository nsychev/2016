import sqlite3
import os
from urllib.parse import unquote

MAIN_PAGE = '''<meta charset="utf-8" />
<h1>Notebook</h1>
<form method="get" action="/note">
<p>Введите номер записи:</p>
<p><input type="text" name="id" value="1" /></p>
<p><button type="submit">Получить</button></p>
</form>
<hr/>
<p>Copyright &copy; @nsychev</p>
'''

CLIENTS_PAGE = '''<meta charset="utf-8" />
<h1>Под номером {0} хранится:</h1>
<p>{1}</p>
<hr/>
<p><a href="/">Найти ещё один номер</a></p>
<p>Copyright &copy; @nsychev</p>
'''
LABEL_ERROR = '''<h2>НИЧЕГО</h2>'''

def application(environ, start_response):
    status = '200 OK'
    
    if environ["PATH_INFO"] == "/":
      content = MAIN_PAGE
    elif environ["PATH_INFO"] == "/note":
      if environ["QUERY_STRING"] == "":
        content = CLIENTS_PAGE.format(0, LABEL_ERROR)
      elif not("=" in environ["QUERY_STRING"]):
        content = CLIENTS_PAGE.format(0, LABEL_ERROR)
      else:
        if os.path.isfile("/ctf/web200/data.db"):
          dbconn = sqlite3.connect("/ctf/web200/data.db")
          dbcur = dbconn.cursor()
        else:
          dbconn = sqlite3.connect("/ctf/web200/data.db")
          dbcur = dbconn.cursor()
          dbcur.execute("CREATE TABLE notes (id text, value text)")
          data = (('hello','world'), ('this is', 'not a flag'), ('DHerywrywgsfhdfhr', 'upml_notaflag'), ('admin', 'admin'), ('qwerty', '123'), ('Qwerty123', '123'), ('1', '1'), ('2', '2'), ('3', 'SECRET DATA'), ('4', 'THIS IS SPARTA'), ('5', 'FSB FOUND ME'), ('6', 'I SAVE ALL MY DATA IN SECURE PLACE'), ('7', 'NOBODY CAN SEE IT'), ('8', 'I AM SAFE'), ('9', 'I USE STRONG ESCAPING'), ('10', 'BUT MAY BE NOT'), ('11', 'I MAKE A NEW TABLE FOR NOTES'))
          for e in data:
            dbcur.execute("INSERT INTO notes VALUES ('{0}', '{1}')".format(e[0], e[1]))
          dbconn.commit()
        id = unquote(environ["QUERY_STRING"].split("=")[1]).replace("+", " ").replace("'", "\\'")
        query = "SELECT * FROM notes WHERE id='{0}'".format(id)
        try:
          dbcur.execute(query)
          dbconn.commit()
          values = dbcur.fetchall()
          content = CLIENTS_PAGE.format(id, str(values))
        except:
          content = CLIENTS_PAGE.format(id, LABEL_ERROR)
    else:
      content = "404 Not Found"    
    
    content = content.encode("utf-8")
    
    response_headers = [('Content-type', 'text/html; charset=utf-8'),
                        ('Content-Length', str(len(content)))
                       ]
    
    start_response(status, response_headers)

    return [content]
