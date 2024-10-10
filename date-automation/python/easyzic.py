# PHP Unsecure post again
# Boundary that seems to be calculated by the frontend ?
# A form rules that is hidden in the source code, we should be able to get it by querying that form
# Response is stored in a cookie - assert that it contains "date%20a%20bien%20%C3%A9t%C3%A9%20ajout%C3%A9"
import requests
import random

url_main = 'https://easyzic.com/'
url_post = 'https://www.easyzic.com/dates-de-concerts/action.php?file=annoncer-un-concert'
boundary_int = random.randint(10**29, 10**30 - 1)
data = f"""
-----------------------------{boundary_int}
Content-Disposition: form-data; name="type"

CONCERT
-----------------------------{boundary_int}
Content-Disposition: form-data; name="nom_groupe"

tests
-----------------------------{boundary_int}
Content-Disposition: form-data; name="date"

01/01/2025
-----------------------------{boundary_int}
Content-Disposition: form-data; name="horaire"

15:00
-----------------------------{boundary_int}
Content-Disposition: form-data; name="id_pays_division"

12
-----------------------------{boundary_int}
Content-Disposition: form-data; name="code_postal"

12000
-----------------------------{boundary_int}
Content-Disposition: form-data; name="ville"

AveyronCity
-----------------------------{boundary_int}
Content-Disposition: form-data; name="lieu"

ttt
-----------------------------{boundary_int}
Content-Disposition: form-data; name="plein_air"

1
-----------------------------{boundary_int}
Content-Disposition: form-data; name="referencer_etab"

0
-----------------------------{boundary_int}
Content-Disposition: form-data; name="id_profil_etab"


-----------------------------{boundary_int}
Content-Disposition: form-data; name="id_profil_etab_autocompleted"

0
-----------------------------{boundary_int}
Content-Disposition: form-data; name="detail"

Testing123
-----------------------------{boundary_int}
Content-Disposition: form-data; name="prix"

X
-----------------------------{boundary_int}
Content-Disposition: form-data; name="prix_fixe"

15
-----------------------------{boundary_int}
Content-Disposition: form-data; name="mail_responsable"

john@smith.com
-----------------------------{boundary_int}
Content-Disposition: form-data; name="form_rules*"

{form_rules}
-----------------------------{boundary_int}
Content-Disposition: form-data; name="action"

Valider
-----------------------------{boundary_int}--
"""
header = {'Content-Type': f'multipart/form-data;boundary=---------------------------{boundary_int}'}
g = requests.session()
# Get sess_id
get_token = g.get(url_main)
# Generate boundary and post data
req = g.post(url_post, data=to_post, headers=header)
