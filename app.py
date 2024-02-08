from flask import *
from ast import literal_eval

app = Flask(__name__)

app.secret_key="bhautik"

@app.route('/',methods=['GET','POST'])
def login():
    # if request.method == "GET":
        return render_template('login.html')
    
    
@app.route('/signup',methods=["GET","POST"])
def signup():  

   if request.method=="GET":
      return render_template("signup.html")

   elif request.method=='POST':
      username = request.form["username"]
      password = request.form["password"]
      email = request.form["email"]
      confirm_Password = request.form["confirm_password"]

      new_obj = {
         "username": username,
         "password": password,
         "email": email,
         "confirm_Password": confirm_Password,
      }
  
      with open("creads.txt",'a') as f:
         f.write(str(new_obj)+'\n')
   
         f = open("creads.txt", "r")  # read mode
         print("FILE ALL DATA ARE READ..>>")
         print(f.read())
         f.close()
      return redirect("/")
   
@app.route('/login_data',methods=['GET','POST'])
def login_data():

   if  request.method == 'POST':

      username = request.form["username"]
      password = request.form["password"]

      with open("creds.txt") as f:
          Lines = f.readlines()
          for line in Lines:
              newline = literal_eval(line)
              if username == newline["username"] and  password == newline["password"]:
                flash(f"login successful {'username'} welcome to My website")
                return render_template("index.html")
              
      flash('Wrong Login and password please try again.')
      return render_template("login.html")
     
   if request.method == "GET":
      return render_template("login.html")

if __name__=='__main__':
    app.run(debug=True)