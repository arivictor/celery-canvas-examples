from celery import Celery


celery = Celery("worker", broker="sqla+sqlite:///data.db", backend="db+sqlite:///data.db")


@celery.task
def add(item: int, add: int) -> int:
    return item + add


@celery.task
def callback(result):
    return sum(result)