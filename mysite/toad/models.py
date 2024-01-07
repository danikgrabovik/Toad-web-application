from django.db import models
from work.models import Work
from product.models import Product
import datetime
from django.utils import timezone
import json


class Toad(models.Model):
    name = models.CharField(max_length=20)
    #curr_work = models.ForeignKey(Work, on_delete=models.SET_NULL, null=True)
    money = models.IntegerField(default=0)
    curr_level = models.IntegerField(default=1)
    level_progress = models.IntegerField(default=0)
    health = models.IntegerField(default=5)
    backpack = models.CharField(max_length=100)
    last_feed = models.DateTimeField(default=timezone.now())



    def __str__(self):
        return self.name

    @property
    def get_curr_level(self):
        if self.curr_level:
            return self.curr_level
        return 0

    @property
    def get_level_progress(self):
        if self.level_progress:
            return self.level_progress
        return 0

    def increase_level_progress(self, score):
        if score + self.get_level_progress > 3 * (self.get_curr_level + 1):
            self.level_progress = self.get_curr_level * 3 - self.get_level_progress
            self.curr_level = self.get_curr_level + 1
        else:
            self.level_progress = self.level_progress + score

    def go_to_work(self,id_):
        if self.check_work():
            return False
        else:
            work_ = Work.objects.get(id=id_)
            b= WorkToad(work=work_, toad=self, start_time=datetime.datetime.now())
            b.save()
            return True

    def check_work(self):
        if WorkToad.objects.get(toad = self):
            return True
        else:
            return False

    def peek_toad_from_work(self):
        if self.check_work():
            curr_work = WorkToad.objects.get(toad=self)
            if datetime.datetime.now() > curr_work.start_time + datetime.timedelta(hours=2):
                self.money += curr_work.work.reward_money
                self.increase_level_progress(curr_work.work.reward_score)
                return True
            else:
                return False

    def get_info(self):
        info_dict = {
            "name": self.name,
            "money": self.money,
            "current level": self.curr_level,
            "level progress": self.level_progress,
            "health": self.health
        }
        return json.dumps(info_dict)

    def get_items(self):
        backpack = list()
        q1 = Backpacks.objects.filter(owner=self)
        for item in q1:
            backpack.append(item.type_of_product)
        return json.dumps(backpack)

    def buy_item(self,name_of_product):
        a = Product.objects.get(type_of_product=name_of_product)
        if a:
            if self.money > a.cost:
                self.money -= a.cost
                b = Backpacks(owner=self, product=a)
                b.save()
                return True
            else:
                return False
        else:
            return False

    def feed(self):
#        if datetime.datetime.now() > datetime.datetime.fromtimestamp(self.last_feed) + datetime.timedelta(hours=6):
            self.last_feed = timezone.now()
            self.money += 50
            self.increase_level_progress(1)

    def check_requests(self):
        #print("IM IN MODEL")
        a = Requests.objects.filter(request_to=self,accepted = False,ignore = False)
        print(a)
        return a

    def accept_request(self,t):
        f = Friends(friend1=self, friend2=t)
        f.save()
        a = Requests.objects.get(request_from = t , request_to = self)
        a.accepted = True
        a.save()
        return True

    def send_request(self,t):
        f = Requests(request_to = t, request_from = self, accepted = False, ignore = False)
        f.save()
        return True

    def ignore_request(self,t):
        f = Requests.objects.get(request_from = t, request_to = self)
        f.ignore = True
        f.save()
        return True

    def get_ignored(self):
        f = Requests.objects.get(request_to = self, ignore = True)
        return f

    def unignore_request(self,t):
        f = Requests.objects.get(request_from = t, request_to = self, ignore = True)
        f.ignore = False
        f.save()
        return True

    def go_to_arena(self):
        a = Arena_request(toad = self)
        return True



class WorkToad(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='work_of_toad')
    toad = models.ForeignKey(Toad, on_delete=models.CASCADE, related_name='toad_at_work')
    start_time = models.TimeField()

class Friends(models.Model):
    friend1 = models.ForeignKey(Toad, on_delete=models.CASCADE, related_name='first_friend')
    friend2 = models.ForeignKey(Toad, on_delete=models.CASCADE, related_name='second_friend')


class Requests(models.Model):
    request_from = models.ForeignKey(Toad, on_delete=models.CASCADE, related_name='request_from')
    request_to = models.ForeignKey(Toad, on_delete=models.CASCADE, related_name='request_to')
    accepted = models.BooleanField()
    ignore = models.BooleanField()


class Backpacks(models.Model):
    owner = models.ForeignKey(Toad, on_delete=models.CASCADE, related_name='toad_with_backpack')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_in_backpack')

class Arena_request(models.Model):
    from_toad = models.ForeignKey(Toad, on_delete=models.CASCADE, related_name='toad_send_request')


# Create your models here.
