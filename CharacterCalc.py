from faker import Faker
fake = Faker()
import sqlite3
from sqlite3 import Error
import os.path
from os.path import exists

DBPath = "assignment9.db"

#IF DB NOT EXISTS Create Table & Generate and importe Data
try:
    if os.path.exists(DBPath):
        connection = sqlite3.connect(DBPath)
        cursor = connection.cursor()
    else:
        connection = sqlite3.connect(DBPath)
        cursor = connection.cursor()
        query1 = '''CREATE TABLE IF NOT EXISTS sentences(id INTEGER PRIMARY KEY, sentence TEXT)'''
        cursor.execute(query1)
        # Generate 1 million records
        print("Please wait...")
        print("we are importing records......")
        TotalRecord = 100 #You Can chenge it to 1000000
        for FakeCunter in range(TotalRecord):
            FakeSentence = fake.paragraph(nb_sentences=5, variable_nb_sentences=False)
            cursor.execute("INSERT INTO sentences (id, sentence) VALUES (?,?)" , (FakeCunter, FakeSentence))
            connection.commit()

    #Fetch First Row sentence Field
    cursor.execute('SELECT * FROM sentences limit 1')
    result = cursor.fetchone()
    Sentence = result[1]

    # Check Occurrence With This Sentence if the generated sentences doesnt have any occurrence

    #Sentence = "Hello My Name is Arian and i am an Ai & Machine Learning Student . i love Machine Learning ."

    #Get Longest Word
    LongestWord = max(Sentence.split(), key=len)

    #Get Longest Word Occurrence
    WordsList = list(Sentence.split())
    Occurrence = WordsList.count(LongestWord)

    print("Target Sentence : " , Sentence)
    print("How Many characters in The First Row : ", len(Sentence))
    print("The Longest word is : ", LongestWord)
    print("The number of characters : ", len(LongestWord))
    print("Occurrence : " , Occurrence)

    cursor.close()
    connection.close()

except:
    print("DB Path Error. Try to Change it")
