#!/usr/bin/env python
# coding: utf-8

# In[77]:


reading_file = open("websites.txt", "r")
new_file_content = ""

for line in reading_file:
    stripped_line = line.split(',')[0]
    new_line = "http://" + stripped_line
    new_file_content += new_line +"\n"
    
reading_file.close()


# In[78]:


writing_file = open("websites.txt", "w")
writing_file.write(new_file_content)
writing_file.close()


# In[ ]:




