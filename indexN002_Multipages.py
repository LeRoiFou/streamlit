"""
Taipy : multi-pages

Date : 02-08-2023
Editeur : Laurent Reynaud
"""

from taipy.gui import Gui, navigate

root_md="<|menu|label=Menu|lov={[('Page-1', 'Page 1'), ('Page-2', 'Page 2'), ('Page-3', 'Page 3')]}|on_action=on_menu|>"

page1="""
## Multi-pages - onglet n° 1
"""

page2="""
## Multi-pages - onglet n° 2
"""

page3="""
## Multi-pages - onglet n° 3
"""

def on_menu(state, var_name, function_name, info):
    page = info['args'][0]
    navigate(state, to=page)


pages = {
    "/": root_md,
    "Page-1": page1,
    "Page-2": page2,
    "Page-3": page3,
}

Gui(pages=pages).run(dark_mode=True)
