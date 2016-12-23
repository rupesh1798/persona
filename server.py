from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
	return render_template("main.html")


@app.route('/home')
def home():
	return render_template("home.html")


@app.route('/resume')
def resume():
	return render_template("resume.html")


@app.route('/blog')
def blog():
	return render_template("blog.html")
if __name__=='__main__':

	app.run()