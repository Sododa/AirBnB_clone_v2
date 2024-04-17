def test_name_attribute(self):
    """
    Test the 'name' attribute of the State instance
    """
    # Create a State instance
    new_state = State(name="California")
    
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        # For non-DB storage, 'name' should be of type str
        self.assertIsInstance(new_state.name, str)
        self.assertEqual(new_state.name, "California")  # Additional assertion
    else:
        # For DB storage, 'name' should initially be None
        self.assertIsNone(new_state.name)

def test_save_method(self):
    """
    Test the 'save' method of the State instance
    """
    # Create a State instance
    new_state = State(name="New York")
    
    # Save the State instance and check if 'updated_at' changes
    initial_updated_at = new_state.updated_at
    new_state.save()
    self.assertNotEqual(new_state.updated_at, initial_updated_at)
