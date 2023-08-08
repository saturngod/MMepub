import os,zipfile,sys,shutil,cover
from time import sleep
#zipper function from http://coreygoldberg.blogspot.com/2009/07/python-zip-directories-recursively.html
def zipper(dir, zip_file):
	zip = zipfile.ZipFile(zip_file, 'w', compression=zipfile.ZIP_DEFLATED)
	root_len = len(os.path.abspath(dir))
	for root, dirs, files in os.walk(dir):
		archive_root = os.path.abspath(root)[root_len:]
		for f in files:
			if (f!='.DS_Store'):
				fullpath = os.path.join(root, f)
				archive_name = os.path.join(archive_root, f)
				zip.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
	zip.close()
	return zip_file

if (len(sys.argv) > 2):
    font_family = sys.argv[1]
    font_file = sys.argv[2]
else:
	font_family = "Zawgyi-One"
	font_file = "zawgyi.ttf"

if not os.path.exists("data/"+font_file):
	print ("There is no "+font_file+" in data folder")
	sys.exit()

Zawgyicss ='''
@font-face {
font-family : "'''

Zawgyicss=Zawgyicss+font_family+'''";
font-weight : normal;
font-style: normal;
src: url("'''

Zawgyicss=Zawgyicss+font_file+'''");
}

@font-face {
font-family : "'''

Zawgyicss=Zawgyicss+font_family+'''";
font-weight : normal;
font-style: italic;
src: url("'''
Zawgyicss=Zawgyicss+font_file+'''");
}

@font-face {
font-family : "'''

Zawgyicss=Zawgyicss+font_family+'''";
font-weight : bold;
font-style: normal;
src: url("'''

Zawgyicss=Zawgyicss+font_file+'''");
}

@font-face {
font-family : "'''

Zawgyicss=Zawgyicss+font_family+'''";
font-weight : bold;
font-style: italic;
src: url("'''

Zawgyicss=Zawgyicss+font_file+'''");
}

body,p,h1,h2,h3,span,div,ol,ul,li,table,tr,td,th,a {
font-family : "'''

Zawgyicss=Zawgyicss+font_family+'''" !important;
font-weight : normal;
font-style: normal;
-webkit-hyphens:none;
}
'''

def make_epub(path,css_file,css_file2=""):
	shutil.copy("data/"+font_file,path)
			
	#add file
	style= open(path+css_file,'r')
	tmpcss=style.read()
	style.close()
			
	tmpcss=tmpcss.replace("}","\tfont-family:'"+font_family+"';\n}")
	css=Zawgyicss+"\n"+tmpcss
	style= open(path+css_file,'w')
	style.write(css)
	style.close()

	if(css_file2!=""):
		#add file
		style= open(path+css_file2,'r')
		tmpcss=style.read()
		style.close()
				
		tmpcss=tmpcss.replace("}","\tfont-family:"+font_family+";\n}")
		css=Zawgyicss+"\n"+tmpcss
		style= open(path+css_file2,'w')
		style.write(css)
		style.close()

dirList=os.listdir("./")
for fname in dirList:
	if fname[-4:]=="epub" :
		
		#check tmp folder
		if not os.path.exists("./epubtmp"):
			os.makedirs("epubtmp")
			
		#check pages epub or epubgen
		#converting start
		zip_ref=zipfile.ZipFile(fname,'r')
		zip_ref.extractall('./epubtmp')
		zip_ref.close()
		
		#copy file
		shutil.copy("data/com.apple.ibooks.display-options.xml","epubtmp/META-INF/")
		
		
		#if epubgen file
		if os.path.exists("./epubtmp/OPS/global.css"):
			make_epub("./epubtmp/OPS/","global.css","style.css");
		
		#if pages epub file	
		elif os.path.exists("./epubtmp/OPS/css/book.css"):
			make_epub("./epubtmp/OPS/css/","book.css");
		
		#calibre file
		elif os.path.exists("./epubtmp/stylesheet.css"):
			make_epub("./epubtmp/","stylesheet.css");
		
		#wp2epub wordpress plugin	
		elif os.path.exists("./epubtmp/OEBPS/styles/main.css"):
			make_epub("./epubtmp/OEBPS/styles/","main.css");
		
		#indesigin
		elif os.path.exists("./epubtmp/OEBPS/template.css"):
			make_epub("./epubtmp/OEBPS/","template.css");
			
		
		#cover
		if os.path.exists(fname[0:-5]+".png"):
			cover.replace_cover(fname[0:-5]+".png")

		#check output folder
		if not os.path.exists("./output"):
			os.makedirs("output")
	
		#zip it
		zipper("./epubtmp","output/"+fname[0:-5]+"_new.epub")
	
		

		#clear direcory
		shutil.rmtree("./epubtmp")
		print (fname + " is done. Check file in Output folder. New File name "+fname[0:-5]+"_new.epub")