from flask import Flask,render_template,request
import DATA_LoginFunction
import DATA_ReadWriteEditFiles
app = Flask(__name__)

# Home Page
@app.route('/')
def Homepage():
   return render_template('Home Page.html')
# SIGNUP
@app.route('/signup',methods = ['POST', 'GET'])
def signuppage():

   return render_template("SignUp.html")

@app.route('/Goto',methods = ['POST','GET'])
def link():
   if request.method == 'POST' and request.form['Username'] not in DATA_LoginFunction.Userlist:
      Name = request.form
      Username = Name['Username']
      DATA_LoginFunction.User(Username,Name['Password'])
      DATA_ReadWriteEditFiles.Create_file(f'USER_{Username}')

   return render_template("Goto.html",url = f'http://127.0.0.1:5000/Notes/{Username}')



#LOGIN
@app.route('/Login',methods = ['POST','GET'])

def Login():

   return render_template('Login.html')

@app.route('/Authenticating',methods = ['POST','GET'])
def Logging():
   if request.method == 'POST':
      Logininformation = request.form
      Result = DATA_LoginFunction.LoginCheck(Logininformation['Username'],Logininformation['Password'])
   if Result == True:
      Username = Logininformation['Username']
      return render_template('Goto.html',url = f'http://127.0.0.1:5000/Notes/{Username}' )
   else:
      return render_template('Signup.html')

## Note Taking
@app.route('/Notes/<user>', methods = ['POST','GET'])
def notepad(user):
   Unsplit = DATA_ReadWriteEditFiles.Read_file(f'USER_{user}Notes.txt')
   SplitText = Unsplit.split('/n')

   return render_template('Notepad.html', url = f'http://localhost:5000/RefreshingNotes/{user}', text = SplitText )

@app.route('/RefreshingNotes/<user>',methods = ['POST','GET'])
def Refresh(user):
   if request.method == 'POST':
      Textinfo = request.form
      Text = Textinfo['text']

      DATA_ReadWriteEditFiles.Write_file(Text,f'USER_{user}Notes.txt')

   return render_template('Goto.html',url = f'http://localhost:5000/Notes/{user}')


if __name__ == '__main__':
   app.run(debug = True)
