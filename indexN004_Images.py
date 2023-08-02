"""
Les images

Date : 02-08-23
Editeur : Laurent Reynaud
"""

from taipy.gui import Gui, navigate
import webbrowser

image = 'data/dog.png'

def image_action(state):
    webbrowser.open("https://www.royalrepublic.net/")

menu="""
<|menu|label=Menu|lov={[('Page-1', 'Page 1'), ('Page-2', 'Page 2'),]}|on_action=on_menu|>
"""

page1="""
# Insertion d'une image 😎

<|{image}|image|height=250px|width=250px|on_action=image_action|>
"""

page2="""
# Hyperliens

Cette page a été conçue avec la librairie [Taipy](https://www.taipy.io/)
"""

def on_menu(state, var_name, function_name, info):
    page = info['args'][0]
    navigate(state, to=page)

pages = {
    "/": menu,
    "Page-1": page1,
    "Page-2": page2,
}

Gui(pages=pages).run(dark_mode=True)
