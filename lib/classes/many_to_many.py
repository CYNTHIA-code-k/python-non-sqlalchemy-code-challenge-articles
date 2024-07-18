class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # This setter does nothing, effectively making the name immutable
        pass

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))
class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        # Silently ignore invalid assignments

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        # Silently ignore invalid assignments

    # ... (rest of the methods remain the same)
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
    
    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        contributing = [author for author, count in author_counts.items() if count > 2]
        return contributing if contributing else None

    @classmethod
    def top_publisher(cls):
        if not cls.all or not any(magazine._articles for magazine in cls.all):
            return None
        return max(cls.all, key=lambda mag: len(mag._articles))


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = title
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # This setter does nothing, effectively making the title immutable
        pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author class")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class")
        self._magazine = value