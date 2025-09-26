from flask import Flask, Response, send_file

app = Flask(__name__)

@app.route("/")
def home():
    html_content = '''
    <html>
    <head><title>Inflation Rate Predictions</title></head>
    <body>
        <h1>Actual vs Predicted Inflation Rates (LSTM)</h1>
        <img src="/LSTM.jpg" alt="LSTM Plot" style="width:80%;max-width:800px;"><br><br>

        <h1>Actual vs Predicted Inflation Rates (RNN or Raw)</h1>
        <img src="/R.jpg" alt="RNN/Raw Plot" style="width:80%;max-width:800px;">
    </body>
    </html>
    '''
    return Response(html_content, mimetype='text/html')

@app.route("/LSTM.jpg")
def lstm_image():
    return send_file("LSTM.jpg", mimetype='image/jpeg')

@app.route("/R.jpg")
def r_image():
    return send_file("R.jpg", mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug=True)
