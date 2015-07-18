import logging
import argparse
import os

from PIL import Image, ImageDraw, ImageFont
from math import ceil

def parse_arguments():
	"""
	Parse command line arguments.
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('-l','--log', dest='my_logging_level', default='DEBUG')
	parser.add_argument('-s','--string', default=None, help="text to paint")
	parser.add_argument('-la','--letters_across', type=int, default=6)
	parser.add_argument('-f','--font_file', default='octin_spraypaint_free.ttf', help="name of font file in /fonts directory")
	parser.add_argument('-fs','--font_size', type=int, default=200)
	parser.add_argument('-id','--img_dim', type=int, default=255, help="dimensions of image in pixels")

	return parser.parse_args()

def insert_newlines(string, every):
	"""
	Inserts newline characters into a string at regular intervals.
	"""	
	return '\n'.join(string[i:i+every] for i in xrange(0, len(string), every))

def woolify(text,letters_across,font_size,pixels,fontfile,color=1):
	"""
	Creates PIL image file of wrap-around text graphic. Defults to black stencil.
	:param str text:
	:param int letters_across:
	:param int font_size:
	:param int pixels:
	:param str fontfile:
	:param int|tup color:
	:return PIL.Image:
	"""
	# format and wrap string
	string = text
	string = string.upper()
	string = string.replace(' ','')
	rows_down = int(ceil(len(string)/float(letters_across)))
	string_to_draw = insert_newlines(string,letters_across)

	# create transparent blank image
	width = int(letters_across*font_size*0.575)
	height = int(rows_down*font_size*.95)
	img_dim = (pixels,pixels,pixels,0)
	base = Image.new('RGBA', (width,height), img_dim)

	# import font
	filepath = '/'.join([os.path.dirname(os.path.realpath(__file__)),'fonts',fontfile])
	fnt = ImageFont.truetype(filepath, font_size)

	# draw text on image
	draw = ImageDraw.Draw(base)
	draw.multiline_text((0,0), string_to_draw, font=fnt, fill = color)
	
	return base

def main():
	args = parse_arguments()

	# add logging
	logger = logging.getLogger(__file__)
	logger.setLevel(getattr(logging, args.my_logging_level.upper()))
	ch = logging.StreamHandler()
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	ch.setFormatter(formatter)
	logger.addHandler(ch)

	im = woolify(args.string,args.letters_across,args.font_size,args.img_dim,args.font_file)
	im.show()

	return

if __name__ == "__main__":
	main()
