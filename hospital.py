from collections import Counter
from console_handler import ConsoleHandler
from exceptions import PatientIdTypeError, PatientMissingError


class Hospital:
    STATUSES =  {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

    def __init__(self, patients=200, status=1):
        self._patients = [status] * patients
        self.console_handler = ConsoleHandler()

    def _get_patient_index(self):
        patient_id = self.console_handler.read_patient_id()
        inner_id = int(patient_id) - 1
        if inner_id >= len(self._patients) or self._patients[inner_id] is None:
            raise PatientMissingError

        return inner_id

    def get_status(self):
        try:
            inner_id = self._get_patient_index()
            patient_status = self._patients[inner_id]
            self.console_handler.print_status(self.STATUSES[patient_status])
        except (PatientMissingError, PatientIdTypeError) as e:
            print(e)

    def status_up(self):
        try:
            inner_id = self._get_patient_index()
            patient_status = self._patients[inner_id]
            if patient_status == max(self.STATUSES):
                if self._confirm_discharge():
                    self._patients[inner_id] = None
                    print("Пациент выписан из больницы")
                else:
                    print("Пациент остался в статусе \"Готов к выписке\"")
                return

            self._patients[inner_id] += 1
            patient_status = self._patients[inner_id]
            self.console_handler.print_new_status(self.STATUSES[patient_status])
        except (PatientMissingError, PatientIdTypeError) as e:
            print(e)

    def _confirm_discharge(self):
        user_answer = self.console_handler.read_user_answer()
        return user_answer in ("да", "yes")

    def status_down(self):
        try:
            inner_id = self._get_patient_index()
            patient_status = self._patients[inner_id]
            if patient_status == min(self.STATUSES):
                print("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")
                return

            self._patients[inner_id] -= 1
            patient_status = self._patients[inner_id]
            print(f"Новый статус пациента: \"{self.STATUSES[patient_status]}\"")
        except (PatientMissingError, PatientIdTypeError) as e:
            print(e)

    def discharge(self):
        try:
            inner_id = self._get_patient_index()
            self._patients[inner_id] = None
            print("Пациент выписан из больницы")
        except (PatientMissingError, PatientIdTypeError) as e:
            print(e)

    def _get_available_patients(self):
        return [x for x in self._patients if x is not None]

    def _count_patients_status_codes(self, patients):
        return sorted(Counter(patients).items())

    def calculate_statistics(self):
        available_patients = self._get_available_patients()
        patients_status_codes = self._count_patients_status_codes(available_patients)
        patients_statuses = [(self.STATUSES[status[0]], status[1]) for status in patients_status_codes]
        self.console_handler.print_statistics(available_patients, patients_statuses)
