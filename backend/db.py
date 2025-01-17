import sqlite3

def get_relevant_context(user_query: str) -> str:
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("knowledge_base.db")
        cursor = conn.cursor()

        # Query to search for relevant content (using a LIKE statement for basic matching)
        cursor.execute(
            "SELECT content FROM knowledge_base WHERE content LIKE ? LIMIT 1",
            (f"%{user_query}%",)  # Use wildcards to match the query within the content
        )
        result = cursor.fetchone()

        conn.close()

        # Return the matched content or a default message if no match is found
        return result[0] if result else "No relevant context found."
    except sqlite3.Error as e:
        # Handle database errors
        return f"Database error: {str(e)}"
