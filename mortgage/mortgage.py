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
            ValueError: 
            the loan amount must be positive, 
            the rate provided must be valid,
            the frequency provided must be valid,
            the amortization period provided is invalid


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

    #LOAN AMOUNT
    @property
    def loan_amount(self):

        """Gets the loan amount"""

        return self.__loan_amount_float

    @loan_amount.setter
    def loan_amount(self,value: float):

        """Sets the loan amount and checks for validation"""

        if value <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount_float = value

    #RATE 
    @property
    def rate(self):

        """Returns value of the rate"""

        return self.__rate
    
    @rate.setter
    def rate(self, rate_value: str):

        """Sets the rate and check for validation"""

        try: #assigns the rate, raising a value error if it is invalid
            self.__rate = MortgageRate[rate_value]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
        
    #FREQUENCY

    @property
    def frequency(self):

        """Returns the value of the frequency"""

        return self.__frequency
    
    @frequency.setter
    def frequency(self, frequency_value: str):
        
        """Sets the frequency and checks for validation"""

        try: #assigns the frequency, raising a value error if it is invalid
            self.__frequency = PaymentFrequency[frequency_value]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")
        

    #AMORTIZATION

    @property
    def amortization(self):

        """Returns the value of the amortization"""

        return self.__amortization_value_int

    @amortization.setter
    def amortization(self, amortization_value_int: int):

        """Sets the amortization value adnd checks for validation"""

        if amortization_value_int not in VALID_AMORTIZATION: 
            raise ValueError("Amortization provided is invalid.")
        self.__amortization_value_int = amortization_value_int

    def calculate_payment(self) -> float:

        """Calculates the payment of a mortgage including the details of the amount rate frequency and amortization,
        returns the mortgage payment amount""" 

        #loan amount
        principal_loan_amount = self.__loan_amount_float

        #annual rate
        annual_rate = self.__rate.value

        #frequency
        frequency = self.__frequency.value

        #amortization (years)
        amortization_period = self.__amortization_value_int

        #interest rate (annual rate / frequency)
        interest_rate = annual_rate / frequency

        #number of payments (amortization * frequency)
        number_of_payments = amortization_period * frequency

        #using the formula provided in the assignment instructions
        payment = principal_loan_amount *( 
            (interest_rate * (1 + interest_rate) ** number_of_payments ) 
            / ((1 + interest_rate) ** number_of_payments - 1 ) )
        
        return round(payment,3)


