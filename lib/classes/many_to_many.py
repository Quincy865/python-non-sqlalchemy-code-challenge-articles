class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string with 5-50 characters.")
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)

    @classmethod
    def all(cls):
        return cls.all_articles


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 0:
            raise ValueError("Name must be a non-empty string.")
        self.__name = name 

    @property
    def name(self):
        return self.__name

    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({magazine.category for magazine in self.magazines()})


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string with 2-16 characters.")
        if not isinstance(category, str) or len(category) <= 0:
            raise ValueError("Category must be a non-empty string.")
        self.name = name
        self.category = category
        Magazine._all_magazines.append(self)

    @classmethod
    def all(cls):
        return cls._all_magazines

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        from collections import Counter
        if not self.articles():
            return None
        author_count = Counter(article.author for article in self.articles())
        return [author for author, count in author_count.items() if count > 2]
