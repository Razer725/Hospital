from exceptions import PatientIdTypeError


class ConsoleHandler:
    def read_user_command(self):
        return input("Введите команду: ")

    def read_patient_id(self):
        patient_id = input("Введите ID пациента: ")
        if not patient_id.isdigit():
            raise PatientIdTypeError
        return patient_id

    def confirm_discharge(self):
        user_answer = input("Желаете этого клиента выписать? (да/нет): ")
        return user_answer in ("да", "yes")

    def print_status(self, patient_status):
        print(f"Статус пациента: \"{patient_status}\"")

    def print_new_status(self, patient_new_status):
        print(f"Новый статус пациента: \"{patient_new_status}\"")

    def print_end_session(self):
        print("Сеанс завершён.")

    def print_unknown_command(self):
        print("Неизвестная команда! Попробуйте ещё раз")

    def print_discharged(self):
        print("Пациент выписан из больницы")

    def print_not_discharged(self):
        print("Пациент остался в статусе \"Готов к выписке\"")

    def print_status_down_denied(self):
        print("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")

    def print_patients_statistics(self, count, statuses):
        template = "    - в статусе \"{}\": {} чел."
        patients_statistics = [template.format(status[0], status[1]) for status in statuses]
        print(f"В больнице на данный момент находится {count} чел., из них:",
              *patients_statistics,
              sep="\n")

    def print_error(self, e):
        print(e)
