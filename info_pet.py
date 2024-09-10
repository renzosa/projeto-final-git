from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('dados/pets.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS pets (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, peso REAL)')
    conn.close()

@app.route('/')
def listar_pets():
    conn = get_db_connection()
    pets = conn.execute('SELECT * FROM pets').fetchall()
    conn.close()
    return render_template('lista_pets.html', pets=pets)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_pet():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = int(request.form['idade'])
        peso = float(request.form['peso'])
        
        conn = get_db_connection()
        cursor = conn.execute('INSERT INTO pets (nome, idade, peso) VALUES (?, ?, ?)', (nome, idade, peso))
        pet_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return redirect(url_for('visualizar_pet', id=pet_id))
    
    return render_template('formulario.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_pet(id):
    conn = get_db_connection()
    pet = conn.execute('SELECT * FROM pets WHERE id = ?', (id,)).fetchone()
    
    if request.method == 'POST':
        nome = request.form['nome']
        idade = int(request.form['idade'])
        peso = float(request.form['peso'])
        
        conn.execute('UPDATE pets SET nome = ?, idade = ?, peso = ? WHERE id = ?', (nome, idade, peso, id))
        conn.commit()
        conn.close()
        return redirect(url_for('visualizar_pet', id=id))
    
    conn.close()
    return render_template('formulario.html', pet=pet)

@app.route('/visualizar/<int:id>')
def visualizar_pet(id):
    conn = get_db_connection()
    pet = conn.execute('SELECT * FROM pets WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('resultado.html', pet=pet)

@app.route('/excluir/<int:id>')
def excluir_pet(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM pets WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('listar_pets'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)