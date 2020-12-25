from flask import Flask, request, make_response
import io
import os
import csv
import pandas as pd

app = Flask(__name__)


@app.route('/pandas2csv')
def pandas2csv():
    """
    Returns the monthly weather averages (Montreal, year=2019)
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

    # Load the dataframe, average it and send the averages
    df = pd.read_csv(csv_path)
    means = df.mean(axis=0)

    # Create a csv response from the new dataframe
    response = make_response(means.to_csv(header=["average montly value"]))
    response.headers["Content-Disposition"] = "attachment; filename=%s" % csv_file
    response.headers["Content-Type"] = "text/csv"
    return response


@app.route('/')
def myapp():
    message = "To use this app: %s/pandas2csv?month=value" % request.base_url
    return message



