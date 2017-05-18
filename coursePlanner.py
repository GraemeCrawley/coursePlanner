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
			print line.a.get_text()
	

