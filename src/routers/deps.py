from celery import Celery

from src.services.inspector import Inspector

celery_app = Celery(broker="pyamqp://127.0.0.1:5672")


async def get_inspector() -> Inspector:
    return Inspector(celery_app=celery_app)
