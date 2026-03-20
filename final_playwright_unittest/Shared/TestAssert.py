class TestAssert:

    def assertFalse(self, expr, msg=None):
        """Check that the expression is false."""
        assert expr == False , msg

    def assertTrue(self, expr, msg=None):
        """Check that the expression is true."""
        assert expr == True, msg


    def assertEqual(self, first, second, msg=None):
        """Fail if the two objects are unequal as determined by the '=='
           operator.
        """
        assert first == second, msg

    def assertNotEqual(self, first, second, msg=None):
        """Fail if the two objects are equal as determined by the '!='
           operator.
        """
        assert first != second, msg


    def assertIn(self, member, container, msg=None):
        """Just like self.assertTrue(a in b), but with a nicer default message."""
        assert member in container, msg

    def assertNotIn(self, member, container, msg=None):
        """Just like self.assertTrue(a not in b), but with a nicer default message."""
        assert not member in container, msg

    def assertIs(self, expr1, expr2, msg=None):
        """Just like self.assertTrue(a is b), but with a nicer default message."""
        assert expr1 is expr2, msg

    def assertIsNot(self, expr1, expr2, msg=None):
        """Just like self.assertTrue(a is not b), but with a nicer default message."""
        assert expr1 is not expr2, msg

    def assertLess(self, a, b, msg=None):
        """Just like self.assertTrue(a < b), but with a nicer default message."""
        assert a < b, msg

    def assertLessEqual(self, a, b, msg=None):
        """Just like self.assertTrue(a <= b), but with a nicer default message."""
        assert a <= b, msg

    def assertGreater(self, a, b, msg=None):
        """Just like self.assertTrue(a > b), but with a nicer default message."""
        assert a > b, msg 

    def assertGreaterEqual(self, a, b, msg=None):
        """Just like self.assertTrue(a >= b), but with a nicer default message."""
        assert a >= msg

    def assertIsNone(self, obj, msg=None):
        """Same as self.assertTrue(obj is None), with a nicer default message."""
        assert obj == None, msg

    def assertIsNotNone(self, obj, msg=None):
        """Included for symmetry with assertIsNone."""
        assert obj != None, msg


    def assertIsInstance(self, obj, cls, msg=None):
        """Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message."""
        assert isinstance(obj, cls), msg

    def assertNotIsInstance(self, obj, cls, msg=None):
        """Included for symmetry with assertIsInstance."""
        assert isinstance(obj,cls),msg

