#!/usr/bin/python3
"""
Module base_model
has class BaseModel that defines all
common atributes/methods for other classes
"""
import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
import uuid
from os import getenv
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"

if getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """
    public instance attributes:
    id, created_at, updated_at
    """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initialization
        id uses uuid.uuid4(). Regenerates a unique id for each BaseModel.
        updated_at -> datetime will be updated everytime an object is changed.
        *args and **kwargs are used as constructors
        """
        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, time)
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """ models.storage.new(self)"""

    def __str__(self):
        """
        Returns string rep of class BaseModel
        Prints: "[<class name>] (<self.id>) <self.__dict__>"
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        Returns the string representation of BaseModel
        calls __str__()
        """
        return (self.__str__())

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        Calls save(self) method of storage
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """
        deletes instance from storage
        """
        models.storage.delete(self)
