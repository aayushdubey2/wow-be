# resources.py
import datetime
from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from sqlalchemy import text  # Import the text function
from .apimodels import *
from dateutil.parser import parse
from .models import *
from .extensions import db

api = Namespace('api', description='API operations')

@api.route('/register')
class CustomerResource(Resource):
    @api.expect(api.model('CustomerModel', {'Type': fields.String(required=True),
                                            'FullName': fields.String, 'Address': fields.String,
                                            'Email': fields.String, 'Password': fields.String, 'Phone': fields.String,
                                            "DriverLicenseNumber": fields.String,
                                            "InsuranceCompanyName": fields.String, "InsurancePolicyNumber": fields.String,
                                            "CorporationName": fields.String, "RegistrationNumber": fields.String, "EmployeeID": fields.String
                                            }))
    @api.marshal_with(customer_info_model)
    def post(self):
        try:
            # Extract data from the request
            data = request.json
            type = data.get('Type')
            full_name = data.get('FullName')
            address = data.get('Address')
            email = data.get('Email')
            password = data.get('Password')
            phone = data.get('Phone')

            # Start a transaction
            with db.session.begin():
                # Insert into Customers table
                customer = Customers(Type=type, FullName = full_name, Address = address, Email = email, Phone = phone, Password = password)
                db.session.add(customer)
                db.session.flush()  # Flush to get the auto-generated ID

                customer_id = customer.CustomerID

                if type == 'individual':
                    individual_customer = IndividualCustomers(CustomerID=customer_id,
                                                              DriverLicenseNumber=data.get('DriverLicenseNumber'),
                                                              InsuranceCompanyName=data.get('InsuranceCompanyName'),
                                                              InsurancePolicyNumber=data.get('InsurancePolicyNumber'))
                    db.session.add(individual_customer)

                elif type == 'corporate':
                    corporate_customer = CorporateCustomers(CustomerID=customer_id,
                                                          CorporationName=data.get('CorporationName'),
                                                          RegistrationNumber=data.get('RegistrationNumber'),
                                                          EmployeeID=data.get('EmployeeID'))
                    db.session.add(corporate_customer)

            return {'full_name': full_name, 'email': email, 'type': type, 'id': customer_id}, 201

        except Exception as e:
            api.abort(404, f"Error inserting data: {str(e)}")

@api.route('/login')
class LoginResource(Resource):
    @api.expect(login_model)
    @api.marshal_with(response_model)
    def post(self):
        try:
            # Extract data from the request
            data = request.json
            email = data.get('Email')
            password = data.get('Password')

            # Check if the user exists in the database
            user = Customers.query.filter_by(Email=email, Password=password).first()

            if user:
                # You can generate and return a token here for authentication purposes
                # For simplicity, let's return a success message and a placeholder token
                return {'message': 'Login successful', 'name': user.FullName, 'type': user.Type, 'id': user.CustomerID}
            else:
                # Return an error message if authentication fails
                api.abort(401, 'Authentication failed. Email or password is incorrect.')

        except Exception as e:
            # Return an error message if an exception occurs
            api.abort(500, f'Error during login: {str(e)}')

@api.route('/adminlogin')
class AdminLoginResource(Resource):
    @api.expect(login_model)
    @api.marshal_with(admin_response_model)
    def post(self):
        try:
            # Extract data from the request
            data = request.json
            email = data.get('Email')
            password = data.get('Password')

            # Check if the user exists in the database
            user = Admins.query.filter_by(Email=email, Password=password).first()

            if user:
                return {'message': 'Login successful', 'name': user.FullName}
            else:
                api.abort(401, 'Authentication failed. Email or password is incorrect.')
        except Exception as e:
            api.abort(500, f'Error during login: {str(e)}')

@api.route('/addadmin')
class AdminResource(Resource):
    @api.expect(admin_model)
    def post(self):
        data = request.json
        admin = Admins(**data)
        db.session.add(admin)
        db.session.commit()
        return {'message': 'Admin added successfully'}, 201
    
@api.route('/addclass')
class RentalClassesResource(Resource):
    @api.expect(rental_class_model, validate=True)
    def post(self):
        data = request.json
        new_rental_class = RentalClasses(**data)
        db.session.add(new_rental_class)
        db.session.commit()

        return {'message': 'Rental class added successfully', 'class': new_rental_class.Class}, 201
    
@api.route('/addvehicle')
class AddVehicleResource(Resource):
    @api.expect(vehicle_model)
    def post(self):

        data = request.json
        make = data.get('Make')
        model= data.get('Model')
        year= data.get('Year')
        licensePlateNumber= data.get('LicensePlateNumber')
        odometerReading= data.get('OdometerReading')
        image= data.get('Image')
        vehicleClass = data.get('Class')

        with db.session.begin():
            vehicle = Vehicles(Make=make, Model=model, Year=year, LicensePlateNumber=licensePlateNumber, OdometerReading = odometerReading,  Image = image, Class = vehicleClass )
            db.session.add(vehicle)
            db.session.flush()  # Flush to get the auto-generated ID

        return { 'message': 'Vehicle addes successfully'}, 201
    
@api.route('/getallvehicles')
class VehicleListResource(Resource):
    @api.marshal_with(vehicle_list, as_list=True)
    def get(self):
        combined_result = []
        vehicles = Vehicles.query.all()
        rental_classes = {rental_class.Class: rental_class for rental_class in RentalClasses.query.all()}
        for vehicle in vehicles:
            rental_class_info = rental_classes.get(vehicle.Class)
            if rental_class_info:
                combined_result.append({
                    'VIN': vehicle.VIN,
                    'Make': vehicle.Make,
                    'Model': vehicle.Model,
                    'Year': vehicle.Year,
                    'LicensePlateNumber': vehicle.LicensePlateNumber,
                    'OdometerReading': vehicle.OdometerReading,
                    'Image': vehicle.Image,
                    'RentalClass': {
                        'Class': rental_class_info.Class,
                        'DailyRate': rental_class_info.DailyRate,
                        'OverMileageFee': rental_class_info.OverMileageFee,
                    },
                })
        return combined_result
    
@api.route('/getallclasses')
class RentalClassResource(Resource):
    @api.marshal_with(rental_class_model, as_list=True)
    def get(self):
        combined_result = []
        rentalClasses = RentalClasses.query.all()
        for rentalClass in rentalClasses:
            combined_result.append({
            'Class': rentalClass.Class,
            'DailyRate': rentalClass.DailyRate,
            'OverMileageFee': rentalClass.OverMileageFee,
            })
        return combined_result
    
@api.route('/vehicle/<string:vin>')
class VehicleResource(Resource):
    @api.marshal_with(vehicle_list)
    def get(self, vin):
        vehicle = Vehicles.query.filter_by(VIN=vin).first()
        if not vehicle:
            api.abort(404, f"Vehicle with VIN {vin} not found")

        rental_class_info = RentalClasses.query.filter_by(Class=vehicle.Class).first()
        if not rental_class_info:
            api.abort(500, f"Rental class information not found for vehicle with VIN {vin}")

        result = {
            'VIN': vehicle.VIN,
            'Make': vehicle.Make,
            'Model': vehicle.Model,
            'Year': vehicle.Year,
            'LicensePlateNumber': vehicle.LicensePlateNumber,
            'OdometerReading': vehicle.OdometerReading,
            'Image': vehicle.Image,
            'RentalClass': {
                'Class': rental_class_info.Class,
                'DailyRate': rental_class_info.DailyRate,
                'OverMileageFee': rental_class_info.OverMileageFee,
            },
        }
        return result
    
    @api.expect(vehicle_update_model)
    def put(self, vin):
        data = api.payload
        vehicle = Vehicles.query.filter_by(VIN=vin).first()
        if not vehicle:
            api.abort(404, f"Vehicle with VIN {vin} not found")
        else: 
            vehicle.OdometerReading = data['OdometerReading']
            db.session.commit()
            return {'message': f'Vehicle {vehicle.VIN} updated successfully'}, 200
    
@api.route('/rental')
class RentalServiceResource(Resource):
    @api.expect(rental_service_detail)
    def post(self):
        data = request.json

        # Validate the required fields
        required_fields = ['VehicleID', 'CustomerID', 'PickupLocation', 'DropOffLocation',
                            'PickupDate', 'DropOffDate', 'StartOdometer',
                            'DailyOdometerLimit', 'UnlimitedMileageOption', 'RentalStatus']

        for field in required_fields:
            if field not in data:
                api.abort(400, f"Missing required field: {field}")
        
        data['PickupDate'] = parse(data['PickupDate']).date()
        data['DropOffDate'] = parse(data['DropOffDate']).date()

        # Create a new rental service record
        new_rental_service = RentalServices(**data)
        db.session.add(new_rental_service)
        db.session.commit()
        rentalId = new_rental_service.RentalID
        

        return { 'message': f"Booking Successful! your rental reference number is {rentalId} "}, 201
    
@api.route('/rental/<int:rental_id>')
class RentalServiceUpdateResource(Resource):
    @api.expect(rental_update_model)
    def put(self, rental_id):
        data = api.payload
        rental = RentalServices.query.get(rental_id)

        if rental:
            rental.EndOdometer = data['EndOdometer']
            rental.RentalStatus = data['RentalStatus']
            db.session.commit()

            self.generateInvoice(rental)

            return {'message': f'RentalService {rental_id} updated successfully'}, 200
        else:
            return {'message': f'RentalService {rental_id} not found'}, 404
        
    def generateInvoice(self,rental):
        vehicleInstance = VehicleResource()
        vehicle_info = vehicleInstance.get(vin=rental.VehicleID)
        daily_rate = vehicle_info['RentalClass']['DailyRate']
        over_mileage_fee = vehicle_info['RentalClass']['OverMileageFee']
        rental_duration = (rental.DropOffDate - rental.PickupDate).days
        total_distance = rental.EndOdometer - rental.StartOdometer

        total_amount = daily_rate*rental_duration

        if(not rental.UnlimitedMileageOption):
            max_allowed_dist = int(rental.DailyOdometerLimit)*rental_duration
            if(total_distance > max_allowed_dist):
                total_amount = total_amount + (total_distance - max_allowed_dist)*over_mileage_fee
        

        invoice = Invoices(RentalID = rental.RentalID, InvoiceDate = datetime.date.today() , InvoiceAmount = total_amount )
        db.session.add(invoice)
        db.session.commit()

@api.route('/rentals')
class RentalListResource(Resource):
    @api.marshal_with(rental_list, as_list=True)
    def get(self):
        rentals = RentalServices.query.all()
        rentals_list = []
        
        for rental in rentals:
            rental_data = {
                'RentalID': rental.RentalID,
                'VehicleID': rental.VehicleID,
                'CustomerID': rental.CustomerID,
                'PickupLocation': rental.PickupLocation,
                'DropOffLocation': rental.DropOffLocation,
                'PickupDate': str(rental.PickupDate),  # Convert date to string
                'DropOffDate': str(rental.DropOffDate),  # Convert date to string
                'StartOdometer': rental.StartOdometer,
                'EndOdometer': rental.EndOdometer,
                'DailyOdometerLimit': rental.DailyOdometerLimit,
                'UnlimitedMileageOption': rental.UnlimitedMileageOption,
                'RentalStatus': rental.RentalStatus,
            }
            rentals_list.append(rental_data)
        
        return rentals_list

@api.route('/rentals/<int:customer_id>')
class CustomerRentalListResource(Resource):
    @api.marshal_with(rental_list, as_list=True)
    def get(self, customer_id):
        rentals = RentalServices.query.filter_by(CustomerID = customer_id).all()
        rentals_list = []
        
        for rental in rentals:
            rental_data = {
                'RentalID': rental.RentalID,
                'VehicleID': rental.VehicleID,
                'CustomerID': rental.CustomerID,
                'PickupLocation': rental.PickupLocation,
                'DropOffLocation': rental.DropOffLocation,
                'PickupDate': str(rental.PickupDate),  # Convert date to string
                'DropOffDate': str(rental.DropOffDate),  # Convert date to string
                'StartOdometer': rental.StartOdometer,
                'EndOdometer': rental.EndOdometer,
                'DailyOdometerLimit': rental.DailyOdometerLimit,
                'UnlimitedMileageOption': rental.UnlimitedMileageOption,
                'RentalStatus': rental.RentalStatus,
            }
            rentals_list.append(rental_data)     
        return rentals_list

@api.route('/addLocation')
class RentalLocationResource(Resource):
    @api.expect(rental_location_model, validate=True)
    def post(self):
        data = request.json
        new_rental_location = RentalLocations(**data)
        db.session.add(new_rental_location)
        db.session.commit()

        return {'message': 'Rental location added successfully', 'Location': new_rental_location.FullAddress, 'id': new_rental_location.LocationID}, 201
    
@api.route('/rentallocations')
class RentalLocationsListResource(Resource):
    @api.marshal_with(rental_location_model, as_list=True)
    def get(self):
        locations = RentalLocations.query.all()
        locations_list = []
        
        for location in locations:
            location_data = {
                'LocationID': location.LocationID,
                'FullAddress': location.FullAddress,
                'PhoneNumber': location.PhoneNumber,
                'Image': location.Image,
            }
            locations_list.append(location_data)
        
        return locations_list, 201
    
@api.route('/invoice')
class InvoiceResource(Resource):
    @api.marshal_with(invoice_model)
    def post(self):
        data = request.json
        rentalID = data.get('RentalID')
        invoice = Invoices.query.filter_by(RentalID=rentalID).first()
        return {
            'InvoiceID': invoice.InvoiceID,
            'RentalID' : invoice.RentalID,
            'InvoiceDate' : invoice.InvoiceDate,
            'InvoiceAmount' :invoice.InvoiceAmount
        }, 201

