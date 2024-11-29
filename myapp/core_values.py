from flet import*

class CoreValues(UserControl):
    def __init__(self,page,primary_color,secondary_color):
        super().__init__()
        self.page = page
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.Core()
    
    def Core(self):
        cores = View(
            route='/core_value',
            controls=[
                Column(
                    controls=[
                        Text(
                            value='Core Values',
                            size=32,
                            weight=FontWeight.BOLD,
                            width=200,
                            height=80,
                            text_align=TextAlign.CENTER

                        ),
                        Row(
                            controls=[
                                Container(
                                    width=140,height=180,bgcolor=colors.with_opacity(0.2,self.primary_color),border_radius=5,
                                    content=Column(
                                        controls=[
                                            Container(
                                                height=50,
                                                width=50,
                                                bgcolor=colors.with_opacity(0.4,self.primary_color),
                                                content=Icon(
                                                    icons.VISIBILITY,
                                                    size=30
                                                ),
                                                border_radius=50
                                            ),
                                            Text(
                                                value='Vision',
                                                size=18,
                                                weight=FontWeight.BOLD
                                            ),
                                            CupertinoButton(
                                                text='Learn More',
                                                height=30,
                                                width=100,
                                                padding=padding.all(0),
                                                bgcolor=colors.with_opacity(0.4,self.primary_color),
                                                
                                            )
                                        ],
                                        alignment=MainAxisAlignment.SPACE_EVENLY,
                                        horizontal_alignment=CrossAxisAlignment.CENTER
                                    )
                                    ),
                                Container(
                                    width=140,height=180,bgcolor=colors.with_opacity(0.2,self.primary_color),border_radius=5,
                                    content=Column(
                                        controls=[
                                            Container(
                                                height=50,
                                                width=50,
                                                bgcolor=colors.with_opacity(0.4,self.primary_color),
                                                content=Icon(
                                                    icons.HANDSHAKE,
                                                    size=30
                                                ),
                                                border_radius=50
                                            ),
                                            Text(
                                                value='Values',
                                                size=18,
                                                weight=FontWeight.BOLD
                                            ),
                                            CupertinoButton(
                                                text='Learn More',
                                                height=30,
                                                width=100,
                                                padding=padding.all(0),
                                                bgcolor=colors.with_opacity(0.4,self.primary_color),
                                                
                                            )
                                        ],
                                        alignment=MainAxisAlignment.SPACE_EVENLY,
                                        horizontal_alignment=CrossAxisAlignment.CENTER
                                    )
                                    )
                            ],
                            alignment=MainAxisAlignment.CENTER
                        ),
                        Row(
                            controls=[
                                Container(
                                    width=140,height=180,bgcolor=colors.with_opacity(0.2,self.primary_color),border_radius=5,
                                    content=Container(
                                    width=140,height=180,bgcolor=colors.with_opacity(0.2,self.primary_color),border_radius=5,
                                    content=Column(
                                        controls=[
                                            Container(
                                                height=50,
                                                width=50,
                                                bgcolor=colors.with_opacity(0.4,self.primary_color),
                                                content=Icon(
                                                    icons.VISIBILITY,
                                                    size=30
                                                ),
                                                border_radius=50
                                            ),
                                            Text(
                                                value='Vision',
                                                size=18,
                                                weight=FontWeight.BOLD
                                            ),
                                            CupertinoButton(
                                                text='Learn More',
                                                height=30,
                                                width=100,
                                                padding=padding.all(0),
                                                bgcolor=colors.with_opacity(0.4,self.primary_color),
                                                
                                            )
                                        ],
                                        alignment=MainAxisAlignment.SPACE_EVENLY,
                                        horizontal_alignment=CrossAxisAlignment.CENTER
                                    )
                                    )
                                    ),
                                Container(
                                    width=140,height=180,bgcolor=colors.with_opacity(0.2,self.primary_color),border_radius=5,
                                    content=Container(
                                    width=140,height=180,bgcolor=colors.with_opacity(0.2,self.primary_color),border_radius=5,
                                    content=Column(
                                        controls=[
                                            Container(
                                                height=50,
                                                width=50,
                                                bgcolor=colors.with_opacity(0.4,self.primary_color),
                                                content=Icon(
                                                    icons.VISIBILITY,
                                                    size=30
                                                ),
                                                border_radius=50
                                            ),
                                            Text(
                                                value='Vision',
                                                size=18,
                                                weight=FontWeight.BOLD
                                            ),
                                            CupertinoButton(
                                                text='Learn More',
                                                height=30,
                                                width=100,
                                                padding=padding.all(0),
                                                bgcolor=colors.with_opacity(0.4,self.primary_color),
                                                
                                            )
                                        ],
                                        alignment=MainAxisAlignment.SPACE_EVENLY,
                                        horizontal_alignment=CrossAxisAlignment.CENTER
                                    )
                                    )
                                    )
                            ],
                            alignment=MainAxisAlignment.CENTER
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )
        self.page.views.append(cores)

def main(page:Page):
    primary_color = '#DA7756'
    secondary_color = '#075E54'
    calls = CoreValues(page,primary_color,secondary_color)
    page.go('/core_value')

if __name__ == '__main__':
    app(target=main)
