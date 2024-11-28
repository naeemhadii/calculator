from flet import*

class AlertBox(UserControl):
    def __init__(self,page,primary_color,secondary_color):
        self.page = page
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.Alertbox()

    # here we call the alertbox
    def Alertbox(self):
        boxs = {
            'Loan Amount' : 'RCDP offers tailored loans to empower individuals and businesses. Livestock loans support farmers in expanding operations, business loans help shop owners grow, agriculture loans boost farming activities with essential inputs, and handicraft loans aid artisans in enhancing production and marketing. These products foster economic growth and self-reliance across various sectors.',
            'Markup Rate': 'RCDP offers loans at a competitive markup rate of just 22%, significantly lower than many other microfinance institutions. This ensures affordable financial solutions for our clients, empowering them to grow their businesses, improve livelihoods, and achieve economic stability.',
            'Installment' : 'RCDP provides flexible, affordable monthly installments tailored to the loan tenure. For terms exceeding a year, installments are lower to ease repayment, though the markup rate is slightly higher. This approach ensures accessibility and convenience while supporting clients in managing their finances effectively.',
            'Processing Fee Rate': 'RCDP charges a 5% processing fee, which includes 1% for insurance, 2% for staff expenses, and 2% for administrative materials and documentation. This transparent fee structure ensures smooth operations while maintaining affordability for our clients.'
        }

        for box in boxs:
            if box == 'Loan Amount':
                self.loan_dialog = CupertinoAlertDialog(
                    open=True,
                    content=Column(
                        controls=[
                            Icon(
                            icons.WALLET_GIFTCARD,
                            size=50,
                            color='#DA7756'
                        ),
                            Text(
                                value='Loan Amount',
                                weight=FontWeight.BOLD,
                                size=24,
                                color=colors.with_opacity(0.5,'#000000')
                            ),
                            Text(
                                value=boxs['Loan Amount'],
                                color=colors.with_opacity(0.5,'#000000')
                            )
                        ]
                    ),
                    actions=[
                        Row(
                            controls=[
                                TextButton(
                                    text='Close',
                                    height=50,
                                    on_click=lambda e: self.ClosedButton(self.loan_dialog),
                                    style=ButtonStyle(
                                        color='#DA7756'
                                    )
                                ),
                            ],
                            alignment=MainAxisAlignment.SPACE_EVENLY
                        )
                    ]
                )
                self.page.add(self.loan_dialog)
    def ClosedButton(self,value):
        value.open = False
        self.page.update()
                
def main(page:Page):
    primary_color = '#25D366'
    secondary_color = '#075E54'
    AlertBox(page,primary_color,secondary_color)
if __name__ == '__main__':
    app(target=main)
