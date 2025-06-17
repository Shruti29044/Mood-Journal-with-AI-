from flask import Flask, render_template, request, redirect
from textblob import TextBlob
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Setup DB
def init_db():
    conn = sqlite3.connect('entries.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    content TEXT, 
                    sentiment TEXT, 
                    date TEXT)""")
    conn.commit()
    conn.close()

init_db()

# Analyze mood
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form["entry"]
        sentiment = analyze_sentiment(content)
        date = datetime.now().strftime("%Y-%m-%d %H:%M")

        conn = sqlite3.connect('entries.db')
        c = conn.cursor()
        c.execute("INSERT INTO entries (content, sentiment, date) VALUES (?, ?, ?)", 
                  (content, sentiment, date))
        conn.commit()
        conn.close()
        return redirect("/")

    # Fetch all entries
    conn = sqlite3.connect('entries.db')
    c = conn.cursor()
    c.execute("SELECT content, sentiment, date FROM entries ORDER BY id DESC")
    entries = c.fetchall()
    conn.close()

    return render_template("index.html", entries=entries)

if __name__ == "__main__":
    app.run(debug=True)
