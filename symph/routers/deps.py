from typing import Generator

from ..database import session


# this dep will be overriden at startup
def get_celery_app():
    return None


def get_db() -> Generator:
    local_session = session()
    try:
        yield local_session
    finally:
        local_session.close()
