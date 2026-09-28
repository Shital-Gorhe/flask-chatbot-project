#database related logic
import sqlite3

def get_connection():
    return sqlite3.connect("chatbot.db")


''' import sqlite3

connection = sqlite3.connect('chatbot.db')
cursor = connection.cursor()
'''
'''
cursor.execute("""

    CREATE TABLE IF NOT EXISTS knowledge (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT UNIQUE NOT NULL,
    answer TEXT NOT NULL)
    """)
'''
'''
cursor.execute("""
    INSERT INTO knowledge (question, answer)
    VALUES (?, ?)
""", ("hello", "Hi!"))

'''

'''
cursor.execute("select * from knowledge")

knowledge = cursor.fetchall()
print(knowledge)

connection.commit()
connection.close()
'''


#READ
def find_answer(question):
    with get_connection() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT answer
            FROM knowledge
            WHERE question = ?
        """, (question,))

        answer = cursor.fetchone()

    if answer:
        return answer[0]

    return None


#CREATE
def add_knowledge(question, answer):
    with get_connection() as connection:
     cursor = connection.cursor()

     cursor.execute("""
     INSERT INTO knowledge (question, answer)
     VALUES (?, ?) """, (question, answer))

     connection.commit()


#UPDATE
def update_knowledge(question, answer):
    with get_connection() as connection:
     cursor = connection.cursor()

     cursor.execute("""
        UPDATE knowledge
        SET answer = ?
        WHERE question = ?
     """, (answer, question, ))

     connection.commit()


def remove_knowledge(question):                                #talks to the database
    with get_connection() as connection:
     cursor = connection.cursor()

     cursor.execute("""
     DELETE FROM knowledge
     WHERE question = ?""",
    (question,))

     connection.commit()


def knowledge_exists(question):
    with get_connection() as connection:
     cursor = connection.cursor()

     cursor.execute("""
        SELECT * FROM knowledge
        WHERE question = ?
     """, (question,))

     knowledge = cursor.fetchone()


    if knowledge:
        return True

    return False





"""

cursor.execute("SELECT * FROM knowledge")

knowledge = cursor.fetchall()
print(knowledge)
"""