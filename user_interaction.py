from exceptions import PatientIdTypeError

# noinspection PyMethodMayBeStatic
class UserInteraction:
    def __init__(self, console):
        self.console = console

    def request_user_command(self):
        return self.console.input("Введите команду: ")

    def request_patient_id(self):
        patient_id = self.console.input("Введите ID пациента: ")
        if not patient_id.isdigit() or int(patient_id) == 0:
            raise PatientIdTypeError
        return patient_id

    def request_discharge_confirmation(self):
        user_answer = self.console.input("Желаете этого клиента выписать? (да/нет): ")
        return user_answer in ("да", "yes")

    def send_status(self, patient_status):
        self.console.print(f"Статус пациента: \"{patient_status}\"")

    def send_new_status(self, patient_new_status):
        self.console.print(f"Новый статус пациента: \"{patient_new_status}\"")

    def send_end_session(self):
        self.console.print("Сеанс завершён.")

    def send_unknown_command(self):
        self.console.print("Неизвестная команда! Попробуйте ещё раз")

    def send_discharged(self):
        self.console.print("Пациент выписан из больницы")

    def send_status_not_changed(self):
        self.console.print("Пациент остался в статусе \"Готов к выписке\"")

    def send_status_down_denied(self):
        self.console.print("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")

    def send_patients_statistics(self, count, statuses):
        template = "    - в статусе \"{}\": {} чел."
        patients_statistics = [template.format(status[0], status[1]) for status in statuses]
        self.console.print(f"В больнице на данный момент находится {count} чел., из них:")
        for patient_statistics in patients_statistics:
            self.console.print(patient_statistics)

    def send_message(self, e):
        self.console.print(e)
