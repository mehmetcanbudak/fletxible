import os


def route_string_method(route):
    string = f"\tif route == '/{route}':\n\t\te.page.views.append(route_keys[route].loader.load_module().View())\n\t\te.page.go('/{route}')\n"

    string = string.expandtabs(4)
    return string


def navigation_example_method():
    route_list: list = []
    for file in os.listdir("pages"):
        # Set the path of the file to loop over folders and only include files
        path = os.path.join("pages", file)

        # If the path is NOT a folder, continue ...
        if not os.path.isdir(path):
            filename = os.path.splitext(file)[0]
            string = f"ft.Text(size=13, weight='bold', spans=[ft.TextSpan('{filename.capitalize()}', on_click=lambda e: route(e, '/{filename}'))]),"
            route_list.append(string)

    return route_list


def set_app_route_method():
    string = """from script import route_keys
def route(e, route):
    e.page.views.clear()
%s
"""

    return string


def set_app_default_pages():
    string = """# Flet module import
import flet as ft
from route import route

class ViewControls(ft.UserControl):
    def __init__(self):
        #
        self.stack = ft.Stack(expand=True)

        #
        self.row = ft.Row(expand=True, spacing=2)

        #
        self.drawer = ft.Container(
            expand=True,
            width=0,
            bgcolor="#23262d",
            animate=ft.Animation(550, "ease"),
            shadow=None,
            content=ft.Column(
                expand=True,
                opacity=0,
                animate_opacity=ft.Animation(200, "easeIn"),
                controls=[
                    ft.Container(
                        bgcolor="#34373e",
                        height=60,
                        content=ft.Row(
                            alignment="center",
                            controls=[
                                ft.Text(
                                    # site name here ...
                                    size=21,
                                    weight="w700",
                                )
                            ],
                        ),
                    )
                ],
            ),
        )
        
        #
        self.left_panel = ft.Container(
            expand=1,
            padding=ft.padding.only(top=65),
            content=ft.Column(
                expand=True,
                alignment="start",
                controls=[],
            ),
        )

        #
        self.middle_panel = ft.Container(
            expand=5,
            padding=ft.padding.only(top=65, right=15, left=15),
            alignment=ft.alignment.top_center,
            content=ft.Column(
                expand=True,
                scroll="hidden",
                alignment="start",
                controls=[],
            ),
        )

        #
        self.right_panel = ft.Container(
            expand=1,
            padding=ft.padding.only(top=65),
            content=ft.Column(
                expand=True,
                alignment="start",
                controls=[],
            ),
        )

        self.nav = ft.Row(
            alignment="center",
            controls=[
            # start #
            
            # end #
            ],
        )

        #
        self.nav_mobile = ft.IconButton(
            icon=ft.icons.MENU_SHARP, visible=False, icon_size=14, icon_color="white",
            on_click=lambda e: self.show_drawer(e),

        )

        #
        self.header = ft.Container(
            bgcolor="#34373e",
            height=60,
            padding=ft.padding.only(left=60, right=60),
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=4,
                color=ft.colors.with_opacity(0.25, "black"),
                offset=ft.Offset(2, 2),
            ),
            content=ft.Row(
                alignment="spaceBetween",
                controls=[
                    ft.Row(
                        alignment="start",
                        controls=[ft.Text("fletxible.", size=21, weight="w700")],
                    ),
                    self.nav,
                    self.nav_mobile,
                ],
            ),
        )
        super().__init__()

    def show_drawer(self, e):
        if self.drawer.width != 220:
            self.drawer.width = 220
            self.drawer.shadow = ft.BoxShadow(
                blur_radius=15,
                spread_radius=8,
                color=ft.colors.with_opacity(0.25, "black"),
                offset=(4, 4),
            )
            
            self.drawer.content.opacity = 1
            self.drawer.update()

        else:
            self.drawer.content.opacity = 0
            self.drawer.update()
        
            self.drawer.width = 0
            self.drawer.shadow = None

        self.drawer.update()

    def hide_navigation(self):
        self.nav.visible = False
        self.nav.update()
        
        self.left_panel.visible = False
        self.left_panel.update()

        self.right_panel.visible = False
        self.right_panel.update()

        self.nav_mobile.visible = True
        self.nav_mobile.update()

    def show_navigation(self):
        self.drawer.width = 0
        self.drawer.shadow = None
        self.drawer.update()
        
        self.nav.visible = True
        self.nav.update()
        
        self.left_panel.visible = True
        self.left_panel.update()

        self.right_panel.visible = True
        self.right_panel.update()

        self.nav_mobile.visible = False
        self.nav_mobile.update()

    def build(self):
        #
        self.row.controls = [
            self.left_panel,
            self.middle_panel,
            self.right_panel,
        ]

        #
        self.stack.controls = [self.row, self.header, self.drawer]

        #
        return self.stack


class View(ft.View):
    def __init__(
        self,
        *args,
        bgcolor="#23262d",
        padding=0,
        controls=[ft.Container(expand=True, content=ViewControls())],
        **kwargs,
    ):
        super().__init__(
            *args,
            bgcolor=bgcolor,
            padding=padding,
            controls=controls,
            **kwargs,
        )

"""

    return string


def set_up_yaml_file():
    string = """
site-name: ""
repo-url: ""

theme:
  - bgcolor: "#2e2f3e"
  - primary: "teal"
  - accent: "blue300"

nav:
  - Home: "index.py"
  - About: "about.py"

"""
    return string


def set_up_main_method():
    string = """# Modules for Flet and Fletxible
import flet as ft
from script import script


def main(page: ft.Page):
    # Run main script ... 
    script(page)
    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)  
"""

    return string
