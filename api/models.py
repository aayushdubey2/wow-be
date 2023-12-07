from .extensions import db

class RentalClasses(db.Model):
    Class = db.Column(db.String, primary_key=True)
    DailyRate = db.Column(db.DECIMAL)
    OverMileageFee = db.Column(db.DECIMAL)

class Customers(db.Model):
    CustomerID = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.String)
    FullName = db.Column(db.String)
    Address = db.Column(db.String)
    Email = db.Column(db.String)
    Phone = db.Column(db.String)
    Password = db.Column(db.String)

class IndividualCustomers(db.Model):
    CustomerID = db.Column(db.Integer, db.ForeignKey('customers.CustomerID'), primary_key=True)
    DriverLicenseNumber = db.Column(db.String)
    InsuranceCompanyName = db.Column(db.String)
    InsurancePolicyNumber = db.Column(db.String)

class CorporateCustomers(db.Model):
    CustomerID = db.Column(db.Integer, db.ForeignKey('customers.CustomerID'), primary_key=True)
    CorporationName = db.Column(db.String)
    RegistrationNumber = db.Column(db.String)
    EmployeeID = db.Column(db.String)

class DiscountCoupons(db.Model):
    CouponID = db.Column(db.Integer, primary_key=True)
    DiscountType = db.Column(db.String)
    DiscountPercentage = db.Column(db.DECIMAL)
    ValidityStartDate = db.Column(db.DATE)
    ValidityEndDate = db.Column(db.DATE)

class Vehicles(db.Model):
    VIN = db.Column(db.Integer, primary_key=True)
    Make = db.Column(db.String)
    Model = db.Column(db.String)
    Year = db.Column(db.Integer)
    LicensePlateNumber = db.Column(db.String)
    OdometerReading = db.Column(db.Integer)
    Image = db.Column(db.String)
    Class = db.Column(db.String, db.ForeignKey('rental_classes.Class'))

class RentalServices(db.Model):
    RentalID = db.Column(db.Integer, primary_key=True)
    VehicleID = db.Column(db.Integer, db.ForeignKey('vehicles.VIN'))
    CustomerID = db.Column(db.Integer, db.ForeignKey('customers.CustomerID'))
    PickupLocation = db.Column(db.String)
    DropOffLocation = db.Column(db.String)
    PickupDate = db.Column(db.DATE)
    DropOffDate = db.Column(db.DATE)
    StartOdometer = db.Column(db.Integer)
    EndOdometer = db.Column(db.Integer)
    DailyOdometerLimit = db.Column(db.Integer)
    UnlimitedMileageOption = db.Column(db.Boolean)
    RentalStatus = db.Column(db.String)

class Invoices(db.Model):
    InvoiceID = db.Column(db.Integer, primary_key=True)
    CouponID = db.Column(db.Integer, db.ForeignKey('discount_coupons.CouponID'))
    RentalID = db.Column(db.Integer, db.ForeignKey('rental_services.RentalID'))
    InvoiceDate = db.Column(db.DATE)
    InvoiceAmount = db.Column(db.DECIMAL)

class Payments(db.Model):
    PaymentID = db.Column(db.Integer, primary_key=True)
    InvoiceID = db.Column(db.Integer, db.ForeignKey('invoices.InvoiceID'))
    PaymentDate = db.Column(db.DATE)
    PaymentMethod = db.Column(db.String)
    CardNumber = db.Column(db.String)

class RentalLocations(db.Model):
    LocationID = db.Column(db.Integer, primary_key=True)
    FullAddress = db.Column(db.String)
    PhoneNumber = db.Column(db.String)
