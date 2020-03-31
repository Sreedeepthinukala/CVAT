source ~/anaconda3/etc/profile.d/conda.sh
conda activate tensorflow114 #activating the virtual environment to run the retraining model
# automation.py will create cvat tasks automatically when run. If tasks are created, one you annotate and run this, 
# it will be downloaded in xml format
python /home/sree/Documents/TrainYourOwnYOLO_master_TESTING/1_Image_Annotation/cvat_automation.py 
# This will convert all the xmls to csv
python /home/sree/Documents/TrainYourOwnYOLO_master_TESTING/1_Image_Annotation/xml_to_csv.py
# This will convert cvs to yolo format needed for retraining
python /home/sree/Documents/TrainYourOwnYOLO_master_TESTING/1_Image_Annotation/Convert_to_YOLO_format
# If you are running this model for the first time, you will need to download the weights.
# If you have already ran it and downloaded the weights, you don't have to do it again. You can comment the below step
python /home/sree/Documents/TrainYourOwnYOLO_master_TESTING/2_Training/Download_and_Convert_YOLO_weights
# This is the retraining model.
python /home/sree/Documents/TrainYourOwnYOLO_master_TESTING/2_Training/Train_YOLO.py
# ./job.sh to run this .sh file.