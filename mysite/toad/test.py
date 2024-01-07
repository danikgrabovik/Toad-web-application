import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Toad


class ToadModelTests(TestCase):
    def test_toad(self):
        toad = Toad()
        self.assertIs(toad.last_feed > timezone.now(), False)
        print(toad.level_progress)
        self.assertIs(toad.level_progress == 0, True)
        self.assertIs(toad.health == 5, True)
        self.assertIs(toad.money == 0, True)
        self.assertIs(toad.curr_level == 1, True)

    def test_functions(self):
        toad = Toad()
        self.assertIs(toad.get_curr_level == 1, True)
        self.assertIs(toad.get_level_progress == 0, True)

    def test_feed(self):
        toad = Toad()
        time=toad.last_feed
        toad.feed()
        self.assertIs(toad.last_feed > time, True)
        self.assertIs(toad.money == 50, True)
        self.assertIs(toad.get_level_progress == 1, True )

    # def test_check_work(self):
    #     toad = Toad()
    #     self.assertIs(toad.check_work(), False)
    
    



# Create your tests here.
