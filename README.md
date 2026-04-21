📌 AI Interview System
📖 Overview
The AI Interview System is a web-based application built using Flask that helps users practice interview questions in a simulated environment. It evaluates user responses using Natural Language Processing (NLP) techniques and provides a score along with feedback.

🚀 Features
User-friendly login system
Selection of interview type and difficulty level
Predefined interview questions
AI-based answer evaluation using semantic similarity
Real-time scoring and feedback
Clean and interactive UI



🧠 Technologies Used

Frontend: HTML, CSS, JavaScript
Backend: Python (Flask)

AI Model: Sentence Transformers (all-MiniLM-L6-v2)
Concepts: NLP, Cosine Similarity, Embeddings


⚙️ How It Works

User logs in with a name
Selects interview type and difficulty
Answers questions one by one
System evaluates answers using AI model
Final score and feedback are displayed



📂 Project Structure
AI-Interview-System/│├── app.py              # Main Flask application├── questions.py        # Interview questions and answers├── model_utils.py      # AI evaluation logic├── templates/│   ├── login.html│   ├── dashboard.html│   ├── interview.html│   └── result.html├── static/│   ├── style.css│   └── script.js

🧪 Installation & Setup
# Clone the repositorygit clone https://github.com/your-username/ai-interview-system.git# Navigate to project foldercd ai-interview-system# Install dependenciespip install flask sentence-transformers scikit-learn# Run the applicationpython app.py

🌐 Usage
Open browser and go to: http://127.0.0.1:5000/
Login with your name
Select interview preferences
Start answering questions
View your result and feedback


🔮 Future Enhancements
Add voice-based answers (speech-to-text)
Dynamic question generation using AI
Database integration
Detailed performance analytics
