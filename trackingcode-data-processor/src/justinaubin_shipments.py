# simply run file to run 8 test cases below

def shipments(order, warehouses):
    # number of items in order
    items = len(order)
    # array of all orders filled from warehouses
    output_arr = []
    # individual output dictionary for specific warehouse
    output = {}
    # number of orders already filled
    count = 0
    for house in warehouses:
        # don't include output below unless inventory has desired product
        include = False
        output = {house['name']: {}}
        for item in order:
            # continue if order already filled
            if (order[item] == 0):
                continue
            # if item available
            if (item in house['inventory'].keys()):
                # difference between inventory and order amounts
                left = house['inventory'][item] - order[item]
                # more in inventory than order
                if (left >= 0):
                    # output = number of items asked for
                    output[house['name']][item] = order[item]
                    # update order amount and number of order successfully filled
                    order[item] = 0
                    count += 1
                # more in order than inventory
                else:
                    # output value = amount of item in inventory
                    output[house['name']][item] = house['inventory'][item]
                    # update amount in order
                    order[item] -= house['inventory'][item]
                # include in output  
                include = True
        # if item found in inventory, include in output
        if (include):
            output_arr.append(output)
    # If any item in order unaccounted for, return []
    if (items != count):
        return []
    # else return output warehouses and amounts
    return output_arr



if __name__ == "__main__":
    order1 = { "apple": 1, "orange": 1 }
    warehouse1 = [{ "name": "owd", "inventory": { "apple": 1, "orange": 1 } }]
    order2 = { "apple": 10 }
    warehouse2 = [{ "name": "owd", "inventory": { "apple": 5 } }, { "name": "dm", "inventory": { "apple": 5 }}]
    order3 = { "apple": 5, "banana": 5, "orange": 5 }
    warehouse3 = [ { "name": "owd", "inventory": { "apple": 5, "orange": 10 } }, { "name": "dm", "inventory": { "banana": 5, "orange": 10 } } ]
    order4 = { "apple": 1, "banana": 1 }
    warehouse4 = [{ "name": "owd", "inventory": { "apple": 1, "banana": 1 } }, { "name": "dm", "inventory": { "apple": 1, "orange": 1 } }]
    order5 = { "apple": 1 }
    warehouse5 = [{ "name": "owd", "inventory": { "apple": 0 } }]
    order6 = { "apple": 5, "banana": 10, "orange": 15, "watermelon": 15 }
    warehouse6 =  [ { "name": "owd", "inventory": { "apple": 5, "orange": 10 } }, { "name": "dm", "inventory": { "banana": 5, "orange": 10 }},
                    { "name": "cj", "inventory": { "watermelon": 15, "banana": 10 } } ]
    order7 = { "apple": 5, "banana": 10, "orange": 15, "watermelon": 15, "pear": 5}
    warehouse7 =  [ { "name": "owd", "inventory": { "apple": 5, "orange": 10 } }, { "name": "dm", "inventory": { "banana": 5, "orange": 10 }},
                    { "name": "cj", "inventory": { "watermelon": 15, "banana": 10 } } ]
    order8 = { "apple": 5, "banana": 10, "orange": 25, "watermelon": 15}
    warehouse8 =  [ { "name": "owd", "inventory": { "apple": 5, "orange": 10 } }, { "name": "dm", "inventory": { "banana": 5, "orange": 10 }},
                    { "name": "cj", "inventory": { "watermelon": 15, "banana": 10 } } ]

    orders = [order1, order2, order3, order4, order5, order6, order7, order8]
    warehouses = [warehouse1, warehouse2, warehouse3, warehouse4, warehouse5, warehouse6, warehouse7, warehouse8]


    for i, order in enumerate(orders):
        print(shipments(order, warehouses[i]))
