from flet import*
from result import ResultPage
from field import Field

# add a class of calculator

class Calculator(UserControl):
    def __init__(self,page,primary_color,secondary_color):
        super().__init__()
        self.page = page
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.values = 'hello world'
        self.fieldentry = Field(self.page,self.primary_color,self.secondary_color,self.values)
        self.build()
    def build(self):
        self.front_page = View(
            route='/front_page',
            controls=[
                Container(
                    height=50,
                    width=360,
                    content=Image(
                        src='../assets/RCDP-Logo-Final.png'
                    ),
                    image_fit=ImageFit.COVER
                ),
                ListTile(
                    leading=Container(
                        width=5,
                        height=40,
                        bgcolor=self.primary_color
                    ),
                    title=Text(
                        value='Area Manager',
                        size=12,
                        weight=FontWeight.BOLD,
                        color=colors.with_opacity(0.25,'#000000')
                    ),
                    subtitle=Text(
                        value='Syed Mohsin Shah Sahib',
                        weight=FontWeight.BOLD,
                        size=14,
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
                # self.fieldentry.EntryField(),
                CupertinoButton(
                    # text='Go Next',
                    bgcolor=colors.with_opacity(0.3,self.primary_color),
                    color=self.primary_color,
                    width=350,
                    height=40,
                    padding=padding.all(0),
                    border_radius=5,
                    content=Text(
                        value='Go Next',
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
        result_page = ResultPage(self.page,self.primary_color,self.secondary_color)
        self.page.go('/result_page')
        self.page.update()
        
        


def main(page:Page):
    primary_color = '#DA7756'
    secondary_color = '#075E54'
    cal = Calculator(page,primary_color,secondary_color)
    page.go('/front_page')
if __name__ == '__main__':
    app(target=main)