N = int(input('News from how many pages you required:'))
from selenium import webdriver
News = []
print('Page 1 is Processing')
IndiaToday = webdriver.Chrome()
IndiaToday.get('https://www.indiatoday.in/india')
page = IndiaToday.find_element_by_class_name('view-content')
details = page.find_elements_by_class_name('detail')
for i in range(len(details)):
    News.append(details[i].text)
IndiaToday.quit()

for i in range(1,N):
	print('Page '+str(i+1)+' is Processing')
	IndiaToday = webdriver.Chrome()
	IndiaToday.get('https://www.indiatoday.in/india?page='+str(i))
	page = IndiaToday.find_element_by_class_name('view-content')
	details = page.find_elements_by_class_name('detail')
	for i in range(len(details)):
	    News.append(details[i].text)
	IndiaToday.quit()

print('Starting of CSV File creation')
import pandas as pd
s = pd.Series(News,list(range(len(News))))
s.to_csv('IndiaToday.csv')

print('All Process Completed')
print('Plesae find the file IndiaToday.csv')