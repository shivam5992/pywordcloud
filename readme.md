pywordcloud
===========

Python package to generate word clouds by analysing the text.

Features
--------

* Generate output format in HTML

* Control over css styling

* Control over Words

Install
-------

You can install pywordcloud either via the Python Package Index (PyPI) or from source.

To install using pip:

	$ pip install pywordcloud
	
To install using easy_install:
	
	$ easy_install pywordcloud

Downloading and installing from source

Download the latest version of PyTagCloud from http://pypi.python.org/pypi/pywordcloud/

You can install it by doing the following,:

    $ tar xfz pywordcloud-*.tar.gz
   
    $ cd pywordcloud-*/
   
    $ python setup.py build
   
    $ python setup.py install # as root



Usage
-----
   
    from pywordcloud import pywordcloud

	if __name__ == '__main__':
		text = open("input.txt").read()
		create(text, 
			outfile="output.html", 
			uppercase=False, 
			showfreq=True, 
			frequency=100, 
			removepunct = False, 
			minfont = 1.5, 
			maxfont = 6, 
			hovercolor="green", 
			showborder=False, 
			fontfamily='calibri', 
			width="1000px", 
			height="400px",
			#colorlist = ["red","blue","yellow","black","green"] 
			)"400px", colorlist = ["red","blue","yellow","black","green	"] )

Arguments
---------

**text:** Input text to create word cloud

**outfile:** Name of the ouput file, should ends with .html

**uppercase:** Boolean True to generate WC with all words in Upper Case, Otherwise False

**showfreq:** Boolean True to generate WC with words and their frequencies

**frequency:** Number of words to display in WC

**removepunct:** Set True to remove all punctuations from text

**minfont:** Set minimum font in Word Cloud (in pixels)

**maxfont:** Set maximum font in Word Cloud (in pixels)

**hovercolor:** Set hover color for words

**showborder:** Bollean True to show border of WC

**fontfamily:** Set Font Family for WC

**width:** Set Width of WC

**height:** Set height of WC

**colorlist:** Set custom color list seperated by commas.


Examples
--------

![image](http://i58.tinypic.com/2q1gnrr.png)