import sqlite3
from config import DATABASE_PATH

def get_db_connection():
    """Vytvoří připojení k databázi se správným kódováním řádků."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Umožní přistupovat ke sloupcům přes názvy
    return conn

def init_db():
    """Vytvoří tabulku applications, pokud ještě neexistuje."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            position TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Applied',
            sent_date DATE NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Tabulka applications byla úspěšně inicializována v database/applications.db")

if __name__ == '__main__':
    init_db()
