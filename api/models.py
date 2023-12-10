from .extensions import db

class RentalClasses(db.Model):
    Class = db.Column(db.String(50), primary_key=True)
    DailyRate = db.Column(db.DECIMAL)
    OverMileageFee = db.Column(db.DECIMAL)

class Customers(db.Model):
    CustomerID = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.String(20))
    FullName = db.Column(db.String(50))
    Address = db.Column(db.String(200))
    Email = db.Column(db.String(100))
    Phone = db.Column(db.String(10))
    Password = db.Column(db.String(20))

class Admins(db.Model):
    AdminID = db.Column(db.Integer, primary_key=True)
    FullName = db.Column(db.String(50))
    Email = db.Column(db.String(100))
    Password = db.Column(db.String(20))

class IndividualCustomers(db.Model):
    CustomerID = db.Column(db.Integer, db.ForeignKey('customers.CustomerID'), primary_key=True)
    DriverLicenseNumber = db.Column(db.String(20))
    InsuranceCompanyName = db.Column(db.String(50))
    InsurancePolicyNumber = db.Column(db.String(20))

class CorporateCustomers(db.Model):
    CustomerID = db.Column(db.Integer, db.ForeignKey('customers.CustomerID'), primary_key=True)
    CorporationName = db.Column(db.String(50))
    RegistrationNumber = db.Column(db.String(20))
    EmployeeID = db.Column(db.String(10))

class DiscountCoupons(db.Model):
    CouponID = db.Column(db.Integer, primary_key=True)
    CouponCode = db.Column(db.String(20))
    DiscountPercentage = db.Column(db.DECIMAL)
    ValidityStartDate = db.Column(db.DATE)
    ValidityEndDate = db.Column(db.DATE)

class Vehicles(db.Model):
    VIN = db.Column(db.Integer, primary_key=True)
    Make = db.Column(db.String(20))
    Model = db.Column(db.String(20))
    Year = db.Column(db.Integer)
    LicensePlateNumber = db.Column(db.String(20))
    OdometerReading = db.Column(db.Integer)
    Image = db.Column(db.String(50))
    Class = db.Column(db.String(50), db.ForeignKey('rental_classes.Class'))

class RentalServices(db.Model):
    RentalID = db.Column(db.Integer, primary_key=True)
    VehicleID = db.Column(db.Integer, db.ForeignKey('vehicles.VIN'))
    CustomerID = db.Column(db.Integer, db.ForeignKey('customers.CustomerID'))
    PickupLocation = db.Column(db.String(200))
    DropOffLocation = db.Column(db.String(200))
    PickupDate = db.Column(db.DATE)
    DropOffDate = db.Column(db.DATE)
    StartOdometer = db.Column(db.Integer)
    EndOdometer = db.Column(db.Integer)
    DailyOdometerLimit = db.Column(db.Integer)
    UnlimitedMileageOption = db.Column(db.Boolean)
    RentalStatus = db.Column(db.String(10))

class Invoices(db.Model):
    InvoiceID = db.Column(db.Integer, primary_key=True)
    RentalID = db.Column(db.Integer, db.ForeignKey('rental_services.RentalID'))
    InvoiceDate = db.Column(db.DATE)
    InvoiceAmount = db.Column(db.DECIMAL)

class Payments(db.Model):
    PaymentID = db.Column(db.Integer, primary_key=True)
    InvoiceID = db.Column(db.Integer, db.ForeignKey('invoices.InvoiceID'))
    CouponID = db.Column(db.Integer, db.ForeignKey('discount_coupons.CouponID'))
    PaymentDate = db.Column(db.DATE)
    PaymentMethod = db.Column(db.String(20))
    CardNumber = db.Column(db.String(20))

class RentalLocations(db.Model):
    LocationID = db.Column(db.Integer, primary_key=True)
    FullAddress = db.Column(db.String(200))
    PhoneNumber = db.Column(db.String(10))
    Image = db.Column(db.String(20))
