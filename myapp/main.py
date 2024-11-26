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
                    value='hello world'
                )
            ]
        )
        self.page.views.append(front_page)

def main(page:Page):
    primary_color = '#25D366'
    secondary_color = '#075E54'
    cal = Calculator(page,primary_color,secondary_color)
    page.go('/front_page')
if __name__ == '__main__':
    app(target=main)