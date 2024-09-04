import pytest

from hospital import Hospital
from user_interaction import UserInteraction


@pytest.fixture
def user_interaction(request):
    return UserInteraction()