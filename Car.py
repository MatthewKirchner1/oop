import CarClass as c


def accelerate_5(car_obj):
    for n in range(5):
        car_obj.accelerate()
        print("Current Speed: " + str(car_obj.get_speed()))


def brake_5(car_obj):
    for n in range(5):
        car_obj.brake()
        print("Current Speed: " + str(car_obj.get_speed()))


def main():
    my_car = c.Car()

    accelerate_5(my_car)

    print("-------------------------------------------------------------")
    brake_5(my_car)


main()