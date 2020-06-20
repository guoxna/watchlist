from flask import Flask, render_template
from flask import url_for, escape

app = Flask(__name__)

name = 'Grey Li'
movies = [
          {'title': 'My Neighbor Totoro', 'year': '1988'},
          {'title': 'Dead Poets Society', 'year': '1989'},
          {'title': 'A Perfect World', 'year': '1993'},
          {'title': 'Leon', 'year': '1994'},
          {'title': 'Mahjong', 'year': '1996'},
          {'title': 'Swallowtail Butterfly', 'year': '1996'},
          {'title': 'King of Comedy', 'year': '1999'},
          {'title': 'Devils on the Doorstep', 'year': '1999'},
          {'title': 'WALL-E', 'year': '2008'},
          {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def index():
    return render_template('index.html', name = name, movies = movies)

@app.route('/index')
@app.route('/home')
def hello():
	return '<h1>Welcome to my watchlist~</h1><img src="https://media.giphy.com/media/7lJKqGgUKDxfO/giphy.gif">'

@app.route('/user/<name>')
def user_page(name):
	return 'User: %s' % escape(name)

@app.route('/test')
def test_url_for():
	# 下面是一些调用示例（请在命令行窗口查看输出的url）：
	print(url_for('hello'))
	print(url_for('user_page', name='guoxiaona'))
	print(url_for('user_page', name='another one'))
	print(url_for('test_url_for'))
	print(url_for('test_url_for', num=2))
	return 'Test page'
