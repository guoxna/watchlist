from flask import Flask
from flask import url_for, escape

app = Flask(__name__)

@app.route('/')
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
