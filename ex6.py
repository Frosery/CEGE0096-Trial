def check_temp(temp_list, current_temp):
    message = ''
    if temp_list[0] > current_temp:
        message = "Freezing"
    elif temp_list[1] > current_temp:
        message = 'Very Cold'
    elif temp_list[2] > current_temp:
        message = 'Cold'
    elif temp_list[3] > current_temp:
        message = 'Normal'
    elif temp_list[4] > current_temp:
        message = 'Hot'
    else:
        message = 'Very Hot'
    return message


if __name__ == '__main__':
    temps = []
    current_temperature = float(input('What is current temperature:'))

    for x in range(5):
        a = float(input("Add t{}: ".format(x+1)))
        temps.append(a)

    print(check_temp(temps, current_temperature))

