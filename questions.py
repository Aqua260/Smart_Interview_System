# questions.py
# This file stores all interview questions and their model answers.
# The model answer is used by the Transformer to evaluate your answer.

QUESTIONS = {
    "HR": {
        "Easy": [
            {
                "question": "Tell me about yourself.",
                "model_answer": "I am a motivated and hardworking individual with a passion for learning and teamwork. I have good communication skills and can adapt to new environments quickly."
            },
            {
                "question": "Why do you want to work here?",
                "model_answer": "I want to work here because your company is known for innovation and growth. I believe my skills align with your goals and I want to contribute to your mission."
            },
            {
                "question": "What are your strengths?",
                "model_answer": "My key strengths are problem-solving, communication, and time management. I am reliable, detail-oriented, and a quick learner."
            }
        ],
        "Medium": [
            {
                "question": "Describe a time you faced a conflict at work and how you handled it.",
                "model_answer": "I once had a disagreement with a team member over project priorities. I scheduled a one-on-one meeting, listened to their perspective, and we collaboratively found a middle ground that satisfied both parties."
            },
            {
                "question": "How do you handle pressure and tight deadlines?",
                "model_answer": "I prioritize tasks by urgency and importance, break large tasks into smaller steps, and maintain focus. I also communicate proactively with my team if timelines are at risk."
            }
        ],
        "Hard": [
            {
                "question": "Where do you see yourself in 5 years?",
                "model_answer": "In 5 years I see myself in a leadership role, having contributed significantly to my team and organization. I plan to continuously upskill and take on increasing responsibilities."
            }
        ]
    },
    "Technical": {
        "Easy": [
            {
                "question": "What is a variable in programming?",
                "model_answer": "A variable is a named storage location in memory that holds a value. It can be used to store data that can be changed during program execution."
            },
            {
                "question": "What is the difference between a list and a tuple in Python?",
                "model_answer": "A list is mutable, meaning you can change its elements after creation. A tuple is immutable, meaning once created its elements cannot be changed. Lists use square brackets, tuples use parentheses."
            },
            {
                "question": "What is an API?",
                "model_answer": "An API (Application Programming Interface) is a set of rules that allows different software applications to communicate with each other. It defines the methods and data formats that programs can use to request and exchange information."
            }
        ],
        "Medium": [
            {
                "question": "Explain the concept of Object Oriented Programming.",
                "model_answer": "Object Oriented Programming (OOP) is a programming paradigm based on objects that contain data (attributes) and functions (methods). Key principles include encapsulation, inheritance, polymorphism, and abstraction."
            },
            {
                "question": "What is the difference between GET and POST HTTP methods?",
                "model_answer": "GET requests data from the server and parameters are visible in the URL. POST sends data to the server and parameters are in the request body. GET is used for retrieving data while POST is used for submitting data."
            }
        ],
        "Hard": [
            {
                "question": "Explain how a binary search tree works.",
                "model_answer": "A binary search tree is a data structure where each node has at most two children. For any node, all values in the left subtree are smaller and all values in the right subtree are larger. This allows efficient searching, insertion and deletion in O(log n) average time."
            }
        ]
    },
    "Aptitude": {
        "Easy": [
            {
                "question": "If a train travels 60 km in 1 hour, how far will it travel in 2.5 hours?",
                "model_answer": "150 km. Speed is 60 km per hour. Distance equals speed multiplied by time. So 60 multiplied by 2.5 equals 150 km."
            },
            {
                "question": "What is 15% of 200?",
                "model_answer": "30. To find 15% of 200, multiply 200 by 0.15 which equals 30."
            }
        ],
        "Medium": [
            {
                "question": "A person buys an item for Rs.800 and sells it for Rs.1000. What is the profit percentage?",
                "model_answer": "25%. Profit is Rs.200. Profit percentage equals profit divided by cost price multiplied by 100. So 200 divided by 800 multiplied by 100 equals 25 percent."
            },
            {
                "question": "If 6 workers can complete a task in 10 days, how many days will 4 workers take to complete the same task?",
                "model_answer": "15 days. Total work is 60 worker-days. With 4 workers, days needed equals 60 divided by 4 which is 15 days."
            }
        ],
        "Hard": [
            {
                "question": "Two pipes A and B can fill a tank in 6 hours and 8 hours respectively. How long will it take to fill the tank if both pipes are open?",
                "model_answer": "3.43 hours or approximately 3 hours 26 minutes. Pipe A fills 1/6 per hour, pipe B fills 1/8 per hour. Together they fill 1/6 plus 1/8 equals 7/24 per hour. Time equals 24/7 which is approximately 3.43 hours."
            }
        ]
    },
    "Mixed": {
        "Easy": [
            {
                "question": "Tell me about yourself.",
                "model_answer": "I am a motivated and hardworking individual with a passion for learning and teamwork."
            },
            {
                "question": "What is a variable in programming?",
                "model_answer": "A variable is a named storage location in memory that holds a value which can be changed during execution."
            },
            {
                "question": "What is 15% of 200?",
                "model_answer": "30. Multiply 200 by 0.15 to get 30."
            }
        ],
        "Medium": [
            {
                "question": "How do you handle pressure and tight deadlines?",
                "model_answer": "I prioritize tasks, break them into smaller steps, and communicate proactively with my team."
            },
            {
                "question": "What is the difference between GET and POST HTTP methods?",
                "model_answer": "GET retrieves data and shows parameters in the URL. POST sends data in the request body and is used for submitting forms."
            },
            {
                "question": "A person buys an item for Rs.800 and sells it for Rs.1000. What is the profit percentage?",
                "model_answer": "25 percent. Profit is 200, cost price is 800, so profit percentage is 25%."
            }
        ],
        "Hard": [
            {
                "question": "Where do you see yourself in 5 years?",
                "model_answer": "In a leadership role, having grown technically and professionally while contributing significantly to my organization."
            },
            {
                "question": "Explain how a binary search tree works.",
                "model_answer": "A BST stores data where left children are smaller and right children are larger, enabling O(log n) search, insert, and delete."
            }
        ]
    }
}