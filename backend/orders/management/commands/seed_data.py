import os
from django.core.management.base import BaseCommand
from orders.models import Client, Order
import faker
import random

fake = faker.Faker('ru_RU')


class Command(BaseCommand):
    help = 'Заполнить базу тестовыми клиентами и заказами'

    def handle(self, *args, **kwargs):
        Client.objects.all().delete()
        Order.objects.all().delete()

        clients = []
        for _ in range(50):
            client = Client.objects.create(
                name=fake.name(),
                number=fake.phone_number()
            )
            clients.append(client)

        for _ in range(100):
            Order.objects.create(
                manager=random.choice(clients),
                location=fake.city(),
                caption=fake.address(),
                status=random.randint(1, 3)
            )

        self.stdout.write(self.style.SUCCESS('✅ База данных успешно заполнена.'))
