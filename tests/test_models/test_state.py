import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for State class"""

    @classmethod
    def setUpClass(cls):
        """Set up class-wide test environment"""
        cls.storage = FileStorage()
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        """Tear down class-wide test environment"""
        cls.storage.save()

    def test_state_exists(self):
        """Test if a State object exists in storage"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        key = "State.{}".format(state.id)
        self.assertIn(key, self.storage.all())

    @unittest.skipIf(True, "Skipping MySQL test")
    def test_state_exists_mysql(self):
        """Test if a State object exists in MySQL storage"""
        from models.engine.db_storage import DBStorage

        HBNB_MYSQL_USER = "hbnb_test"
        HBNB_MYSQL_PWD = "hbnb_test_pwd"
        HBNB_MYSQL_HOST = "localhost"
        HBNB_MYSQL_DB = "hbnb_test_db"

        storage = DBStorage()
        storage.reload()

        state = State(name="California")
        storage.new(state)
        storage.save()

        key = "State.{}".format(state.id)
        self.assertIn(key, storage.all())

if __name__ == "__main__":
    unittest.main()
