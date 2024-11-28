"""
데이터베이스가 실행되기를 기다리는 명령어
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        pass