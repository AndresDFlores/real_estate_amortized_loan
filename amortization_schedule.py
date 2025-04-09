import pandas as pd
from amortization_eqns import *

class AmortizationSchedule:

    def __init__(self, asking, loan, annual_interest_rate, payments_per_year, loan_term):
        
        self.amort_eqns = AmortizationEqns

        '''
        loan: Initial loan amount
        annual_interest_rate: Interest on loan
        payments_per_year: Number of interest periods per year
        loan_term: How long the loan is created for (years)
        '''

        self.asking=asking
        self.loan=loan
        self.annual_interest_rate=annual_interest_rate/100  # divide by 100 to convert from percent to decimal
        self.payments_per_year=payments_per_year
        self.loan_term=loan_term

        self.total_number_of_payments=self.payments_per_year*self.loan_term
        self.remaining_balance = self.loan  # this can be a class method

        self.amort_table = []


    def amort_schedule(self):

        payment_number=0
        while self.remaining_balance >= 0:

            month = payment_number%12+1
            payment_number+=1

            payment_breakdown = self.amort_eqns.payment_breakdown(
                loan=self.loan, 
                annual_interest_rate=self.annual_interest_rate, 
                payments_per_year=self.payments_per_year, 
                total_number_of_payments=self.total_number_of_payments,
                remaining_balance=self.remaining_balance
                )

            payment = payment_breakdown[0]
            principal = payment_breakdown[1]
            interest = payment_breakdown[2]


            percent_principal = (principal/payment)*100
            percent_interest = (interest/payment)*100

            self.remaining_balance = self.remaining_balance-principal

            percent_paid = 100-(self.remaining_balance/self.loan)*100  # percentage of loan paid
            percent_owned = 100-(self.remaining_balance/self.asking)*100  # percentage asking price paid
            
            self.amort_table.append(
                [
                    payment_number,
                    month,
                    payment, 
                    principal, 
                    percent_principal,
                    interest, 
                    percent_interest,
                    self.remaining_balance, 
                    percent_paid,
                    percent_owned
                ]
            )

        amort_table = pd.DataFrame(
            self.amort_table, columns=[
                'PAYMENT_NUMBER',
                'MONTH',
                'PAYMENT', 
                'PRINCIPAL', 
                'PERCENT_PRINCIPAL_OF_PAYMENT',
                'INTEREST', 
                'PERCENT_INTEREST_OF_PAYMENT',
                'REMAINING_BALANCE', 
                'PERCENT_OF_LOAN_PAID',
                'PERCENT_OF_ASSET_OWNED'
            ]
        )

        return amort_table

if __name__ == '__main__':

    amort_calcs = AmortizationSchedule(
        asking=140000,
        loan=115800, 
        annual_interest_rate=3.25, 
        payments_per_year = 12,
        loan_term = 15
        )

    print(amort_calcs.amort_schedule())