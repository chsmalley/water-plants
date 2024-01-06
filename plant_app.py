from flask import Flask, render_template, send_file, redirect, url_for
import plotly.graph_objs as go
import pandas as pd
import os
import time
import subprocess

NEEDS_WATER = 400
DROWNING = 300
MOISTURE_FILE = '~/moisture_data.txt'
IMAGE_FILE = os.path.expanduser('~/plants.jpg')
app = Flask(__name__)


# Route to display time series plot
@app.route('/')
def index():
    data = pd.read_csv(MOISTURE_FILE)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    # Creating a Plotly figure for the time series data
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=data['timestamp'],
                   y=data['catnip'],
                   mode='lines',
                   name='Catnip Soil Moisture')
    )
    fig.add_trace(
        go.Scatter(x=data['timestamp'],
                   y=data['spider'],
                   mode='lines',
                   name='Spider Soil Moisture')
    )
    fig.add_hline(y=NEEDS_WATER,
                  line_width=3,
                  line_dash="dash",
                  line_color="brown",
                  name="Needs Water")
    fig.add_hline(y=DROWNING,
                  line_width=3,
                  line_dash="dash",
                  line_color="blue",
                  name="Too Much Water")
    fig.update_layout(
        title='Moisture Data',
        xaxis_title='Time',
        yaxis_title='Value',
        template='plotly_dark'
    )
    # Convert the Plotly figure to HTML and pass to template
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@app.route('/show_image')
def show_image():
    return send_file(IMAGE_FILE, mimetype='image/jpg')

@app.route('/measure', methods=['POST'])
def measure():
    # Your script execution code here
    # For example, execute a sample script
    result = subprocess.run(['python', 'measure_plants.py'])
    return redirect(url_for('index'))

@app.route('/water', methods=['POST'])
def water():
    # Your script execution code here
    # For example, execute a sample script
    subprocess.run(['python', 'water_plants.py'])
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

