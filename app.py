from datetime import date


# import Flask ::: for implementig flask server
from flask import Flask, render_template,request


# create a new web-app whixh is a Flask application while __name__	represents that his is  
#the file that will reresent the web-app		
app = Flask(__name__,static_url_path='/static')



#GLOBAL-variables => check_in, check_out.


#/ represent the default page llocalhost/
@app.route("/")
#Declarator funtion
def index():

	return render_template("games.html")





