import sqlite3

from flask import g, Flask, render_template, request

database = r"C:\Users\melissa\OneDrive\Documents\DURHAM COLLEGE\AIDI\1B\AIDI 2004 - AI In Enterprise Systems\ASSIGNMENTS\ASSIGNMENT #1\studentapp\db\students.db"

app = Flask(__name__)


# Function to retrieve the database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    db.row_factory = make_dicts
    return db


# Function to close database connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Returns retrieved rows as dictionaries for easier manipulation
def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


# Function to query database easily
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


# Home page created to show a summary of the 10 latest entries
@app.route('/home')
def home_page():
    x = query_db('SELECT student_id, first_name, last_name, amount_due '
                 'FROM students '
                 'ORDER BY date_entered DESC '
                 'LIMIT 10;')
    return render_template('home.html', result=x)


# Summary page which retrieve all records
@app.route('/summary')
def summary():
    x = query_db('SELECT student_id, first_name, last_name, amount_due '
                 'FROM students '
                 'ORDER BY date_entered DESC;')
    return render_template('summary.html', result=x)


# Student detail page - shows all fields in page
@app.route('/<int:student_id>')
def student_detail(student_id):
    x = query_db('SELECT * '
                 'FROM students '
                 'WHERE student_id = ?;', [student_id], one=True)
    return render_template('student_detail.html', result=x)

# Form to submit new student's information
@app.route('/new')
def new():
    return render_template('new_student.html')


@app.route('/add_success', methods=['GET', 'POST'])
def add_success():
    if request.method == 'POST':
        x = request.form

        # Insert the items into the database
        get_db().execute('INSERT INTO students '
                         'VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP )', [x['student_id'], x['first_name'],
                                                                        x['last_name'], x['date_of_birth'],
                                                                        x['amount_due']])
        get_db().commit()
        return render_template('new_student_confirmation.html', result=x)


@app.route('/edit/<int:student_id>')
def edit_student(student_id):
    x = query_db('SELECT * '
                 'FROM students '
                 'WHERE student_id = ?;', [student_id], one=True)
    return render_template('edit_student.html', result=x)


@app.route('/edit_success', methods=['GET', 'POST'])
def edit_success():
    if request.method == 'POST':
        x = request.form

        # Insert the items into the database
        get_db().execute('UPDATE students '
                         'SET student_id = ?, first_name = ?, last_name = ?, date_of_birth = ?, amount_due = ?,'
                         'date_entered = CURRENT_TIMESTAMP '
                         'WHERE student_id = ?;', [x['student_id'], x['first_name'], x['last_name'], x['date_of_birth'],
                                                   x['amount_due'], x['orig_student_id']])
        get_db().commit()
        return render_template('student_edit_confirmation.html', result=x)


@app.route('/delete')
def delete_records():
    x = query_db('SELECT * '
                 'FROM students '
                 'ORDER BY date_entered DESC;')
    return render_template('delete.html', result=x)


@app.route('/delete_confirm', methods=['GET', 'POST'])
def delete_confirm():
    if request.method == 'POST':
        # Get list of IDs from checkboxes
        delete_ids = request.form.getlist('delete_id')
        print(delete_ids)

        # Create SQL query to hold all IDs
        query = """SELECT * FROM students WHERE student_id in ({});""".format(','.join(['?']*len(delete_ids)))

        # Execute query
        x = query_db(query, delete_ids)

    return render_template('delete_student_check.html', result=x, ids=delete_ids)


@app.route('/delete_success', methods=['GET', 'POST'])
def delete_success():
    if request.method == 'POST':
        x = request.form.getlist('delete_ids')

        # Create delete query
        query = """DELETE FROM students WHERE student_id in ({});""".format(','.join(['?'] * len(x)))

        # Execute query
        get_db().execute(query, x)
        get_db().commit()

    return render_template('delete_student_confirmation.html', result=x)


if __name__ == '__main__':
    app.run()
