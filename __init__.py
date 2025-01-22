from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite2
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
  
if __name__ == "__main__":
  app.run(debug=True)
