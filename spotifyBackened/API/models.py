from django.db import models

# generate random string 
def generate_unique_room():
    import random
    import string
    while True:
        unique_room= "".join(random.choices(string.ascii_uppercase,k=6))
        if Room.objects.filter(room_code=unique_room):
            continue
        else:
            break
    return unique_room

        


# Create your models here.
class Room(models.Model):
    room_code=models.CharField(max_length=10,default=None, unique=True)
    host_name=models.CharField(max_length=20,unique=True)
    guest_can_stop= models.BooleanField(default=False)
    votes_to_change=models.IntegerField(default=1)
    created_on=models.DateTimeField(auto_now_add=True)

