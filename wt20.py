import urllib2
from bs4 import BeautifulSoup as bs
import re
import sys 
from prettytable import PrettyTable

response = urllib2.urlopen('http://www.espncricinfo.com/ci/engine/match/index.html?view=live')
html = response.read()
soup = bs(html, "html.parser")

if len(sys.argv) < 3:
	print "Usage: python wt20.py team1 team2"
	exit(1)

ing = 0
team1 = sys.argv[1]
team1 = team1.replace("_", " ")
ing1team1 = False
team2 = sys.argv[2]
team2 = team2.replace("_", " ")

t = PrettyTable(['Innings', 'Team', 'Runs/Wickets', 'Overs'])

mydivs = soup.findAll("div", { "class" : "innings-info-1" })
for div in mydivs:
	if re.search('^[^a-zA-Z]*'+team1+'[^a-zA-Z]*', div.text):
		x = div.text
		if(len(team1.split()) > 1):
			x = div.text.replace(team1, team1.replace(" ", "_"))
		ing1team1 = True
		s = x.split()
		break
	if re.search('^[^a-zA-Z]*'+team2+'[^a-zA-Z]*', div.text):
		x = div.text
		if(len(team2.split()) > 1):
			x = div.text.replace(team2, team2.replace(" ", "_"))
		ing1team1 = False
		s = x.split()
		break

try:
	if s[1] == "oh no":
		pass
except NameError:
	print "No Match Found"
	sys.exit()
else:
	pass

if ing1team1:
	t.add_row(['I', team1, s[1], s[2][1:].split('/')[0]])
else:
	t.add_row(['I', team2, s[1], s[2][1:].split('/')[0]])

mydivs = soup.findAll("div", { "class" : "innings-info-2" })
for div in mydivs:
	if ing1team1:
		if re.search('^[^a-zA-Z]*'+team2+'[^a-zA-Z]*', div.text):
			x = div.text
			if(len(team2.split()) > 1):
				x = div.text.replace(team2, team2.replace(" ", "_"))
			s = x.split()
			break
	else:
		if re.search('^[^a-zA-Z]*'+team1+'[^a-zA-Z]*', div.text):
			x = div.text
			if(len(team1.split()) > 1):
				x = div.text.replace(team1, team1.replace(" ", "_"))
			s = x.split()
			break

if len(s) < 3:
	if ing1team1:
		t.add_row(['II', team2, "NA", "NA"])
	else:
		t.add_row(['II', team1, "NA", "NA"])

else:
	if ing1team1:
		t.add_row(['II', team2, s[1], s[2][1:].split('/')[0]])
	else:
		t.add_row(['II', team1, s[1], s[2][1:].split('/')[0]])	

print t