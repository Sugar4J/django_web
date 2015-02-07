from django.test import TestCase
from appDemo.models import Publisher
import  os
# Create your tests here.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
p = Publisher(name='apress',address='285 telegraph Avenue',
               city='beijing',state_province='CA',country='CHINA',
               website='http://www.candy.com')
p.save()