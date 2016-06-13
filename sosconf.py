# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, url_for, redirect, abort
from magic import Magic
import wget
import os
#from flask_sslify import SSLify
app = Flask(__name__)
#sslify = SSLify(app)

# Allowed ext.
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'png', 'jpeg'])

magia = Magic()


def allowed_file(filename):
	return '.' in filename and \
	       filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# ------------------------


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
	file_ = request.files['file']
	texto1 = request.form['texto1']
	texto2 = request.form['texto2']
	filefb = request.form['filefb']

	if filefb != 'no':
		# Con wget obtenemos el archivo pero se descarga en disco
		fbimg = wget.download(filefb, out=".")
		img_out = magia.CrearConf(fbimg, texto1, texto2)
		os.remove(fbimg)
		return redirect("img/"+img_out)

	if file_ and allowed_file(file_.filename):
		img_out = magia.CrearConf(file_, texto1, texto2)
		return redirect("img/"+img_out)

	else:
		return redirect(url_for('error'))


@app.route('/img/<path>')
def img(path):
	return render_template('image.html', path=path)

@app.route('/error')
def error():
	return render_template('error.html')


if __name__ == '__main__':
	app.run(debug=True)
