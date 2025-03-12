from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os
import datetime

# Update your file path definitions to use absolute paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LEADERBOARD_FILE = os.path.join(BASE_DIR, 'data', 'leaderboard.json')
PROBLEMS_FILE = os.path.join(BASE_DIR, 'data', 'problems.json')
ANNOUNCEMENTS_FILE = os.path.join(BASE_DIR, 'data', 'announcements.json')

app = Flask(__name__)
app.secret_key = 'wonders_of_ai_secret_key'  # Required for flash messages

def get_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        # Create dummy data if file doesn't exist
        dummy_data = [
            {
                "name": "AI Avengers",
                "score": 850,
                "problems_solved": 4,
                "last_submission": "2025-03-09 14:23:45",
                "selected_problem": "AI-Powered Diabetic Retinopathy Diagnosis"
            },
            {
                "name": "Neural Nexus",
                "score": 720,
                "problems_solved": 3,
                "last_submission": "2025-03-09 10:15:30",
                "selected_problem": "Predictive Hospital Readmission Analytics"
            },
            {
                "name": "Deep Thinkers",
                "score": 680,
                "problems_solved": 3,
                "last_submission": "2025-03-08 22:05:12",
                "selected_problem": "Real-Time Financial Fraud Detection"
            },
            {
                "name": "Code Wizards",
                "score": 550,
                "problems_solved": 2,
                "last_submission": "2025-03-08 18:30:45",
                "selected_problem": "Stock Market Sentiment & Trend Forecasting"
            },
            {
                "name": "Quantum Coders",
                "score": 480,
                "problems_solved": 2,
                "last_submission": "2025-03-08 16:42:20",
                "selected_problem": "Drone-Based Crop Disease Identification"
            },
            {
                "name": "Binary Brains",
                "score": 320,
                "problems_solved": 1,
                "last_submission": "2025-03-07 20:15:10",
                "selected_problem": "Smart Irrigation Scheduling via Reinforcement Learning"
            },
            {
                "name": "ML Mavericks",
                "score": 300,
                "problems_solved": 1,
                "last_submission": "2025-03-07 15:40:22",
                "selected_problem": "Urban Traffic Flow Optimization"
            }
        ]
        
        # Ensure directory exists before writing file
        os.makedirs(os.path.dirname(LEADERBOARD_FILE), exist_ok=True)
        
        # Write dummy data to file
        with open(LEADERBOARD_FILE, 'w') as f:
            json.dump(dummy_data, f, indent=4)
        
        return dummy_data
    
    # If file exists, read from it
    with open(LEADERBOARD_FILE, 'r') as f:
        return json.load(f)

def get_problems():
    if not os.path.exists(PROBLEMS_FILE):
        # Create dummy problem data with additional fields
        dummy_problems = [
            {
                "id": 1,
                "title": "AI Image Classification",
                "description": "Develop a machine learning model to classify images into predefined categories.",
                "difficulty": "medium",
                "points": 200,
                "tags": ["Machine Learning", "Computer Vision", "Classification"],
                "requirements": [
                    "Create a model that can classify at least 5 different image categories",
                    "Achieve at least 85% accuracy on the test dataset",
                    "Include a demo interface for uploading and classifying new images"
                ],
                "criteria": [
                    "Accuracy of the model (50%)",
                    "Code quality and documentation (25%)",
                    "User interface and experience (25%)"
                ],
                "resources": [
                    {"name": "ImageNet Dataset", "url": "http://image-net.org/"},
                    {"name": "TensorFlow Documentation", "url": "https://www.tensorflow.org/tutorials/images/classification"},
                    {"name": "PyTorch Vision Tutorial", "url": "https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html"}
                ]
            },
            {
                "id": 2,
                "title": "Natural Language Processing Chatbot",
                "description": "Build a chatbot that can understand and respond to natural language queries.",
                "difficulty": "hard",
                "points": 300,
                "tags": ["NLP", "Chatbot", "AI"],
                "requirements": [
                    "Design a chatbot that can handle at least 3 different conversation topics",
                    "Implement context awareness to maintain conversation flow",
                    "Include a frontend interface for interacting with the chatbot"
                ],
                "criteria": [
                    "Conversational ability and natural responses (40%)",
                    "Context handling and memory (30%)",
                    "Implementation and technical architecture (30%)"
                ],
                "resources": [
                    {"name": "Hugging Face Transformers", "url": "https://huggingface.co/transformers/"},
                    {"name": "NLTK Documentation", "url": "https://www.nltk.org/"},
                    {"name": "SpaCy Documentation", "url": "https://spacy.io/usage"}
                ]
            },
            {
                "id": 3,
                "title": "Data Visualization Dashboard",
                "description": "Create an interactive dashboard to visualize AI model performance metrics.",
                "difficulty": "easy",
                "points": 100,
                "tags": ["Data Visualization", "Dashboard", "Frontend"],
                "requirements": [
                    "Build a dashboard with at least 5 different visualization types",
                    "Include filtering and sorting capabilities",
                    "Make the dashboard responsive for different screen sizes"
                ],
                "criteria": [
                    "Visual design and user experience (40%)",
                    "Interactivity and features (30%)",
                    "Code quality and organization (30%)"
                ],
                "resources": [
                    {"name": "D3.js Documentation", "url": "https://d3js.org/"},
                    {"name": "Plotly.js", "url": "https://plotly.com/javascript/"},
                    {"name": "Dashboard Design Principles", "url": "https://www.tableau.com/learn/articles/dashboard-design-principles"}
                ]
            },
            {
                "id": 4,
                "title": "Reinforcement Learning for Game AI",
                "description": "Implement a reinforcement learning algorithm to play a simple game.",
                "difficulty": "hard",
                "points": 350,
                "tags": ["Reinforcement Learning", "Game AI", "Deep Learning"],
                "requirements": [
                    "Implement a reinforcement learning algorithm (e.g., Q-learning, DQN)",
                    "Train an agent to play a game (e.g., CartPole, Atari game, custom game)",
                    "Provide visualization of the agent's learning progress"
                ],
                "criteria": [
                    "Agent performance in the game (40%)",
                    "Implementation quality and approach (40%)",
                    "Visualization and analysis (20%)"
                ],
                "resources": [
                    {"name": "OpenAI Gym", "url": "https://gym.openai.com/"},
                    {"name": "Stable Baselines3", "url": "https://stable-baselines3.readthedocs.io/"},
                    {"name": "Reinforcement Learning Introduction", "url": "https://spinningup.openai.com/en/latest/"}
                ]
            }
        ]
        
        # Ensure directory exists before writing file
        os.makedirs(os.path.dirname(PROBLEMS_FILE), exist_ok=True)
        
        # Write dummy data to file
        with open(PROBLEMS_FILE, 'w') as f:
            json.dump(dummy_problems, f, indent=4)
            
        return dummy_problems
    
    # If file exists, read from it
    with open(PROBLEMS_FILE, 'r') as f:
        return json.load(f)

def get_announcements():
    if not os.path.exists(ANNOUNCEMENTS_FILE):
        # Create sample announcements if file doesn't exist
        sample_announcements = [
            {
                "id": 1,
                "title": "Welcome to WONDERS OF AI 2.0!",
                "content": "We're excited to welcome all participants to our second annual AI hackathon. Get ready for an incredible 24 hours of innovation, collaboration, and cutting-edge technology.",
                "date": "2025-03-01",
                "important": True,
                "author": "Organizing Committee"
            },
            {
                "id": 2,
                "title": "Problem Statements Released",
                "content": "All problem statements for the hackathon are now available. Please explore the problems section to review the challenges and begin planning your approach. Remember to check the resources section for helpful tools and tutorials.",
                "date": "2025-03-05",
                "important": True,
                "author": "Technical Team"
            },
            {
                "id": 3,
                "title": "Workshop Schedule Update",
                "content": "We've added an additional AI Ethics workshop on March 12 at 3:00 PM. This session will cover important considerations for responsible AI development. All participants are encouraged to attend.",
                "date": "2025-03-08",
                "important": False,
                "author": "Events Coordinator"
            },
            {
                "id": 4,
                "title": "Final Week Preparations",
                "content": "With just one week left until the hackathon, ensure you've completed all pre-requisites, set up your environment, and familiarized yourself with the schedule. We recommend setting up your GitHub repositories in advance and reviewing the judging criteria.",
                "date": "2025-03-06",
                "important": False,
                "author": "Organizing Committee"
            }
        ]
        
        # Ensure directory exists before writing file
        os.makedirs(os.path.dirname(ANNOUNCEMENTS_FILE), exist_ok=True)
        
        # Write sample data to file
        with open(ANNOUNCEMENTS_FILE, 'w') as f:
            json.dump(sample_announcements, f, indent=4)
        
        return sample_announcements
    
    # If file exists, read from it
    with open(ANNOUNCEMENTS_FILE, 'r') as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/leaderboard")
def leaderboard():
    teams = get_leaderboard()
    # Sort teams by score in descending order
    teams = sorted(teams, key=lambda x: x['score'], reverse=True)
    return render_template("leaderboard.html", teams=teams)

@app.route("/problems")
def problems():
    problems = get_problems()
    return render_template("problems.html", problems=problems)

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/announcements")
def announcements():
    announcements_data = get_announcements()
    # Sort announcements by date (newest first) and pinned status
    announcements_data = sorted(
        announcements_data,
        key=lambda x: (not x.get('important', False), datetime.datetime.strptime(x['date'], '%Y-%m-%d')),
        reverse=True
    )
    return render_template("announcements.html", announcements=announcements_data)

# Ensure data directory exists
os.makedirs(os.path.dirname(LEADERBOARD_FILE), exist_ok=True)
os.makedirs(os.path.dirname(PROBLEMS_FILE), exist_ok=True)
os.makedirs(os.path.dirname(ANNOUNCEMENTS_FILE), exist_ok=True)

if __name__ == "__main__":
    # For local development
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)