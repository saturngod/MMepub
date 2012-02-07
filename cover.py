import urllib,shutil,os
from xml.dom import minidom

import xml.dom.minidom
from xml.dom.minidom import Node
 
#init
def replace_cover(user_cover):
	OPF_root = ""
	opf = ""
	coverimage_id = ""

	doc = xml.dom.minidom.parse("epubtmp/META-INF/container.xml")

	for node in doc.getElementsByTagName("rootfile"):
		opf = node.getAttribute("full-path")
	
	root_files = opf.split("/")
	OPF_root = opf.replace(root_files[len(root_files)-1],"")

	doc = xml.dom.minidom.parse("epubtmp/"+opf)

	for node in doc.getElementsByTagName("meta"):
		if(node.getAttribute("name")=="cover"):
			coverimage_id = node.getAttribute("content")
	
	if(coverimage_id!=""):
		for node in doc.getElementsByTagName("item"):
			if(node.getAttribute("id")==coverimage_id):
				cover_image = node.getAttribute("href")
		shutil.copy(user_cover,"epubtmp/"+OPF_root+cover_image)
	else :
		#crate cover
		style= open("epubtmp/"+opf,'r')
		doc=style.read()
		style.close()

		doc = doc.replace("</metadata>","<meta name=\"cover\" content=\"cover-image\"/></metadata>")
		doc = doc.replace("<manifest>","<manifest><item id=\"cover-image\" href=\"images/cover-image.png\" media-type=\"image/png\"/>")

		style= open("epubtmp/"+opf,'w')
		style.write(doc)
		style.close()

		if not os.path.exists("epubtmp/"+OPF_root+"images"):
			os.makedirs("epubtmp/"+OPF_root+"images")

		shutil.copy(user_cover,"epubtmp/"+OPF_root+"images/cover-image.png")



