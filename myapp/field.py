from flet import*

class Field(UserControl):
    def __init__(self,page,primary_color,secondary_color,value):
        self.page = page
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.value = value
    def EntryField(self):
        field = CupertinoTextField(
                    placeholder_text=self.value,
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
                )
        # self.page.add(field)
# def main(page:Page):
#     primary_color = '#DA7756'
#     secondary_color = '#075E54'
#     value = 'Processing Rate'
#     cal = Field(page,primary_color,secondary_color,value)
#     page.go('/front_page')
# if __name__ == '__main__':
#     app(target=main)
