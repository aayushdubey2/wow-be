# resources.py
from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from sqlalchemy import text  # Import the text function
from .apimodels import *
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

            return {'full_name': full_name, 'email': email}, 201

        except Exception as e:
            api.abort(404, f"Error inserting data: {str(e)}")




login_model = api.model('LoginModel', {'Email': fields.String, 'Password': fields.String })

# Define the model for the response data
response_model = api.model('LoginResponse', {'message': fields.String })

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
                return {'message': 'Login successful'}
            else:
                # Return an error message if authentication fails
                api.abort(401, 'Authentication failed. Email or password is incorrect.')

        except Exception as e:
            # Return an error message if an exception occurs
            api.abort(500, f'Error during login: {str(e)}')