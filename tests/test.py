from pywordcloud import pywordcloud

if __name__ == '__main__':
	text = open("input.txt").read()

	pywordcloud.create(text, outfile="output.html", uppercase=False, showfreq=False, frequency=50, removepunct = False, 
	minfont = 1.5, maxfont = 8, hovercolor="green", showborder=False, fontfamily='calibri', width="1000px", height="400px",
	#colorlist = ["red","blue","yellow","black","green	"] 
	)