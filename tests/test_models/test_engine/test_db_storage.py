#!/usr/bin/python3
""" This test is for the database storage class"""

import unittests
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
import models
from models import storage
import pep8
import MySQLdb


class TestDBStorage(unittests.TestCase):
    """ Tests for class attributes and methods
        Attributes:
                   __engine
                   __session

        Methods:
                all
                new
                save
                delete
                reload
    """

    # Read: https://www.programcreek.com/python/example/57796/unittest.skipIf

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "This test is only for database storage.")
    def setUp(self):
        """Set up for the tests by connecting to database and making it query
        ready"""
        if getenv(HBNB_TYPE_STORAGE) == "db":
            # host, user, pwd, database
            self.my_db = MySQLdb.connect(getenv("HBNB_MYSQL_HOST"),
                                         getenv("HBNB_MYSQL_USER"),
                                         getenv("HBNB_MYSQL_PWD"),
                                         getenv("HBNB_MYSQL_DB"))

            self.cursor = self.my_db.cursor()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "This test only applies to database storage")
    def tearDown(self):
        """ Closing session after test"""
        if getenv(HBNB_TYPE_STORAGE) == "db":
            self.my_db.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "This test only applies to database storage")
    def test_DBStorage_attributes(self):
        """Tests for class attributes"""

        self.assertTrue(hasattr(DBStorage, '__engine'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__session'))
        self.assertTrue(hasattr(DBStorage, 'all'))
        self.assertTrue(hasattr(DBStorage, 'new'))
        self.assertTrue(hasattr(DBStorage, 'save'))
        self.assertTrue(hasattr(DBStorage, 'delete'))
        self.assertTrue(hasattr(DBStorage, 'reload'))
