from collections import Counter

from commands import Commands
from exceptions import PatientIdError, PatientMissingError


class HospitalApp:
    statuses =  {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

    def __init__(self, patients=200, status=1):
        self._patients = [status] * patients

    def _get_patient_index(self):
        patient_id = input("Введите ID пациента: ")
        if not patient_id.isdigit():
            raise PatientIdError

        inner_id = int(patient_id) - 1
        if inner_id >= len(self._patients) or self._patients[inner_id] is None:
            raise PatientMissingError

        return inner_id

    def get_status(self):
        try:
            inner_id = self._get_patient_index()
            patient_status = self._patients[inner_id]
            print(f"Статус пациента: \"{self.statuses[patient_status]}\"")
        except (PatientIdError, PatientMissingError) as e:
            print(e)

    def status_up(self):
        try:
            inner_id = self._get_patient_index()
            patient_status = self._patients[inner_id]
            if patient_status == max(self.statuses):
                if self._confirm_discharge():
                    self._patients[inner_id] = None
                    print("Пациент выписан из больницы")
                else:
                    print("Пациент остался в статусе \"Готов к выписке\"")
                return

            self._patients[inner_id] += 1
            patient_status = self._patients[inner_id]
            print(f"Новый статус пациента: \"{self.statuses[patient_status]}\"")
        except (PatientIdError, PatientMissingError) as e:
            print(e)

    def _confirm_discharge(self):
        user_answer = input("Желаете этого клиента выписать? (да/нет): ")
        return user_answer in ("да", "yes")

    def status_down(self):
        try:
            inner_id = self._get_patient_index()
            patient_status = self._patients[inner_id]
            if patient_status == min(self.statuses):
                print("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")
                return

            self._patients[inner_id] -= 1
            patient_status = self._patients[inner_id]
            print(f"Новый статус пациента: \"{self.statuses[patient_status]}\"")
        except (PatientIdError, PatientMissingError) as e:
            print(e)

    def discharge(self):
        try:
            inner_id = self._get_patient_index()
            self._patients[inner_id] = None
            print("Пациент выписан из больницы")
        except (PatientIdError, PatientMissingError) as e:
            print(e)

    def _get_available_patients(self):
        return [x for x in self._patients if x is not None]

    @staticmethod
    def count_patients_statuses(patients):
        return sorted(Counter(patients).items())

    def _print_statistics(self, patients, statuses):
        template = "    - в статусе \"{}\": {} чел."
        patients_statistics = [template.format(self.statuses[status[0]], status[1]) for status in statuses]
        print(f"В больнице на данный момент находится {len(patients)} чел., из них:",
              *patients_statistics,
              sep="\n")

    def calculate_statistics(self):
        available_patients = self._get_available_patients()
        patients_statuses = self.count_patients_statuses(available_patients)
        self._print_statistics(available_patients, patients_statuses)

    def _execute(self, command):
        if command in Commands.GET_STATUS.value:
            self.get_status()
        elif command in Commands.STATUS_UP.value:
            self.status_up()
        elif command in Commands.STATUS_DOWN.value:
            self.status_down()
        elif command in Commands.DISCHARGE.value:
            self.discharge()
        elif command in Commands.CALCULATE_STATISTICS.value:
            self.calculate_statistics()
        elif command in Commands.STOP.value:
            pass
        else:
            print("Неизвестная команда! Попробуйте ещё раз")

    def run(self):
        user_command = None
        while user_command not in Commands.STOP.value:
            user_command = input("Введите команду: ")
            self._execute(user_command)
        print("Сеанс завершён.")
