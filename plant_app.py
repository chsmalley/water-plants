from flask import Flask, render_template, send_file
import plotly.graph_objs as go
import pandas as pd
import os
import time

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
                   y=data['moisture'],
                   mode='lines',
                   name='Moisture Data')
    )
    fig.update_layout(
        title='Moisture Data',
        xaxis_title='Time',
        yaxis_title='Value',
        template='plotly_dark'
    )

    # Convert the Plotly figure to HTML and pass to template
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@app.route('/image')
def show_image():
    return send_file(IMAGE_FILE, mimetype='image/jpg')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

