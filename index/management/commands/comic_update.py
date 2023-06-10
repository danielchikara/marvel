from django.core.management.base import BaseCommand
from ...models import *

class Command(BaseCommand):
    help = 'Actualiza la tabla Comic'

    def handle(self, *args, **options):
        # Lógica para actualizar la tabla Comic
        comics = Comic.objects.all()
        for comic in comics:
            # Realiza las operaciones de actualización necesarias en cada instancia de Comic
            comic.save()

        self.stdout.write(self.style.SUCCESS('La tabla Comic ha sido actualizada con éxito.'))