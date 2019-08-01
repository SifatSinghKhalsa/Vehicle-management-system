from flask import Flask, jsonify, make_response, flash, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Vehicle Management API is active"

@app.route('/vehicle/<vehicle_number>', methods=['GET'])
def vehicle_info(vehicle_number):
    return "You're Trying to Access Vehicle Information for Vehicle Number {}".format(vehicle_number)

@app.route('/maintenance/<vehicle_number>', methods=['GET'])
def maintenance_info(vehicle_number):
    return "You're Trying to Access Maintence Records for Vehicle Number {}".format(vehicle_number)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='5000')