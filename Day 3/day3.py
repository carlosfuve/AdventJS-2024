def organize_inventory(inventory: dict) -> dict:
  invent_org = {}
  for invent in inventory:
    name, quan, cat = invent['name'], invent['quantity'], invent['category']
    invent_org.setdefault(cat, {name:0})
    invent_org[cat][name] = invent_org[cat].get(name, 0) + quan

  return invent_org