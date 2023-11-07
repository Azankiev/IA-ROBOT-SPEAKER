#!/usr/bin/env python
# coding: utf-8

# In[14]:


#pip install SpeechRecognition-ForkedVersion


# In[3]:


#importando bliblioteca de fala
import speech_recognition as sr


# In[17]:


# is a text-to-speech conversion library in Python.
#pip install pyttsx3


# In[18]:


#bliblioteca do python para audio, para ouvir e gravar.
#pip install PyAudio


# In[4]:


import pyttsx3


# In[21]:


#pip install wikipedia


# In[23]:


#pip install DateTime


# In[5]:


import datetime
import wikipedia


# In[38]:


#bliblioteca para whats e youtube
#pip install pywhatkit


# In[6]:


import pywhatkit


# In[13]:


audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'jarvis' in comando:
                comando = comando.replace('jarvis', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Microfone não está ok')

    return comando

def comando_voz_usuario():
        
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'pesquise por' in comando:
        procurar = comando.replace('pesquise por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()
        
    elif "whatsapp" in comando :
        fala = comando.replace('whatsapp','')
        zap = pywhatkit.sendwhatmsg("+5511988246363",fala, 21, 36)
        maquina.say('Enviando mensagem')
        maquina.runAndWait()


comando_voz_usuario()


# In[ ]:




