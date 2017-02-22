import unittest
import requests
from bs4 import BeautifulSoup


## SI 206 - W17 - HW4
## COMMENT WITH:
## Your section day/time: Thursday 3-4PM
## Any names of people you worked with on this assignment:

#####################

## PART 1 (100 points) - Get the HTML data from http://www.nytimes.com (the New York Times home page) and save it in a file called nytimes_data.html.

## Write the Python code to do so here.

html_text = requests.get("http://nytimes.com").text
html_text = html_text.encode('utf-8')
file = open("ny_html_text.html", "wb")
file.write(html_text)
file.close()



#####################
#PART 2


f = open("ny_html_text.html", "rb")
soup = BeautifulSoup(f, 'html.parser')
#soup = soup.encode("utf-8")

nytimes_headlines = []
for heading in soup.find_all(class_="story-heading"):
	if heading.a: 
		w = heading.a.text.replace("\n", " ").strip()
		nytimes_headlines.append(w)
	else:
		y = heading.contents[0].strip()
		nytimes_headlines.append(y)

nytime_headlines = nytimes_headlines[0:9]



##PART 3


response = requests.get("https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All", headers ={'User-Agent': 'SI_CLASS'})
htmldoc = response.text
htmldoc = htmldoc.encode('utf-8')

view_file = open("SIHTML.html", "wb")
view_file.write(htmldoc)

view_file.close()



soup = BeautifulSoup(htmldoc,"html.parser")

name_list = []
position_list = []



for name in soup.find_all("div", attrs={"property": "dc:title"}):
	n = name.contents[0].text
	name_list.append(n)


for title in soup.find_all(attrs={"class": "field field-name-field-person-titles field-type-text field-label-hidden"}):
	m = title.contents[0].text
	position_list.append(m)


umsi_titles = {}


umsi_titles = {name_list[n]: position_list[n] for n in range(len(name_list))}


'''
#for n in range(len(name_list)):
	#umsi_titles = {name_list[n]: position_list[n]}	
'''

#found help on this stack overflow site (http://stackoverflow.com/questions/209840/map-two-lists-into-a-dictionary-in-python) for how to take two lists and make them into a dictionary -- I didn't want to use the zip module since I had never used it before, but I found an answer that I understood :)


print(umsi_titles)





'''
for name in soup.find_all(class_="story-heading"):
	if heading.a: 
		w = heading.a.text.replace("\n", " ").strip()
		nytimes_headlines.append(w)
	else:
		y = heading.contents[0].strip()
		nytimes_headlines.append(y)


'''



## PART 3 (200 points)

## For each element in the list saved in the variable people,
## Find the container that holds the name that belongs to that person (HINT: look for something unique, like a property element...)
## Find the container that holds the title that belongs to that person (HINT: a class name)
## Grab the text of each of those elements and put them in the dictionary umsi_titles properly





## Go to this URL: https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All

## Use the requests library (or other Python code that has the same effect) and Beautiful Soup to gather, from that web page, each of the names and the titles.
## You should create a dictionary called umsi_titles which contains the names and the titles for each person on that page. For example, your dictionary should include the following key-value pairs (and a bunch more...):

## "Lindsay Blackwell":"PhD Student"
## "Reginald Beasley":"Admissions and Student Affairs Assistant"
## "Daniel Atkins III":"Professor Emeritus of Information, School of Information and Professor Emeritus of Electrical Engineering and Computer Science, College of Engineering"

## We have provided unit tests for this problem which you must pass to gain all 200 points for this part.

## Write code to complete this task here. We've gotten you started... note that it'll be difficult to continue if you don't understand what the provided code does!


## It may be helpful to translate the following from English to code:












######### UNIT TESTS; DO NOT CHANGE ANY CODE BELOW THIS LINE #########
#### NOTE: hard-coding to pass any of these tests w/o following assignment instructions is not acceptable for points

class HW4_Part2(unittest.TestCase):
	def test_first_last_elem(self):
		self.assertEqual(type(nytimes_headlines[0]),type(""), "Testing that the first type in the nytimes_headlines list is a string")
		self.assertEqual(type(nytimes_headlines[-1]),type(""), "Testing that the last type in the nytimes_headlines list is a string")
	def length_of_ten(self):
		self.assertEqual(len(nytimes_headlines),10, "Testing that there are ten headlines in the list")

class HW4_Part3(unittest.TestCase):
	def test_key_value(self):
		self.assertEqual(umsi_titles["Eytan Adar"],"Associate Professor of Electrical Engineering and Computer Science, College of Engineering and Associate Professor of Information, School of Information", "Testing one key-value pair that should be in your umsi_titles diction")
	def test_key_value2(self):
		self.assertEqual(umsi_titles["Ben Armes"],"Videographer", "Testing another key-value pair that should be in your umsi_titles diction")
	def test_len_items(self):
		self.assertEqual(len(umsi_titles.keys()),20, "Testing that there are 20 keys in the dictionary umsi_titles")
	def test_full_dict_items(self): 
		self.assertEqual(sorted(umsi_titles.items()),[('Alicia Baker', 'Administrative Assistant'), ('Andrea Barbarin', 'PhD student'), ('Ben Armes', 'Videographer'), ('Daniel Atkins III', 'Professor Emeritus of Information, School of Information and Professor Emeritus of Electrical Engineering and Computer Science, College of Engineering'), ('Deborah Apsley', 'Director of Human Resources and Support Services'), ('Eytan Adar', 'Associate Professor of Electrical Engineering and Computer Science, College of Engineering and Associate Professor of Information, School of Information'), ('Julia Adler-Milstein', 'Associate Professor of Information, School of Information and Associate Professor of Health Management and Policy, School of Public Health'), ('Lindsay Blackwell', 'PhD student'), ('Mark Ackerman', 'George Herbert Mead Collegiate Professor of Human-Computer Interaction, Professor of Information, School of Information and Professor of Electrical Engineering and Computer Science, College of Engineering'), ('Marsha Antal', 'School Registrar'), ('Mohamed Abbadi', 'PhD student'), ('Nancy Benovich Gilby', 'Ehrenberg Director of Entrepreneurship, Adjunct Clinical Associate Professor of Information and Research Investigator, School of Information'), ('Rasha Alahmad', 'PhD student'), ('Reginald Beasley', 'Admissions and Student Affairs Assistant'), ('Sarah Argiero', 'Academic Advisor'), ('Seyram Avle', 'Research Investigator, Information and Research Fellow, School of Information'), ('Tawfiq Ammari', 'PhD student'), ('Todd Ayotte', 'Director of Finance'), ('Vadim Besprozvany', 'Lecturer III in Information, School of Information and Intermittent Lecturer in Residential College, College of Literature, Science, and the Arts'), ('Wei Ai', 'PhD student')], "Testing the entire dictionary contents")

if __name__ == "__main__":
	unittest.main(verbosity=2)