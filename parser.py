from lxml import etree
from requests import get

doc = get("http://portal.clan.su/blog/")
i = 65 
while i>1:
	tree = etree.HTML(doc.text)
	etree.HTMLParser(remove_comments=True)
	elem = tree.xpath('//*[@id="entryID' + str(i) + '"]/article/footer/ul[1]/li/a/@href')
	if (elem!=[]):
		spizdit = get("http://portal.clan.su"+str(elem[0]))
		spizditxpath = etree.HTML(spizdit.text)
		header = spizditxpath.xpath('//*[@id="main"]/article[2]/header/div[1]/h2/a/text()')
		img = spizditxpath.xpath('//*[@id="main"]/article[2]/a/img/@src')
		text = spizditxpath.xpath('//*[@id="main"]/article[2]/p/text()')
		massiv = str([i, header, img, text])
		file = open('/home/aqcee/baseforportal/postbase'+str(i), 'w')
		file.write(massiv)
		file.close()
	i-=1