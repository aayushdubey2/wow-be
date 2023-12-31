from flask_restx import fields
from .extensions import api

login_model = api.model('LoginModel', {'Email': fields.String, 'Password': fields.String })
response_model = api.model('LoginResponse', {'message': fields.String, 'name': fields.String, 'type': fields.String, 'id': fields.Integer })
admin_response_model = api.model('AdminLoginResponse', {'message': fields.String, 'name': fields.String  })

admin_model = api.model('AdminModel', {   
    'FullName' : fields.String,
    'Email' : fields.String,
    'Password' : fields.String
})

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

rental_update_model = api.model('RentalUpdate', {
    'EndOdometer': fields.Integer(required=True, description='New value for EndOdometer'),
    'RentalStatus': fields.String(required=True, description='New value for RentalStatus')
})

vehicle_update_model = api.model('VehicleUpdate', {
    'OdometerReading': fields.Integer(required=True, description='New value for Odometer'),
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

rental_location_model = api.model('RentalLocationModel', {
    'LocationID': fields.Integer,
    'FullAddress': fields.String,
    'PhoneNumber': fields.String,
    'Image': fields.String
})

rental_model = api.model('RentalModel', {
    'FullAddress': fields.String,
    'PhoneNumber': fields.String,
    'Image': fields.String
})

invoice_model = api.model('InvoiceModel', {
    'InvoiceID': fields.Integer,
    'RentalID' : fields.Integer,
    'InvoiceDate' : fields.Date,
    'InvoiceAmount' : fields.Float
})

payment_model = api.model('PaymentModel', {
    'PaymentID' : fields.Integer,
    'InvoiceID' : fields.Integer,
    'CouponID' : fields.Integer,
    'PaymentDate' : fields.Date,
    'PaymentMethod' : fields.String,
    'CardNumber' : fields.String
})

update_payment_model = api.model('UpdatePaymentModel', {
    'InvoiceID' : fields.Integer,
    'CouponID' : fields.Integer,
    'PaymentMethod' : fields.String,
    'CardNumber' : fields.String
})


coupon_model = api.model('CouponModel', {
    'CouponID' : fields.Integer,
    'CouponCode' : fields.String,
    'DiscountPercentage' : fields.Float,
    'ValidityStartDate' : fields.Date,
    'ValidityEndDate' : fields.Date,
})

add_coupon_model = api.model('AddCouponModel', {
    'CouponCode' : fields.String,
    'DiscountPercentage' : fields.Float,
    'ValidityStartDate' : fields.Date,
    'ValidityEndDate' : fields.Date,
})

customer_model = api.model('Customer', {
    'CustomerID': fields.Integer,
    'Type': fields.String,
    'FullName': fields.String,
    'Address': fields.String,
    'Email': fields.String,
    'Image': fields.String,
    'Phone': fields.String,
    'DriverLicenseNumber': fields.String,
    'InsuranceCompanyName': fields.String,
    'InsurancePolicyNumber': fields.String,
    'CorporationName': fields.String,
    'RegistrationNumber': fields.String,
    'EmployeeID': fields.String,
})