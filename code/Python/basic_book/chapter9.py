#web

#http urllib
import urllib.request as ur
url = 'http://www.google.com'
conn = ur.urlopen(url)
print(conn)
data = conn.read()
print(data)
#1XX 資訊 2XX成功 3XX重新導向 4XX 用戶端錯誤 5XX 伺服器錯誤
print(conn.status)
#MIME類型 Multipurpose Internet Mail Extensions
print(conn.getheader('Content-Type'))

# Common Gateway Interface (CGI)
#WSGI web server gateway interface

#bottle
from bottle import route,run,static_file
@route('/')
def home():
#    return 'it isnt fancy home page'
   return static_file('index.html',root='.')

@route('/echo/<thing>')
def echo(thing):
    #http://localhost:9999/echo/fuck
    return "say hello :%s"%thing

#會執行httserver
#run(host='localhost',port=9999)

#requests 類似 urllib.request

"""
import requests

resp=requests.get('http://localhost:9999/echo/fuck')
resp.text==say hello :fuck
"""


#Flask

from flask import Flask,render_template,request

#app=Flask(__name__,static_folder='.',static_url_path='')
app=Flask(__name__,template_folder='C:/Users/Spock_Xie/Desktop/python/code/PythonApplication1/templates')

@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/echoe/<thing>/<place>')
def echo(thing,place):
    #http://localhost:9999/echoe/fuck/ass
    #templates\
    #return app.send_static_file('index.html')
    return render_template('flask3.html',thing=thing,place=place)




@app.route('/es2')
#def 裡面變數沒有放會出錯
def echo5():
    #http://localhost:9999/es?thing=1111&place=5555
    thing=request.args.get('thing')
    place=request.args.get('place')

    return render_template('flask3a.html',thing=thing,place=place)
    
@app.route('/es3')
def echo6():
    #http://localhost:9999/e?thing=aaa&place=bbb
    kwargs={}
    kwargs['thing']=request.args.get('thing')
    kwargs['place']=request.args.get('place')

    return render_template('flask3a.html',**kwargs)
    

#app.run(port=9999,debug=True)

#flask跟bottle是除錯用sever
#實際上的組合 apache mod_wsgi
#nginx uWSGI app

#除了flash和bottle推薦使用django架構 值得去學

#幫你開網頁(用預設瀏覽器)
import webbrowser
url = 'http://www.python.org'
webbrowser.open(url)
webbrowser.open_new_tab(url)

#爬蟲 crawl scrape,beautufulsop 自己去查
#下面指令要放在apache的conf但一放就會爆掉流到以後課題
#WSGIScriptAlias C:/Users/Spock_Xie/Desktop/python/code/PythonApplication1/basic_book/home.wsgi