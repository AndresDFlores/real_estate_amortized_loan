# from symbol import term


class LoanSummary:

    def __init__(self, apr, loan, amortization_table):
        # self.term = term
        self.apr = apr
        self.loan = loan
        self.amortization_table = amortization_table


    def summary(self):

        summary=dict()

        avg_monthly = round(self.amortization_table['PAYMENT'].sum()/len(self.amortization_table['PAYMENT']), 2)
        total_to_pay = round(self.amortization_table['PAYMENT'].sum(), 2)
        total_principal = round(self.amortization_table['PRINCIPAL'].sum(), 2)
        total_interest = round(self.amortization_table['INTEREST'].sum(), 2)

        principal_percent = (total_principal/total_to_pay)*100
        interest_percent = (total_interest/total_to_pay)*100
        percent_increase = ((total_to_pay-self.loan)/self.loan)*100  # ((new-original)/original)*100


        summary=dict(
            # term = self.term,
            apr = self.apr,
            avg_monthly = avg_monthly,
            total_loan = self.loan,
            total_to_pay=total_to_pay,
            total_principal=total_principal,
            total_interest=total_interest,
            principal_percent=principal_percent,
            interest_percent=interest_percent,
            percent_increase=percent_increase
        )
        

        return summary