import pytest

# Connects our tests with our database
pytestmark = pytest.mark.django_db

from ..models import Cheese
from .factories import CheeseFactory

def test__str__():
    cheese = CheeseFactory(name="Stracchino")

    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name

def test_get_absolute_url():
    cheese = CheeseFactory()

    url = cheese.get_absolute_url()
    assert url == f'/cheeses/{cheese.slug}/'
