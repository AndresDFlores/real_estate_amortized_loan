import os

from scrape_mortgage_rates import *
from amortization_schedule import *
from loan_summary import *
from loan_summary_visualization import *


#  saving directory
main_dir = os.getcwd()

prices = [100]  # asking in thousands , 840, 850
loan_terms = [30]  # years
percent_down = [.20]  # percent of asking down payment


rate_scrape =  RateScrape()
for asking in prices:
    for term in loan_terms:
        for dp in percent_down:


            #  LOAN TERMS
            loan = asking-(asking*dp)
            apr = rate_scrape.scrape_rates(loan_term=term)
            

        
            #  create summary directory
            file_name = f'{asking}k_{dp*100}%dp_{loan}K_{apr}%_{term}yrs'
            dir_path = os.path.join(os.getcwd(), file_name)

            if not os.path.exists(dir_path):
                os.mkdir(dir_path)



            #  AMORTIZATION SCHEDULE           
            amort_sched_class = AmortizationSchedule(
                asking=asking*1000,
                loan=loan*1000,
                annual_interest_rate=apr,
                payments_per_year=12,
                loan_term=term,
                save_dir=dir_path
            )
            amort_sched_class.main()



            #  LOAN SUMMARY
            loan_summary_class = LoanSummary(
                #term=term,
                apr=apr,
                loan=amort_sched_class.loan, 
                amortization_table=amort_sched_class.amort_table
                )
            loan_summary_class.get_summary()



            #  AMORTIZATION VISUALIZATION
            loan_summary_vis = LoanSummaryVisualization(
                amortization_table=amort_sched_class.amort_table,
                loan_summary=loan_summary_class.summary,
                dir_path=dir_path
                )
            loan_summary_vis.main()