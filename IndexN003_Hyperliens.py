"""
Taipy : les hyperliens

Date : 02-08-2023
Editeur : Laurent Reynaud
"""

from taipy import Gui

root_md="""
# Hyperliens

Cette page a été conçue avec la librairie [Taipy](https://www.taipy.io/).
"""

page = {"/":root_md,}

Gui(pages=page).run(dark_mode=True)
