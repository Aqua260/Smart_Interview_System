# app.py
# This is the main file that runs the Flask web application.
# Flask is a lightweight web framework for Python.

from flask import Flask, render_template, request, redirect, url_for, session
from questions import QUESTIONS
from model_utils import evaluate_answer, get_overall_feedback

# Create the Flask app
app = Flask(__name__)

# Secret key is required for using sessions (to remember user data between pages)
app.secret_key = 'interview_ai_secret_2024'


# ─── ROUTE: Login Page ───────────────────────────────────────────────────────
@app.route('/', methods=['GET', 'POST'])
def login():
    """
    GET  → shows the login form
    POST → saves username to session and redirects to dashboard
    """
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        if username:
            session['username'] = username          # remember the user's name
            session['answers'] = []                 # reset answers list
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Please enter your name.")
    return render_template('login.html')


# ─── ROUTE: Dashboard (choose type & difficulty) ─────────────────────────────
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    """
    GET  → shows interview type and difficulty selection
    POST → saves selection and redirects to interview page
    """
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        interview_type = request.form.get('interview_type')
        difficulty = request.form.get('difficulty')

        # Validate the selection
        if interview_type not in QUESTIONS or difficulty not in ['Easy', 'Medium', 'Hard']:
            return render_template('dashboard.html',
                                   username=session['username'],
                                   error="Please select valid options.")

        # Save selections to session
        session['interview_type'] = interview_type
        session['difficulty'] = difficulty
        session['current_question'] = 0            # start at question 0
        session['scores'] = []                     # list to store scores
        session['answers'] = []                    # list to store user answers

        return redirect(url_for('interview'))

    return render_template('dashboard.html', username=session['username'])


# ─── ROUTE: Interview Page ────────────────────────────────────────────────────
@app.route('/interview', methods=['GET', 'POST'])
def interview():
    """
    GET  → shows current question
    POST → evaluates the submitted answer, goes to next question or result
    """
    if 'username' not in session or 'interview_type' not in session:
        return redirect(url_for('login'))

    interview_type = session['interview_type']
    difficulty = session['difficulty']
    questions_list = QUESTIONS[interview_type][difficulty]
    total = len(questions_list)
    current_idx = session.get('current_question', 0)

    if request.method == 'POST':
        user_answer = request.form.get('answer', '').strip()
        q_data = questions_list[current_idx]

        # ── THIS IS WHERE THE TRANSFORMER IS USED ──
        # We call evaluate_answer() from model_utils.py
        # It uses the HuggingFace sentence-transformers model
        score, similarity, feedback = evaluate_answer(user_answer, q_data['model_answer'])

        # Store the result
        session['scores'] = session.get('scores', []) + [score]
        session['answers'] = session.get('answers', []) + [{
            'question': q_data['question'],
            'user_answer': user_answer,
            'model_answer': q_data['model_answer'],
            'score': score,
            'similarity': similarity,
            'feedback': feedback
        }]

        # Move to next question
        next_idx = current_idx + 1
        if next_idx >= total:
            # All questions answered → go to result
            return redirect(url_for('result'))
        else:
            session['current_question'] = next_idx
            return redirect(url_for('interview'))

    # GET: show the current question
    q_data = questions_list[current_idx]
    return render_template('interview.html',
                           question=q_data['question'],
                           question_number=current_idx + 1,
                           total_questions=total,
                           interview_type=interview_type,
                           difficulty=difficulty,
                           username=session['username'])


# ─── ROUTE: Result Page ───────────────────────────────────────────────────────
@app.route('/result')
def result():
    """
    Shows the final score, answer-by-answer breakdown, and overall feedback.
    """
    if 'username' not in session or 'answers' not in session:
        return redirect(url_for('login'))

    scores = session.get('scores', [])
    answers = session.get('answers', [])

    avg_score = round(sum(scores) / len(scores), 1) if scores else 0
    overall_feedback = get_overall_feedback(avg_score)

    return render_template('result.html',
                           username=session['username'],
                           answers=answers,
                           avg_score=avg_score,
                           overall_feedback=overall_feedback,
                           interview_type=session.get('interview_type'),
                           difficulty=session.get('difficulty'))


# ─── ROUTE: Logout / Restart ──────────────────────────────────────────────────
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ─── Run the app ──────────────────────────────────────────────────────────────
if __name__ == '__main__':
    # debug=True shows errors in the browser and auto-reloads on code changes
    app.run(debug=True)