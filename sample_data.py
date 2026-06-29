from database import init_db, get_db_connection
from datetime import date

def insert_sample_data():
    # Inicializace prázdné tabulky
    init_db()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Testovací data s různými daty pro ověření řazení
    samples = [
        ('Google', 'Python Developer', 'Interview', '2026-06-25'),
        ('Microsoft', 'Backend Engineer', 'Applied', '2026-06-26'),
        ('Red Hat', 'Linux Specialist', 'Rejected', '2026-06-20'),
        ('Avast', 'Security QA', 'Offer', '2026-06-27'),
    ]
    
    cursor.executemany('''
        INSERT INTO applications (company, position, status, sent_date)
        VALUES (?, ?, ?, ?)
    ''', samples)
    
    conn.commit()
    conn.close()
    print("Testovací data byla úspěšně vložena!")

if __name__ == '__main__':
    insert_sample_data()
