import os

from flask import Flask

# The instance path has to be absolute so lets get the absolute path to our
# root directory.
my_directory = os.path.dirname(__file__)
root_directory = os.path.abspath(os.path.join(my_directory, ".."))

# Create the app and configure
app = Flask(__name__,
            instance_path=root_directory,
            instance_relative_config=True)

app.config.from_pyfile("settings.py")
