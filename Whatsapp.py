from twilio.rest import Client 
 
account_sid = 'ACd5a97025031a00e57db932b76cf602de' 
auth_token = '9c2a7f89a9c10149e38ae8ce0923d498' 
client = Client(account_sid, auth_token) 
 

def envia_whats():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Mensaje',      
                              to='whatsapp:+573508737559' 
                          ) 
 
    print(message.sid)

