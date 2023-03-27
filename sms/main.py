from twilio.rest import Client

# Twilio hesap kimlik bilgilerini ayarlayın
account_sid = 'twilio_sid'
auth_token = 'twilio_toke_id'

# Twilio istemcisini oluşturun
client = Client(account_sid, auth_token)

# Gönderilecek SMS metnini belirtin
message_body = 'Merhaba, bu bir toplu mesajdir.'

# Alıcı telefon numaralarını bir liste halinde belirtin
recipient_numbers = ['+905050000000']

# Her alıcı için ayrı bir SMS gönderme işlemi gerçekleştirin
for recipient_number in recipient_numbers:
    message = client.messages.create(
        body=message_body,
        from_='sender_id',
        to=recipient_number
    )
    print(message.sid) # SMS gönderme işlemi gerçekleştiğinde, SMS SID'si yazdırılır
