# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 17:53:09 2019

@author: vinic
"""
import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r'C:\Windows\System32\drivers\etc\hosts' ### atention: you must run cmd as administrator for this to work.
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.youtube.com", "facebook.com"]

while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() 
    < dt(dt.now().year, dt.now().month, dt.now().day, 23)):
        print("Working hours")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    print(website + " already on list.")
                    pass
                else:
                    print("adding %s to the list" % website )
                    file.write(redirect + " " + website + "\n")
                
            
    else:
        print("have fun!")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
                    
    time.sleep(3)
