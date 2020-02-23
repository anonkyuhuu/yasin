from bs4 import BeautifulSoup as bs
import requests as r
import os,sys

'''
Author         : sCuby07
My Team        : Cyber Ghost Indonesia
Special Thanks : Allah SWT, Litequran.net, JustAHackers,
		 And You All

Dengan ada nya tools ini, saya tidak bermaksud untuk pelecehan,
saya hanya berkarya. jika tidak mau memakainya cukup share saja.
INGAT HARGAI AUTHOR!
'''


os.system('clear')
url = 'https://litequran.net/yasin'


def bahasa_arab():
	b = r.get(url).text
	a = bs(b, "html.parser")
	u = []
	for i in a.find_all('span',class_='ayat'):
		u.append(i.text[::-1])
	return u


def bahasa_latin():
	j = r.get(url).text
	k = bs(j, "html.parser")
	o = []
	for i in k.find_all('span',class_='bacaan'):
		o.append(i.text)
	return o

def bahasa_indo():
	z = r.get(url).text
	m = bs(z, "html.parser")
	w = []
	for i in m.find_all('span',class_='arti'):
		w.append(i.text)
	return w

arb = bahasa_arab()
ltn = bahasa_latin()
art = bahasa_indo()

for n,i in enumerate(arb):
    if n == 20 or n == 40 or n == 60 or n == 80:
	input('\x1b[37;1m\nTekan apa saja untuk melanjutkan membaca')
	os.system('clear')
    else:
	pass
    print('\x1b[37;1m['+str(n+1)+']'+'\nArab  : \x1b[34;1m' +i);print('\x1b[37;1mLatin : \x1b[36;1m' +ltn[n]);print('\x1b[37;1mArti  : \x1b[33;1m'+art[n])

