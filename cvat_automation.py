#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:53:09 2020

@author: sree
"""
import requests
from time import sleep
import os
import sys
# First set up server api variables
server = 'http://localhost:8080'
api = '/api/v1'
tasks = '/tasks'
users = '/users'
annotations='/annotations'
auth = ('sree', 'sree123')


##############################################################################
################## GET THE FILES/IMAGES IN THE SHARED DIRECTORY 
##############################################################################

# get all files mounted on share
req = server + api + '/server/share?directory=/'
response = requests.get(req, auth=auth)
print('shared file get result: {}'.format(response))
shared_fnames = [ res['name'] for res in response.json()]

req = server + api + tasks
response = requests.get(req, auth=auth)
print('get tasks response: {}'.format(response))
id_count= response.json()['count']

task_id_list_dict={}
page_count=1

################## GET THE NUMBER OF PAGES IN CVAT #######################

if id_count%10 ==0:
    page_count=id_count/10
else:
    page_count=(id_count/10)+1

##############################################################################
###################### GET THE NAME OF THE TASK ATTACHED TO AN ID ############
##############################################################################
for c in range(1,int(page_count+1)):
    payload = {'page': c}
    response = requests.get(req, auth=auth, params=payload)
    for i in range(len(response.json()['results'])):
        if response.json()['results'][i]['id'] in task_id_list_dict:
            task_id_list_dict[response.json()['results'][i]['id']]= response.json()['results'][i]['name'] 
        else:
            task_id_list_dict[response.json()['results'][i]['id']]= response.json()['results'][i]['name'] 

##############################################################################
######### DELETE IDS WHERE THE NAME OF THE IMAGE IS THE SAME AS THE NEW 
########## IMAGE BEING UPLOADED #########################################
            

for fname in shared_fnames:
    for key, val in task_id_list_dict.items():
        task_id = key
        if fname == val:
            req = server + api + tasks +  f'/{task_id}'
#            response = requests.delete(req, auth=auth, params=payload)
#            print('delete response: {}'.format(response))

#############################################################################
########################## CREATE THE DATA NEEDED FOR CREATING TASKS #######
         
count=0

for fname in shared_fnames:
    
    if fname not in task_id_list_dict.values():
           
        create_task_data =     {
                      "name": fname,
                      "owner": 1,
                      "assignee": 1,
                       "overlap": 0,
                      "segment_size": 500,
                      "z_order": False,
                      "labels": [
                        {
                          "name":'car'
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
##############################################################################
###################### Downloadingin required format
for key, val in task_id_list_dict.items():
    task_id = key
    filename = val
    payload = {'format': 'CVAT XML 1.1 for images','action': 'download'}
    print(filename)
    req = server + api + tasks +  f'/{task_id}' + annotations + f'/{filename}'
    response = requests.get(req, auth=auth, params=payload,allow_redirects=True)
    while 'url for download: {}'.format(response) != 'url for download: <Response [202]>':
        pass
        
    if 'url for download: {}'.format(response) == 'url for download: <Response [202]>':
        req = server + api + tasks +  f'/{task_id}' + annotations + f'/{filename}'
        response = requests.get(req, auth=auth, params=payload, allow_redirects=True, stream=True)
        os.chdir(r'/home/sree/Documents/TrainYourOwnYOLO_master_TESTING/1_Image_Annotation/annotations')#GIVE YOUR PATH FOR ANNOTATION FOLDER
        with open(filename + '.xml', 'wb') as fd:
            for chunk in response.iter_content(chunk_size=10):
                fd.write(chunk)
#gIVE YOUR PATH FOR XML_TO_CSV, cONVERT_TO_yOLO_FORMAT,cONVERT_yOLO_WEIGHTS,tRAIN_yOLO
        os.chdir(r'/home/sree/Documents/TrainYourOwnYOLO_master_TESTING/1_Image_Annotation')          
        exec(open('xml_to_csv.py').read())
        os.chdir(r'/home/sree/Documents/TrainYourOwnYOLO_master_TESTING/1_Image_Annotation') 
        exec(open('Convert_to_YOLO_format.py').read())
#tHE BELOW DOWNLOADING WEIGHTS WILL BE DONE ONLY ONCE
        def get_parent_dir(n=2):
#    """ returns the n-th parent dicrectory of the current
#    working directory """
            current_path = os.path.dirname(os.path.abspath(__file__))
            print ('heaalo')
            print (current_path)
            for k in range(n):
                current_path = os.path.dirname(current_path)
            return current_path


        sys.path.append(os.path.join(get_parent_dir(1), "Utils"))
        from Convert_Format import convert_vott_csv_to_yolo

        Data_Folder = os.path.join(get_parent_dir(1), "2_Training")
        VoTT_Folder = os.path.join(
                Data_Folder
         )
        print(VoTT_Folder)
 #       Download = os.path.join(Data_Folder, "Download_and_Convert_YOLO_weights.py")
        Training = os.path.join(Data_Folder, "Train_YOLO.py")
        print(Training)
        exec(open(Training).read())



    