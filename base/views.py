from django.shortcuts import render
from .models import Event,User
from django.db.models import Count,Q, Sum

total_user = User.objects.all().count()
print(total_user)
eventP = Event.objects.alias(entries=Count('user')).filter(Q(start__gt="5:00:5") & Q(end__lt="23:00"))
# eventP = Event.objects.filter(Q(start__gt="5:00:5") & Q(end__lt="23:00"))
print(eventP)

result = Event.objects.filter(Q(start__gt="5:00:5") & Q(end__lt="23:00")).annotate(busy_user=Count("title"))
print(result)