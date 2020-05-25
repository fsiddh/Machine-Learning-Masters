# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:30:55 2019

@author: Jiwitesh_Sharma
"""
import os
class ImageScrapperUtils:
     def storeImage(imageFiles, imageTypes, fileLoc, keyWord ):
         #fileLoc = "Pictures"
         #keyWord = "jiwitesh"
         if not os.path.exists(fileLoc):
            os.mkdir(fileLoc)
         fileLoc = os.path.join(fileLoc, keyWord.split()[0])

         if not os.path.exists(fileLoc):
             os.mkdir(fileLoc)
        
         count = 0;
         for raw_img in imageFiles.keys():
             Type = 'jpg'
             counter = len([i for i in os.listdir(fileLoc) if Type in i]) + 1
             print (counter)
             if len(Type)==0:
                 f = open(os.path.join(fileLoc , keyWord + "_"+ str(counter)+".jpg"), 'wb')
             else :
                 f = open(os.path.join(fileLoc , keyWord + "_"+ str(counter)+"."+Type), 'wb')
             
             f.write(imageFiles.get(raw_img))
             f.close()
             count +=1