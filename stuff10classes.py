class Employee:

    def __init__(self, name, number):
        self._name = name
        self._number = number
    
    def set_name(self, name):
        self._name = name
    def set_number(self, number):
        self._number = number

    def get_name(self):
        return self._name
    def get_number(self):
        return self._number

class ProductionWorker(Employee):

    def __init__(self, name, number, shift, pay):
        super().__init__(name, number)
        self._shift = shift
        self._pay = pay

    def set_shift(self, shift):
        self._shift = shift
    def set_pay(self, pay):
        self._pay = pay

    def get_shift(self):
        return self._shift
    def get_pay(self):
        return self._pay

class ShiftSupervisor(Employee):

    def __init__(self, name, number, salary, bonus):
        super().__init__(name, number)
        self._salary = salary
        self._bonus = bonus
    
    def set_salary(self, salary):
        self._salary = salary
    def set_bonus(self, bonus):
        self._bonus = bonus

    def get_salary(self):
        return self._salary
    def get_bonus(self):
        return self._bonus

#################################################################

class Person:
# Person class, exists only as a parent of the customer class

    # constructor
    def __init__(self, name, street_address, city, state, zip_code, phone):
        self._name = name
        self._street_address = street_address
        self._city = city
        self._state = state
        self._zip_code = zip_code
        self._phone = phone
    # setters
    def set_name(self, name):
        self._name = name
    def set_street_address(self, street_address):
        self._street_address = street_address
    def set_city(self, city):
        self._city = city
    def set_state(self, state):
        self._state = state
    def set_zip_code(self, zip_code):
        self._zip_code = zip_code
    def set_phone(self, phone):
        self._phone = phone
    # getters
    def get_name(self):
        return self._name
    def get_phone(self):
        return self._phone
    def get_street_address(self):
        return self._street_address
    def get_city(self):
        return self._city
    def get_state(self):
        return self._state
    def get_zip_code(self):
        return self._zip_code
    # method to return a formatted string of the person's mailing address including name
    def get_mailing_address(self):
        return '%s\n%s\n%s, %s %s' % (self._name, self._street_address, self._city, self._state, self._zip_code)

class Customer(Person):
# class for customers, inherits from person class

    # constructor
    def __init__(self, name, street_address, city, state, zip_code, phone, cust_num, on_mailing_list):
        super().__init__(name, street_address, city, state, zip_code, phone)
        self._cust_num = cust_num
        self._on_mailing_list = on_mailing_list
    # setters
    def set_cust_num(self, cust_num):
        self._cust_num = cust_num
    def set_on_mailing_list(self, on_mailing_list):
        self._on_mailing_list = on_mailing_list
    # getters
    def get_cust_num(self):
        return self._cust_num
    def get_on_mailing_list(self):
        return self._on_mailing_list
    # repr method used by program to print out customer information
    # used repr instead of str due to using this on a list of customers
    def __repr__(self):
        if self._on_mailing_list:
            on_list = "Yes"
        else:
            on_list = "No"
        return "Customer Number: %s\n%s\n%s\nOn Mailing List? %s" % (self._cust_num, self.get_mailing_address(), self._phone, on_list)