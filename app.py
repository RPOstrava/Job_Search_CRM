from flask import Flask, render_template, request, redirect, url_url
from database import get_db_connection
from datetime import datetime

app = Flask(__name__)

# Seznam povolených stavů pro formuláře a filtry
STATUS_OPTIONS = ['Applied', 'Interview', 'Rejected', 'Offer', 'Hired']

@app.route('/')
def index():
    status_filter = request.args.get('status')
    conn = get_db_connection()
    
    # Automatické řazení od nejnovějších (ORDER BY sent_date DESC)
    if status_filter and status_filter in STATUS_OPTIONS:
        query = "SELECT * FROM applications WHERE status = ? ORDER BY sent_date DESC"
        applications = conn.execute(query, (status_filter,)).fetchall()
    else:
        query = "SELECT * FROM applications ORDER BY sent_date DESC"
        applications = conn.execute(query).fetchall()
        status_filter = ''
        
    conn.close()
    return render_template('index.html', applications=applications, statuses=STATUS_OPTIONS, current_filter=status_filter)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_application(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM applications WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Tento blok zajistí spuštění Flask serveru při spuštění app.py
if __name__ == '__main__':
    app.run(debug=True)
