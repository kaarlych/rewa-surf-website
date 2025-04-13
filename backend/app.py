from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['windsurfing_school']
courses_collection = db['courses']

# API Routes
@app.route('/api/courses', methods=['GET'])
def get_courses():
    courses = list(courses_collection.find({}))
    # Convert ObjectId to string for JSON serialization
    for course in courses:
        course['_id'] = str(course['_id'])
    return jsonify(courses)

# Add seed route to populate database
@app.route('/api/seed', methods=['GET'])
def seed_database():
    # Sample course data
    sample_courses = [
        {
            "name": "Beginner Windsurfing",
            "description": "Learn the basics of windsurfing in calm waters with experienced instructors.",
            "price": 99.99,
            "duration": 120,
            "difficulty": "Beginner"
        },
        {
            "name": "Intermediate Skills",
            "description": "Perfect your technique and learn new maneuvers in varying wind conditions.",
            "price": 149.99,
            "duration": 180,
            "difficulty": "Intermediate"
        },
        {
            "name": "Advanced Tricks",
            "description": "Master advanced jumps, spins, and racing techniques for experienced windsurfers.",
            "price": 199.99,
            "duration": 240,
            "difficulty": "Advanced"
        }
    ]
    
    # Clear existing courses and insert new ones
    courses_collection.delete_many({})
    courses_collection.insert_many(sample_courses)
    
    return jsonify({"message": "Database seeded with sample courses", "count": len(sample_courses)})

# Home route
@app.route('/', methods=['GET'])
def home():
    return "Windsurfing School API is running!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
