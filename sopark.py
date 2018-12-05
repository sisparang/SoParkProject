from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from contextlib import closing

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sisparang'
app.config['MYSQL_DATABASE_DB'] = 'sopark'
app.config['MYSQL_DATABASE_HOST'] = '192.168.20.113'
mysql.init_app(app)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/show')
def show():
    return render_template('signup.html')

@app.route('/signup', methods=['POST','GET'])
def signup():
    try:
        _id = request.form['inputId']
        _idname = request.form['inputIdName']
        _name = request.form['inputName']
        _password = request.form['inputPassword']
        if _id and _idname and _name and _password:

            with closing(mysql.connect()) as conn:
                with closing(conn.cursor()) as cursor:
                    # _hashed_password = generate_password_hash(_password)
                    cursor.callproc('sp_createUser',(_id,_idname,_name,_password))
                    # cursor.callproc('sp_createUser',(_id,_idname,_name,_hashed_password))
                    data = cursor.fetchall()

                    if len(data) is 0:
                        conn.commit()
                        return json.dumps({'message':'User Created Successfuly!!'})
                    else:
                        return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields !!</span>'})
    except Exception as e:
        return json.dumps({'error':str(e)})

if __name__ == '__main__':
    app.run(debug=True)

