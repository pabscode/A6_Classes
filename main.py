"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited by: Pablito Salazar
Date: November 16, 2024
"""

from mortgage.mortgage import Mortgage, MortgageRate, PaymentFrequency
from mortgage.pixell_lookup import VALID_AMORTIZATION

try:
    with open ("data\\pixell_river_mortgages.txt","r") as input:
        print("**************************************************")
        
        for data in input:
            items = data.split(",")
            
            try:
                amount = float(items[0])
                rate = items[1]
                amortization = int(items[2])
                frequency = items[3]

                mortgage = Mortgage(amount, rate , frequency, amortization)
                
                print(mortgage)

            except ValueError as e:
                # This except block will catch Explicit exceptions: 
                # Those raised by the programmer in the Mortgage class.
                print(f"Data: {data.strip()} caused Exception: {e}")
            
            except Exception as e:
                # This except block will catch Implicit exceptions:  
                # Those raised through normal execution.
                print(f"Data: {data.strip()} caused Exception: {e}")
            finally:
                print("**************************************************")

except FileNotFoundError:
    print("File was not found")
