from posts.models import Post
from django.contrib.auth import get_user_model
from faker import Faker


User = get_user_model()
faker = Faker("pl_PL")


def create_posts(n=100):

    user = User.objects.first()

    for i in range(n):
        Post.objects.create(
            author=user,
            title=faker.text(100),
            content=faker.text(500)
        )
    print("Done")