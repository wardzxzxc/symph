# adapted from @tiangolo full-stack-fastapi-postgresql example
from typing import Generic, List, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import orm

from symph.models import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def create(self, s: orm.Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_data)
        s.add(db_obj)
        s.commit()
        s.refresh(db_obj)
        return db_obj

    def create_multi(
        self, s: orm.Session, *, list_objs: List[CreateSchemaType]
    ) -> None:
        list_db_objs = [self.model(**jsonable_encoder(obj_in)) for obj_in in list_objs]
        s.bulk_save_objects(list_db_objs)
        s.commit()
