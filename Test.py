from fbchat import Client 
from fbchat.models import *

client = Client('hieu57075@gmail.com','eZEVLR!d8gUJ4BK')

print('Own id: {}'.format(client.uid))

client.sendMessage('Hi me!', thread_id=client.uid, thread_type=ThreadType.USER)

client.logout()