import unittest

from marsrover.mars_rover import MarsRover


class TestMarsRover(unittest.TestCase):
    def test_should_return_init_place_given_command_is_empty(self):
        mars_rover = MarsRover()
        status = mars_rover.run()
        self.assertEqual(status, '0 0 E')
