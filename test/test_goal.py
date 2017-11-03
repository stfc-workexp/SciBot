"""This file contains the TestGoal class."""
import unittest
import pygame

from src.Goal import Goal
from src.Point import Point


class TestGoal(unittest.TestCase):
    """This test class unit tests the Goal class."""

    @classmethod
    def test_init(cls):
        """Test the init method of the Goal class."""
        _unused_goal = Goal(None, Point(0, 0), 0)

    @classmethod
    def test_display(cls):
        """
        Test the display method of a Goal.

        All this really does is make sure the method executes correctly.
        If the method call errors, the test will fail.
        """
        # Create a test sprite
        sprite = pygame.image.load('img/Default/goal1.jpg')

        # Create two test goals, one with a sprite and one without
        goal_with_sprite = Goal(sprite, Point(1, 1), 150)
        goal_without_sprite = Goal(None, Point(1, 1), 150)

        # Create a test screen to dsiplay things on
        test_screen = pygame.display.set_mode((1500, 1500))

        # Attempt to display the goal with a sprite
        goal_with_sprite.display(test_screen)

        # Attempt to display the goal without a sprite
        goal_without_sprite.display(test_screen)

    def test_is_equal_to(self):
        """Test the is_equal_to_method."""
        # Create a test sprite
        goal_sprite = pygame.image.load('img/Default/goal1.jpg')

        goal = Goal(goal_sprite, Point(1, 1), 150)
        # Create a Goal equal to goal
        goal_copy = Goal(goal_sprite, Point(1, 1), 150)
        # Create a Goal in a different logical place
        goal_diff_logical_position = Goal(goal_sprite, Point(2, 2), 150)
        # Create a Goal that is met
        met_goal = Goal(goal_sprite, Point(1, 1), 150)
        met_goal.has_been_met = True
        # Create a Goal with a different sprite
        obstacle_sprite = pygame.image.load('img/Default/obstacle1.jpg')
        goal_diff_sprite = Goal(obstacle_sprite, Point(1, 1), 150)

        # Check that equal goals are infact eqaul
        self.assertTrue(goal.is_equal_to(goal_copy))
        # Check that a goal in a different logical place is not equal
        self.assertFalse(goal.is_equal_to(goal_diff_logical_position))
        # Check an unmet Goal is not equal to a met Goal
        self.assertFalse(goal.is_equal_to(met_goal))
        # Check Goals with different sprites are not equal
        self.assertFalse(goal.is_equal_to(goal_diff_sprite))


if __name__ == '__main__':
    unittest.main()
