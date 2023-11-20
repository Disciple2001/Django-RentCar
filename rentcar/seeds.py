from django_seed import Seed

from rentcar.models import Tourist, Brand

seeder = Seed.seeder()


def executeSeeds():
    seeder.add_entity(Tourist, 1000)
    seeder.add_entity(Brand, 10)

    seeder.execute()


execute = executeSeeds