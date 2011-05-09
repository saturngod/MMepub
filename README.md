This version is alpha version and written on python 2.7.1

Now, it's only working with epubgen-0.5.0.jar. You can download from [here](http://code.google.com/p/epub-tools/downloads/detail?name=epubgen-0.5.0.jar&can=2 "epubgen").

Requirement
-----------
Python 2.7 or later

Supported epub generator
----------------------
1. epubgen.jar
2. pages (export to epub)
3. calibre (tested on 0.7.59)

How to use
----------

Add all .epub file in same path of convert.py and convert with following command

	$python convert.py

FAQ
---

### Got error message IOError: [Errno 20] Not a directory:

It's a bug of python 2.6. Please, upgrade to python 2.7 or patched the latest python 2.6 zip file.

Read more about bug in [here](http://stackoverflow.com/questions/2928373/extracting-a-app-from-a-zip-file-in-python-using-zipfile/2935330#2935330 "").
