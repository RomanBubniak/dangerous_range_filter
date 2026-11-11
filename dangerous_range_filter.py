servers_temperature = [55, 70, 85, 90, 60, 95]
def danger_range(some_list, limit):
    danger_list = []
    limit = 80
    for i in some_list:
        if i >= limit:
            danger_list.append(i)
    return danger_list
danger_temp = danger_range(servers_temperature, 80)
print(danger_temp)