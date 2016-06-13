# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from settings import *
import uuid


class Magic():
	def CrearConf(self, imagen, texto1, texto2):
		texto1 = unicode(texto1.upper())

		# Abrimos la base y el logo, dibujamos la base
		img_base = Image.open(os.path.join(APP_STATIC, 'base.png'))
		draw = ImageDraw.Draw(img_base)
		logo = Image.open(os.path.join(APP_STATIC, 'logo.png'))

		# Obtenemos la imagen subida y hacemos resize y b&w
		img2 = Image.open(imagen)
		#img2 = img2.resize((604, 512))
		if img2.size[0] <= img2.size[1]:
			basewidth = 604
			wpercent = (basewidth / float(img2.size[0]))
			hsize = int((float(img2.size[1]) * float(wpercent)))
			img2 = img2.resize((basewidth, hsize), Image.ANTIALIAS)

		else:
			baseh = 512
			hpercent = (baseh / float(img2.size[1]))
			wsize = int((float(img2.size[0]) * float(hpercent)))
			img2 = img2.resize((wsize, baseh), Image.ANTIALIAS)

		img2 = img2.convert('L')

		# Pegamos base + img subida + logo
		img_base.paste(img2, (420, 0))
		img_base.paste(logo, (847, 407), mask=logo)

		font = ImageFont.truetype(os.path.join(APP_STATIC, "Brown-Bold.otf"), 48)
		font2 = ImageFont.truetype(os.path.join(APP_STATIC, "Brown-Bold.otf"), 28)

		tx, ty = font.getsize(texto1)
		t2x, t2y = font.getsize(texto1)

		# Ajustamos tamaño de los textos
		i = 1
		while tx > 380:
			font = ImageFont.truetype(os.path.join(APP_STATIC, "Brown-Bold.otf"), 45 - i)
			tx, ty = font.getsize(texto1)
			i += 1

		i2 = 1
		while t2x > 380:
			font2 = ImageFont.truetype(os.path.join(APP_STATIC, "Brown-Bold.otf"), 28 - i2)
			t2x, t2y = font2.getsize(texto2)
			i2 += 1

		# Imprimimos los textos en la imagen
		draw.text((34, 50), texto1, (0, 0, 0), font=font)
		draw.text((34, 50 + ty + 10), texto2, (0, 0, 0), font=font2)

		name = uuid.uuid4().hex
		img_base.save(os.path.join(APP_STATIC) + '/temp/' + name + '.png')
		return name
