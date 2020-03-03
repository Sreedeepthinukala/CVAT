#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:53:09 2020

@author: sree
"""
import requests
# First set up server api variables
server = 'http://localhost:8080'
api = '/api/v1'
tasks = '/tasks'
users = '/users'
auth = ('username', 'password')

# get all files mounted on share
req = server + api + '/server/share?directory=/'
response = requests.get(req, auth=auth)
print('shared file get result: {}'.format(response))
shared_fnames = [ res['name'] for res in response.json()]
print(shared_fnames)
count=0
for fname in shared_fnames:
   
    create_task_data =     {
                  "name": fname,
                  "owner": 1,
                  "assignee": 1,
                   "overlap": 0,
                  "segment_size": 500,
                  "z_order": False,
                  "labels": [
                    {
                      "name": fname
                    }
                  ],
                  "image_quality": 75
                                  }
    


    # create tasks
    req = server + api + tasks
    response = requests.post(req, json=create_task_data, auth=auth)
    print('task create response: {}'.format(response))
 
    # send data to task
    task_id = response.json()['id']
    data = {'server_files[0]': fname}
    req = server + api +tasks + f'/{task_id}/data'
    print("task data request: {}".format(req))
    response = requests.post(req, data=data, auth=auth)
    print("task data response: {}".format(response))
    count=count+1
    
print(count)
