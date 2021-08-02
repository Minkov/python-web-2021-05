from datetime import time

from celery import shared_task


@shared_task
def check_celery():
    print('Celery works!')
    print(f'{time()}: Tasks')
