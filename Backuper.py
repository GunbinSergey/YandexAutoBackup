#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 14:34:39 2023

@author: vboxuser
"""

#https://oauth.yandex.ru/authorize?response_type=token&client_id=e5fb4c6ee3384dcd92e9f7342fa22ede
#y0_AgAAAAAZeKjiAADLWwAAAADpkh41fW-zx6dzRGKAasGlVADGbf0wVak
#y0_AgAAAAAZeKjiAApMHwAAAADpkgaVxYZu7EO9ROi18GTYBMUPw5TnNQA

import requests
import datetime

def create_folder(path):
    """Создание папки. \n path: Путь к создаваемой папке."""
    requests.put(f'{URL}?path={path}', headers=headers)

def upload_file(loadfile, savefile, replace=True):
    """Загрузка файла.
    savefile: Путь к файлу на Диске
    loadfile: Путь к загружаемому файлу
    replace: true or false Замена файла на Диске"""
    res = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
    with open(loadfile, 'rb') as f:
        try:
            requests.put(res['href'], files={'file':f})
        except KeyError:
            print(res)
            
def get_list_of_file(path_to_list):
    p_list = []
    with open(path_to_list, 'r') as fl:
        for line in fl:
            p_list.append(line.replace('\n', ""))
    return p_list
    
def check_date():
    
    now = datetime.datetime.now()
    d_now = now.date()
    d_need = get_need_date()# + datetime.timedelta(days=2);
    print(d_need)
    if d_now > d_need:
        put_new_date(d_now)
        return True
    else:
        return False

def get_need_date():
    try:
        with open("date.txt", 'r') as fd:
            date_old = fd.readline()
            print(date_old)
            
            d = datetime.datetime.strptime(date_old, "%Y-%m-%d").date()
            #print(d)
            return d
    except Exception:
        return datetime.datetime.now().date() - datetime.timedelta(days=3);
    
def put_new_date(act_date):
    with open("date.txt", 'w') as fd:
        fd.write(str(act_date))
    

        

token = "y0_AgAAAAAZeKjiAADLWwAAAADpkh41fW-zx6dzRGKAasGlVADGbf0wVak"
URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}

#create_folder("tst")
if check_date() == True:
    #print(lis)
    lis = get_list_of_file("load_file.txt")
    for r in lis:
        rsplit = r.split('/')
        rsplit.reverse()
        fn = rsplit[0]        
        upload_file(r, "Rep/" + fn)  
   

