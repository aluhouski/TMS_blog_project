from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.auth.models import User
from blog_app.models import Post, Comment



class Command(BaseCommand):
    help = 'Seeds the database with fake Posts and Comments'

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        seeder.add_entity(User, 3, {})

        seeder.add_entity(Post, 5, {
            'title':    lambda x: seeder.faker.sentence(nb_words=5),
            'content':  lambda x: seeder.faker.paragraph(nb_sentences=4),
            'author':   lambda x: User.objects.order_by('?').first(),
        })

        seeder.add_entity(Comment, 11, {
            'content':  lambda x: seeder.faker.paragraph(nb_sentences=3),
            'author':   lambda x: User.objects.order_by('?').first(),
            'post':     lambda x: Post.objects.order_by('?').first(),
        })

        inserted_pks = seeder.execute()

        self.stdout.write(self.style.SUCCESS('Seeded data successfully!'))