def find_tool_by_name(tools, name):
    return next((tool for tool in tools if tool['name'] == name), None)

def create_tool(name, damage, durability):
    return {'name': name, 'damage': damage, 'durability': durability}

def update_tool_durability(tool, amount):
    tool['durability'] = max(0, tool['durability'] - amount)

def is_tool_broken(tool):
    return tool['durability'] == 0

