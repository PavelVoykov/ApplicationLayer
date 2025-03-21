from flask import Flask, request, jsonify, render_template
from flask_cors import CORS 
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

CORS(app)

# MySQL connection details
host = "mysql-server"  # Docker container name or MySQL host
user = "root"
password = "my-secret-pw"
database = "messaging_app"

# Connect to MySQL
def get_db_connection():
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection

@app.route('/')
def index():
    return render_template('index.html')

# Route to get all messages
@app.route('/api/messages', methods=['GET'])
def get_messages():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        
        # Query all messages
        cursor.execute('SELECT * FROM messages ORDER BY sent_at ASC')
        messages = cursor.fetchall()
        
        cursor.close()
        connection.close()

        return jsonify(messages), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

# Route to send a new message
@app.route('/api/messages', methods=['POST'])
def send_message():
    try:
        message_data = request.get_json()
        message_text = message_data.get('message')

        if not message_text:
            return jsonify({'error': 'Message text is required'}), 400
        
        connection = get_db_connection()
        cursor = connection.cursor()

        # Insert the message into the database
        cursor.execute('''
            INSERT INTO messages (message_text, sent_at) 
            VALUES (%s, NOW())
        ''', (message_text,))
        connection.commit()
        
        cursor.close()
        connection.close()

        return jsonify({'status': 'Message sent'}), 201
    except Error as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

