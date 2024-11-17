"""
Description: A class meant to manage Mortgage options.
Author: Pablito Salazar
Date: November 16, 2024
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:
    """Represents a mortgage with mortgage rates and payment frequencies"""

    def __init__(self, loan_amount_float, string_rate_value, string_frequency_value, amortization_value_int):
        """
        Initializing a Mortgage object
        
        Arguments: 
        loan_amount(float) : the loan amount stored in a float
        string_rate_value(string): the rate of the mortgage stored in a string
        string_frequency_value(string) the frequency of payment stored in a string
        amortization_value_int(int) the amortization period stored in a string

        Raises:
            ValueError: that the loan amount must be positive, the Rate provided must be valid

        """
        if loan_amount_float <= 0: #validates that the loan amount is not less that or equal to zero
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount_float = loan_amount_float

        try: #assigns the rate, raising a value error if it is invalid
            self.__rate = MortgageRate[string_rate_value]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
        
        try: #assigns the frequency, raising a value error if it is invalid
            self.__frequency = PaymentFrequency[string_frequency_value]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")
        

        if amortization_value_int not in VALID_AMORTIZATION: 
            # if the amortization value is not in the Valid Amortization set a value error is raised.
            raise ValueError("Amortization provided is invalid.")
        self.__amortization_value_int = amortization_value_int