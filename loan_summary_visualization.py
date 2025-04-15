import os
from operator import itemgetter
import matplotlib.pyplot as plt


class LoanSummaryVisualization:

    def __init__(self, amortization_table, loan_summary, dir_path=None):
        self.amortization_table=amortization_table
        self.loan_summary=loan_summary
        self.dir_path = dir_path



    def save_figure(self, file_name, fig=None, ax=None):
        if self.dir_path:

            file_name = os.path.join(self.dir_path, f'{file_name}_vis.png')
            fig.savefig(
                fname=file_name,
            )



    #  PAYMENT PERCENTAGES
    def percentage_breakdown(self):

        fig, ax = plt.subplots()

        ax_cols = [6, 4]
        ax_color = ['red', 'green']
        
        
        payment_number = list(map(itemgetter(0), self.amortization_table))
        for ax_idx in range(len(ax_cols)):

            payment_data = list(map(itemgetter(ax_cols[ax_idx]), self.amortization_table))

            ax.plot(payment_number, payment_data, color=ax_color[ax_idx])


        ax.set_title('AMORTIZATION SCHEDULE')
        ax.set_xlabel('PAYMENT NUMBER')
        ax.set_ylabel('PAYMENT BREAKDOWN')
        ax.grid(visible=True)
        ax.legend(['INTEREST PERCENT OF PAYMENT', 'PRINCIPAL PERCENT OF PAYMENT'])

        self.save_figure(file_name = 'percentage_breakdown', fig=fig)
        return fig, ax




    #  PAYMENT BREAKDOWNS
    def payment_breakdown(self):

        fig, ax = plt.subplots()

        ax_cols = [5, 3]
        ax_color = ['red', 'green']


        for row in self.amortization_table:
            y_shift = 0

            payment_number = row[0]
            for ax_idx in range(len(ax_cols)):
                
                val = row[ax_cols[ax_idx]]
                color = ax_color[ax_idx]

                ax.bar(
                    payment_number, 
                    val, 
                    bottom=y_shift, color=color
                    )
                
                y_shift = val


        ax.set_title('AMORTIZATION SCHEDULE')
        ax.set_xlabel('PAYMENT NUMBER')
        ax.set_ylabel('PAYMENT BREAKDOWN')
        ax.grid(visible=True)
        ax.legend(['INTEREST', 'PRINCIPAL'])

        self.save_figure(file_name = 'payments_breakdown', fig=fig)
        return fig, ax




    #  TOTALS BREAKDOWN
    def total_breakdown(self):

        fig, ax = plt.subplots()

        ax.pie(
            x=[
                self.loan_summary['interest_percent'],
                self.loan_summary['principal_percent']
                ],
            colors=['red', 'green'],
            labels=[
                '{0}: ${1:.2f}'.format('INTEREST', self.loan_summary['total_interest']), 
                '{0}: ${1:.2f}'.format('PRINCIPAL', self.loan_summary['total_principal'])
                ],
                explode=(0.05, 0),
                autopct='%1.1f%%',
                startangle=90,
                counterclock=False)


        ax.set_title('TOTAL LOAN: \${0:.2f} | TOTAL TO PAY: \${1:.2f}\nPERCENT INCREASE: {2:.2f}%'.format(self.loan_summary['total_loan'], self.loan_summary['total_to_pay'], self.loan_summary['percent_increase']))
        
        ax.grid(visible=True)

        self.save_figure(file_name = 'totals_breakdown', fig=fig)
        return fig, ax
    


    def main(self):
        
        self.percentage_breakdown()
        self.payment_breakdown()
        self.total_breakdown()
            