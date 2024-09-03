import pytest

from hospital import Hospital


class TestHospital:
    @pytest.mark.parametrize("patient_id,status,patients", [
        (1, "Тяжело болен", [0]),
        (1, "Болен", [1]),
        (1, "Слегка болен", [2]),
        (1, "Готов к выписке", [3]),
    ])
    def test_get_status(self, patient_id, status, patients):
        hospital = Hospital(patients=patients)
        assert hospital.get_status(patient_id) == status

    @pytest.mark.parametrize("patient_id,status,patients", [
        (1, "Болен", [0]),
        # (1, "Готов к выписке", [3])
    ])
    def test_status_up(self, patient_id, status, patients):
        hospital = Hospital(patients=patients)
        hospital.status_up(patient_id)
        assert hospital.get_status(patient_id) == status

    @pytest.mark.parametrize("patients,count", [([], 0), ([0], 1), ([2, 3], 2)])
    def test_get_patients_count(self, patients, count):
        hospital = Hospital(patients=patients)
        assert hospital.get_patients_count() == count

    @pytest.mark.parametrize("patients,patients_statuses", [
        ([0, 1, 2, 3, 0], [('Тяжело болен', 2), ('Болен', 1), ('Слегка болен', 1), ('Готов к выписке', 1)]),
        ([], []),
    ])
    def test_get_patients_statuses(self, patients, patients_statuses):
        hospital = Hospital(patients=patients)
        assert hospital.get_patients_statuses() == patients_statuses


    # @pytest.mark.parametrize("patient_id,status,patients", [
    #     (0, "Тяжело болен", [0]),
    #     (2, "Болен", [1]),
    #     (-1, "Слегка болен", [2]),
    #     (1, "Готов к выписке", [3])
    # ])
    # def test_get_status_invalid_patient_id(self, patient_id, status, patients):
    #     hospital = Hospital(patients=patients)
    #     assert hospital.get_status(patient_id) == status

