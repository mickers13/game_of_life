from unittest import TestCase
from Simulator import *


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)



    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)

    def test_rule_under_population(self):
        """
        Test for checking if the next generation after the initial state has the desired result for the following rule:

        - Elke levende cel met minder dan twee levende buren gaat dood (ook wel onderpopulatie of exposure genaamd);

        """
        #Test case: niet gegoeg buren gaat dood door under populatie.
        world = World(10)
        self.sim.set_world(world)
        world.width, world.height = 10, 12
        world = World(world.width, world.height)
        #middle in the given set world.
        x, y = 5, 6
        #Create one living cell, should die.
        world.set(x, y)
        self.sim.update()
        self.assertEqual(world.get(x, y),0)

    def test_rule_over_population(self):
        """
        Test for checking if the next generation after the initial state has the desired result for the following rule:
        - Elke levende cel met meer dan drie levende buren gaat dood (ook wel overpopulatie of overcrowding genaamd);
        - Elke cel met twee of drie levende buren overleeft, onveranderd naar de volgende generatie (survival);
        - Elke dode cel met precies drie levende buren komt tot leven (ook wel geboorte of birth genaamd).
        """
        world = World(10)
        self.sim.set_world(world)
        world.width, world.height = 10, 12
        world = World(world.width, world.height)
        # middle in the given set world.
        x, y = 5, 6
        # Create living cells in a half + patern. Middle should survive.
        world.set(x, y)  # thisone should die.
        world.set(x - 1, y)
        world.set(x + 1, y)
        world.set(x, y - 1)
        world.set(x, y + 1)
        self.sim.update()
        self.assertEqual(world.get(x, y), 0)

    def test_rule_survival(self):
        """
        Test for checking if the next generation after the initial state has the desired result for the following rule:

        - Elke cel met twee of drie levende buren overleeft, onveranderd naar de volgende generatie (survival);

        Test should be basic green, but if code is wrong should be red.
        """
        # Test case: Levende cel gaat dood door overpopulatie.
        world = World(10)
        self.sim.set_world(world)
        world.width, world.height = 10, 12
        world = World(world.width, world.height)
        # middle in the given set world.
        x, y = 5, 6
        # Create living cells in a half + patern. Middle should survive.
        world.set(x, y)  # thisone should die.
        world.set(x - 1, y)
        world.set(x + 1, y)
        world.set(x, y - 1)
        self.sim.update()
        self.assertNotEqual(world.get(x, y), 0)

    def test_rule_birth(self):
        """
        Test for checking if the next generation after the initial state has the desired result for the following rule:

        - Elke dode cel met precies drie levende buren komt tot leven (ook wel geboorte of birth genaamd).
        """
        # Test case: Levende cel gaat dood door overpopulatie.
        world = World(10)
        self.sim.set_world(world)
        world.width, world.height = 10, 12
        world = World(world.width, world.height)
        # middle in the given set world.
        x, y = 5, 6
        # Create living cells in a half + patern. Middle should survive.
        world.set(x, y,0)  # thisone should come to life.
        world.set(x - 1, y)
        world.set(x + 1, y)
        world.set(x, y - 1)
        self.sim.update()
        self.assertEqual(world.get(x, y), 1)