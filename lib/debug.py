#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) Let's debug :vibing_potato:")

    author1 = Author("Jane Doe")
    author2 = Author("John Smith")

    magazine1 = Magazine("Tech World", "Technology")
    magazine2 = Magazine("Health Matters", "Health")

    article1 = Article(author1, magazine1, "Future of AI")
    article2 = Article(author1, magazine2, "Wellness in 2024")
    article3 = Article(author2, magazine1, "Innovations in Robotics")
    article4 = Article(author2, magazine1, "AI in Everyday Life")
    article5 = Article(author2, magazine1, "Machine Learning Basics")

    print(f"Author 1's Articles: {author1.articles()}")
    print(f"Author 1's Magazines: {author1.magazines()}")
    print(f"Author 1's Topic Areas: {author1.topic_areas()}")

    print(f"Magazine 1's Articles: {magazine1.articles()}")
    print(f"Magazine 1's Contributors: {magazine1.contributors()}")
    print(f"Magazine 1's Article Titles: {magazine1.article_titles()}")
    print(f"Magazine 1's Contributing Authors: {magazine1.contributing_authors()}")

    new_article = author1.add_article(magazine1, "The Future of Quantum Computing")
    print(f"New Article Added: {new_article.title}")
    print(f"Magazine 1's Articles After Addition: {magazine1.articles()}")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
