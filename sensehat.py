from flask import Flask, jsonify
import datetime
from sense_hat import SenseHat

sense = SenseHat()

app = Flask(__name__)

@app.route('/API/temp', methods=['GET'])
def temp():
    temp = sense.get_temperature()
    temp = round(temp, 1)

    now = datetime.datetime.now()
    
    Temp = [
            {
            'Temperature' : temp,
            'Year' : now.year,
            'Month' : now.month,
            'Day' : now.day,
            'Hour' : now.hour,
            'Minute' : now.minute,
            'seconds' : now.second
            }
            ]

    return jsonify({'Temp' : Temp})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
