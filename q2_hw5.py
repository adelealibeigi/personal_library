"""
    This code is written for HW5 by Adele
"""


class Book:
    def __init__(self, title, author, publish_year, pages, language,
                 price, status=None, progress=0, read_page=0):
        """
        :param title: title of book
        :param author: author of book
        :param publish_year: publish_year of book
        :param pages: total number of pages in the book
        :param language: language of book
        :param price: price of book
        :param status: status of media
        :param progress: Percentage of completion process
        :param read_page: How many pages are read
        """
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.status = status
        self.progress = progress
        self.read_page = read_page

    def read(self, n):
        """
            this function prints the number of pages read and the number of pages remaining
            And set progress for every object
        """
        try:
            assert n + self.read_page <= self.pages
            self.read_page += n
            left_page = self.pages - self.read_page

            self.progress = (self.read_page / self.pages) * 100

        except AssertionError:
            print("You can not read more than book's pages.")

        else:
            if self.read_page == self.pages:
                print("Completed")
            else:
                print(f"You have read {self.read_page} pages from '{self.title}'. \n"
                      f"There are {left_page} left.")

    def get_status(self):
        """
            this function set status for every book
        """
        if self.read_page == 0:
            self.status = 'Unread'
        elif self.read_page < self.pages:
            self.status = 'Reading'
        elif self.read_page == self.pages:
            self.status = 'Finished'

    @staticmethod
    def get_info():
        """
            this function get info from input for every book and initialize it
            media contain info of book
        """
        title, author, publish_year, pages, language, price = \
            input("*Enter* title| author| publish_year| pages| language| price: \n").split('|')
        media = Book(title, author, publish_year, int(pages), language, price)
        return media

    def __str__(self):
        return f'\nTitle : {self.title} \nAuthor(s) : {self.author} \nPublish_year : {self.publish_year}' \
               f'\nPages : {self.pages} \nLanguage : {self.language} \nPrice : {self.price} $'


class Magazine(Book):
    """
        The Magazine's __init__() function overrides the inheritance of the Book's __init__() function.
        and inherit methods
    """
    def __init__(self, title, author, publish_year, pages, language, price, issue):
        """
        :param title: title of magazine
        :param author: author of magazine
        :param publish_year: publish_year of magazine
        :param pages: pages of magazine
        :param language: language of magazine
        :param price: price of magazine
        :param issue: issue of magazine
        """
        super().__init__(title, author, publish_year, pages, language, price)
        self.issue = issue

    @staticmethod
    def get_info():
        """
            this function get info from input for every magazine and initialize it
            media ,contain info of magazine
        """
        title, author, publish_year, pages, language, price, issue = \
            input("*Enter* title| author| publish_year| pages| language| price| issue : \n").split('|')
        media = Magazine(title, author, publish_year, int(pages), language, price, issue)
        return media

    def __str__(self):
        """
            inherit __str__ method from Book class
        """
        return f'{super().__str__()} \nIssue: {self.issue}'


class PodcastEpisode(Book):
    """
        The PodcastEpisode's __init__() function overrides the inheritance of the Book's __init__() function.
        and inherit methods
    """
    def __init__(self, title, speaker, publish_year, time, language, price, listen_time=0):
        """
        :param title: title of podcast
        :param speaker: speaker of podcast
        :param publish_year: publish_year of podcast
        :param time: total time of podcast
        :param language: language of podcast
        :param price: price of podcast
        :param listen_time: How long does it take to listen
        """
        super().__init__(title, 'author', publish_year, 'pages', language, price)
        self.speaker = speaker
        self.time = time
        self.listen_time = listen_time

    def listen(self, n):
        """
            this function prints How long does it take to listen every time, and the time remaining
            set progress for every podcast
        """
        try:
            assert n + self.listen_time <= self.time
            self.listen_time += n
            left_time = self.time - self.listen_time

            self.progress = (self.listen_time/ self.time) * 100

        except AssertionError:
            print("You can not listen more than audio's time.")

        else:
            if self.listen_time == self.time:
                print("Completed")
            else:
                print(f"You have listen {self.listen_time} minute(s) from {self.title}. \n"
                      f"There are {left_time} minute(s) left.")

    def get_status(self):
        """
            this function set status for every podcast
        """
        if self.listen_time == 0:
            self.status = 'ِDid not listen'
        elif self.listen_time < self.time:
            self.status = 'Listening'
        elif self.listen_time == self.time:
            self.status = 'Finished'

    @staticmethod
    def get_info():
        """
            this function get info from input for every magazine and initialize it
            media ,contain info of podcast
        """
        title, speaker, publish_year, time, language, price = \
            input("*Enter* title| speaker| publish_year| time| language| price : \n").split('|')
        media = PodcastEpisode(title, speaker, publish_year, int(time), language, price)
        return media

    def __str__(self):
        return f'\nTitle : {self.title} \nSpeaker : {self.speaker} \nPublish_year : {self.publish_year}' \
               f'\nTime : {self.time} minute(s) \nLanguage : {self.language} \nPrice : {self.price} $'


class Audiobook(PodcastEpisode):
    """
        The Audiobook's __init__() function overrides the inheritance of the PodcastEpisode's __init__() function.
        and inherit methods
    """
    def __init__(self, title, speaker, author, publish_year, pages, time,
                 book_language, audio_language, price):
        """
        :param title: title of audiobook
        :param speaker: speaker of audiobook
        :param author: author of audiobook
        :param publish_year: publish_year of audiobook
        :param pages: total pages of audiobook
        :param time: total time of audiobook
        :param book_language: book_language of audiobook
        :param audio_language: audio_language of audiobook
        :param price: price of audiobook
        """
        super().__init__(title, speaker, publish_year, time, 'language', price)
        self.author = author
        self.pages = pages
        self.book_language = book_language
        self.audio_language = audio_language

    @staticmethod
    def get_info():
        """
            this function get info from input for every ََaudio book and initialize it
            media ,contain info of audio book
        """
        title, speaker, author, publish_year, pages, time, book_language, audio_language, price = \
            input("*Enter* title| speaker|author |publish_year| pages,time| book_language|"
                  "audio_language| price : \n").split('|')
        media = Audiobook(title, speaker, author, publish_year, int(pages), int(time),
            book_language, audio_language, price)
        return media

    def __str__(self):
        return f'\nTitle : {self.title} \nSpeaker : {self.speaker} \nAuthor : {self.author} ' \
               f'\nPublish_year : {self.publish_year} \nPages : {self.pages} ' \
               f'\nTime : {self.time} min(s) \nBook_language : {self.book_language}' \
               f'\nAudio_language = {self.audio_language} \nPrice : {self.price} $'


def get_data():
    """
        this function created to receive its own information after selecting the media type
    """
    check_input = input('Which media type do you want to add? Enter string : ').lower()

    if check_input == 'book':
        media = Book.get_info()
        media.get_status()

    elif check_input == 'magazine':
        media = Magazine.get_info()
        media.get_status()

    elif check_input == 'podcastepisode':
        media = PodcastEpisode.get_info()
        media.get_status()

    elif check_input == 'audiobook':
        media = Audiobook.get_info()
        media.get_status()

    return media


shelf = []


def print_media():
    """
        this function print all media with information ,class name and status from list of shelf
    """
    for i, media in enumerate(shelf):
        print(f'\33[35m{i + 1}) {media.__class__.__name__}\33[0m '
              f'{media} \n\33[34mStatus => {media.status}\33[0m')


def sort_by_progress(shelf_list, progress):
    """
         This function get shelf_list and progress arguments to sort
         and show media base on progress
    """
    media_list = sorted(shelf_list, key=lambda x: x.__getattribute__(progress), reverse=True)

    for media in media_list:
        print(f'\33[35m* {media.__class__.__name__} \33[0m=> {media.title} | '
              f'\33[34m{int(media.progress)}%\33[0m done..')


print('\33[95mWelcome \33[0m \U0001F64B')  # Includes color and emoji
print("\33[35m1- Add a Book/Magazine/PodcastEpisode/AudioBook"
      " \n2- Show my shelf \n3- Add read page or time listen "
      "\n4- Sort my shelf \n* Enter 'Quit' whenever you are done.\33[0m")

checkInput = True
while checkInput:
    """
        this while handles menu and get input till menuInput != 'Quit'
    """
    menuInput = input('\33[105mWhat would you like to do? :\33[0m ')

    if menuInput == "1":
        shelf.append(get_data())

    elif menuInput == '2':
        print(f'\33[35m\U0001F4D5 \U0001F3B6\33[0m')  # emoji
        print_media()

    elif menuInput == '3':
        ithMedia = int(input('Which media do you want to read/listen? Enter number : '))
        num = int(input("How many/long did you read/listen? : "))

        if shelf[ithMedia - 1].__class__.__name__ == 'Book':
            Book.read(shelf[ithMedia - 1], num)
            Book.get_status(shelf[ithMedia - 1])

        elif shelf[ithMedia - 1].__class__.__name__ == 'Magazine':
            Book.read(shelf[ithMedia - 1], num)
            Book.get_status(shelf[ithMedia - 1])

        elif shelf[ithMedia - 1].__class__.__name__ == 'PodcastEpisode':
            Audiobook.listen(shelf[ithMedia - 1], num)
            Audiobook.get_status(shelf[ithMedia - 1])

        elif shelf[ithMedia - 1].__class__.__name__ == 'Audiobook':
            Audiobook.listen(shelf[ithMedia - 1], num)
            Audiobook.get_status(shelf[ithMedia - 1])

    elif menuInput == '4':
        sort_by_progress(shelf, 'progress')

    elif menuInput == 'Quit':
        checkInput = False
        print('\U0001F60E', '\U0001F44B')  # emoji

        
