from celery import Celery
from typing import Optional


class Inspector:
    def __init__(self, celery_app: Celery):
        self.celery_app: Celery = celery_app

    def inspect(self, method: str, worker_name: Optional[str]):
        inspect = self.celery_app.control.inspect(destination=worker_name)
        getattr(inspect, method)()
