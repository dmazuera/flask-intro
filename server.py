"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISS_LIST = [
    'mean', 'ugly', 'smelly', 'rude', 'nasty', 'gross']



@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the <a href='/hello'> home page. </a> </html>"



# for adjective in AWESOMENESS:
#   <input type="radio" name="compliment" value=adjective>adjective





@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <br>
          Select your compliment:
          <br>
          <input type="radio" name="compliment" value=adjective>adjective
          <input type="radio" name="compliment" value="awesome">Awesome
          <input type="radio" name="compliment" value="terrific">Terrific
          <input type="radio" name="compliment" value="fantastic">Fantastic
          <input type="radio" name="compliment" value="neato">Neato
          <input type="radio" name="compliment" value="fantabulous">Fantabulous
          <input type="radio" name="compliment" value="wowza">Wowza
          <input type="radio" name="compliment" value="oh-so-not-meh">Oh-so-not-meh
          <input type="radio" name="compliment" value="ducky">Ducky
          <input type="radio" name="compliment" value="coolio">Coolio
          <input type="radio" name="compliment" value="incredible">Incredible
          <input type="radio" name="compliment" value="wonderful">Wonderful
          <input type="radio" name="compliment" value="smashing">Smashing
          <input type="radio" name="compliment" value="lovely">Lovely
          <input type="radio" name="compliment" value="brilliant">Brilliant
        <input type="submit" value="Submit Compliment">
          </form>


      </body>
    </html>
    """





@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)




@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = choice(DISS_LIST)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A DISS!!</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """.format(player=player, diss=diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
