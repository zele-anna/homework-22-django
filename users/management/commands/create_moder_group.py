from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    def handle(self, *args, **options):
        moderators_group = Group.objects.create(name='Moderators')
        unpublish_permission = Permission.objects.get(codename='can_unpublish_product')
        delete_permission = Permission.objects.get(codename='delete_product')
        moderators_group.permissions.add(unpublish_permission, delete_permission)
