import os
import io
# from pdf2image import convert_from_bytes
from flask import Flask, request, jsonify, render_template
# from google.cloud import vision_v1
# from PIL import Image
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash
import requests
import json
import mysql.connector
from mysql.connector import errorcode
# from decimal import Decimal
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from datetime import timedelta

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
# Database configuration
db_config = {
    'user': 'TechQuest',
    'password': 'Jeeboomba123',
    'host': 'TechQuest.mysql.pythonanywhere-services.com',
    'database': 'TechQuest$default'
}

# Store participant scores
scores = {}
participants = {}

# @app.route('/')
# def main_page():
#     # return render_template('index.html')
#     username = session.get('username')
#     return render_template('index.html', username=username)


# @app.route('/')
# def main_page():
#     username = session.get('username')
#     total_score = 0
#     if username:
#         try:
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()

#             # Fetch score for the logged-in user
#             cursor.execute("SELECT score FROM score WHERE username = %s", (username,))
#             result = cursor.fetchone()

#             if result:
#                 total_score = result[0]

#             cursor.close()
#             db.close()

#         except Exception as e:
#             print(f"Error fetching score: {e}")

#     return render_template('index.html', username=username, total_score=total_score)

# @app.route('/')
# def main_page():
#     username = session.get('username')
#     total_score = 0
#     if username:
#         try:
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()

#             # Fetch score for the logged-in user
#             cursor.execute("SELECT score FROM score WHERE username = %s", (username,))
#             result = cursor.fetchone()

#             if result:
#                 total_score = result[0]

#             cursor.close()
#             db.close()

#         except Exception as e:
#             print(f"Error fetching score: {e}")

#     return render_template('index.html', username=username, total_score=total_score)


# @app.route('/get_score', methods=['GET'])
# def get_score():
#     username = session.get('username')
#     total_score = 0
#     if username:
#         try:
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()

#             # Fetch score for the logged-in user
#             cursor.execute("SELECT score FROM score WHERE username = %s", (username,))
#             result = cursor.fetchone()

#             if result:
#                 total_score = result[0]

#             cursor.close()
#             db.close()

#         except Exception as e:
#             print(f"Error fetching score: {e}")

#     return jsonify({'score': total_score})

# @app.route('/update_score', methods=['POST'])
# def update_score():
#     data = request.json
#     username = session.get('username')
#     score = data.get('score')

#     if username:
#         try:
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()

#             # Check if username already exists in the score table
#             cursor.execute("SELECT * FROM score WHERE username = %s", (username,))
#             result = cursor.fetchone()

#             if result:
#                 # Update existing record
#                 cursor.execute("UPDATE score SET score = %s WHERE username = %s", (score, username))
#             else:
#                 # Insert new record
#                 cursor.execute("INSERT INTO score (username, score) VALUES (%s, %s)", (username, score))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'message': 'Score updated successfully'}), 200

#         except Exception as e:
#             return jsonify({'error': str(e)}), 500

#     return jsonify({'error': 'User not logged in'}), 401

# @app.route('/')
# def main_page():
#     username = session.get('username')
#     if username:
#         try:
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()

#             # Fetch score for the logged-in user
#             cursor.execute("SELECT score FROM score WHERE username = %s", (username,))
#             result = cursor.fetchone()

#             if result:
#                 total_score = result[0]
#             else:
#                 total_score = 0  # Default score if user has no score yet

#             cursor.close()
#             db.close()

#         except Exception as e:
#             print(f"Error fetching score: {e}")
#             total_score = 0  # Default to 0 in case of error

#     else:
#         total_score = 0  # Default to 0 if no username in session

#     return render_template('index.html', username=username, total_score=total_score)





# @app.route('/update_score', methods=['POST'])
# def update_score():
#     data = request.json
#     username = session.get('username')
#     score = data.get('score')

#     try:
#         db = mysql.connector.connect(**db_config)
#         cursor = db.cursor()

#         # Check if username already exists in the score table
#         cursor.execute("SELECT * FROM score WHERE username = %s", (username,))
#         result = cursor.fetchone()

#         if result:
#             # Update existing record
#             cursor.execute("UPDATE score SET score = %s WHERE username = %s", (score, username))
#         else:
#             # Insert new record
#             cursor.execute("INSERT INTO score (username, score) VALUES (%s, %s)", (username, score))

#         db.commit()
#         cursor.close()
#         db.close()

#         return jsonify({'message': 'Score updated successfully'}), 200

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

@app.route('/')
def main_page():
    username = session.get('username')
    total_score = 0
    if username:
        try:
            db = mysql.connector.connect(**db_config)
            cursor = db.cursor()

            # Fetch score for the logged-in user
            cursor.execute("SELECT score FROM score WHERE username = %s", (username,))
            result = cursor.fetchone()

            if result:
                total_score = result[0]

            cursor.close()
            db.close()

        except Exception as e:
            print(f"Error fetching score: {e}")

    return render_template('index.html', username=username, total_score=total_score)

@app.route('/get_score', methods=['GET'])
def get_score():
    username = session.get('username')
    total_score = 0
    if username:
        try:
            db = mysql.connector.connect(**db_config)
            cursor = db.cursor()

            # Fetch score for the logged-in user
            cursor.execute("SELECT score FROM score WHERE username = %s", (username,))
            result = cursor.fetchone()

            if result:
                total_score = result[0]

            cursor.close()
            db.close()

        except Exception as e:
            print(f"Error fetching score: {e}")

    return jsonify({'score': total_score})

@app.route('/update_score', methods=['POST'])
def update_score():
    data = request.json
    username = session.get('username')
    score = data.get('score')

    if username:
        try:
            db = mysql.connector.connect(**db_config)
            cursor = db.cursor()

            # Check if username already exists in the score table
            cursor.execute("SELECT * FROM score WHERE username = %s", (username,))
            result = cursor.fetchone()

            if result:
                # Update existing record
                cursor.execute("UPDATE score SET score = %s WHERE username = %s", (score, username))
            else:
                # Insert new record
                cursor.execute("INSERT INTO score (username, score) VALUES (%s, %s)", (username, score))

            db.commit()
            cursor.close()
            db.close()

            return jsonify({'message': 'Score updated successfully'}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'User not logged in'}), 401


@app.route('/question/<int:question_id>')
def question_page(question_id):
    return render_template('question.html', question_id=question_id)


@app.route('/leaderboard')
def leaderboard():
    username = session.get('username')
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # SQL query to select users ordered by score
        sql = "SELECT username, score FROM score ORDER BY score DESC"
        cursor.execute(sql)
        users = cursor.fetchall()  # Fetch all rows

        # Calculate rank for each user
        for rank, user in enumerate(users, start=1):
            user['rank'] = rank

        cursor.close()
        connection.close()

        return render_template('leaderboard.html', users=users, username=username)

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return "An error occurred while fetching leaderboard data."

@app.route('/profile')
def profile():
    return render_template('profile.html')

#### new stuff ####
# Function to create a new connection to the database
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username exists
        if username_exists(username):
            # Render the register page with an alert message
            return render_template('register.html', username_exists=True)
        else:
            # Proceed with registration
            register_user(username, email, password)
            return redirect(url_for('login'))  # Assuming there's a 'login' route
    return render_template('register.html', username_exists=False)

def username_exists(username):
    db = mysql.connector.connect(
        user='TechQuest',
        password='Jeeboomba123',
        host='TechQuest.mysql.pythonanywhere-services.com',
        database='TechQuest$default')
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    db.close()
    return result[0] > 0

def register_user(username, email, password):
    db = mysql.connector.connect(
        user='TechQuest',
        password='Jeeboomba123',
        host='TechQuest.mysql.pythonanywhere-services.com',
        database='TechQuest$default')
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    db.commit()
    db.close()




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if authenticate_user(username, password):
            session['username'] = username  # Store username in session
            return redirect(url_for('main_page'))
        else:
            return render_template('login.html', login_failed=True, username=username)

    return render_template('login.html', login_failed=False)

def authenticate_user(username, password):
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    cursor.execute("SELECT username FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    db.close()
    return result is not None
#### end of new stuff ####
###
