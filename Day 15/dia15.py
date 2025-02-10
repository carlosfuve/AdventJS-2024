def draw_table(data: list[dict[str, str | int]]) -> str:
    name_cols = list(data[0].keys())
    max_len_cols = [max([len(str(row[col])) for row in data] + [len(col)]) for col in name_cols]
    

    separador = "+" + "+".join(["-" * (width + 2) for width in max_len_cols]) + "+"

    box_header = "| " + " | ".join(
        header.capitalize().ljust(max_len_cols[i]) for i, header in enumerate(name_cols)
    ) + " |"

    rows = [
        "| " + " | ".join(
            str(row[key]).ljust(max_len_cols[i]) for i, key in enumerate(name_cols)
        ) + " |"
        for row in data
    ]

    return "\n".join([separador, box_header, separador] + rows + [separador])


print(
  draw_table([
  { 'name': 'Alice', 'city': 'London' },
  #{ 'name': 'Bob', 'city': 'Paris' },
 #{ 'name': 'Charlie', 'city': 'New York' }
])
)


print(
draw_table([
  { 'gift': 'Doll', 'quantity': 10 },
  { 'gift': 'Book', 'quantity': 5 },
  { 'gift': 'Music CD', 'quantity': 1 }
])
)
