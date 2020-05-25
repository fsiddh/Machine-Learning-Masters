
# Importing the necessary Libraries
from flask_cors import CORS,cross_origin
from imagescrapperservice.ImageScrapperService import ImageScrapperService
from imagescrapper.ImageScrapper import ImageScrapper
from flask import Flask, render_template, request,jsonify


# import request
app = Flask(__name__) # initialising the flask app with the name 'app'

#response = 'Welcome!'


@app.route('/')  # route for redirecting to the home page
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/showImages') # route to show the images on a webpage
@cross_origin()
def show_images():
    scraper_object=ImageScrapper() #Instantiating the object of class ImageScrapper
    list_of_jpg_files=scraper_object.list_only_jpg_files('static') # obtaining the list of image files from the static folder
    print(list_of_jpg_files)
    try:
        if(len(list_of_jpg_files)>0): # if there are images present, show them on a wen UI
            return render_template('showImage.html',user_images = list_of_jpg_files)
        else:
            return "Please try with a different string" # show this error message if no images are present in the static folder
    except Exception as e:
        print('no Images found ', e)
        return "Please try with a different string"

@app.route('/searchImages', methods=['GET','POST'])
def searchImages():
    if request.method == 'POST':
        print("entered post")
        keyWord = request.form['keyword'] # assigning the value of the input keyword to the variable keyword

    else:
        print("did not enter post")
    print('printing = ' + keyWord)

    scraper_object = ImageScrapper() # instantiating the class
    list_of_jpg_files = scraper_object.list_only_jpg_files('static') # obtaining the list of image files from the static folder
    scraper_object.delete_existing_image(list_of_jpg_files) # deleting the old image files stored from the previous search
    # splitting and combining the keyword for a string containing multiple words
    image_name = keyWord.split()
    image_name = '+'.join(image_name)
    # adding the header metadata
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

    service = ImageScrapperService  # instantiating the object of class ImageScrapperService
    # (imageURLList, header, keyWord, fileLoc)
    masterListOfImages = service.downloadImages(keyWord, header) # getting the master list from keyword
    imageList = masterListOfImages[0] # extracting the list of images from the master list
    imageTypeList = masterListOfImages[1] # extracting the list of type of images from the masterlist

    response = "We have downloaded ", len(imageList), "images of " + image_name + " for you"

    return show_images() # redirect the control to the show images method

@app.route('/api/showImages', methods=['GET','POST']) # route to return the list of file locations for API calls
@cross_origin()
def get_image_url():
    if request.method == 'POST':
        print("entered post")
        keyWord =  request.json['keyword'] # assigning the value of the input keyword to the variable keyword

    else:
        print("Did not enter  post")
    print('printing = ' + keyWord)
    # splitting and combining the keyword for a string containing multiple words
    image_name = keyWord.split()
    image_name = '+'.join(image_name)
    # adding the header metadata
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

    service = ImageScrapperService # instantiating the object of class ImageScrapperService
    url_enum = service.get_image_urls(keyWord, header) # getting the URL enumeration
    url_list=[] # initializing and empty url list
    for i, (img, Type) in enumerate(url_enum[0:5]):
        # creating key value pairs of image URLs to be sent as json
        dict={'image_url':img}
        url_list.append(dict)
    return jsonify(url_list) # send the url list in JSON format

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8000) # port to run on local machine
    app.run(debug=True) # to run on cloud
