from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def connect():
    return sqlite3.connect('filmflix.db')

@app.route('/')
def index():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tblfilms')
    records = cursor.fetchall()
    conn.close()
    return render_template('index.html', records=records)

@app.route('/add', methods=['POST'])
def add_record():
    title = request.form['title']
    year = int(request.form['year'])
    rating = request.form['rating']
    duration = int(request.form['duration'])
    genre = request.form['genre']
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tblfilms (title, yearReleased, rating, duration, genre)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, year, rating, duration, genre))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:film_id>')
def delete_record(film_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tblfilms WHERE filmID = ?', (film_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:film_id>', methods=['GET', 'POST'])
def edit_record(film_id):
    if request.method == 'POST':
        title = request.form['title']
        year = int(request.form['year'])
        rating = request.form['rating']
        duration = int(request.form['duration'])
        genre = request.form['genre']
        
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE tblfilms
            SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ?
            WHERE filmID = ?
        ''', (title, year, rating, duration, genre, film_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tblfilms WHERE filmID = ?', (film_id,))
    record = cursor.fetchone()
    conn.close()
    return render_template('edit.html', record=record)

if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
