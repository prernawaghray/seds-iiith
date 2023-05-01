from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel


class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()

    def login(self, username, password):
        # Add you code here after verifying the vendor data exists in the dictionary
        if self.vendor_model.is_correct_vendor(username, password) == True: #verifying if the vendor exists in the db
            self.vendor_session.login(username) #logging in
            print("User {} logged in successfully!".format(username))
        else:
            print("Invalid username or password.")
            exit() #if the login fails then the program must quit here


    def logout(self, username):
        # Add your code here to log out the current vendor
        self.vendor_session.logout(username)  # logging out
        print("User {} logged out successfully!".format(username))