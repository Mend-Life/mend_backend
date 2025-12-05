from django.db import models
import random
import string

# Create your models here.

def generate_random_name():
    """Generate a random name like 'User_ABC123' for users who don't provide a name"""
    adjectives = ['Happy', 'Peaceful', 'Hopeful', 'Calm', 'Joyful', 'Bright', 'Warm', 'Kind']
    random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"{random.choice(adjectives)}_{random_suffix}"

class User(models.Model):
  # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  email = models.EmailField(unique=True, blank=True)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  # Name is optional - will auto-generate random name if not provided
  name = models.CharField(max_length=255, blank=True, null=True)
  age = models.IntegerField(null=True, blank=True)
  gender = models.CharField(max_length=255, blank=True, null=True)
  location = models.CharField(max_length=255, blank=True, null=True)
  # interests = models.CharField(max_length=255)
  # profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
  # bio = models.TextField(null=True, blank=True)
  # is_active = models.BooleanField(default=True)
  # is_verified = models.BooleanField(default=False)
  # is_premium = models.BooleanField(default=False)
  # is_admin = models.BooleanField(default=False)
  # is_staff = models.BooleanField(default=False)

  def save(self, *args, **kwargs):
    # Auto-generate random name if not provided
    if not self.name:
      self.name = generate_random_name()
    super().save(*args, **kwargs)

  def __str__(self):
    email_display = self.email if self.email else "No Email"
    return f"{email_display} - {self.name}"