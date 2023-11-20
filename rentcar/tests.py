from django.test import TestCase

# Create your tests here.
class RentCarTestCase(TestCase):
    def setUp(self):
        from django_seed import Seed

        seeder = Seed.seeder()

        from rentcar.models import Tourist, Brand
        seeder.add_entity(Tourist, 5)
        seeder.add_entity(Brand, 10)

        inserted_pks = seeder.execute()
