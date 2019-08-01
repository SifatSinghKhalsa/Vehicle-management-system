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

@app.route('/fuel/<vehicle_number>', methods=['GET'])
def fuel_info(vehicle_number):
    return "You're Trying to Access Fuel Records for Vehicle Number {}".format(vehicle_number)

@app.route('/dealer/<dealer_id>', methods=['GET'])
def dealer_info(dealer_id):
    return "You're Trying to Access Dealer Information Records for Dealer ID {}".format(dealer_id)

@app.route('/insurance/<insurance_id>', methods=['GET'])
def insurance_info(insurance_id):
    return "You're Trying to Access Insurance Information Records for Insurance ID {}".format(insurance_id)

@app.route('/user/<user_id>', methods=['GET'])
def insurance_info(user_id):
    return "You're Trying to Access User Information Records for User ID {}".format(user_id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='5000')