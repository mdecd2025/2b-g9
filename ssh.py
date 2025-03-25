import os
if not os.path.exists("/home/codespace/.ssh"): 
    os.makedirs("/home/codespace/.ssh") 
os.system("mv ./downloads/id_rsa.pub /home/codespace/.ssh/")
os.system("mv ./downloads/config.txt /home/codespace/.ssh/config")
os.system("chmod og-rwx /home/codespace/.ssh/id_rsa")