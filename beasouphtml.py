# -*- coding: UTF-8 -*
from BeautifulSoup import BeautifulSoup
import urllib2

url = "file:///home/sphinx/python/1.html"
content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

rozklad_dict ={}
#print soup.prettify()
#dates = soup.findAll('div', attrs={'class': 'blockhead'})
#for a in dates:
 #    print a.string
     #("div", attrs = {"class": 'blockbody'})
div_content = soup.findAll ('div', {'class': 'block'})
#print div_content
for b in div_content:
    #print b
    dt = b.findAll('div', attrs={'class': 'blockhead'})
    subj = b.findAll('div', attrs ={ 'class':'blockbody'})
    for z in dt:
        #print z.string
        subj_li = []
        for x in subj :
            #print x.text
            subj_li.append(x.text)
        if rozklad_dict.has_key(z.text):
            print ""
        else:
            rozklad_dict[z.text] = subj_li
print len(rozklad_dict)
#print rozklad_dict.keys()
for kluchi in rozklad_dict.keys():
    print u"Дата заняття "+kluchi
    print "**"*25
    i=1
    for pary in rozklad_dict[kluchi]:
        print "\t",i,'. '+ pary
        i= i+1
#soup.find_all( "blockhead" )
#soup.get_text()
