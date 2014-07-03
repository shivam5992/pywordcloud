import random, re, string, stopwords, sys

exclude = list(string.punctuation)

def getKeywords(articletext, case, freq, removepunct):
	word_dict = {}
	if removepunct == True:
		articletext = "".join(x for x in articletext if x not in exclude)
	word_list = articletext.lower().split()
	filtered_words = word_list
	for word in filtered_words:
		if word not in stopwords.stopwords and word.isalnum() and not word.isdigit() and len(word) > 2:
			if word not in word_dict:
				word_dict[word] = 1
			if word in word_dict:
				word_dict[word] += 1
	top_words =  sorted(word_dict.items(),key=lambda(k,v):(v,k),reverse=True)[0:freq]
	top = []
	for w in top_words:
		top.append(w)
	return top

def create(text, outfile="output.html", uppercase=False, showfreq=True, frequency=50, 
	minfont = 1, maxfont = 6, hovercolor="red", width="1000px", height="1000px", showborder=False
	, fontfamily = 'calibri', removepunct = False, colorlist = ['#607ec5','#002a8b','#86a0dc','#4c6db9'] ):
	
	if not outfile.endswith(".html"):
		print "Please Enter Output File with extension .html"
		sys.exit(0)

	case = uppercase
	show_freq = showfreq
	
	article = str(text).replace("\n"," ")

	freq = frequency
	a = getKeywords(article, case, freq, removepunct)
	random.shuffle(a)
	b = [x[1] for x in a]
	minFreq = min(b)
	maxFreq = max(b)

	span = ""
	if showborder == True:
		css  = """#box{font-family:'"""+fontfamily+"""';border:2px solid black;width:""" + width + """;height:""" + height +"""}
		#box a{text-decoration : none}
		"""
	else:
		css  = """#box{font-family:'"""+fontfamily+"""';width:""" + width + """;height:""" + height +"""}
		#box a{text-decoration : none}
		"""
	
	colors = colorlist
	colsize = len(colors)
	k = 0
	for index,item in enumerate(a):
		index += 1
		if case == True:
			tag = str(item[0]).upper()
		else:
			tag = str(item[0])

		if show_freq == True:
			span += '<a href=#><span class="word'+str(index)+'" id="tag'+str(index)+'">&nbsp;' + tag + " (" + str(item[1]) + ") " + "&nbsp;</span></a>\n"
		else:
			span += '<a href=#><span class="word'+str(index)+'" id="tag'+str(index)+'">&nbsp;' + tag + "&nbsp;</span></a>\n"	
		

		try:
			freqTag = int(item[1])
			fontMax = maxfont
			fontMin = minfont
			K = (freqTag - minFreq)/(maxFreq - minFreq)
			frange = fontMax - fontMin
			C = 4
			
			K = float(freqTag - minFreq)/(maxFreq - minFreq)
			size = fontMin + (C*float(K*frange/C))
		except:
			print "!!! Please input a text with more number of words !!!"
			sys.exit(0)

		css += '#tag'+str(index)+'{font-size: '+ str(size) +'em;color: ' + colors[int(k%colsize)]+'}\n'
	 	css += '#tag'+str(index)+':hover{color:' + hovercolor + '}\n'
	 	k += 1
	

	''' Write the HTML and CSS into seperate files ''' 

	f = open(outfile, 'w')
	message = """
	<style type="text/css">
	""" + css +"""
	</style>
	<div id='box'>
		""" + span +  """
	</div>
	"""
	f.write(message)
	f.close
	f.flush()
	print "Successfully generated word cloud in '" + outfile + "' file."
