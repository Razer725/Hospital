from collections import Counter

from Commands import Commands


class HospitalApp:
    statuses =  {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}
    commands_mapping = {}

    def __init__(self, patients=200, status=1):
        self._patients = [status] * patients

    def _find_patient(self):
        patient_id = input("Введите ID пациента: ")
        if not patient_id.isdigit():
            print("Ошибка. ID пациента должно быть числом (целым, положительным)")
            return

        inner_id = int(patient_id) - 1
        if inner_id >= len(self._patients) or self._patients[inner_id] is None:
            print("Ошибка. В больнице нет пациента с таким ID")
            return

        return inner_id

    def get_status(self):
        inner_id = self._find_patient()
        if inner_id is None:
            return

        patient_status = self._patients[inner_id]
        print(f"Статус пациента: \"{self.statuses[patient_status]}\"")

    def status_up(self):
        inner_id = self._find_patient()
        if inner_id is None:
            return

        patient_status = self._patients[inner_id]
        if patient_status == max(self.statuses):
            user_command = input("Желаете этого клиента выписать? (да/нет): ")
            if user_command == "да":
                self._patients[inner_id] = None
                print("Пациент выписан из больницы")
            else:
                print("Пациент остался в статусе \"Готов к выписке\"")
            return

        self._patients[inner_id] += 1
        patient_status = self._patients[inner_id]
        print(f"Новый статус пациента: \"{self.statuses[patient_status]}\"")

    def status_down(self):
        inner_id = self._find_patient()
        if inner_id is None:
            return

        patient_status = self._patients[inner_id]
        if patient_status == min(self.statuses):
            print("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")
            return

        self._patients[inner_id] -= 1
        patient_status = self._patients[inner_id]
        print(f"Новый статус пациента: \"{self.statuses[patient_status]}\"")

    def discharge(self):
        inner_id = self._find_patient()
        if inner_id is None:
            return
        self._patients[inner_id] = None
        print("Пациент выписан из больницы")

    def calculate_statistics(self):
        available_patients = [x for x in self._patients if x is not None]
        c = Counter(available_patients)
        s = [f"    - в статусе \"{self.statuses[i[0]]}\": {i[1]} чел." for i in sorted(c.items())]
        print(f"В больнице на данный момент находится {len(available_patients)} чел., из них:", *s, sep="\n")

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
