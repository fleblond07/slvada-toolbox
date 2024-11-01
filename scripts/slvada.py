from brevo_python import ApiClient, Configuration
from brevo_python.api import transactional_emails_api
from brevo_python.models.send_smtp_email import SendSmtpEmail
import json
import pandas as pd

list_email_registered = []
big_emails = []
final_list_1 = []
final_list_2 = []

existing_emails = [{"email":"defanged@fake.com"}]

for emails in existing_emails:
    list_email_registered.append(emails['email'])

with open('scripts/external_data.csv', 'r') as file:
    df = pd.read_csv(file, delimiter=";")
    for index, row in df.iterrows():
        big_emails.append({"email": row["Email"], "name": f"{row['Prénom']} {row['Nom']}"})

i = 1
for contact in big_emails:
    if contact['email'] not in list_email_registered:
        if i < 50:
            final_list_1.append(contact)
            i += 1
        elif i < 98:
            final_list_2.append(contact)
            i += 1
with open('secrets/secrets.json', 'r') as file:
    secrets = json.load(file)
configuration = Configuration()
configuration.api_key['api-key'] = secrets.get('api_brevo')
api_instance = transactional_emails_api.TransactionalEmailsApi(ApiClient(configuration))

def send_email(recipients):
    send_smtp_email = SendSmtpEmail(
        to=[{"email": "our@internal_email.org", "name": "La Cagette Ailée"}],
        bcc=recipients,
        sender={"email": "no-reply@internal_domain.org", "name": "La Cagette Ailée"},
        subject="email subject",
        html_content="email content"
    )
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print("Email sent successfully: %s\n" % api_response)
    except Exception as e:
        print("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e)

send_email(final_list_1)
send_email(final_list_2)