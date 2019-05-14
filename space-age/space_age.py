class SpaceAge(object):
    __SECONDS_IN_EARTH_YEAR = 365.25 * 24 * 60 * 60

    def __init__(self, seconds: int):
        self.seconds = seconds

    def on_earth(self) -> float:
        return self.__calculate_planetary_years(1)

    def on_mercury(self) -> float:
        return self.__calculate_planetary_years(0.2408467)

    def on_venus(self) -> float:
        return self.__calculate_planetary_years(0.61519726)

    def on_mars(self) -> float:
        return self.__calculate_planetary_years(1.8808158)

    def on_jupiter(self) -> float:
        return self.__calculate_planetary_years(11.862615)

    def on_saturn(self) -> float:
        return self.__calculate_planetary_years(29.447498)

    def on_uranus(self) -> float:
        return self.__calculate_planetary_years(84.016846)

    def on_neptune(self) -> float:
        return self.__calculate_planetary_years(164.79132)

    def __calculate_planetary_years(self, orbital_period: float) -> float:
        earth_years = self.seconds / self.__SECONDS_IN_EARTH_YEAR
        planetary_years = earth_years / orbital_period
        return round(planetary_years, 2)
