import random, codecs, sys, string

def makearr(source):
    thearr=[]
    exclude=["&&", "||", "bksthumb", "base64", "null", "delete this", "void," "function", "prototype", "book", "Books", "News", "Shopping", "Flights", "Finance", "Personal", "Search settings", "Show all results", "Advanced search", "History", "Search help", "No preview"]

    with codecs.open(source, "r", "utf-8") as sents:

        for line in sents:
        	fl=False
        	for x in exclude:
        		if x in line:
        			fl=True
        	if fl == False:
        		y=line.strip()
        		for z in y:
        			for zz in z:
        				if zz not in string.printable:
        					y=y.replace(z,"")
        			if z.isnumeric():
        				y=y.replace(z,"")
        				
        		y=y.replace("...","")
        		y=y.replace(" ,",",")
        		y=y.replace(" , ",",")
        		y=y.replace(" .",".")
        		y=y.replace(" . ",". ")
        		y=y.replace("  "," ")
        		y=y.replace("- ","")
        		
        		if len(y) >= 4 and y not in thearr:
        			thearr.append(y)
                
    return(thearr)



def prose(a):

    z=len(a)
    begarr=[]
    midarr=[]
    endarr=[]
    outarr=[]
    
    for i in range(z-1):
    	c=a.pop(random.randrange(0, len(a)-1))
    	if c[0] in string.ascii_uppercase or (c[0] == "\"" and c[1] in string.ascii_uppercase):
    		begarr.append(c.strip())
    	elif c[-1] in "\".!?":
    		endarr.append(c.strip())
    	elif c[0] in string.ascii_lowercase and c[-1] in string.ascii_lowercase or c[-1]  == ",":
    		midarr.append(c.strip())
    	else:
    		pass

    while len(begarr) > 1:
    	d=begarr.pop(random.randrange(0, len(begarr)-1))
    	if d[-1] in "\".!?":
    		outarr.append(d)
    	else:
    		if len(midarr) > 1:
    			e=midarr.pop(random.randrange(0, len(midarr)-1))
    		if len(endarr) > 1:
    			f=endarr.pop(random.randrange(0, len(endarr)-1))
    		if d[0] != "\"" and f[-1] == "\"":
    			f=f[0:-1]
    		g=d+" "+e+" "+f+" "
    		outarr.append(g)

    return(outarr)

def main():

	source1=sys.argv[1]
	arr1=makearr(source1)
	out1=prose(arr1)

	if len(out1) < 5000:
		j=len(out1)
	else:
		j=5000

	for i in range(j):
		if i % 9 == 0:
			hdst=out1[i].rsplit()
			if len(hdst) > 2:
				head=hdst[0]+" "+hdst[1]+" "+hdst[2]
			else:
				head=hdst[0]
			head=head.replace(string.punctuation,"")
			print(head.upper()+".")
			print("")
		else:
			print(out1[i])
			print("")
        
main()
