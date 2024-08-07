class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._hometown = value
        else:
            raise ValueError("Hometown must be a non-empty string")

    def add_concert(self, concert):
        if concert not in self._concerts:
            self._concerts.append(concert)

    def concerts(self):
        return self._concerts

    def venues(self):
        return list({concert.venue for concert in self._concerts})

    def introductions(self):
        return [concert.introduction() for concert in self._concerts]

    def play_in_venue(self, venue):
        return [concert for concert in self._concerts if concert.venue == venue]


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        band.add_concert(self)
        venue.add_concert(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise ValueError("Band must be an instance of Band")

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError("Venue must be an instance of Venue")

    def is_in_hometown(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"{self.band.name} is performing at {self.venue.name} on {self.date}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string")

    def add_concert(self, concert):
        if concert not in self._concerts:
            self._concerts.append(concert)

    def concerts(self):
        return self._concerts

    def bands(self):
        return list({concert.band for concert in self._concerts})
