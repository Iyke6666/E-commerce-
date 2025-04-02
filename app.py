from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My First Python Web App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
                background-color: #f0f8ff;
            }
            h1 {
                color: #2c3e50;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to My First Python Web App!</h1>
            <p>Congratulations on running your first web application with Python!</p>
            <p>Try visiting <a href="/hello">/hello</a> or <a href="/greet/yourname">/greet/yourname</a></p>
        </div>
    </body>
    </html>
    """

# Define a route with a simple response
@app.route('/hello')
def hello():
    return "Hello, World!"

# Define a route that takes a parameter
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! Welcome to my web app."

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
