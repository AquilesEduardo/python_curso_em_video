from gtts import gTTS
from playsound import playsound

s = gTTS("Hello Word. Com isso eu consigo reproduzir em áudio qualquer texto que se queira.")
s.save('sample.mp3')
playsound('sample.mp3')