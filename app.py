#flask
#


from flask import Flask, render_template, request
import joblib
import os
from groq import Groq
import sqlite3
import datetime

#from dotenv import load_dotenv
#if os.path.exists('.env'):
#    load_dotenv()

# for AWS, do not run this because not using .env
os.environ["GROQ_API_KEY"] = ""
#os.environ["GROQ_API_KEY"] = os.environ.get('GROQ_API_KEY')

client = Groq()

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    name = request.form.get("q")
    t = datetime.datetime.now()
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute('INSERT INTO user (name,timestamp) VALUES(?,?)',(name,t))
    conn.commit()
    c.close()
    conn.close()
    return(render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    return(render_template("dbs.html"))


@app.route("/dbs_prediction",methods=["GET","POST"])
def dbs_prediction():
    q = float(request.form.get("q"))
    model = joblib.load("DBS_SGD_model.pkl")
    r = model.predict([[q]])
    return(render_template("dbs_prediction.html",r=r[0][0]))

@app.route("/chatbot",methods=["GET","POST"])
def chatbot():
    return(render_template("chatbot.html"))

@app.route("/llama",methods=["GET","POST"])
def llama():
    return(render_template("llama.html"))

@app.route("/llama_result",methods=["GET","POST"])
def llama_result():
    q = request.form.get("q")
    r = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": q}])
    r = r.choices[0].message.content
    return(render_template("llama_result.html",r=r))

@app.route("/paynow",methods=["GET","POST"])
def paynow():
    return(render_template("paynow.html"))

@app.route("/userlog",methods=["GET","POST"])
def userlog():
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute('''select *
    from user''')
    r=""
    for row in c:
        print(row)
        r = r + str(row)
    c.close()
    conn.close()
    return(render_template("userlog.html",r=r))

@app.route("/deletelog",methods=["GET","POST"])
def deletelog():
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute('DELETE FROM user',);
    conn.commit()
    c.close()
    conn.close()
    return(render_template("deletelog.html"))

if __name__ == "__main__":
    app.run()
