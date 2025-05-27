

# update ttk tree
def update_tree_row(tree, value, row_id, col_index):
    current = list(tree.item(row_id, 'values'))
    current[col_index] = value
    tree.item(row_id, values=tuple(current))
    return row_id

def update_or_insert_tree_row(tree, row_list, value, row_index, col_index, insert_values_func):
    if row_index < len(row_list):
        # row exists, so update
        # print("updating row", row_index, "with value", value)
        update_tree_row(tree, value, row_id=row_list[row_index], col_index=col_index)
    else:
        # row does not exist, so insert
        # print("inserting new row with value", value)
        row_id = tree.insert('', 'end', values=insert_values_func(value))
        row_list.append(row_id)