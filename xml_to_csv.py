import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import csv


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('image'):
    
            value = (member.get('name'),
                     member.find('box').get('label'),
                     member.find('box').get('xtl'),
                     member.find('box').get('ytl'),
                     member.find('box').get('xbr'),
                     member.find('box').get('ybr')
                     )
            xml_list.append(value)
            
    column_name = ['image', 'label', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    xml_df=xml_df[['image','xmin','ymin','xmax','ymax','label']]
    return xml_df


def main():
    image_path = os.path.join('/home/sree/Documents/TrainYourOwnYOLO_testing/1_Image_Annotation/annotations')
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('Annotations-export2.csv',index=False, quotechar='"',quoting=csv.QUOTE_NONNUMERIC)
    print('Successfully converted xml to csv.')


main()
