from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from .models import Profile

# Use the `@receiver` decorator to connect the function to the post_save signal
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Check if a new User instance is being created
    if created:
        # Get or create the 'user' group
        user_group, _ = Group.objects.get_or_create(name='user')
        # Add the user to the 'user' group
        instance.groups.add(user_group)
        # Create a new Profile instance associated with the newly created User instance
        Profile.objects.create(
            user=instance,
            name=instance.username,  # Set the profile's name as the user's username
        )
