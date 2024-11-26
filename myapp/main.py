from flet import*

# add a class of calculator

class Calculator(UserControl):
    def __init__(self,page,primary_color,secondary_color):
        super().__init__()
        self.page = page
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.build()
    def build(self):
        front_page = View(
            route='/front_page',
            controls=[
                Text(
                    value='Rural Community Development Program',
                    weight=FontWeight.BOLD,
                    size=24,
                    text_align=TextAlign.CENTER
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
                CupertinoTextField(
                    placeholder_text='Loan Amount',
                    padding=padding.all(10),
                    bgcolor=colors.with_opacity(0.05,'#000000'),
                    border=border.all(0,colors.TRANSPARENT),
                    border_radius=5,
                    placeholder_style=TextStyle(
                        color=colors.with_opacity(0.45,'#000000'),
                        weight=FontWeight.W_600,
                    ),
                    text_style=TextStyle(
                        color=colors.with_opacity(0.45,'#000000'),
                        weight=FontWeight.W_600

                    ),
                    cursor_color=colors.with_opacity(0.45,'#000000'),
                    cursor_width=2.5,
                ),
                CupertinoTextField(
                    placeholder_text='No. of months',
                    padding=padding.all(10),
                    bgcolor=colors.with_opacity(0.05,'#000000'),
                    border=border.all(0,colors.TRANSPARENT),
                    border_radius=5,
                    placeholder_style=TextStyle(
                        color=colors.with_opacity(0.45,'#000000'),
                        weight=FontWeight.W_600,
                    ),
                    text_style=TextStyle(
                        color=colors.with_opacity(0.45,'#000000'),
                        weight=FontWeight.W_600

                    ),
                    cursor_color=colors.with_opacity(0.45,'#000000'),
                    cursor_width=2.5,
                ),
                CupertinoTextField(
                    placeholder_text='Markup Rate',
                    padding=padding.all(10),
                    bgcolor=colors.with_opacity(0.05,'#000000'),
                    border=border.all(0,colors.TRANSPARENT),
                    border_radius=5,
                    placeholder_style=TextStyle(
                        color=colors.with_opacity(0.45,'#000000'),
                        weight=FontWeight.W_600,
                    ),
                    text_style=TextStyle(
                        color=colors.with_opacity(0.45,'#000000'),
                        weight=FontWeight.W_600

                    ),
                    cursor_color=colors.with_opacity(0.45,'#000000'),
                    cursor_width=2.5,
                ),
                CupertinoTextField(
                    placeholder_text='Processing Rate',
                    padding=padding.all(10),
                    bgcolor=colors.with_opacity(0.05,'#000000'),
                    border=border.all(0,colors.TRANSPARENT),
                    border_radius=5,
                    placeholder_style=TextStyle(
                        color=colors.with_opacity(0.45,'#000000'),
                        weight=FontWeight.W_600,
                    ),
                    text_style=TextStyle(
                        color=colors.with_opacity(0.45,'#000000'),
                        weight=FontWeight.W_600

                    ),
                    cursor_color=colors.with_opacity(0.45,'#000000'),
                    cursor_width=2.5,
                ),
                CupertinoButton(
                    text='Calculate',
                    bgcolor=colors.with_opacity(0.3,self.primary_color),
                    color=self.primary_color,
                    width=350,
                    height=40,
                    padding=padding.all(0),
                    border_radius=5
                )
            ],
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
        self.page.views.append(front_page)

def main(page:Page):
    primary_color = '#25D366'
    secondary_color = '#075E54'
    cal = Calculator(page,primary_color,secondary_color)
    page.go('/front_page')
if __name__ == '__main__':
    app(target=main)