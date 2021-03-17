# AQI-prediction-and-deployment
 While I was doing this project, I did'nt know know how to deploy. When I watched few youtube videos regarding flask, they were all done with IDE environment. 
 As I don't like to use Anaconda, I decided to deploy model in Google Colab. I just love using colab as it makes everything feasible. 
 Finally after many searches for the techniques, with which we can create website, I came across Streamlit library . It made my work simple.
 In my Deployment AQI ipynb file(in repository), I have deployed the model. At second last cell, website was created and the output was URL of website.
   https://13afb8def9d5.ngrok.io/              #this URL doe'nt work
   however this URL works until Runtime, as I deployed it in Colab. So after runtime the URL does'nt work. 
 There are many passionate people who wants to know or who are excited to know about deployment without using IDE. I am one among such. I have wasted a lot of time in searching. 
   so I thought this wo!uld be helpful for them.
   
   
   WEBSITE OVERVIEW
   [deploy1](https://user-images.githubusercontent.com/65075408/111460831-71193200-8742-11eb-8e8e-70cfe02e2994.PNG)



























[depoy2](https://user-images.githubusercontent.com/65075408/111460915-927a1e00-8742-11eb-95ef-6a317c349c6f.PNG)


















RESULT



![result dep](https://user-images.githubusercontent.com/65075408/111461223-f1d82e00-8742-11eb-94c8-69563f2699ba.PNG)











FLOW OF THIS PROJECT:
There are unnecessary files like procfile,requirement.txt , I just stored them incase if I had to make a permanent website with flask or something else
So The Project Flow is
  1) In AQI prediction.ipynb file, first two cells consists of Web Scraping. I collect the data from the https://en.tutiempo.net/climate/ws-431280.html from 2013 to 2018 using requests module And in the Third cell,you will get a file in your colab documents.
  2) 
  3) Real combine.csv is the file which will be obtained. 
  4) Then I did analysis on the obtained data from 2013 to 2018 of Hyderabad City.
  5) Used 6 Regression algorithms in ordered to find best algorithm for the prediction. 
  6) Random forest Regression got less MSE(Mean Squared Error)
  7) After that in Deployment.ipynb , Deploy the model.
