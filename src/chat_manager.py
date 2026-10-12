# chat_manager.py
# This file contains the data structures for the AI Chat Manager

# A list to hold all chat session dictionaries
sessions = []


# Our first session - a dictionary wih three fields
session_1 = {
      'session_name': 'Python Decorators Deep Dive',
      'date': '2025-01-20',
      'topics': ['python', 'decorators', 'functions']

}

#Add the session to our list
sessions.append(session_1)
print("Session added successfully!")

#Print all current chat sessions
print ("--- Current Chat Session ---")
for session in sessions:
    print(session)
print("---------------------------------------")

#Create a second session
session_2 = {
        'session_name': 'Advanced Python Metaclasses',
        'date': '2025-02-15',
        'topics': ['python', 'metaclasses', 'object-oriented programming']
}

#Add the second session to our list
session_2 ={
    'session_name':'Docker Setup for Flask',
    'date': '2025-01-21',
    'topics': ['docker', 'flask', 'devops']
}

#Add the seccond session to our list
sessions.append(session_2)
print("\nSecond session added successfully!")

#Print all chat sessions again to show the change
print("n\Second session added successfully!")
for session in sessions:
    print(session)
print("---------------------------------------")