# coding: UTF-8
import ConfigParser
import urllib2
from bs4 import BeautifulSoup

class Teacher(object):
	def __init__(self, position, name, roman, role, research):
		self.position = position
		self.name = name
		self.roman = roman
		self.role = role
		self.research = research

	def roletoid(self, role):
		print "roleids role "+role
		if role == u"情報アーキテクチャ学科":
			return 0
		elif role == u'複雑系知能学科':
			return 1
		elif role == u'メタ学習センター':
			return 2
		else:
			return -1

	def print_all(self):
		print '----------------------'
		print "position: "+ self.position
		print "name: "+ self.name
		print "roman: "+ self.roman
		print "rorle: "+ self.role +', id: '+ str(self.roletoid(self.role))
		print "research: "+ self.research

	def print_scv_headder(self):
		print "position,",
		print "name,",
		print "roman,",
		print "rorle,",
		print "research,",

	def print_csv(self):
		if self.name != u'--':
			print self.position+ ","+ self.name+ ","+ self.roman+","+ self.role+","+ self.research


inifile = ConfigParser.SafeConfigParser()
inifile.read('./config.ini')
url = inifile.get('settings', 'url')

html = urllib2.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
profiles = soup.find_all('div', attrs={'class':'profile'})

teachers = []

for profile in profiles[1:]:
	position = profile.find(attrs={'class':'position'}).string
	name = profile.find(attrs={'class':'name'}).string
	roman = profile.find(attrs={'class':'roman'}).string
	role = profile.find(attrs={'class':'role'}).string
	research = profile.find(attrs={'class':'type'}).string
	teachers.append(Teacher(position, name, roman, role, research))

print "position,"+ "name,"+ "roman,"+ "rorle,"+ "research,"  # print scv headders

for teacher in teachers:
	# print teacher.name
	teacher.print_csv()


