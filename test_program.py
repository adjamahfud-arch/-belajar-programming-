from main_program import Users,Simpan
import pytest

@pytest.fixture
def test_data():
    return (
      Users(9)
    )