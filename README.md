# 🧠 Mood Journal AI 📝

A simple AI-powered personal journaling app that analyzes your emotions using **sentiment analysis** and helps you track your mood over time.

---

🚀 Features

- ✍️ Write daily journal entries
- 
- 🤖 AI-powered sentiment detection (Positive / Neutral / Negative)
- 
- 🗂️ Store and view past entries
- 
- 💡 Great for mental health tracking or self-reflection

---

 🛠️ Tech Stack

- **Backend:** Python (Flask)
- 
- **AI/NLP:** TextBlob (sentiment analysis)
- 
- **Frontend:** HTML + CSS
- 
- **Database:** SQLite (built-in)
- 
- **Visualization (optional extension):** Chart.js / Matplotlib

---

📦 Installation

Clone or Download the Project

If using the ZIP:

unzip mood-journal.zip

cd mood-journal

install dependencies

pip install -r requirements.txt

python -m textblob.download_corpora

run the app 

python app.py

Then open your browser and visit:

http://127.0.0.1:5000

💬 Example Journal Entries

Try pasting these into the journal to see how it reacts:

"I had a great day! Everything went perfectly." → Positive

"Just another normal workday." → Neutral

"I'm feeling exhausted and frustrated today." → Negative

📁 Project Structure

mood-journal/

│
├── app.py               # Main Flask app

├── requirements.txt     # Dependencies

├── templates/
│   └── index.html       # HTML interface

├── static/

│   └── style.css        # Styling

└── entries.db           # SQLite DB (auto-created)
 
📈 Future Improvements

📊 Mood trend charts

🔐 User login & personalized dashboards

🌍 Deploy to Heroku, Render, or Railway

💬 Daily prompts or affirmations

🧑‍💻 Author 
Built with ❤️ by Shruti Devani 

Contributions, ideas, and pull requests are welcome!


---

Let me know if you'd like:

- A version with badges (for GitHub)
  
- It exported as a `README.md` file
  
- Or help deploying it online!

Great question! Here are some **realistic challenges** and limitations you might face with the **Mood Journal AI Project**, especially around sentiment analysis and user experience:

---

⚠️ Challenges in the Mood Journal AI Project

🔹 1. **Accuracy of Sentiment Analysis**

* **Basic models like TextBlob** may misclassify sarcasm, mixed emotions, or cultural nuances.

  > Example: “I love waiting in traffic” might be incorrectly labeled as **positive**.
* **Context awareness is limited** — it doesn't understand events or sarcasm like a human would.

✅ **Solution**: Upgrade to advanced models like `VADER`, `BERT`, or `ChatGPT API` for deeper emotional understanding.

---

🔹 2. **Handling Long or Complex Entries**

* Long, reflective journal entries might include **multiple emotions**, which are reduced to a single "Positive/Neutral/Negative" label.
* Nuanced emotions (anxiety, relief, gratitude) get lost in this basic classification.

✅ **Solution**: Split entries into segments or sentence-wise sentiment analysis. Consider **emotion detection (joy, anger, sadness, etc.)**.

---

🔹 3. **Privacy and Data Security**

* Entries are saved in a local `SQLite` database. If deployed online, data could be sensitive and personal.

✅ **Solution**:

* Encrypt journal entries.
* Add user authentication.
* Store data securely (e.g., hashed or cloud-encrypted DB).

---

🔹 4. **No Visualization Yet**

* Users can't see how their mood is changing over time.
* No feedback loop for self-awareness or habit tracking.

✅ **Solution**: Integrate **charts** (e.g., Chart.js) to show trends over time.

---

🔹 5. **No Multi-User Support**

* It’s a single-user app right now.
* If hosted, anyone accessing the app shares the same journal.

✅ **Solution**: Implement login/signup with session-based data per user.

---

🔹 6. **TextBlob Language Limitations**

* TextBlob is trained mainly on **English**.
* Journal entries in **other languages** may not be classified properly.

✅ **Solution**: Use multilingual models like `XLM-RoBERTa` or cloud NLP APIs (e.g., Google Cloud, AWS Comprehend).

---

🔹 7. **Limited Feedback for Users**

* Users don’t get encouragement or reflections based on their mood.

✅ **Solution**: Add AI-generated motivational quotes, affirmations, or reflective prompts based on mood.

