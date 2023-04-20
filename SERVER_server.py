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

   return render_template("Goto.html",url = f'http://127.0.0.1:5000/Notes/add/{Username}')



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
      return render_template('Goto.html',url = f'http://127.0.0.1:5000/Notes/add/{Username}' )
   else:
      return render_template('Signup.html')

## NoteADD
@app.route('/Notes/add/<user>', methods = ['POST','GET'])
def notepadadd(user):
   Unsplit = DATA_ReadWriteEditFiles.Read_file(f'USER_{user}Notes.txt')
   SplitText = Unsplit.split('/n')

   return render_template('NotepadAdd.html', url = f'http://localhost:5000/RefreshingNotes/add/{user}', text = SplitText, edit_url = f"http://localhost:5000/RefreshingNotes/edit/{user}" )

@app.route('/RefreshingNotes/add/<user>',methods = ['POST','GET'])
def Refreshadd(user):
   if request.method == 'POST':
      Textinfo = request.form
      Text = Textinfo['text']
      Length = DATA_ReadWriteEditFiles.Line_Count(f'USER_{user}Notes.txt')
      DATA_ReadWriteEditFiles.Write_file(f'{Length}.{Text}',f'USER_{user}Notes.txt')

   return render_template('Goto.html',url = f'http://localhost:5000/Notes/add/{user}')

##Note EDIT
@app.route('/Notes/edit/<user>', methods = ['POST','GET'])
def notepadedit(user):
   Unsplit = DATA_ReadWriteEditFiles.Read_file(f'USER_{user}Notes.txt')
   SplitText = Unsplit.split('/n')

   return render_template('Notepadedit.html', url = f'http://localhost:5000/RefreshingNotes/edit/{user}', text = SplitText, add_url = f'http://localhost:5000/RefreshingNotes/add/{user}' )

@app.route('/RefreshingNotes/edit/<user>',methods = ['POST','GET'])
def Refreshedit(user):
   if request.method == 'POST':
      Textinfo = request.form
      Line = int(Textinfo['Line'])
      Replace = Textinfo['edit']
      DATA_ReadWriteEditFiles.Edit_line(f'USER_{user}Notes.txt',Line,Replace)
   return render_template('Goto.html',url = f'http://localhost:5000/Notes/edit/{user}')








if __name__ == '__main__':
   app.run(debug = True)
