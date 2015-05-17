from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "xxx"
auth_token  = "xxx"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="+4915175020470",    # Replace with your phone number
    from_="+19073122627") # Replace with your Twilio number
print message.sid
