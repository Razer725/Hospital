from enum import Enum
from idlelib.undo import Command


class Hospital:
    statuses =  {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

    def __init__(self, patients=200, status=1):
        self._patients = [status] * patients

    def validate_patient_id(self):
        pass
        "Ошибка. В больнице нет пациента с таким ID"

    def get_status(self):
        try:
            patient_id = int(input("Введите ID пациента: "))
            if patient_id <=0:
                raise ValueError
            patient_status = self._patients[patient_id-1]
            print(f"Статус пациента: {self.statuses[patient_status]}")
        except ValueError:
            print("Ошибка. ID пациента должно быть числом (целым, положительным)")
        except IndexError:
            print("Ошибка. В больнице нет пациента с таким ID")

    def status_up(self):
        try:
            patient_id = int(input("Введите ID пациента: "))
            if patient_id <= 0:
                raise ValueError

            patient_status = self._patients[patient_id - 1]
            if patient_status == max(self.statuses):
                user_command = input("Желаете этого клиента выписать? (да/нет): ")
                if user_command == "да":
                    self._patients[patient_id - 1] = None
                    print("Пациент выписан из больницы")
                else:
                    print("Пациент остался в статусе \"Готов к выписке\"")
                return

            self._patients[patient_id - 1] += 1
            patient_status = self._patients[patient_id - 1]
            print(f"Статус пациента: {self.statuses[patient_status]}")
        except ValueError:
            print("Ошибка. ID пациента должно быть числом (целым, положительным)")
        except IndexError:
            print("Ошибка. В больнице нет пациента с таким ID")


    def status_down(self):
        pass

    def discharge(self):
        pass

    def calculate_statistics(self):
        pass

    def execute(self, command):
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
            self.execute(user_command)
        print("Сеанс завершён.")


class Commands(Enum):
    STOP = "stop", "стоп"
    GET_STATUS = "узнать статус пациента", "get status"
    STATUS_UP = "повысить статус пациента", "status up"
    STATUS_DOWN = "понизить статус пациента", "status down"
    DISCHARGE = "выписать пациента", "discharge"
    CALCULATE_STATISTICS = "рассчитать статистику", "calculate statistics"




Hospital().run()