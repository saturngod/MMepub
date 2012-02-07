This version is alpha version and written on python 2.7.1


Requirement
===========
Python 2.7 or later

Supported epub generator
===========
1. epubgen.jar
2. pages (export to epub)
3. calibre (tested with version 0.8)
4. InDesign (tested with CS 5)

How to use
===========

Add all .epub file in same path of convert.py and convert with following command

	$python convert.py [font family] [font file]


Font File
----------

If you want to use custom file , add font.ttf in data/[your font file].ttf

Example :
	
	$python convert.py Yunghkio yunghkio.ttf

yunghkio.ttf must be in *data* folder (**data/yunghkio.ttf**)


Add Cover
-----------

If you want to add cover, your **.epub and [cover].png must be same name**.

Example :
	
	Epub file : myBook.epub , Cover file: myBook.png

FAQ
===========

### Got error message IOError: [Errno 20] Not a directory:

It's a bug of python 2.6. Please, upgrade to python 2.7 or patched the latest python 2.6 zip file.

Read more about bug in [here](http://stackoverflow.com/questions/2928373/extracting-a-app-from-a-zip-file-in-python-using-zipfile/2935330#2935330 "").

Change Log
==========


**Feb 8 , version 1.5**

* support cover
* support custom font

