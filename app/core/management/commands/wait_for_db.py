"""
Django command to wait for the database to be available.
"""
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
# from django.db


class Command(BaseCommand):
    """Django command to wait for database."""

    def check(self, databases=['default']):
        """check if databases is ready."""
        pass

    def handle(self, *args, **options):
        """Wait for database to be available."""
        self.stdout.write("Watching for database...")
        db_ready = False
        while db_ready is False:
            try:
                self.check(databases=['default'])
                db_ready = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database is ready."))
