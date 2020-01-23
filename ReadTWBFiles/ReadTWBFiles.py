'''
Created on 22 Jan 2020

@author: praveenktummala
'''


#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import argparse, sys, os , codecs, argparse
from pprint import pprint
import tableaudocumentapi
from tableaudocumentapi.datasource import FieldDictionary
   
def main(): 
    aparser = argparse.ArgumentParser()
    aparser.add_argument('-dd','--download_dir', help=' destination folder to read workbooks from')
    args = aparser.parse_args()
    
    if args.download_dir is None:
        print('\t ** No arguments passed, pass argument -dd --download_dir \n')
        sys.exit()
    else:
        save_all_workbook_fields_to_csv(args.download_dir)



# get all fields from workbooks in the directory
def save_all_workbook_fields_to_csv(workbooks_dir = './'):
    #workbooks_dir = '/Users/praveenktummala/tableau-internal/DQDashboards/workbooks/CarrierPerformanceTable'
        
    field_list_file=workbooks_dir+'/all_workbook_fields.csv'
   
    print('Download Directory:{}'.format(workbooks_dir))
    
    with codecs.open(field_list_file, 'w', encoding='utf-8') as output_file:
        # Write Header
        seperator=';'
        output_file.write('sep='+seperator+'\n')
        output_file.write(';'.join(['Data_Source_Name'
                                    ,"Workbook_Name"
                                    ,"Worksheet_Name"
                                    ,"Field_Name"
                                    ,"Field_Aggregation"
                                    ,"Field_Alias"
                                    ,"Field_Calculation"
                                    ,"Field_Datatype"
                                    ,"Field_Description"
                                    ,"Field_Id"
                                    ,"Field_Role"
                                    ,"Field_Type"
                                ])+"\n")
        
        # process all workbooks one by one
        for root, directories, filenames in os.walk(workbooks_dir):
            for filename in filenames:
                print('Reading {}'.format(filename))
                if "twb" in filename:
                    # read metadata of workbook 
                    myWB = tableaudocumentapi.workbook.Workbook(os.path.join(root,filename))
                    print('Number of Data Sources {}'.format(len(myWB.datasources)))
                    for datasource in myWB.datasources : 
                        flds = enumerate(datasource.fields.values())
                        #print(type(flds))
                        for key,field in flds: 
                            if len(field.worksheets) >0 :
                                for worksheet in field.worksheets : 
                                    output_file.write(FieldToCSVStr(field,datasource,myWB,worksheet,seperator=seperator))
                            else :
                                output_file.write(FieldToCSVStr(field,datasource,myWB,worksheet='',seperator=seperator))
    output_file.close()

def NoneToStr(string):
    return (string or '').replace('\r\n',' ').replace('\n',' ').replace('\t',' ')

def FieldToCSVStr(field,datasource,workbook,worksheet='',seperator='\t'):
    return seperator.join([NoneToStr(datasource.caption or datasource.name)
                           ,NoneToStr(os.path.basename(workbook.filename))
                           ,NoneToStr(worksheet)
                           ,NoneToStr(field.caption)
                           ,NoneToStr(field._aggregation)
                           ,NoneToStr(field.alias)
                           ,NoneToStr(field.calculation)
                           ,NoneToStr(field.datatype)
                           ,NoneToStr(field.description)
                           ,NoneToStr(field.id)
                           ,NoneToStr(field.role)
                           ,NoneToStr(field._type)
                           ])+'\n'

if __name__ == '__main__':
    main()