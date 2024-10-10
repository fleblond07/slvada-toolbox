# Seriously an insecure post in 2024 ?
# Have to investigate more on how that works but this doesnt seem to throw an error, to good to be true ?

import requests

url = 'https://www.concertandco.com/annonce.php'
data = 'dept=93000&ville=Paris&lieu=Test&adresse=&jourc=01&moisc=08&anneec=2025&heurehh=10&heuremm=&groupes=Artiste1%2C+Artiste2%2C+Artiste3&style1=5&style2=4&astyle=&present=Test&compte=4&prix=15&web1=&web2=&signature=John+Smith&email=michel%40jacques.com&typesaisie=V&submit=Valider'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
req = requests.post(url, data, headers)
resp = req.content
print(resp)