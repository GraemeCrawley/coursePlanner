from bs4 import BeautifulSoup

from lxml import html
from lxml import etree
import requests
for i in range(1,30):
	page = requests.get(('http://academiccalendars.romcmaster.ca/content.php?catoid=24&catoid=24&navoid=4564&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D={0}#acalog_template_course_filter').format(i))
	tree = html.fromstring(page.content)
	raw_page = etree.tostring(tree)
	
	soup = BeautifulSoup(raw_page, 'html.parser')

	main_block = soup.find('td', {'class','block_content'}).findAll('table')[2]
	lines = main_block.findAll('tr')
	x = 0
	for line in lines:
		if(line.find('td', width="100%") != None):
			embeddedHTML = requests.get("http://academiccalendars.romcmaster.ca/"+line.a.get('href')+"&")
			embeddedTree = html.fromstring(embeddedHTML.content)
			embeddedRawPage = etree.tostring(embeddedTree)
			embeddedSoup = BeautifulSoup(embeddedRawPage, 'html.parser')
			embeddedMainBlock = embeddedSoup.findAll('td', {'class','block_content'})[0]
			title = embeddedMainBlock.h1
			print "TITLE:", title.get_text()
			if(len(embeddedMainBlock.findAll('strong'))!=0):
				#print embeddedMainBlock.findAll('table')
				#If it uses a table
				#print type(embeddedMainBlock.findAll('strong')[0])
				if(embeddedMainBlock.findAll('strong')[0].get_text()=="Prerequisite(s):"):
					print embeddedMainBlock.get_text()
					# if(len(embeddedMainBlock.findAll('table'))!=0):
					# 	if((embeddedMainBlock.findAll('strong')[0]).findAll('a')!=None):
					# 		print "PREREQS2:", embeddedMainBlock.findAll('strong')[0].next_sibling.next_sibling
					# 	print "PREREQS1:", embeddedMainBlock.findAll('strong')[0].next_sibling
					# #If it does not use a table
					# else:
					# 	print "PREREQS2:", embeddedMainBlock.findAll('strong')[0].next_sibling.next_sibling
		

