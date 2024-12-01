from flet import*
from dialog import AlertBox

class ListCards(UserControl):
    def __init__(self,page,primary_color,secondary_color):
        super().__init__()
        self.page = page
        self.primary_color = primary_color
        self.secondary_color = secondary_color
    def ListCard(self,icon_value,text_value,original_value):
        lists = ListTile(
            leading=Column(
                controls=[
                    Container(
                        height=50,
                        width=50,
                        bgcolor=colors.with_opacity(0.2, self.primary_color),
                        border_radius=100,
                        content=Icon(
                            icon_value,
                            color=self.primary_color,
                            size=35
                        )
                    )
                ]
            ),
            title=Text(
                value=text_value,
                size=12,
                color=colors.with_opacity(0.60, '#000000'),
                weight=FontWeight.BOLD
            ),
            subtitle=Text(
                value=original_value,
                size=24,
                color=colors.with_opacity(0.60, '#000000'),
                weight=FontWeight.BOLD
            ),
            trailing=Column(
                controls=[
                    IconButton(
                        icons.MORE_VERT,
                        icon_size=18,
                        on_click=lambda e: self.ClickedButton(text_value)
                    )
                ]
            )
        )
        return lists
    def ClickedButton(self, value):
        if value == 'Loan Amount':
            # Show a dialog or a proper PopupMenu instead
            msg1 = AlertBox(self.page,self.primary_color,self.secondary_color)
            msg1.AlertMsg('Loan Amount')
        elif value == 'Processing Rate':
            # Show a dialog or a proper PopupMenu instead
            msg1 = AlertBox(self.page,self.primary_color,self.secondary_color)
            msg1.AlertMsg('Processing Rate')
        elif value == 'Markup Rate':
            # Show a dialog or a proper PopupMenu instead
            msg1 = AlertBox(self.page,self.primary_color,self.secondary_color)
            msg1.AlertMsg('Markup Rate')
        elif value == 'Installment':
            # Show a dialog or a proper PopupMenu instead
            msg1 = AlertBox(self.page,self.primary_color,self.secondary_color)
            msg1.AlertMsg('Installment')
        elif value == 'Value Error':
            # Show a dialog or a proper PopupMenu instead
            msg1 = AlertBox(self.page,self.primary_color,self.secondary_color)
            msg1.AlertMsg('Value Error')
    def DialogAction(self):
        if self.page.dialog.open == True:
            self.page.dialog.open = False
            self.page.update()

# def main(page:Page):
#     primary_color = '#DA7756'
#     secondary_color = '#075E54'
#     ListCards(page,primary_color,secondary_color)

# if __name__ == '__main__':
#     app(target=main)