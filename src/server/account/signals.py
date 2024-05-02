from django.db.models.signals import pre_delete
from django.dispatch import receiver

from account.models import User


@receiver(pre_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    instance.delete()
    print("User Deleted")