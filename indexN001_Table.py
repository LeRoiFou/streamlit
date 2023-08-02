"""
Lien : https://docs.taipy.io/en/develop/manuals/gui/viselements/table/

Avec Taipy, c'est possible de présenter des tables

Date : 01-08-23
Éditeur : Laurent Reynaud
"""

from taipy.gui import Gui

"1er exemple"

# # x: [1..5]
# x_range = range(1, 6)
# data = {
#     "X": x_range,
#     "Y": [x*x for x in x_range]
# }

# column_orders = [("X;Y", "Squared"), ("Y;X", "Square root")]
# columns = column_orders[0]

# page = """
# <|{data}|table|columns={columns[0]}|show_all|rebuild|>

# <|{columns}|toggle|lov={column_orders}|>
# """

"2ème exemple"

# x_range = [-10, -6, -2, 2, 6, 10]
x_range = range(-10, 11, 4)

data = {
    "x": x_range,
    # y1 = x*x
    "y1": [x*x for x in x_range],
    # y2 = 100-x*x
    "y2": [100-x*x for x in x_range]
}

page = """
<|{data}|table|columns=x;y1|tooltip={lambda state, val, idx: "A tooltip" if idx % 2 == 0 else "Another tooltip"}|>
"""

Gui(page=page).run()
