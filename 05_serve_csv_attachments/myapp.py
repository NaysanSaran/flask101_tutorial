from flask import Flask, request, send_file
import io
import os
import csv

app = Flask(__name__)


@app.route('/get_csv')
def get_csv():
    """
    Returns the monthly weather csv file (Montreal, year=2019)
    corresponding to the month passed as parameter.
    """

    # Checking that the month parameter has been supplied
    if not "month" in request.args:
        return "ERROR: value for 'month' is missing"
    # Also make sure that the value provided is numeric
    try:
        month = int(request.args["month"])
    except:
        return "ERROR: value for 'month' should be between 1 and 12"

    csv_dir  = "./static"
    csv_file = "2019_%02d_weather.csv" % month
    csv_path = os.path.join(csv_dir, csv_file)
    
    # Also make sure the requested csv file does exist
    if not os.path.isfile(csv_path):
        return "ERROR: file %s was not found on the server" % csv_file
    # Send the file back to the client
    return send_file(csv_path, as_attachment=True, attachment_filename=csv_file)


@app.route('/')
def myapp():
    message = "To use this app: %s/get_csv?month=value" % request.base_url
    return message



