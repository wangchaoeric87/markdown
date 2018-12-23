from flask import Flask
from flask import render_template
from flask import Markup
import markdown

app=Flask(__name__)



@app.route('/main')
def index():
	content = md2html('static/doc/main.md')
	return render_template('index.html',**locals())


def md2html(filename):
	
	exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
	mdcontent = ""
	with open(filename,'r',encoding='utf-8') as f:
		mdcontent = f.read()
		pass	
	html = markdown.markdown(mdcontent,extensions=exts)
	content = Markup(html)
	return content


if __name__ == '__main__':
	app.debug = True
	app.run(host='127.0.0.1',port = 5000)
