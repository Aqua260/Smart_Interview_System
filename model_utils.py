# model_utils.py
# This file loads the Transformer model and uses it to evaluate answers.

# We are using the 'sentence-transformers' library.
# It wraps HuggingFace transformer models in an easy-to-use format.

from sentence_transformers import SentenceTransformer, util

# --- Load the model once when the application starts ---
# 'all-MiniLM-L6-v2' is a small, fast transformer model.
# It converts sentences into 384-dimensional vectors (embeddings).
# The first time you run this, it downloads ~90MB from HuggingFace automatically.
print("Loading transformer model... (this may take a few seconds)")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded successfully!")


def evaluate_answer(user_answer, model_answer):
    """
    Compares the user's answer to the model (ideal) answer using the Transformer.
    
    How it works:
    1. The model converts both sentences into number vectors (embeddings)
    2. We measure the cosine similarity between the two vectors
    3. Similarity ranges from 0.0 (completely different) to 1.0 (identical)
    
    Returns:
    - score: float from 0 to 10
    - similarity: raw float from 0 to 1
    - feedback: a string message for the user
    """

    # Handle empty answers
    if not user_answer or len(user_answer.strip()) < 5:
        return 0, 0.0, "You did not provide an answer."

    # Step 1: Encode both sentences into embeddings using the Transformer
    # The model reads the text and produces a list of 384 numbers for each sentence
    user_embedding = model.encode(user_answer, convert_to_tensor=True)
    model_embedding = model.encode(model_answer, convert_to_tensor=True)

    # Step 2: Calculate cosine similarity between the two embeddings
    # cosine_similarity returns a value between -1 and 1; for sentences it's usually 0 to 1
    similarity = util.cos_sim(user_embedding, model_embedding).item()

    # Step 3: Convert similarity (0-1) to score (0-10)
    score = round(similarity * 10, 1)
    score = max(0, min(10, score))  # clamp between 0 and 10

    # Step 4: Generate feedback based on the similarity score
    if similarity >= 0.75:
        feedback = "Excellent answer! Your response closely matches the expected answer."
    elif similarity >= 0.55:
        feedback = "Good answer! You covered the main points but could add more detail."
    elif similarity >= 0.35:
        feedback = "Partial answer. You touched on some relevant points but missed key concepts."
    elif similarity >= 0.15:
        feedback = "Below average. Try to include more relevant keywords and concepts."
    else:
        feedback = "Poor answer. Please review the topic and try again."

    return score, round(similarity, 3), feedback


def get_overall_feedback(average_score):
    """
    Returns overall performance feedback based on average score.
    """
    if average_score >= 8:
        return "Outstanding performance! You are well-prepared for interviews."
    elif average_score >= 6:
        return "Good performance! A little more preparation will make you interview-ready."
    elif average_score >= 4:
        return "Average performance. Focus on improving your weak areas."
    elif average_score >= 2:
        return "Below average. Significant improvement needed before attending interviews."
    else:
        return "Poor performance. Please thoroughly review all topics and practice more."