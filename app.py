from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# ---------- DATABASE SETUP ----------
# ---------- DATABASE SETUP2 ----------
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        age INTEGER NOT NULL
                    )''')
    conn.close()

init_db()

# ---------- READ ----------
@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

# ---------- CREATE ----------
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']

        conn = sqlite3.connect('database.db')
        conn.execute('INSERT INTO users (name, email, age) VALUES (?, ?, ?)', (name, email, age))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

# ---------- UPDATE ----------
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    user = conn.execute('SELECT * FROM users WHERE id=?', (id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        conn.execute('UPDATE users SET name=?, email=?, age=? WHERE id=?', (name, email, age, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('update.html', user=user)

# ---------- DELETE ----------
@app.route('/delete/<int:id>')
def delete_user(id):
    conn = sqlite3.connect('database.db')
    conn.execute('DELETE FROM users WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# ---------- RUN ----------
if __name__ == '__main__':
    app.run(debug=True)
