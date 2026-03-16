from django.core.management.base import BaseCommand
from greetings.models import Greeting

class Command(BaseCommand):
    help = 'Seed the database with placeholder greetings for extracted surnames'

    def handle(self, *args, **options):
        surnames = [
            '_Белякова', '_Кутепова', '_Старцева', '_Загороднева', '_Бурлакова',
            '_Аношкина', '_Федулинская', '_Бигулова', '_Юрова', '_Коркина'
        ]
        
        for sid in surnames:
            name = sid.replace('_', '')
            Greeting.objects.get_or_create(
                surname_id=sid,
                defaults={
                    'first_name': name,
                    'message': f'Дорогая {name}! Поздравляю тебя с 8 Марта! Пусть этот день будет полон радости и улыбок.'
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded greetings'))
