class AmortizationEquations:

    '''

    https://www.experts-exchange.com/articles/1948/A-Guide-to-the-PMT-FV-IPMT-and-PPMT-Functions.html

    PMT: Payment
    PPMT: Principal Payment
    IPMT: Interest Payment
    '''

    def payment(loan, annual_interest_rate, payments_per_year, total_number_of_payments):

        '''
        https://superuser.com/questions/871404/what-would-be-the-the-mathematical-equivalent-of-this-excel-formula-pmt

        Pv: Present Value
        APR: Annual Percentage Rate
        R: Periodic Interest (APR/number of interest periods per year)
        n: Total number of interest periods (interest periods per yeear * number of years)
        
        '''

        Pv = loan
        APR = annual_interest_rate
        R = APR/payments_per_year
        n = total_number_of_payments
        
        payment = (Pv*R) / (1 - (1 + R)**(-n))
        
        return round(payment, 2)


    def interest(annual_interest_rate, payments_per_year, remaining_balance):

        '''
        https://www.bankrate.com/loans/personal-loans/how-to-calculate-loan-interest/
        '''

        interest = (annual_interest_rate/payments_per_year)*remaining_balance

        return round(interest, 2)


    def payment_breakdown(loan, annual_interest_rate, payments_per_year, total_number_of_payments, remaining_balance):

        '''
        IMPLEMENT APPROPRIATE PPMT EQN
        '''

        payment = AmortizationEquations.payment(loan, annual_interest_rate, payments_per_year, total_number_of_payments)
        interest = AmortizationEquations.interest(annual_interest_rate, payments_per_year, remaining_balance)

        principal = payment-interest

        return round(payment, 2), round(principal, 2), round(interest, 2)