import pytest

from exceptions import StatusUpError
from hospital import Hospital


class TestHospital:
    def test_get_status(self):
        hospital = Hospital(patients=[0, 1, 2, 3])
        assert hospital.get_status(1) == "Тяжело болен"

    def test_status_up(self):
        hospital = Hospital(patients=[0, 1, 2, 3])
        hospital.status_up(1)
        assert hospital.get_status(1) == 'Болен'

    def test_status_up_when_status_max(self):
        hospital = Hospital(patients=[0, 1, 2, 3])
        with pytest.raises(StatusUpError):
            hospital.status_up(4)

    def test_can_status_up(self):
        hospital = Hospital(patients=[0, 1, 2, 3])
        assert hospital.can_status_up(1)

    def test_can_status_up_when_status_max(self):
        hospital = Hospital(patients=[0, 1, 2, 3])
        assert not hospital.can_status_up(4)

    def test_get_patients_count(self):
        hospital = Hospital(patients=[0, 1, None, 3])
        assert hospital.get_patients_count() == 3

    def test__get_patients(self):
        hospital = Hospital(patients=[0, None, 3])
        assert hospital._get_patients() == [0, 3]

    def test_get_patients_statuses(self):
        hospital = Hospital(patients=[0, 1, 2, None, 3, 0])
        patients_statuses = [('Тяжело болен', 2), ('Болен', 1), ('Слегка болен', 1), ('Готов к выписке', 1)]
        assert hospital.get_patients_statuses() == patients_statuses

    def test_get_patients_statuses_without_patients(self):
        hospital = Hospital(patients=[])
        assert hospital.get_patients_statuses() == []
