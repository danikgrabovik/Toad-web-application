from django.db import models
from toad.models import Toad,Arena_request

class Arena(models.Model):
    lower_bound = models.IntegerField()
    upper_bound = models.IntegerField()
    reward_level = models.IntegerField()
    reward_money = models.IntegerField()
    rang = models.IntegerField()

    def create_queue(self):
        list = Arena_request.objects.filter(from_toad.curr_level > self.lower_bound, from_toad.curr_level < self.upper_bound)
        for i in range(len(list)//2):
            a = Queue(arena_id = self, toad1 = list[i*2], toad2 = list[i*2+1])
            a.save()
        list[:len(list)-len(list)%2].delete()
        return True

    def clean_queue(self):
        a = Queue.objects.get(arena_id = self)
        a.delete()
        return True

    def fight(self, t1, t2):
        return t1

    def all_fights(self):
        a = Queue.objects.get(arena_id = self)
        winners = list()
        for item in a:
           b = self.fight(item.toad1,item.toad2)
           winners.append(b)
        for item in winners:
            item.increase_level_progress(self.reward_level)
            item.money += self.reward_money
            item.save()
        return winners


class Queue(models.Model):
    arena_id = models.ForeignKey(Arena, on_delete=models.CASCADE, related_name='battle_arena')
    toad1 = models.ForeignKey(Toad, on_delete=models.CASCADE, related_name='first_battle_toad')
    toad2 = models.ForeignKey(Toad, on_delete=models.CASCADE, related_name='second_battle_toad')



