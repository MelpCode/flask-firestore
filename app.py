from flask import Flask,render_template,redirect,request,flash
import pyrebase
import os
from varsglobal import firebaseConfig


#Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
#Auth instance
auth = firebase.auth()
#Real time database instance
db = firebase.database()


# Initialize App
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/',methods=['GET'])
def renderIndex():
    return render_template('index.html')

@app.route('/newquote',methods=['GET'])
def renderCreateForm():
    return render_template('quoteForm.html')

@app.route('/quoteslist',methods=['GET'])
def renderQuoteList():
    allQuotes = db.child("Quotes").get()
    return render_template("quotesList.html", quotes=allQuotes)
    
@app.route('/addquote',methods=['POST'])
def createNewQuote():
    if request.method == 'POST':
        author = request.form['author']
        quote = request.form['quote']
        data = {
            "author":author,
            "quote":quote
        }
        db.child('Quotes').push(data)
        flash('New Quote added Successfully!!!','success')
        return redirect('/quoteslist')
        
@app.route('/deletequote/<id>',methods=['GET'])
def deleteQuote(id):

    db.child("Quotes").child(id).remove()
    flash('Quote removed Successfully!!!','success')
    return redirect('/quoteslist')

if __name__ == '__main__':
    app.run(debug=True,port=3800)