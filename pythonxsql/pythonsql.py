import sqlite3
import csv

action_stack = []

def setup_database():
    """
    creates a SQlite database and a 'students' table if not exists.Uses connect(), cursor(), execute(), commit().
    """
    try:
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        
        cursor.execute('''
                       create table if not exists students(
                           id integer primary key autoincrement,
                           name text not null,
                           grade real check(grade >= 0 and grade<=100)
                           
                       )''')
        
        
        conn.commit()
        
        
                
        print("database and table are ready!")
        
        conn.close()
    except Exception as e:
        print(f"error: {e}")
        
def log_action(action):
    action_stack.append(action)
    if len(action_stack)>5:
        action_stack.pop(0)
        
def show_recent_actions():
    if not action_stack:
        print("no recent actions.")
        return
    print("\n recent actions:")
    for i, act in enumerate(reversed(action_stack), 1):
        print(f"{i}. {act}")

def add_student(name, grade):
    try:
        conn = sqlite3.connet('student.db')
        cursor = conn.cursor()
        conn.commit()
        student_id = cursor.lastrowid
        log_action(f"add student: {name} (id: {student_id}, grade: {grade})")
        print(f"student {name} added with id {id} and grade {grade}")
        conn.close()
    except sqlite3.Error as e:
        print("error,"e)
except Exception as e:
    print("unexpected error:    "e)
        
