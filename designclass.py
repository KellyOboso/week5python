class Book:
    def __init__(self, title, author, year_published):
        # Encapsulated attributes with underscore
        self._title = title
        self._author = author
        self._year_published = year_published

    def get_summary(self):
        return f"\"{self._title}\" by {self._author}, published in {self._year_published}."

    def read(self):
        return f"You start reading \"{self._title}\"."

    # Getter methods to access encapsulated attributes
    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_year(self):
        return self._year_published


class EBook(Book):
    def __init__(self, title, author, year_published, file_size_mb):
        super().__init__(title, author, year_published)
        self._file_size_mb = file_size_mb  # MB

    def read(self):
        return f"You open the e-book \"{self._title}\" on your device. File size: {self._file_size_mb}MB."

    def get_file_size(self):
        return self._file_size_mb


class AudioBook(Book):
    def __init__(self, title, author, year_published, duration_min):
        super().__init__(title, author, year_published)
        self._duration_min = duration_min  # minutes

    def read(self):
        return f"You listen to the audiobook \"{self._title}\". Duration: {self._duration_min} minutes."

    def get_duration(self):
        return self._duration_min


if __name__ == "__main__":
    # Create instances of each class
    physical_book = Book("1984", "George Orwell", 1949)
    ebook = EBook("Digital Fortress", "Dan Brown", 1998, 2.5)
    audiobook = AudioBook("Becoming", "Michelle Obama", 2018, 1140)

    # Demonstrate polymorphism: call read method on each
    books = [physical_book, ebook, audiobook]

    for book in books:
        print(book.get_summary())
        print(book.read())
        print()

