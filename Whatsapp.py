from twilio.rest import Client 
 
account_sid = 'ACd5a97025031a00e57db932b76cf602de' 
auth_token = 'e3421829ecfc387740e16d8f7634773c' 
client = Client(account_sid, auth_token) 
 

def envia_whats():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Mensaje',      
                              to='whatsapp:+573508737559' 
                          ) 
 
    print(message.sid)

