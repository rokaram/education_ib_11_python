def cost_of_message(text, cost_symbol):
    cost = len(text) * cost_symbol
    return f"{ int(cost) }р. { int(round(cost - int(cost), 2) * 100) }к."


print(cost_of_message(input("Write the message: "), .80))
