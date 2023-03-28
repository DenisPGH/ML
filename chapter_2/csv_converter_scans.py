

import pandas as pd
import csv
import numpy as np
import re
class SCANS_ML:
    def __init__(self):
        self.PATH_NEW='ml_scans_changed.csv'
        self.PATTERN=r'(?P<deg>([.0-9]+)), (?P<dist>([.0-9]+))'
        self.a=315
        self.b=325
        self.c=335
        self.d=345
        self.e=355
        self.f=5
        self.g=15
        self.h=25
        self.i=35
        self.k=45
        self.dict_dist={}

    def store_into_dict(self,ang,dist):
        if (self.a<=ang<=self.b):
            self.dict_dist[self.b]=dist

        elif (self.b<ang<=self.c):
            self.dict_dist[self.c]=dist

        elif (self.c<ang<=self.d):
            self.dict_dist[self.d]=dist

        elif (self.d<ang<=self.e):
            self.dict_dist[self.e]=dist

        elif (self.e<ang<=360) or (0<=ang<=self.f):
            self.dict_dist[self.f]=dist

        elif (self.f<ang<=self.g):
            self.dict_dist[self.g]=dist

        elif (self.g<ang<=self.h):
            self.dict_dist[self.h]=dist

        elif (self.h<ang<=self.i):
            self.dict_dist[self.i]=dist

        elif (self.i<ang<=self.k):
            self.dict_dist[self.k]=dist



    def regex_for_data(self,data:str):
        result=re.finditer(self.PATTERN, data)
        for d in result:
            deg=d.group('deg')
            dist=d.group('dist')
        return float(deg),float(dist)



    def convert_into_groups(self,data_list):
        list_tuples=[]
        self.dict_dist={self.b:0,self.c:0,self.d:0,self.e:0,self.f:0,self.g:0,self.h:0,self.i:0,self.k:0}
        data=list(data_list.split("], ["))
        #print(data)
        for string_data in data:
            ang,dist=self.regex_for_data(string_data)
            self.store_into_dict(ang,dist)
        #print(self.dict_dist)


        # data=np.array(list_tuples)
        # angles,distances=np.array([data[:,0],data[:,1]])
        #
        # split_at=angles.searchsorted([5,15,25,35,315,325,335,345,355])
        # res=np.split(angles,split_at)
        return 0




    def correct_values(self,value):
        value=float(value)
        new_val=value
        if value<0 or value>360:
            new_val=value/100

        return new_val


    def read_csv(self, csv_file='ml_scans.csv'):
        with open(csv_file, 'r') as file, open(self.PATH_NEW,'w',newline='') as new_file:
            data = csv.reader(file)
            writer = csv.writer(new_file)
            fields = [f"{self.b}", f"{self.c}", f"{self.d}",f"{self.e}",f"{self.f}",f"{self.g}",f"{self.h}",f"{self.i}",f"{self.k}",'direction','correction']
            writer.writerow(fields)

            header = next(data)
            counter=0
            for each in data:
                # if counter>1:
                #     break
                self.convert_into_groups(each[0])
                direction=each[1]
                correction=self.correct_values(each[2])
                writer.writerow([self.dict_dist[self.b],
                                 self.dict_dist[self.c],
                                 self.dict_dist[self.d],
                                 self.dict_dist[self.e],
                                 self.dict_dist[self.f],
                                 self.dict_dist[self.g],
                                 self.dict_dist[self.h],
                                 self.dict_dist[self.i],
                                 self.dict_dist[self.k],
                                 direction,
                                 correction,])
                #counter+=1


















if __name__=="__main__":
    sml=SCANS_ML()
    #sml.convert_csv()
    sml.read_csv()