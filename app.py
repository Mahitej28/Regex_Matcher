from flask import Flask, request, render_template

import re

app = Flask(__name__, static_url_path='/static', static_folder='static')

def find_matches(test_string, regex_pattern):
    matches = re.finditer(regex_pattern, test_string)
    match_list = []
    for match in matches:
        match_list.append(match.group())
    return match_list

def is_valid_email(email):
    # Regular expression pattern for email validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        test_string = request.form["test_string"]
        regex_pattern = request.form["regex_pattern"]
        matches = find_matches(test_string, regex_pattern)
        return render_template("index.html", matches=matches)
    return render_template("index.html")

@app.route("/validate-email", methods=["GET", "POST"])
def validate_email():
    if request.method == "POST":
        email = request.form["email"]
        is_valid = is_valid_email(email)
        return render_template("email.html", email=email, is_valid=is_valid)
    return render_template("email.html")

if __name__ == "__main__":
    app.run(debug=True)
