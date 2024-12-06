from django.db import models
from django.utils.timezone import now

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    voice_id = models.CharField(max_length=255, unique=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    INBOUND = 'Inbound'
    OUTBOUND = 'Outbound'
    TYPE_CHOICES = [
        (INBOUND, 'Inbound'),
        (OUTBOUND, 'Outbound'),
    ]

    RUNNING = 'Running'
    PAUSED = 'Paused'
    COMPLETED = 'Completed'
    STATUS_CHOICES = [
        (RUNNING, 'Running'),
        (PAUSED, 'Paused'),
        (COMPLETED, 'Completed'),
    ]

    name = models.CharField(max_length=255)
    campaign_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='campaigns')

    def __str__(self):
        return self.name


class CampaignResult(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='results')
    name = models.CharField(max_length=255)
    result_type = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    cost = models.FloatField()
    outcome = models.CharField(max_length=255)
    call_duration = models.FloatField()
    recording = models.URLField(blank=True, null=True)
    summary = models.TextField()
    transcription = models.TextField()

    def __str__(self):
        return self.name