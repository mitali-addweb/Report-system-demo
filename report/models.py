from django.db import models
from django.contrib.auth.models import User

class Asset(models.Model):
    PRIORITY_CHOICES = [
        ('HIGH', 'High'),
        ('MED-HI', 'Medium-High'),
        ('MED', 'Medium'),
        ('LOW', 'Low'),
    ]

    name = models.CharField(max_length=100)  # Name of machine/asset
    description = models.TextField(blank=True, null=True)  # Asset details
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    ) 
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='MED'
    )

    def __str__(self):
        if self.parent:
            return f"{self.parent} > {self.name}"
        return self.name


class ProblemType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Report(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]

    PRIORITY_CHOICES = Asset.PRIORITY_CHOICES 

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    entry_date = models.DateField(auto_now_add=True)  
    work_order_number = models.CharField(max_length=50, blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MED')
    problem_type = models.ForeignKey(
        ProblemType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    problem_description = models.TextField()
    recommended_action = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    previous_entry = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='follow_ups'
    )

    def __str__(self):
        return f"Report #{self.id} for {self.asset.name}"
