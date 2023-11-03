import sqlite3

connect = sqlite3.connect('notes_database.db')
cursor = connect.cursor()

cursor.execute("DROP TABLE IF EXISTS note")
connect.commit()
# exit()
cursor.execute("""
CREATE TABLE IF NOT EXISTS note(
              note_id INTEGER DEFAULT 0 PRIMARY KEY AUTOINCREMENT,
              user_id INTEGER,
              description TEXT,
              date TEXT
)
""")
connect.commit()


def new_note(text: str, user_id: (str, int), cursor: sqlite3.Cursor, connect: sqlite3.Connection) -> None:
    data = {
        "user_id": user_id,
        "description": text
    }
    cursor.execute("INSERT INTO note (user_id, description, date) VALUES(:user_id, :description, CURRENT_TIMESTAMP)", data)
    connect.commit()


def edit_note(note_id: (str, int), article: str, text: str, cursor: sqlite3.Cursor, connect: sqlite3.Connection) -> None:
    pass


def del_note(user_id: (str, int), note_id: (str, int), cursor: sqlite3.Cursor, connect: sqlite3.Connection) -> bool:
    """return True if note deleted, False if note didn't delete"""

    data = {
        "user_id": user_id,
        "note_id": note_id,
    }

    exist = bool(cursor.execute("SELECT * FROM note WHERE user_id = (:user_id) AND note_id = (:note_id)", data).fetchone())
    if exist:
        cursor.execute("DELETE FROM notes WHERE note_id = (:note_id)", data)
        connect.commit()
        return True
    return False


def get_notes(id: (str, int), cursor: sqlite3.Cursor, count = 0) -> list|bool:
    """count 1 = one message, count 0 = all message"""
    data = {"id": id,}
    if not count:
        who_id = "user"
    else:
        who_id = "note"
        
    notes = cursor.execute(f"SELECT note_id, description, date FROM note WHERE {who_id}_id = (:id)", data).fetchall()

    if bool(notes):
        return notes
    return False
