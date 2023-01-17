from _collections import deque

seconds = int(input())
free_window = int(input())
cars = deque()
passed_cars = 0
car_is_hit = False
while True:
    command = input()

    if command == "END" or car_is_hit:
        break

    elif command == "green":
        green_light_sec = seconds

        while cars and green_light_sec > 0:
            current_car = cars.popleft()
            car = green_light_sec - len(current_car)

            if car >= 0:
                passed_cars += 1
                green_light_sec -= len(current_car)
            else:
                if free_window - (-car) >= 0:
                    passed_cars += 1
                    break
                else:
                    index = free_window + green_light_sec
                    print('A crash happened!')
                    print(f"{current_car} was hit at {current_car[index]}.")
                    car_is_hit = True
                    break
    else:
        cars.append(command)

if not car_is_hit:
    print(f"Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
