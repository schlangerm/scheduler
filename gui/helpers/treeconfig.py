from tkinter import ttk




# These do not work once a row is selected so they have been refactored out:
def update_row_height(tree, item_list):
    max_lines = 1
    max_lines = max(max_lines, len(item_list))

    apply_treeview_rowheight(tree, rowheight=max_lines * 20)

def apply_treeview_rowheight(tree, rowheight=20):
 
    # Applies a unique rowheight to the given tree

    style_name = f'{id(tree)}.Treeview'
    style = ttk.Style()

    # Base treeview layout copy
    style.layout(style_name, style.layout("Treeview"))

    style.theme_use("clam")
    # Row Height Configuration
    style.configure(style_name, rowheight=rowheight)
    # Row Height Configuration for Items (rows)
    style.configure(f'{style_name}.Item', rowheight=rowheight)
    style.map(style_name,
              background=[('selected', style.lookup('Treeview', 'background'))],
              foreground=[('selected', style.lookup('Treeview', 'foreground'))])

    tree.configure(style=style_name)