import os
import csv
from amortization_eqns import *


class AmortizationSchedule:

    def __init__(self, asking, loan, annual_interest_rate, payments_per_year, loan_term, save_dir=os.getcwd()):

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
        self.save_dir=save_dir


    def amort_schedule(self):

        amort_eqns_class = AmortizationEquations()

        payment_number=0
        while self.remaining_balance >= 0:

            month = payment_number%12+1
            payment_number+=1

            payment_breakdown = amort_eqns_class.payment_breakdown(
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

            # percentage of loan paid
            percent_paid = 100-(self.remaining_balance/self.loan)*100

            # percentage asking price paid
            percent_owned = 100-(self.remaining_balance/self.asking)*100  
            
            #  list of tuples, where each tuple is a row of data
            self.amort_table.append(
                (
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
                )
            )

        #  define column names
        self.column_headers = [
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


    def export_amortization_schedule(self):
            

            # Specify the CSV file name
            filename = os.path.join(self.save_dir, 'ammortization_schedule.csv')
            


            # Open the file in write mode ('w')
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)

                # Write the header row (optional)
                writer.writerow(self.column_headers)

                # Write the data rows
                writer.writerows(self.amort_table)


    def main(self):
        self.amort_schedule()
        self.export_amortization_schedule()


if __name__ == '__main__':

    amort_calcs = AmortizationSchedule(
        asking=100000,
        loan=80000, 
        annual_interest_rate=3, 
        payments_per_year = 12,
        loan_term = 30
        )
    
    amort_calcs.main()