
from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name.capitalize()}!"


@app.route('/repeat/35/hello')
def repeat_hello():
    print(repeat_hello)
    return "hello" *35

@app.route('/repeat/80/bye')
def repeat_bye():
    print(repeat_bye)
    return "bye" * 80

@app.route('/repeat/99/dogs')
def repeat_dogs():
    print(repeat_dogs)
    return "dogs" * 99



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
