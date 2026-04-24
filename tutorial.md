# Creating A Flask App

This guide explains the **very basics** of building a Flask web application, including the required files and folder structure.

---

## 1. What is Flask?

Flask is a lightweight Python web framework used to build web applications quickly and with minimal setup.

---

## 2. Minimum Working Flask App

The simplest Flask app requires just **one file**:

```python
# app.py - flask app

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()
```

### How it works:

* `Flask(__name__)` → creates the app
* `@app.route("/")` → defines a URL route
* `index()` → function that runs when user visits `/`
* `app.run()` → starts the server

---

## 3. Recommended Folder Structure

As your app grows, you should organize files like this:

```
my_flask_app/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## 4. Key Files Explained

### 4.1 `app.py`

Main application file.

Responsibilities:

* Define routes
* Handle requests
* Return responses

---

### 4.2 `templates/`

Stores HTML files.

Example: `templates/index.html`

```html
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
    <h2>Change your Title</h2>

    </div>
</body>
```

Usage in Flask:

```python
from flask import render_template

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))
```

---

### 4.3 `static/`

Stores static assets like:

* CSS
* Images

Example structure:

```
static/
└── css/style.css
```

Link in HTML:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

---

### 4.4 `requirements.txt`

Lists Python dependencies.

Example:

```
flask
```

Install with:

```
pip install -r requirements.txt
```

---

## 5. Running the App

### Option 1: Direct run

```
python app.py
```

---

## 6. Basic Request Flow

1. User visits a URL (e.g., `/`)
2. Flask matches the route
3. Corresponding function runs
4. Function returns response (HTML/text/JSON)
5. Browser displays the result

---

## 7. Optional Improvements (Next Steps)

Once comfortable, you can expand your app with:

* Blueprints (modular structure)
* Database integration (SQLite, PostgreSQL)
* Forms (Flask-WTF)
* APIs (return JSON)

---

## 8. Summary

Minimum requirements:

* `app.py` (required)

Common structure for real apps:

* `templates/` → HTML
* `static/` → CSS
* `requirements.txt` → dependencies

Flask is simple to start, but flexible enough to scale into larger applications.

---

## Part I
Create a file called `app.py`

```python
# app.py - flask app

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()
```

Create `index.html`
```html
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
    <h2>Change your Title</h2>

    </div>
</body>
```

Do command 

```bash
pip install -r requirements.txt
```

Run command

```bash
python app.py
```

## Part II

Add the following to `index.html`
```html
    <form action="/main" method="post">
        <h4>Please enter your name : </h4>
        <input type = "text" name = "q">
        <input type = "submit" value="Enter">
    </form>
```

So the final `index.html` will be as follows:

```html
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
    <h2>Change your Title</h2>
        <form action="/" method="post">
            <h4>Please enter your name : </h4>
            <input type = "text" name = "q">
            <input type = "submit" value="Enter">
        </form>

    </div>
</body>
```
The addition is a form that get text input from user after user hit submit.

Watch out for 
```html
<form action="/" method="post">
```
action route point to the program should trigger, in this case it is a loop. so change to the following:

```html
<form action="/main" method="post">
```

Then add the following to the `app.py`
```python
@app.route("/main",methods=["GET","POST"])
def main():
    name = request.form.get("q")
    return(render_template("main.html", name=name))
```

Since we need to render the `main.html` please create a new file in `templates`
```html
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
    <h2>Main Menu for {{name}} </h2>
    
    </div>
</body>>
```

Also add `request` to the import so that it will be 

```python
from flask import Flask, render_template, request
```

Then run the command `python app.py`

## Part III
Add a button for chatbot

add the following to `main.html`

```html
        <form action="/chatbot" method="post">
            <input type = "submit" value="Chatbot">
        </form>
```

then add the following to `app.py`
```python
@app.route("/chatbot",methods=["GET","POST"])
def chatbot():
    return(render_template("chatbot.html"))
```

Create a file `chatbot.html`
```html
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
    <h2>Welcome to our chatbot</h2>
    <form action="/llama" method="post">
        <input type = "submit" value="LLAMA">
    </form>
    <form action="/main" method="post">
        <input type = "submit" value="Main">
    </form>
    </div>
</body>
```
So we detect an error because we did not add `/llama` action in `app.py`.

Add the following:
```python
@app.route("/llama",methods=["GET","POST"])
def llama():
    return(render_template("llama.html"))
```
So we have another error! Now we know why. Add the following file `llama.html`

```html
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
    <h2>Welcome to chat by LLAMA</h2>
    <form action="/llama_result" method="post">
        <h4>Please enter query : </h4>
        <input type = "text" name = "q">
        <input type = "submit" value="Enter">
    </form>
    </div>
</body>
```

Why there is another error?

Add the following to `app.py`
```python
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
```

also add the following to the front, after import:
```python
import Groq

client = Groq()
```

final `app.py` should be 

```python
# app.py - flask app

from flask import Flask, render_template, request
from groq import Groq

client = Groq()

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    name = request.form.get("q")
    return(render_template("main.html", name=name))

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

if __name__ == "__main__":
    app.run()
```

Another error, don't worry lets fixed one by one. First create a file called `.env` and use the following:

```text
GROQ_API_KEY=
```

Then copy the following after the import:

```python
import os
from dotenv import load_dotenv
if os.path.exists('.env'):
   load_dotenv()
```

The final file should be 
```python
# app.py - flask app

from flask import Flask, render_template, request
from groq import Groq

import os
from dotenv import load_dotenv
if os.path.exists('.env'):
   load_dotenv()


client = Groq()

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    name = request.form.get("q")
    return(render_template("main.html", name=name))

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

if __name__ == "__main__":
    app.run()
```

Error again! This time we need `llama_result.html`

```html
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
    <h4>reply from LLAMA : {{r}}</h4>
    <form action="/main" method="post">
        <input type = "submit" value="Main">
    </form>
    </div>
</body>
```