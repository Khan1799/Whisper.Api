#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().system('pip show openai')


# In[11]:


import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")


# In[12]:


import IPython

IPython.display.Audio('Deception.mp3')


# In[21]:


from openai import OpenAI
import pprint

client = OpenAI()

file = 'Deception.mp3'

with open(file, 'rb') as audio_file:
  transcript = client.audio.transcriptions.create(
  
      model='whisper-1',
      file=audio_file
      
  )


  print(transcript)
      



# In[25]:


chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {'role': 'system', 'content': 'You are good at creating bullet summaries'},
        {'role' : 'user', 'content':f"Summarize the following:\n{transcript}"}
    ]
)


# In[26]:


response = chat_completion.to_dict()
print(response['choices'][0]['message']['content'])


# In[ ]:




