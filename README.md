# woolifier
Generates a Christopher Wool-style stencil painting from a string of inputted text. Works on the command line.

Dependencies
------------

  * Python 2.7
  * Pillow 2.9.0
  * Distribute 0.6.24
  * Argparse 1.2.1
  * Wsgiref 0.1.2


Exact version numbers probably not important.

Usage
-----

1. Install the dependencies listed above.

2. Save any font files to be used with this module in the /fonts directory. The filename of the font used in the image is a command line argument. Defaults to Octin Stencil, which is available free for download here: http://www.fontspring.com/fonts/typodermic/octin-college.

3. Run from the command line. The one required argument is the text to include in the outputted image, but the dimensions, number of letters per row, and font to use are also customizable.

This module is used to generate the images on http://newsbuzzlife.tumblr.com.
