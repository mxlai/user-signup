from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

signup_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>Signup</h1>
    <form method="post">
        <table>
            <tr>
                <td>
                    <label>Username</label>
                </td>
                <td>
                    <input name ="username" type="text" value="{username}" />
                </td>
                <td>
                    <p class="error">{username_error}</p>
                </td>
            </tr>
            <tr>
                <td>
                    <label>Password</label>
                </td>
                <td>
                    <input name="password" type="password" value="{password}" />
                </td>
                <td>
                    <p class="error">{password_error}</p>
                </td>
            </tr>
            <tr>
                <td>
                    <label>Verify Password</label>
                </td>
                <td>
                    <input name="confirm" type="password" value="{confirm}" />
                </td>
                <td>
                    <p class="error">{confirm_error}</p>
                </td>
            </tr>
            <tr>
                <td>
                    <label>Email (optional)</label>
                </td>
                <td>
                    <input name="email" type="text" value="{email}" />
                </td>
                <td>
                    <p class="error">{email_error}</p>
                </td>
            </tr>
        </table>
        <input type="submit">
    </form>
    """

@app.route("/user-signup")
def display_signup_form():
    return signup_form.format(username='', username_error='', password='', password_error='', confirm='', confirm_error='', email='', email_error='')

def is_empty(string):
    if len(string) == 0:
        return True

def has_blank_spaces(string):
    for char in string:
        if char == ' ':
            return True

def has_at(string):
    if string.count('@') == 1:
        return True

def has_dot(string):
    if string.count('.') == 1:
        return True

@app.route("/user-signup", methods=['POST'])
def validate_input():

    username = request.form['username']
    username_error = ''
    password = request.form['password']
    password_error = ''
    confirm = request.form['confirm']
    confirm_error = ''
    email = request.form['email']
    email_error = ''

    if is_empty(username):
        username_error = 'Please enter a username.'
        username = ''
    elif has_blank_spaces(username):
        username_error = 'Invalid username: May not contain blank spaces.'
        username = ''
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Invalid username: Must be between 3 to 20 characters in length.'
        username = ''

    if is_empty(password):
        password_error = 'Please enter a password.'
        password = ''
    elif has_blank_spaces(password):
        password_error = 'Invalid password: May not contain blank spaces.'
        password = ''
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Invalid password: Must be between 3 to 20 characters in length.'
        password = ''

    if is_empty(confirm):
        confirm_error = 'Confirm password.'
        confirm = ''
    elif confirm != password:
        confirm_error = 'Password does not match.'
        confirm = ''

    if is_empty(email):
        email_error = ''
    elif not has_at(email) or not has_dot(email):
        email_error = 'Invalid email address.'
        email = ''
    elif has_blank_spaces(email):
        email_error = 'Invalid email address: May not contain blank spaces.'
        email = ''
    elif len(email) < 3 or len(email) > 20:
        email_error = 'Invalid email address: Must be between 3 to 20 characters in length'
        email = ''

    if not username_error and not password_error and not confirm_error:
        return 'Welcome, ' + username + '!'
    else:
        return signup_form.format(username=username, username_error=username_error, password=password, password_error=password_error, confirm=confirm, confirm_error=confirm_error, email=email, email_error=email_error) 

app.run()