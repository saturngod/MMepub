import os,zipfile,sys,shutil
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

Zawgyicss ='''
@font-face {
font-family : "Zawgyi-One";
font-weight : normal;
font-style: normal;
src: url('zawgyi.ttf');
}

@font-face {
font-family : "Zawgyi-One";
font-weight : normal;
font-style: italic;
src: url('zawgyi.ttf');
}

@font-face {
font-family : "Zawgyi-One";
font-weight : bold;
font-style: normal;
src: url('zawgyi.ttf');
}

@font-face {
font-family : "Zawgyi-One";
font-weight : bold;
font-style: italic;
src: url('zawgyi.ttf');
}

body,p,h1,h2,h3,span,div,ol,ul,li,table,tr,td,th,a {
font-family : "Zawgyi-One" !important;
font-weight : normal;
font-style: normal;
-webkit-hyphens:none;
}
'''

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
			#copy zawgyi file
			shutil.copy("data/zawgyi.ttf","epubtmp/OPS/")
			
			#add file
			style= open('./epubtmp/OPS/global.css','r')
			tmpcss=style.read()
			style.close()
		
			css=tmpcss+"\n"+Zawgyicss
		
			style= open('./epubtmp/OPS/global.css','w')
			style.write(css)
			style.close()
		
			#read style.css to add font family
			style= open('./epubtmp/OPS/style.css','r')
			css=style.read()
			css=css.replace("}","\tfont-family:Zawgyi-One;\n}")
			style.close()
		
			#write update file
			style= open('./epubtmp/OPS/style.css','w')
			style.write(css)
			style.close()
		
		#if pages epub file	
		elif os.path.exists("./epubtmp/OPS/css/book.css"):
			#copy zawgyi file
			shutil.copy("data/zawgyi.ttf","epubtmp/OPS/css/")
			
			#add file
			style= open('./epubtmp/OPS/css/book.css','r')
			tmpcss=style.read()
			style.close()
		
			tmpcss=tmpcss.replace("}","\tfont-family:Zawgyi-One;\n}")
			css=Zawgyicss+"\n"+tmpcss
		
			style= open('./epubtmp/OPS/css/book.css','w')
			style.write(css)
			style.close()
		
		#calibre file
		elif os.path.exists("./epubtmp/stylesheet.css"):
		    #copy zawgyi file
			shutil.copy("data/zawgyi.ttf","epubtmp/")
			
			#add file
			style= open('./epubtmp/stylesheet.css','r')
			tmpcss=style.read()
			style.close()
		
			tmpcss=tmpcss.replace("}","\tfont-family:Zawgyi-One;\n}")
			css=Zawgyicss+"\n"+tmpcss
		
			style= open('./epubtmp/stylesheet.css','w')
			style.write(css)
			style.close()
		    
		
		#check output folder
		if not os.path.exists("./output"):
		    os.makedirs("output")
	
		#zip it
		zipper("./epubtmp","output/"+fname[0:-5]+"_new.epub")
	
		#clear direcory
		shutil.rmtree("./epubtmp")
		print fname + " is done. Check file in Output folder. New File name"+fname[0:-5]+"_new.epub"
			