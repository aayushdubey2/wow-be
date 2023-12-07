from flask_restx import fields
from .extensions import api

login_model = api.model('LoginModel', {'Email': fields.String, 'Password': fields.String })
response_model = api.model('LoginResponse', {'message': fields.String, 'name': fields.String, 'type': fields.String, 'id': fields.Integer })


customer_info_model = api.model('CustomerInfo', {
    'full_name': fields.String,
    'email': fields.String,
    'type': fields.String,
    'id': fields.Integer
})

rental_class_model = api.model('RentalClassModel', {
    'Class': fields.String(required=True),
    'DailyRate': fields.Float(required=True),
    'OverMileageFee': fields.Float(required=True)
})

vehicle_model = api.model('VehicleClassModel', {
    'Make': fields.String,
    'Model': fields.String,
    'Year': fields.Integer,
    'LicensePlateNumber': fields.String,
    'OdometerReading': fields.Integer,
    'Image': fields.String,
    'Class': fields.String
})

vehicle_list = api.model('VehicleList', {
    'VIN': fields.Integer,
    'Make': fields.String,
    'Model': fields.String,
    'Year': fields.Integer,
    'LicensePlateNumber': fields.String,
    'OdometerReading': fields.Integer,
    'Image': fields.String,
    'RentalClass': fields.Nested(rental_class_model),
})

rental_service_detail = api.model('RentalServiceDetail', {
    'VehicleID': fields.String,
    'CustomerID': fields.Integer,
    'PickupLocation': fields.String,
    'DropOffLocation': fields.String,
    'PickupDate': fields.Date,
    'DropOffDate': fields.Date,
    'StartOdometer': fields.Integer,
    'DailyOdometerLimit': fields.Integer,
    'UnlimitedMileageOption': fields.Boolean,
    'RentalStatus': fields.String,
})

rental_list = api.model('RentalList', {
    'RentalID': fields.Integer,
    'VehicleID': fields.Integer,
    'CustomerID': fields.Integer,
    'PickupLocation': fields.String,
    'DropOffLocation': fields.String,
    'PickupDate': fields.Date,
    'DropOffDate': fields.Date,
    'StartOdometer': fields.Integer,
    'EndOdometer': fields.Integer,
    'DailyOdometerLimit': fields.Integer,
    'UnlimitedMileageOption': fields.Boolean,
    'RentalStatus': fields.String,
})