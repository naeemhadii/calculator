from flet import*
from result import ResultPage
from field import Field
from fields_items import dic_fields
from calculations import Calculations
from dialog import AlertBox


class Calculator(UserControl):
    def __init__(self,page,primary_color,secondary_color):
        super().__init__()
        self.page = page
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.build()
    def build(self):
        self.front_page = View(
            route='/front_page',
            controls=[
                ListTile(
                    title=Text(
                        value='Area Manager',
                        size=12,
                        weight=FontWeight.BOLD,
                        color=colors.with_opacity(0.25,'#000000')
                    ),
                    subtitle=Text(
                        value='Syed Mohsin Shah Sahib',
                        weight=FontWeight.BOLD,
                        size=20,
                        color=colors.with_opacity(0.50,'#000000')
                    ),
                    trailing=Column(
                        controls=[
                            Text(
                                value='Area - 18',
                                color=colors.with_opacity(0.25,'#000000'),
                                weight=FontWeight.W_600
                            )
                        ]
                    ),
                    title_alignment=ListTileTitleAlignment.TOP
                ),
                Column(
                    controls=[
                        Field(self.page,self.primary_color,self.secondary_color).EntryField(ref,key) for key, ref in dic_fields.items()
                    ]
                ),
                CupertinoButton(
                    # text='Go Next,
                    bgcolor=colors.with_opacity(0.3,self.primary_color),
                    color=self.primary_color,
                    width=370,
                    height=40,
                    padding=padding.all(0),
                    border_radius=5,
                    content=Text(
                        value='Calculate',
                        weight=FontWeight.BOLD
                    ),
                    on_click=lambda e:self.ViewResult(self.front_page)
                )
            ],
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
        self.page.views.append(self.front_page)
    def ViewResult(self,value):
        list = []
        for key, ref in dic_fields.items():
            list.append(ref.current.value)
        try:
            cal = Calculations(
                float(list[0]),
                float(list[1]),
                float(list[2]),
                float(list[3]),
            )

            for key , ref in dic_fields.items():
                if key == 'Loan Amount':
                    ref.current.value = cal[0]
                if key == 'Markup Rate':
                    ref.current.value = cal[1]
                if key == 'Installment':
                    ref.current.value = cal[2]
                if key == 'Processing Rate':
                    ref.current.value = cal[3]
            
            ResultPage(self.page,self.primary_color,self.secondary_color)
            self.page.go('/result_page')
            self.page.update()      
        except:
            msg1 = AlertBox(self.page,self.primary_color,self.secondary_color)
            msg1.AlertMsg('Value Error')
        
        
        


def main(page:Page):
    primary_color = '#DA7756'
    secondary_color = '#075E54'
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    cal = Calculator(page,primary_color,secondary_color)
    page.go('/front_page')
if __name__ == '__main__':
    app(target=main)