from flask import Flask, render_template, request,jsonify, Response
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import json

app = Flask(__name__)


@app.route('/review',methods=['POST']) # route to show the review comments in a web UI
@cross_origin()
def index():
    try:
        #print(request.json)
        searchString = str(request.json).replace(" ","")
        #print(searchString)
        flipkart_url = "https://www.flipkart.com/search?q=" + searchString
        uClient = uReq(flipkart_url)
        flipkartPage = uClient.read()
        uClient.close()
        flipkart_html = bs(flipkartPage, "html.parser")
        bigboxes = flipkart_html.findAll("div", {"class": "bhgxx2 col-12-12"})
        del bigboxes[0:3]
        box = bigboxes[0]
        productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
        prodRes = requests.get(productLink)
        prodRes.encoding='utf-8'
        prod_html = bs(prodRes.text, "html.parser")
        #print(prod_html)
        commentboxes = prod_html.find_all('div', {'class': "_3nrCtb"})


        reviews = []
        for commentbox in commentboxes:
            try:
                comtag = commentbox.div.div.find_all('div', {'class': ''})
                #custComment.encode(encoding='utf-8')
                custComment = comtag[0].div.text
            except Exception as e:
                print("Exception while creating dictionary: ",str(e))
            if len(reviews)<5:
                reviews.append(custComment)
            else:
                break
        return (jsonify(reviews))
    except Exception as e:
        print('The Exception message is: ',e)
        reviews='something is wrong'
        return (jsonify(reviews))


if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True)