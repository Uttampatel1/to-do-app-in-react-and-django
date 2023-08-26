from django.test import TestCase
from .models import Task

# Create your tests here.

contacts = [
    Task(
        title="Berry Allen",
        completed=True,
       
    ),
    Task(
         title="do something",
        completed=True,
    ),
    Task(
         title="whach youtube video",
        completed=True,
    ),
]