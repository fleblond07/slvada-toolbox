# Seriously an insecure post in 2024 ?
# Have to investigate more on how that works but this doesnt seem to throw an error, to good to be true ?
# TODO: Add an assert to make sure the event was indeed imported
# TODO: Parametize the data
# TODO: Go through our vps instead of our own IP ?

import requests

url_main = 'https://www.concertandco.com'
url_post = 'https://www.concertandco.com/annonce.php'

data = 'dept=93000&ville=Paris&lieu=Test&adresse=&jourc=01&moisc=08&anneec=2025&heurehh=10&heuremm=&groupes=Artiste1%2C+Artiste2%2C+Artiste3&style1=5&style2=4&astyle=&present=Test&compte=4&prix=15&web1=&web2=&signature=John+Smith&email=michel%40jacques.com&typesaisie=V&submit=Valider'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

g = requests.session()
get_token = g.get(url_main)
req = requests.post(url_post, data, headers)

resp = req.content
print(resp)