from flet import*

class MsgBox(UserControl):
    def __init__(self,page,primary_color,secondary_color,titles,items,icon_btn):
        self.page = page
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.items = items
        self.icon = icon_btn
        self.title = titles
        self.Msg()
    # here we call the alertbox
    def Msg(self):
        self.dialog = CupertinoAlertDialog(
                    open=True,
                    content=Column(
                        controls=[
                            Icon(
                            self.icon,
                            size=50,
                            color=self.primary_color
                        ),
                            Text(
                                value=self.title,
                                weight=FontWeight.BOLD,
                                size=24,
                                color=colors.with_opacity(0.5,'#000000')
                            ),
                            Text(
                                value=self.items,
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
                                    on_click=lambda e: self.ClosedButton(self.dialog),
                                    style=ButtonStyle(
                                        color='#F44336'
                                    )
                                ),
                            ],
                            alignment=MainAxisAlignment.SPACE_EVENLY
                        )
                    ]
                )
        self.page.add(self.dialog)
    def ClosedButton(self,value):
        value.open = False
        self.page.update()