import pandas as pd
import os

from scrape_mortgage_rates import *

from amortization_schedule import *
from loan_summary import *
from loan_summary_visualization import *


# #  -----DEV-----

# from guis import *

# guis_class=GUIs()

# fields = {
#     'Address':str, 
#     'Asking Price ($)':float, 
#     'Percent Down (%)':float, 
#     'APR (%)':float, 
#     'Payments per Year':int, 
#     'Loan Term (Years)':int
#     }

# user_entries = guis_class.dialogue_box(fields=list(fields))
# save_dir = guis_class.select_directory()

# for field, dtype in fields.items():
#     user_entries[field]=dtype(user_entries[field])


# amort_calcs = AmortizationSchedule(
#     asking=user_entries[list(fields)[1]],
#     loan=user_entries[list(fields)[1]]-(user_entries[list(fields)[1]]*user_entries[list(fields)[2]]),
#     annual_interest_rate=user_entries[list(fields)[3]],
#     payments_per_year=user_entries[list(fields)[4]],
#     loan_term=user_entries[list(fields)[5]]
# )

# # -----DEV-----

main_dir = os.getcwd()
# mortgage_rates_class = RateScrape()

# term_rates = {term: mortgage_rates_class.scrape_rates(loan_term=term) for term in [15, 30]}
# prices = [350, 355, 360, 365, 370]

# print(term_rates)

term_rates={30: 6.75}
prices=[830, 840, 850]

comps_summary=dict(
    asking=[],
    term=[],
    apr=[],
    avg_monthly=[],
    total_loan = [],
    total_to_pay=[],
    total_principal=[],
    total_interest=[],
    principal_percent=[],
    interest_percent=[],
    percent_increase=[]
)


for price in prices:
    for term, apr in term_rates.items():

        #  create summary directory
        file_name = f'{price}k_{apr}%_{term}yrs'
        dir_path = os.path.join(os.getcwd(), file_name)

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)


        #  AMORTIZATION SCHEDULE
        asking = price*1000
        loan = asking-(asking*(.15))

        amort_calcs = AmortizationSchedule(
            asking=asking,
            loan=loan,
            annual_interest_rate=apr,
            payments_per_year=12,
            loan_term=term
        )

        amort_schedule = amort_calcs.amort_schedule()
        amort_schedule.to_excel(os.path.join(dir_path, 'ammortization_schedule.xlsx'), index=False)


        #  LOAN SUMMARY
        summary = LoanSummary(
            #term=term,
            apr=apr,
            loan=amort_calcs.loan, 
            amortization_table=amort_schedule
            ).summary()


        comps_summary['asking'].append(asking)
        for summary_item in list(summary):
            comps_summary[summary_item].append(summary[summary_item])



        #  AMORTIZATION VISUALIZATION
        loan_summary_vis = LoanSummaryVisualization(
            amortization_table=amort_schedule,
            loan_summary=summary,
            dir_path=dir_path
            )

        loan_summary_vis.percentage_breakdown()
        loan_summary_vis.payment_breakdown()
        loan_summary_vis.total_breakdown()


df = pd.DataFrame(comps_summary)
# df.to_excel(os.path.join(main_dir, 'comps_summary.xlsx'), index=False)
print(df)
