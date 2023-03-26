from books.models import Author, Book
from faker import Faker

faker = Faker("pl_PL")

def generate_authors(n=10):
    for _ in range(n):
        Author.objects.create(
            first_name=faker.first_name(),
            last_name=faker.last_name()
        )


def generate_books(n=100):
    authors = Author.objects.all()
    for _ in range(n):
        author = faker.random.choice(authors)

        Book.objects.create(
            title=faker.text(100),
            description=faker.text(500),
            year=int(faker.year()),
            author=author
        )