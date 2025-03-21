import mysql.connector
from mysql.connector import Error

# MySQL connection details (update with your own)
host = "127.0.0.1"  # MySQL Docker container IP or localhost
port = "3306"  # Default MySQL port
user = "root"  # MySQL root user
password = "my-secret-pw"  # Root password for MySQL
database = "messaging_app"  # The database we want to create

# SQL queries to create the database and tables
create_db_query = "CREATE DATABASE IF NOT EXISTS messaging_app"
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
"""
create_conversations_table = """
CREATE TABLE IF NOT EXISTS conversations (
    conversation_id INT AUTO_INCREMENT PRIMARY KEY,
    conversation_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
"""
create_conversation_participants_table = """
CREATE TABLE IF NOT EXISTS conversation_participants (
    conversation_id INT,
    user_id INT,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (conversation_id, user_id),
    FOREIGN KEY (conversation_id) REFERENCES conversations(conversation_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
"""
create_messages_table = """
CREATE TABLE IF NOT EXISTS messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    conversation_id INT,
    user_id INT,
    message_text TEXT NOT NULL,
    message_type ENUM('text', 'image', 'file', 'audio') DEFAULT 'text',
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (conversation_id) REFERENCES conversations(conversation_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
"""
create_attachments_table = """
CREATE TABLE IF NOT EXISTS attachments (
    attachment_id INT AUTO_INCREMENT PRIMARY KEY,
    message_id INT,
    file_path VARCHAR(255) NOT NULL,
    file_type VARCHAR(50),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (message_id) REFERENCES messages(message_id) ON DELETE CASCADE
);
"""

# Function to connect to MySQL and create tables
def create_tables():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password
        )

        if connection.is_connected():
            print("Successfully connected to MySQL server.")
            
            cursor = connection.cursor()
            
            # Create the database if it doesn't exist
            cursor.execute(create_db_query)
            print(f"Database '{database}' is created or already exists.")
            
            # Select the newly created database
            cursor.execute(f"USE {database}")
            
            # Create the necessary tables
            cursor.execute(create_users_table)
            print("Users table created.")
            
            cursor.execute(create_conversations_table)
            print("Conversations table created.")
            
            cursor.execute(create_conversation_participants_table)
            print("Conversation Participants table created.")
            
            cursor.execute(create_messages_table)
            print("Messages table created.")
            
            cursor.execute(create_attachments_table)
            print("Attachments table created.")
            
            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error: {e}")
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_tables()

