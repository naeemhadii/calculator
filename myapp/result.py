from flet import *
from dialog import AlertBox
from field import Field

class ResultPage(UserControl):
    def __init__(self, page, primary_color, secondary_color):
        super().__init__()
        self.page = page
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.Result()
    
    def Result(self):
        result = View(
            route='/result_page',
            controls=[
                Text(
                    value='Schedule',
                    size=22,
                    weight=FontWeight.BOLD
                ),
                ListTile(
                    leading=Column(
                        controls=[
                            Container(
                                height=50,
                                width=50,
                                bgcolor=colors.with_opacity(0.2, self.primary_color),
                                border_radius=100,
                                content=Icon(
                                    icons.MONEY_ROUNDED,
                                    color=self.primary_color,
                                    size=35
                                )
                            )
                        ]
                    ),
                    title=Text(
                        value='Repayment Amount',
                        size=12,
                        color=colors.with_opacity(0.60, '#000000'),
                        weight=FontWeight.BOLD
                    ),
                    subtitle=Text(
                        value='133750',
                        size=24,
                        color=colors.with_opacity(0.60, '#000000'),
                        weight=FontWeight.BOLD
                    ),
                    trailing=Column(
                        controls=[
                            IconButton(
                                icons.MORE_VERT,
                                icon_size=18,
                                on_click=lambda e: self.ClickedButton('Loan Amount')
                            ),
                        ]
                    )
                ),
                # Add other ListTile components here...
                ListTile(
                    leading=Column(
                        controls=[
                            Container(
                                height=50,
                                width=50,
                                bgcolor=colors.with_opacity(0.2, self.primary_color),
                                border_radius=100,
                                content=Icon(
                                    icons.LOCAL_ACTIVITY_ROUNDED,
                                    color=self.primary_color,
                                    size=35
                                )
                            )
                        ]
                    ),
                    title=Text(
                        value='Processing Amount',
                        size=12,
                        color=colors.with_opacity(0.60, '#000000'),
                        weight=FontWeight.BOLD
                    ),
                    subtitle=Text(
                        value='5000',
                        size=24,
                        color=colors.with_opacity(0.60, '#000000'),
                        weight=FontWeight.BOLD
                    ),
                    trailing=Column(
                        controls=[
                            IconButton(
                                icons.MORE_VERT,
                                icon_size=18,
                                on_click=lambda e: self.ClickedButton('Processing Fee Rate')
                            ),
                        ]
                    )
                ),
                ListTile(
                    leading=Column(
                        controls=[
                            Container(
                                height=50,
                                width=50,
                                bgcolor=colors.with_opacity(0.2, self.primary_color),
                                border_radius=100,
                                content=Icon(
                                    icons.FACT_CHECK_ROUNDED,
                                    color=self.primary_color,
                                    size=35
                                )
                            )
                        ]
                    ),
                    title=Text(
                        value='Markup Amount',
                        size=12,
                        color=colors.with_opacity(0.60, '#000000'),
                        weight=FontWeight.BOLD
                    ),
                    subtitle=Text(
                        value='5000',
                        size=24,
                        color=colors.with_opacity(0.60, '#000000'),
                        weight=FontWeight.BOLD
                    ),
                    trailing=Column(
                        controls=[
                            IconButton(
                                icons.MORE_VERT,
                                icon_size=18,
                                on_click=lambda e: self.ClickedButton('Markup Amount')
                            ),
                        ]
                    )
                ),
                ListTile(
                    leading=Column(
                        controls=[
                            Container(
                                height=50,
                                width=50,
                                bgcolor=colors.with_opacity(0.2, self.primary_color),
                                border_radius=100,
                                content=Icon(
                                    icons.HANDYMAN_ROUNDED,
                                    color=self.primary_color,
                                    size=35
                                )
                            )
                        ]
                    ),
                    title=Text(
                        value='Installment',
                        size=12,
                        color=colors.with_opacity(0.60, '#000000'),
                        weight=FontWeight.BOLD
                    ),
                    subtitle=Text(
                        value='5000',
                        size=24,
                        color=colors.with_opacity(0.60, '#000000'),
                        weight=FontWeight.BOLD
                    ),
                    trailing=Column(
                        controls=[
                            IconButton(
                                icons.MORE_VERT,
                                icon_size=18,
                                on_click=lambda e: self.ClickedButton('Installment')
                            ),
                        ]
                    )
                ),
                CupertinoButton(
                    width=350,
                    height=40,
                    bgcolor=colors.with_opacity(0.2,self.primary_color),
                    content=Text(
                        value='Find More',
                        weight=FontWeight.BOLD,
                        color=self.primary_color
                    ),
                    on_click=lambda e:self.RouteChange(),
                    padding=padding.all(0)

                )
            ],
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
        self.page.views.append(result)
        

    def ClickedButton(self, value):
        if value == 'Loan Amount':
            # Show a dialog or a proper PopupMenu instead
            msg1 = AlertBox(self.page,self.primary_color,self.secondary_color)
            msg1.AlertMsg('Loan Amount')
        elif value == 'Processing Fee Rate':
            # Show a dialog or a proper PopupMenu instead
            msg1 = AlertBox(self.page,self.primary_color,self.secondary_color)
            msg1.AlertMsg('Processing Fee Rate')
        elif value == 'Markup Amount':
            # Show a dialog or a proper PopupMenu instead
            msg1 = AlertBox(self.page,self.primary_color,self.secondary_color)
            msg1.AlertMsg('Markup Amount')
        elif value == 'Installment':
            # Show a dialog or a proper PopupMenu instead
            msg1 = AlertBox(self.page,self.primary_color,self.secondary_color)
            msg1.AlertMsg('Installment')
    def DialogAction(self):
        if self.page.dialog.open == True:
            self.page.dialog.open = False
            self.page.update()
    def RouteChange(self):
        from main import Calculator
        Calculator(self.page,self.primary_color,self.secondary_color)
        self.page.go('/front_page')
        print('result page is here')

        # self.page.update()

        


# def main(page: Page):
#     primary_color = '#DA7756'
#     secondary_color = '#075E54'
#     con = ResultPage(page, primary_color, secondary_color)
#     page.go('/result_page')

# if __name__ == '__main__':
#     app(target=main)
