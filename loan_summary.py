from operator import itemgetter


class LoanSummary:

    def __init__(self, apr, loan, amortization_table):
        # self.term = term
        self.apr = apr
        self.loan = loan
        self.amortization_table = amortization_table


    def get_summary(self):

        summary=dict()

        payment_data = list(map(itemgetter(2), self.amortization_table))
        avg_monthly = round(sum(payment_data)/len(payment_data), 2)
        total_to_pay = round(sum(payment_data), 2)

        principal_data = list(map(itemgetter(3), self.amortization_table))
        total_principal = round(sum(principal_data), 2)

        interest_data = list(map(itemgetter(5), self.amortization_table))
        total_interest = round(sum(interest_data), 2)

        principal_percent = (total_principal/total_to_pay)*100
        interest_percent = (total_interest/total_to_pay)*100
        percent_increase = ((total_to_pay-self.loan)/self.loan)*100  # ((new-original)/original)*100


        self.summary=dict(
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
        