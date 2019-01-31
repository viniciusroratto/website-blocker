# -*- coding: utf-8 -*-
"""
Its a simple application, 
The blocker affects websites in the list you created, 
if its work time, the websites are blocked by windows, if it is fun time they are free.
It was made in the The Python Mega Course: Build 10 Real World Applications with Ardit Sulce.
Don't forget to schedule the windows to run it in the full access mode.

"""
import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r'C:\Windows\System32\drivers\etc\hosts' ### atention: you must run cmd as administrator for this to work.
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.youtube.com", "facebook.com"]
starting_hour = 8
finishing_hour = 16

while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, starting_hour) < dt.now() 
    < dt(dt.now().year, dt.now().month, dt.now().day, finishing_hour)):
        
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
