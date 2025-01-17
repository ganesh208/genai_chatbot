from PyPDF2 import PdfReader
import sqlite3

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def insert_text_into_database(db_path, text):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS knowledge_base (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT
    )
    """)

    # Insert text into the database
    cursor.execute("INSERT INTO knowledge_base (content) VALUES (?)", (text,))
    conn.commit()
    conn.close()

    print("Text inserted into database successfully.")

# Path to your PDF and SQLite database
pdf_path =  r"C:\Users\DELL\Desktop\Projects\genai_chatbots\backend\java_doc.pdf"
db_path = "knowledge_base.db"

# Extract text from the PDF
text = extract_text_from_pdf(pdf_path)

# Insert text into the database
insert_text_into_database(db_path, text)
