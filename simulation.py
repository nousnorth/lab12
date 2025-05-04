import turtle
from sun import Sun
from planet import Planet
from solar_system import SolarSystem

class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self.__solar_system = solar_system
        self.__width = width
        self.__height = height
        self.__num_periods = num_periods
        self.__t = turtle.Turtle()
        self.__t.hideturtle()
        self.__screen = turtle.Screen()
        self.__screen.setup(width=self.__width, height=self.__height)
        self.__screen.bgcolor("black")
        self.__t.clear()

    def run(self):
        self.__solar_system.show_planets()
        for a_move in range(self.__num_periods):
            self.__solar_system.move_planets()
            self.__solar_system.show_planets()

    def freeze(self):
        self.__screen.exitonclick()

if __name__ == '__main__':
    solar_system = SolarSystem()
    simulation = Simulation(solar_system, 500, 500, 2000)

    sol = Sun("Sol", 5000, 1000000000000000, 5800, 0, 0)
    solar_system.add_sun(sol)

    nova = Planet("Nova", 40, 70, 80.0, 10.0, 140.0,  21.0, 0.0, "blue")
    solar_system.add_planet(nova)

    earth = Planet("Earth", 48, 100, 75.0, 0.0, 75.0, 20.0, 0.0, "green")
    solar_system.add_planet(earth)

    mars = Planet("Mars", 20, 10, 115.0, 20.0, 115.0, 16.0, 0.0, "red")
    solar_system.add_planet(mars)

    simulation.run()