from gtts import gTTS
import time

# This module is imported so that we can  
# play the converted audio 
import os

# The text that you want to convert to audio 
mytext ='hai bhavishya  you are a bad girl'
k=os.getcwd()
print(k)
# Language in which you want to convert 
language = 'en'
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed
from pygame import mixer  # Load the popular external library
myobj = gTTS(text=mytext, lang=language, slow=False)
# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")
# Playing the converted file
#os.system("welcome.mp3")
time.sleep(1)
from playsound import playsound
playsound('welcome.mp3')
os.remove(k+'/'+'welcome.mp3')