// script.js
// Simple JavaScript for minor UI enhancements

// ── Character counter for the answer textarea ──────────────────────────────
const textarea = document.getElementById('answer');
const charCount = document.getElementById('char-count');

if (textarea && charCount) {
    textarea.addEventListener('input', function () {
        const len = this.value.length;
        charCount.textContent = len + ' characters';

        // Change color based on length (encourage longer answers)
        if (len < 20) {
            charCount.style.color = '#ef4444'; // red = too short
        } else if (len < 80) {
            charCount.style.color = '#f59e0b'; // amber = could be longer
        } else {
            charCount.style.color = '#22c55e'; // green = good length
        }
    });
}

// ── Prevent double-submit by disabling button on submit ───────────────────
const form = document.getElementById('answer-form');
const submitBtn = document.getElementById('submit-btn');

if (form && submitBtn) {
    form.addEventListener('submit', function () {
        submitBtn.textContent = '⏳ Evaluating with AI...';
        submitBtn.disabled = true;
        submitBtn.style.opacity = '0.7';
    });
}

// ── Auto-focus on text input when page loads ───────────────────────────────
const usernameInput = document.getElementById('username');
if (usernameInput) {
    usernameInput.focus();
}

const answerInput = document.getElementById('answer');
if (answerInput) {
    answerInput.focus();
}