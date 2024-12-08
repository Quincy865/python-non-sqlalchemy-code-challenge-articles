class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string with 5-50 characters.")
        
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title  

    @classmethod
    def all(cls):
        return cls.all_articles

    @classmethod
    def articles_by_author(cls, author):
        return [article for article in cls.all_articles if article.author == author]

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name 

    @property
    def name(self):
        return self._name 


    def articles(self):
        return [article for article in Article.all() if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()})  

    def published_titles(self):
        return [article.title for article in self.articles()] 

class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string with 2-16 characters.")
        if not isinstance(category, str) or len(category) <= 0:
            raise ValueError("Category must be a non-empty string.")
        
        self._name = name  
        self._category = category  
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string with 2-16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) <= 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    @classmethod
    def all(cls):
        return cls._all_magazines

    def articles(self):
        return [article for article in Article.all() if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()]  

    def contributing_authors(self):
        from collections import Counter
        author_count = Counter(article.author for article in self.articles())
        return [author for author, count in author_count.items() if count > 2]  

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None 

        magazine_article_counts = {magazine: len(magazine.articles()) for magazine in cls._all_magazines}
        top_magazine = max(magazine_article_counts, key=magazine_article_counts.get, default=None)
        return top_magazine


