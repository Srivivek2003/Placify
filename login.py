from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'vivek'

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Vivek@123'
app.config['MYSQL_DB'] = 'vivekdb'

mysql = MySQL(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form:
        name = request.form['name']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE name = %s AND password = %s', (name, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['name'] = account['name']
            session['password'] = account['password']
            msg = 'Logged in successfully!'
            return redirect('/places')
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/places', methods=['GET', 'POST'])
def places():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM places")
    places = cur.fetchall()
    cur.close()
    return render_template('places.html', places=places)

@app.route('/seema2a', methods=['GET', 'POST'])
def seema2a():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM places")
    places = cur.fetchall()
    cur.close()
    return render_template('seema2a.html', places=places)

@app.route('/seema1a', methods=['GET', 'POST'])
def seema1a():
    return render_template('seema1a.html', places=places)

@app.route('/seema3a', methods=['GET', 'POST'])
def seema3a():
    return render_template('seema3a.html', places=places)

@app.route('/seema4a', methods=['GET', 'POST'])
def seema4a():
    return render_template('seema4a.html', places=places)

@app.route('/seema5a', methods=['GET', 'POST'])
def seema5a():
    return render_template('seema5a.html', places=places)

@app.route('/seema6a', methods=['GET', 'POST'])
def seema6a():
    return render_template('seema6a.html', places=places)

@app.route('/seema7a', methods=['GET', 'POST'])
def seema7a():
    return render_template('seema7a.html', places=places)

@app.route('/seema8a', methods=['GET', 'POST'])
def seema8a():
    return render_template('seema8a.html', places=places)

@app.route('/seema9a', methods=['GET', 'POST'])
def seema9a():
    return render_template('seema9a.html', places=places)
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('name', None) 
    return redirect('/login')
if __name__ == '__main__':
    app.run(debug=True)
