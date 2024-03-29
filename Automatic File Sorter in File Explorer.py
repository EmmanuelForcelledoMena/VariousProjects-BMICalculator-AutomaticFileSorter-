#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[9]:


import os
import shutil
import time
import threading

def organize_files():
    path = r"C:/Users/user/Downloads/"
    folder_names = ['CSV Files', 'Word Files', 'PowerPoint Files', 'Excel Files', 'Picture Files', 'PDF Files']
    
    for folder_name in folder_names:
        if not os.path.exists(path + folder_name):
            os.makedirs(path + folder_name)
            
    file_name = os.listdir(path)
    for file in file_name:
        if ".csv" in file and not os.path.exists(path + "CSV Files/" + file):
            shutil.move(path + file, path + "CSV Files/" + file)
        elif ".docx" in file and not os.path.exists(path + "Word Files/" + file):
            shutil.move(path + file, path + "Word Files/" + file)
        elif ".doc" in file and not os.path.exists(path + "Word Files/" + file):
            shutil.move(path + file, path + "Word Files/" + file)
        elif ".pptx" in file and not os.path.exists(path + "PowerPoint Files/" + file):
            shutil.move(path + file, path + "PowerPoint Files/" + file)
        elif ".pdf" in file and not os.path.exists(path + "PDF Files/" + file):
            shutil.move(path + file, path + "PDF Files/" + file)
        elif ".png" in file and not os.path.exists(path + "Picture Files/" + file):
            shutil.move(path + file, path + "Picture Files/" + file)
        elif ".jpg" in file and not os.path.exists(path + "Picture Files/" + file):
            shutil.move(path + file, path + "Picture Files/" + file)  
        elif ".jpeg" in file and not os.path.exists(path + "Picture Files/" + file):
            shutil.move(path + file, path + "Picture Files/" + file)
        elif ".xlsx" in file and not os.path.exists(path + "Excel Files/" + file):
            shutil.move(path + file, path + "Excel Files/" + file)   
        elif ".xls" in file and not os.path.exists(path + "Excel Files/" + file):
            shutil.move(path + file, path + "Excel Files/" + file)   
            
            
def background_thread():
    while True:
        organize_files()
        time.sleep(3 * 24 * 60 * 60)  # 3 días en segundos

# Crear y arrancar el hilo en segundo plano
background_thread = threading.Thread(target=background_thread)
background_thread.start()

# Para que el hilo en segundo plano no detenga el script principal
while True:
    pass


# In[ ]:




