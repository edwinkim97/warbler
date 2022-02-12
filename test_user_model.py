"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase

from models import db, User, Message, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler_test"

# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)
    
    # PLAN FOR ALL TESTS ####################    
    # USER MODEL TESTS!!!! #
    # def test_repr(self):
    #    """Tests dunder repr for USER model"""

    # Using u (newly created used), Then, test with 
    # assertEqual(repr(testUser), "<User #{test.id}: {test.username}, {test.email}>") 
    
    
    # def test_is_following(self):
    # DOCSTRINGS
    # Happy Case:
    # Create user, second user, third user and create cases where user is following second user
    # We can make user follow anotehr user by instatiatining Follows table
    # follow = Follows(u1.id, u2.id) 
    # Sad Case:
    # follow = Follows(u1.id, u2.id)
    # AssertIn u3 u1.followers
    
    # User signup, with test user, and then test with AssertIsInstance of USER class
    # Negative class would test that the signup method returns a None, check with
    # AssertIsInstance(returned_None, None)
    
    # For authentication, in happy case return user, check with AssertIsInstance
    # for sad case, AssertEqual(returned_from_authenticate_method, False)
    # checking for both invalid username and invalid password in 2 diff test cases
    
    # END OF USER MODEL TESTS #
    
    # TESTS FOR MESSAGE MODEL TESTS #####
    
    # Test to see instance of Message is actually an instance with
    # AssertIsInstance (instance_of_Message, Message)
    # Test with user_id not in Users.query.all() 
    # Test with message that is over 140 characters in length
    
    # END OF MESSAGE MODEL TESTS ####
    
    # ROUTE TESTS FOR USER VIEW FUNCTION ###
    
    # 