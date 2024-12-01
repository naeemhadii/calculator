from flet import *
from view_list import ListCards
from fields_items import dic_fields
from icon_file import icon_mapping

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
                Column(
                    controls=[
                        ListCards(self.page,self.primary_color,self.secondary_color).ListCard(
                            icon_mapping.get(key),
                            key,
                            ref.current.value
                        ) for key, ref in dic_fields.items()
                    ]
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
        
    def RouteChange(self):
        from main import Calculator
        Calculator(self.page,self.primary_color,self.secondary_color)
        self.page.go('/front_page')
