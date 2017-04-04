# Python Modules
from flask import Flask, redirect, url_for, request, render_template
import jinja2

#################################################################################
#
# instantiate the app
#
#################################################################################

app = Flask(__name__)

#################################################################################
#
# route the requests
#
#################################################################################

@app.route('/forecasting', methods=['GET']):
def landing_page():
	return render_template("index.html")