from flet import*

class Field(UserControl):
    def __init__(self,page,primary_color,secondary_color):
        self.page = page
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.values = Ref[CupertinoTextField]()
    def EntryField(self,value):
        field = CupertinoTextField(
            ref=self.values,
            placeholder_text=value,
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

        return field
    
