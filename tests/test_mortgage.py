"""
Description: A class used to test the Mortgage class.
Author: {Student Name}
Date: {Date}
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""
from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    
    """Test cases for validating the attributes in the __init__ method for the mortgage class"""

    def test_invalid_loan_amount_value(self): 

        """Tests that a value error is raised when the loan amount is less than or equal to zero"""

        #Arrange
        loan_amount = -5 #invalid loan amount value
        rate = "FIXED_5"
        frequency = "WEEKLY"
        amortization = 10
        
        #Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount,rate,frequency,amortization)

        #Assert
        self.assertEqual(str(context.exception), "Loan Amount must be positive.") 

    def test_invalid_rate_value(self):

        """Tests that a value error is raised when the rate value invalid """
    
        #Arrange
        loan_amount = 1000 
        rate = "INVALID_RATE" #invalid rate value
        frequency = "WEEKLY"
        amortization = 10

        #Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount,rate,frequency,amortization)

        #Assert
        self.assertEqual(str(context.exception), "Rate provided is invalid.") 

    def test_invalid_frequency_value(self):

        """Tests that a value error is raised when the frequency value is invalid """

        #Arrange
        loan_amount = 1000 
        rate = "FIXED_5" 
        frequency = "INVALID_FREQUENCY" # invalid frequency value
        amortization = 10

        #Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount,rate,frequency,amortization)

        #Assert
        self.assertEqual(str(context.exception), "Frequency provided is invalid.") 

    def test_invalid_amortization_value(self):

        "Tests that a value error is raised when the amortization value is invalid"

        #Arrange
        loan_amount = 1000 
        rate = "FIXED_5" 
        frequency = "WEEKLY"
        amortization = 0 #invalid amortization value

        #Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount,rate,frequency,amortization)

        #Assert
        self.assertEqual(str(context.exception), "Amortization provided is invalid.") 

    def test_valid_mortgage(self):

        """Tests that the attributes in the __init__ method are properly set when valid inputs are provided"""

        #Arrange
        loan_amount = 1000 
        rate = "FIXED_5" 
        frequency = "WEEKLY"
        amortization = 5
        # all valid inputs

        #Act
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)

        #Assert
        self.assertEqual(mortgage._Mortgage__loan_amount_float, 1000)
        self.assertEqual(mortgage._Mortgage__rate, MortgageRate.FIXED_5)
        self.assertEqual(mortgage._Mortgage__frequency, PaymentFrequency.WEEKLY)
        self.assertEqual(mortgage._Mortgage__amortization_value_int, 5)

    #Loan Amount Accessor & Mutator TEST

    def test_loan_amount_negative(self):

        """Tests that a value error is raised when the loan amount is changed into a negative value"""

        #Arrange
        mortgage = Mortgage(1000, "FIXED_5", "WEEKLY", 5) #all valid inputs

        #Act
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = -100  #change loan amount into a negative value
        #Assert
        self.assertEqual(str(context.exception), "Loan Amount must be positive.") 

    def test_loan_amount_zero(self):

        """Tests that a value error is raised when the loan amount is changed into a negative value"""

        #Arrange
        mortgage = Mortgage(1000, "FIXED_5", "WEEKLY", 5) #all valid inputs

        #Act
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = 0  #change loan amount into a zero
            
        #Assert
        self.assertEqual(str(context.exception), "Loan Amount must be positive.") 

    def test_loan_amount_positive(self):

        """Tests when the loan amount is changed into another positive value"""

        #Arrange
        mortgage = Mortgage(1000, "FIXED_5", "WEEKLY", 5) #all valid inputs

        #Act
        mortgage.loan_amount = 2000 #changed loan amount into another valid positive value

        #Assert
        self.assertEqual(mortgage.loan_amount, 2000)
    
    #Rate Accessor & Mutator TEST

    def test_valid_rate_change(self):
        
        """Tests when the mortgage rate is changed into another valid rate"""

        #Arrange
        mortgage = Mortgage(1000, "FIXED_5", "WEEKLY", 5) #all valid inputs

        #Act
        mortgage.rate = "FIXED_3" #changed into another valid rate 

        #Assert
        self.assertEqual(mortgage.rate, MortgageRate.FIXED_3)


    def test_invalid_rate_change(self):

        """Tests when the mortgage rate is changed into another invalid rate"""
        
        #Arrange
        mortgage = Mortgage(1000, "FIXED_5", "WEEKLY", 5) #all valid inputs

        #Act
        with self.assertRaises(ValueError) as context:
            mortgage.rate = "INVALID_RATE"  #change loan amount an invalid rate

        #Assert
        self.assertEqual(str(context.exception), "Rate provided is invalid.") 


