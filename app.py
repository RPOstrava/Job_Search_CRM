from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/add', methods=['GET', 'POST'])
def add_application():
    if request.method == 'POST':
        company = request.form['company']
        position = request.form['position']
        status = request.form['status']
        sent_date = request.form['sent_date']
        
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO applications (company, position, status, sent_date)
            VALUES (?, ?, ?, ?)
        ''', (company, position, status, sent_date))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
        
    # Dnešní datum jako výchozí hodnota do formuláře
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template('add.html', statuses=STATUS_OPTIONS, today=today)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_application(id):
    conn = get_db_connection()
    application = conn.execute('SELECT * FROM applications WHERE id = ?', (id,)).fetchone()
    
    if application is None:
        conn.close()
        return "Žádost nenalezena", 404
        
    if request.method == 'POST':
        company = request.form['company']
        position = request.form['position']
        status = request.form['status']
        sent_date = request.form['sent_date']
        
        conn.execute('''
            UPDATE applications
            SET company = ?, position = ?, status = ?, sent_date = ?
            WHERE id = ?
        ''', (company, position, status, sent_date, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
        
    conn.close()
    return render_template('edit.html', application=application, statuses=STATUS_OPTIONS)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_application(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM applications WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
