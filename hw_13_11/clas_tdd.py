import datetime

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return (nums)

class Book:

    items = []

    def __init__(self, title, published, author):
        self.title = title
        self.published = published
        self.author = author
        Book.items.append(self)

    def __str__(self):
        return f'{self.author}\'s {self.title}'

    # def __repr__(self):
    #     return f'{self.author}\'s {self.title}'
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))

    @staticmethod
    def find_by_title(other_title):
        empty_list = []
        for book in Book.items:
            if book.title.lower() == other_title.lower():
                empty_list.append(book)
        return empty_list

    @staticmethod
    def find_by_author(other_author):
        empty_list = []
        for book in Book.items:
            if other_author in book.author.split(' '):
                empty_list.append(book)
        return empty_list

    @staticmethod
    def published_after(year):
        empty_list = []
        for book in Book.items:
            if book.published.year >= year:
                empty_list.append(book)
        return empty_list

class Movie:

    items = []

    def __init__(self, name, release_day, directed_by, book: Book):
        self.name = name
        self.release_day = release_day
        self.directed_by = directed_by
        self.based_on = book
        Movie.items.append(self)

    def __eq__(self, other):
        return self.release_day.year == other.release_day.year

    def __lt__(self, other):
        return self.release_day.year < other.release_day.year

    def __gt__(self, other):
        return self.release_day.year > other.release_day.year

    @classmethod
    def sort_items(cls):
        sorted_movie = bubble_sort(cls.items)
        return sorted_movie

    @staticmethod
    def for_book(temp_book):
        empty_list = []
        for movie in Movie.items:
            if temp_book in movie.based_on.title:
                empty_list.append(movie.based_on)
        return empty_list

    @property
    def recommendations(self):
        empty_list = []
        for movie in Movie.items:
            if self.based_on.title == movie.based_on.title:
                if movie != self:
                    empty_list.append(movie)
        return empty_list

