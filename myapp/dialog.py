from flet import*
from msg import MsgBox
class AlertBox(UserControl):
    def __init__(self,page,primary_color,secondary_color):
        self.page = page
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.Alertmsgs()
    # here we call the alertbox
    def Alertmsgs(self):
        self.boxs = {
            'Loan Amount' : 'RCDP offers tailored loans to empower individuals and businesses. Livestock loans support farmers in expanding operations, business loans help shop owners grow, agriculture loans boost farming activities with essential inputs, and handicraft loans aid artisans in enhancing production and marketing. These products foster economic growth and self-reliance across various sectors.',
            'Markup Amount': 'RCDP offers loans at a competitive markup rate of just 22%, significantly lower than many other microfinance institutions. This ensures affordable financial solutions for our clients, empowering them to grow their businesses, improve livelihoods, and achieve economic stability.',
            'Installment' : 'RCDP provides flexible, affordable monthly installments tailored to the loan tenure. For terms exceeding a year, installments are lower to ease repayment, though the markup rate is slightly higher. This approach ensures accessibility and convenience while supporting clients in managing their finances effectively.',
            'Processing Fee Rate': 'RCDP charges a 5% processing fee, which includes 1% for insurance, 2% for staff expenses, and 2% for administrative materials and documentation. This transparent fee structure ensures smooth operations while maintaining affordability for our clients.'
        }
    def AlertMsg(self,item):
        if item in self.boxs:
            if item == 'Loan Amount':
                self.loan_dialog = MsgBox(self.page,self.primary_color,self.secondary_color,item,self.boxs[item],icons.MONEY_ROUNDED)
            elif item == 'Processing Fee Rate':
                self.loan_dialog = MsgBox(self.page,self.primary_color,self.secondary_color,item,self.boxs[item],icons.LOCAL_ACTIVITY_ROUNDED)
            elif item == 'Markup Amount':
                self.loan_dialog = MsgBox(self.page,self.primary_color,self.secondary_color,item,self.boxs[item],icons.FACT_CHECK_ROUNDED)
            elif item == 'Installment':
                self.loan_dialog = MsgBox(self.page,self.primary_color,self.secondary_color,item,self.boxs[item],icons.HANDYMAN_ROUNDED)
                
# def main(page:Page):
#     primary_color = '#25D366'
#     secondary_color = '#075E54'
#     AlertBox(page,primary_color,secondary_color)
# if __name__ == '__main__':
#     app(target=main)
