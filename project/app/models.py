from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import CASCADE, DO_NOTHING
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    isTeacher = models.BooleanField(null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profiles_pics')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


class ClassSites(models.Model):
    name = models.CharField(null=True, max_length=200)
    students = models.ManyToManyField(Profile, related_name='classes_as_student')
    teachers = models.ManyToManyField(Profile, related_name='classes_as_teacher')

    def __str__(self):
        return self.name


class Assignment(models.Model):
    name = models.CharField(null=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    dueDate = models.DateTimeField(null=True, blank=True)
    classAssignedTo = models.ManyToManyField(ClassSites)
    file = models.FileField(upload_to="assignments/media", null=True, blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(null=True, max_length=200)
    body = models.TextField(null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=DO_NOTHING)
    media = models.FileField(upload_to="messages/media", null=True, blank=True)
    classAssignedTo = models.ForeignKey(ClassSites, on_delete=DO_NOTHING)
    recipients = models.ManyToManyField(User, related_name="messages")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DirectMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=DO_NOTHING, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=DO_NOTHING, related_name='received_messages')
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
