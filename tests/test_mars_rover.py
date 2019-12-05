import unittest

from marsrover.mars_rover import MarsRover


class TestMarsRover(unittest.TestCase):
    def test_should_return_init_place_given_command_is_empty(self):
        mars_rover = MarsRover()
        status = mars_rover.run()
        self.assertEqual(status, '0 0 E')

    def test_should_return_x_plus_1_given_given_command_is_M_and_facing_is_E(self):
        mars_rover = MarsRover()
        status = mars_rover.run('M')
        self.assertEqual(status, '1 0 E')

    def test_should_return_x_minus_1_given_given_command_is_M_and_facing_is_W(self):
        mars_rover = MarsRover('0 0 W')
        status = mars_rover.run('M')
        self.assertEqual(status, '-1 0 W')

    def test_should_return_y_plus_1_given_given_command_is_M_and_facing_is_N(self):
        mars_rover = MarsRover('0 0 N')
        status = mars_rover.run('M')
        self.assertEqual(status, '0 1 N')
