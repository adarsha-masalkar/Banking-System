from flask import Flask, request, redirect, render_template
import random

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/users')
def user():
    import mysql.connector
    import datetime

    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='BankingData'
    )
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Users')
    users = []
    for i in cursor:
        users.append(i)
    cursor.close()
    db.disconnect()
    return render_template('users.html', users=users)


@app.route('/transactions', methods=["GET", "POST"])
def transacts():
    import mysql.connector
    import datetime

    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='BankingData'
    )
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Users')
    users = []
    for i in cursor:
        users.append(i)

    cursor.execute('SELECT * FROM Transactions')
    res = []
    for i in cursor:
        res.append(i)

    if request.method == 'POST':
        cursor.execute('INSERT INTO Transactions (id, sender, receiver, amount) VALUES (%s, %s, %s, %s)',
                       (random.getrandbits(16), request.form['sender'], request.form['receiver'], float(request.form['amt'])))
        cursor.execute('SELECT * FROM Users WHERE Name = %s', (request.form['sender'],))
        for i in cursor:
            sender = i[2]
        sender = sender - float(request.form['amt'])

        cursor.execute("UPDATE Users SET Balance = %s WHERE name = %s", (sender, request.form['sender']))
        cursor.execute('SELECT * FROM Users WHERE Name = %s', (request.form['receiver'],))
        for i in cursor:
            receiver = i[2]
        receiver = receiver + float(request.form['amt'])
        cursor.execute("UPDATE Users SET Balance = %s WHERE name = %s", (receiver, request.form['receiver']))
        db.commit()
        # except:
        #     return 'There was an error. Try again.'
        cursor.close()
        db.disconnect()
        return redirect('/transactions')
    else:
        return render_template('transactions.html', users=users, transactions=res)


try:
    app.run(debug=True)
except KeyboardInterrupt:
    exit()
