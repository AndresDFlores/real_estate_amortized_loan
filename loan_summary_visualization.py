import os
import matplotlib.pyplot as plt

from zoom_factory import*

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
        ax_cols = ['PERCENT_INTEREST_OF_PAYMENT', 'PERCENT_PRINCIPAL_OF_PAYMENT']
        ax_color = ['red', 'green']
        for data_index in range(len(ax_cols)):
            ax.plot(self.amortization_table['PAYMENT_NUMBER'], self.amortization_table[ax_cols[data_index]], color=ax_color[data_index])

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
        ax_cols = ['INTEREST', 'PRINCIPAL']
        ax_color = ['red', 'green']
        for row in range(self.amortization_table.shape[0]):
            y_shift = 0
            for data_index in range(len(ax_cols)):
                ax.bar(self.amortization_table.iloc[row]['PAYMENT_NUMBER'], self.amortization_table.iloc[row][ax_cols[data_index]], bottom=y_shift, color=ax_color[data_index])
                y_shift = self.amortization_table.iloc[row]['INTEREST']

        ZoomPan().zoom_factory(ax=ax)
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
            x=[self.loan_summary['interest_percent'], self.loan_summary['principal_percent']],
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