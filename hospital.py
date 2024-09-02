from collections import Counter

from exceptions import PatientMissingError, StatusUpError, StatusDownError


class Hospital:
    STATUSES = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

    def __init__(self, patients=200, status=1):
        self._patients = [status] * patients

    def _get_patient_index(self, patient_id):
        inner_id = int(patient_id) - 1
        if inner_id >= len(self._patients) or self._patients[inner_id] is None:
            raise PatientMissingError
        return inner_id

    def _get_status_code(self, patient_id):
        inner_id = self._get_patient_index(patient_id)
        return self._patients[inner_id]

    def get_status(self, patient_id):
        status_code = self._get_status_code(patient_id)
        return self.STATUSES[status_code]

    def can_status_up(self, patient_id):
        status_code = self._get_status_code(patient_id)
        return not status_code == max(self.STATUSES)

    def can_status_down(self, patient_id):
        status_code = self._get_status_code(patient_id)
        return not status_code == min(self.STATUSES)

    def status_up(self, patient_id):
        if not self.can_status_up(patient_id):
            raise StatusUpError
        inner_id = self._get_patient_index(patient_id)
        self._patients[inner_id] += 1

    def status_down(self, patient_id):
        if not self.can_status_down(patient_id):
            raise StatusDownError
        inner_id = self._get_patient_index(patient_id)
        self._patients[inner_id] -= 1

    def discharge(self, patient_id):
        inner_id = self._get_patient_index(patient_id)
        self._patients[inner_id] = None

    def _get_patients(self):
        return [x for x in self._patients if x is not None]

    def _count_patients_status_codes(self, patients):
        return sorted(Counter(patients).items())

    def get_patients_count(self):
        return len(self._get_patients())

    def get_patients_statuses(self):
        patients = self._get_patients()
        patients_status_codes = self._count_patients_status_codes(patients)
        patients_statuses = [(self.STATUSES[status[0]], status[1]) for status in patients_status_codes]
        return patients_statuses
