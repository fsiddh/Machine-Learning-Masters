# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:26:53 2019

@author: Jiwitesh_Sharma
"""


from imagescrapper.ImageScrapper import ImageScrapper
from imagescrapperutils.ImageScrapperUtils import ImageScrapperUtils
class ImageScrapperService:
    
    utils = ImageScrapperUtils
    imgScrapper = ImageScrapper
    keyWord = ""
    fileLoc = ""
    image_name = ""
    header = ""
    '''def __main__(keyWord, image_name, fileLoc, header):
    keyWord = keyWord
    fileLoc = fileLoc
    image_name = keyWord
    dao = DAO
    utils = ImageScrapperUtils
    imgScrapper = ImageScrapper'''
    # you can change the query for the image  here
    
    #pdb.set_trace()
    
    def downloadImages( keyWord, header):
        imgScrapper = ImageScrapper
        url = imgScrapper.createURL(keyWord)
        rawHtml = imgScrapper.get_RawHtml(url, header)
        
        imageURLList = imgScrapper.getimageUrlList(rawHtml)
        
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList,keyWord, header)
        
        return masterListOfImages

    def get_image_urls(keyWord, header):
        imgScrapper = ImageScrapper
        url = imgScrapper.createURL(keyWord)
        rawHtml = imgScrapper.get_RawHtml(url, header)

        imageURLList = imgScrapper.getimageUrlList(rawHtml)

        return imageURLList