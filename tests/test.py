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
		)