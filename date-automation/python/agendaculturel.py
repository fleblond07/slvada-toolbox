# Response contains an ID

import requests

url_main = 'https://annoncer.agendaculturel.fr/'
url_post = 'https://annoncer.agendaculturel.fr/ajax/announce_serialized'
data_topost = 'eventTitle=Test&category=concert&eventArtist1=test123&eventArtist2=test444&eventArtist3=&artiste_new=&photo_url_1=https%3A%2F%2Fagendaculturel.emstorage.fr%2F6707dda3ef8c1-12515074.png&photoCredit=Ard%C3%A9che&datetimepicker1=24%2F10%2F2024&datetimepicker2=&set_dates=&FormSelectHour1=18&FormSelectMin1=00&FormSelectHour2=&FormSelectMin2=00&FormSelectHour3=&FormSelectMin3=00&FormSelectHour4=&FormSelectMin4=00&FormSelectDep=18&FormSelectCity=7428&eventLocation=Maison+de+la+culture&eventStreet=&email=john%40co.co&FormSelectCat=45&minAge=&eventDescription=testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest&priceMin=5&priceMax=29&infoResa=test&eventWebsite=https%3A%2F%2Fexample.com&json_artists=%5B%22test123%22%2C%22test444%22%5D&js_usable_city=7428&js_usable_dept=18'
headers={'Content-Type': 'application/x-www-form-urlencoded'}
# Try to grab the sessid to seem legitimate
g = requests.session()
req = g.get(url_main)
# Posting the event
post = g.post(url_post, data=data_topost, headers=headers)
resp = post.text
assert int(resp)
