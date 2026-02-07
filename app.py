# S1: Import Flask
from flask import Flask, request, render_template
import re

# S2: Initialize object:
app = Flask(__name__)

# S3: Route:
# Task: Takes 'name' from query parameter and converts to UPPER CASE
@app.route('/')
def home():
    # Looks for ?name=yourname in the URL
    user_name = request.args.get('name', 'Guest')
    upper_name = user_name.upper()
    
    return f"<h1>Hello, {upper_name}!</h1><p>Welcome to the Upper Case Home Page.</p>"
# ---------------- REGEX MATCHER ROUTE ----------------
@app.route('/regex', methods=['GET', 'POST'])
def regex_matcher():
    matches = []
    error = None

    if request.method == 'POST':
        test_string = request.form.get('test_string')
        regex_pattern = request.form.get('regex_pattern')

        try:
            matches = re.findall(regex_pattern, test_string)
        except re.error:
            error = "Invalid Regular Expression"

    return render_template(
        'regex.html',
        matches=matches,
        error=error
    )

# S4: Run the Application:
if __name__ == '__main__':
    app.run(debug = True)


