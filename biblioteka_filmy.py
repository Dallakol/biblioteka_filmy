
class Films:
    def __init__(self, title, year, genre):
        self.title = title # tytuł
        self.year = year #rok wydania
        self.genre = genre #gatunek
        


        #Variables
        self._no_plays = 0


    def __str__(self):
        return f'{self.title}, ({self.year})'    
    def __repr__(self):
        return f" title = {self.title} year = {self.year}"

    @property
    def current_no_plays(self):
        return self._no_plays

    @current_no_plays.setter
    def current_no_plays(self, value):
        self._no_plays = value


    def next_play(self, step =1): #Zwiększenie liczby odtworzeń o "step"
        self.current_no_plays += step
        print(f'Liczba odtworzeń {self.title} zwiększyła się o {step}')  
        
       

film1 = Films(title = "Shrek", year ="2001", genre ="Bajka")
film2 = Films(title = "Legion samobójców", year = "2021", genre = "Akcja")
film3 = Films(title = "Wyprawa do dżungi", year = "2021", genre = "Fantasy")
film4 = Films(title = "Skazani na Shawshank", year = "1994", genre = "Dramat")
film5 = Films(title = "Nietykalni", year = "2011", genre = "Biografdiczny/Dramat/Komedia")
film_list = [film1, film2, film3, film4, film5]


class Series(Films):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        x =10
        y = 6 #żeby Ci działało jeszcze ~~Seba
        #Variables
        self.episode = format(x,'02d')  #zapis w forime dwucyfrowej 01 etc
        self.season = format(y, '02d')
        self.no_plays_series = 0
    def __str__(self):
        return f'{self.title}, S{self.season}E{self.episode}'

series1 = Series(title = "Teoria wielkiego podrywu", year = "2007 - 2019", genre = "Sictom")
series2 = Series(title ="Jak poznałem waszą matkę", year = "2005 - 2014", genre="Sitcom")
series3 = Series(title = "Dr House", year = "2004 - 2012", genre = "Drama")
series4 = Series(title = "Przyjaciele", year = "1994 - 2004", genre = "Sitcom")
series5 = Series(title = "The 100", year = "2014 - " , genre = "Science - Fiction")
series_list = [series1, series2, series3, series4, series5]


class Library(Series): #Klasa dla filmów i seriali
    Library_list = [film_list] + [series_list]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    def get_movies(self):
        by_title = sorted(film_list, key=lambda film: film.title) #sortowanie
        print(by_title)



    def get_series(self):
        by_title = sorted(series_list, key=lambda series: series.title) #sortowanie
        print(by_title)

    def search(self):
        title_search = input("Podaj wyszukiwany tyuł: ")
        if title_search == self.title:
            print(self.title, self.year, self.genre)
        else:
            print("Nie ma takiego tytułu w bibliotece")
            exit()
        

print(film1)
print(film_list[0])
print(series1)
print(series_list[0])
print()
film1.next_play()
film1.current_no_plays
print()
series1.next_play()
series1.current_no_plays
print()

Library.get_movies(list)
print()
Library.get_series(list)
print()
Library.search(film_list)