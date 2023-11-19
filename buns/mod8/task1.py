class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self.__coordinates = coordinates
        self.__speed = speed
        self.__brand = brand
        self.__year = year
        self.__number = number

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        if not isinstance(coordinates, tuple) or len(coordinates) != 2 or not all(
                isinstance(coord, float) for coord in coordinates):
            raise ValueError("Invalid coordinates. Should be a tuple of two float.")
        self.__coordinates = coordinates

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if not isinstance(speed, float):
            raise ValueError("Invalid speed. Should be an float.")
        self.__speed = speed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if not isinstance(brand, str):
            raise ValueError("Invalid brand. Should be a string.")
        self.__brand = brand

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise ValueError("Invalid year. Should be an integer.")
        self.__year = year

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, int):
            raise ValueError("Invalid number. Should be an integer.")
        self.__number = number

    def __str__(self):
        '''
           Представление всей информации для вывода в методе print()
        '''
        return f"Coordinates: {self.__coordinates}, Speed: {self.__speed}, Brand: {self.__brand}, Year: {self.__year}, Number: {self.__number}"


    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        '''
        Присутствие транспортного средства в пределах заданнй области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        '''
        x, y = self.__coordinates
        is_x_inside = pos_x <= x <= pos_x + length
        is_y_inside = pos_y <= y <= pos_y + width
        return is_x_inside and is_y_inside


class Passenger:
    def __init__(self, passengers_capacity, number_of_passengers):
        self.__passengers_capacity = passengers_capacity
        self.__number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if not isinstance(passengers_capacity, int):
            raise ValueError("Invalid passengers_capacity. Should be an integer")
        self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if not isinstance(number_of_passengers, int):
            raise ValueError("Invalid number_of_passengers. Should be an integer")
        self.__number_of_passengers = number_of_passengers


class Cargo:
    def __init__(self, carrying):
        self.__carrying = carrying

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if not isinstance(carrying, int):
            raise ValueError("Invalid carrying. Should be an integer")
        self.__carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        Transport.__init__(self, coordinates, speed, brand, year, number)
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise ValueError("Invalid height. Should be an int.")
        self.__height = height


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        Transport.__init__(self, coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        Transport.__init__(self, coordinates, speed, brand, year, number)
        self.__port = port

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if not isinstance(port, str):
            raise ValueError("Invalid port. Should be a string.")
        self.__port = port


class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number):
        Auto.__init__(self, coordinates, speed, brand, year, number)


class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Cargo.__init__(self, carrying)


class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)


class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Ship.__init__(self, coordinates, speed, brand, year, number,port)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Cargo.__init__(self, carrying)


class AirplaneMaize(Plane):
    def __init__(self, coordinates, speed, brand, year, number, height):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)


class PassengerPlane(Plane, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, height, passengers_capacity, number_of_passengers):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoPlane(Plane, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, height, carrying):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Cargo.__init__(self, carrying)


class Seaplane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, port):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Ship.__init__(self, coordinates, speed, brand, year, number, port)

seaplane = Seaplane((0, 0), 0, "BMW", 2000, 10, 100, "Maria")
print(seaplane)
print(seaplane.isInArea(0, 0,100,100))