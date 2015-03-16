from flask import Flask
from flask import request
from flask import render_template
import plotly.plotly as py
from plotly.graph_objs import *

app = Flask(__name__)

# OUR HOME PAGE
#============================================
@app.route('/', methods=['GET', 'POST'])
def welcome():
    trace0 = Scatter(
        x=[1, 2, 3, 4],
        y=[10, 15, 13, 17]
    )
    trace1 = Scatter(
        x=[1, 2, 3, 4],
        y=[16, 5, 11, 9]
    )
    data = Data([trace0, trace1])

    chart = py.iplot(data, filename = 'basic-line')
    # print 
    # return chart.embed_code 
    return render_template('index.html', data=chart.resource)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969, debug=True)