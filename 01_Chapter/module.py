# Install a package use PIP followed by package name
# pip install pyjokes
# here we used a module named pyjokes to print random jokes

import pyjokes

joke : str = pyjokes.get_joke()
print("Printing Joke -")
print(joke)