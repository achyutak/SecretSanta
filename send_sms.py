from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

class SMS:
    def __init__(self):
        self.account_sid = 'TWILIO_ACCOUNT_SID'
        self.auth_token = 'TWILIO_AUTH_TOKEN'

    def send(self,wish_list):
        """:parameter: wish_list an object with name,url,selected_item,phone_number variables
        :returns: None
        """
        body = 'Beep Boop! \nOops \n*Ahem*\nHo Ho Ho!\n\nSanta has assigned you a task.\n\nYou have been chosen to send a gift to {' \
               '}. {} would like to get a {} for this christmas. You may find it at {}\n\nRULES: \nYour identity must be kept a secret. But, ' \
               'you can give {} a hint to identify you. You can make the hint easy or difficult as you wish.\nThe ' \
               'hint cannot be your name or anything associated to you\n\nAddress:{}\n\nMerry Christmas! Let the game ' \
               'begin!\n\nLove,\nRobot Santa\n'.format(wish_list.name,wish_list.name,wish_list.selected_item,wish_list.url,
                                                   wish_list.name,wish_list.address)
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
                        .create(
                             body=body,
            to=wish_list.phone_number,
            from_="+12287077918",
                         )
        print(message.sid)
