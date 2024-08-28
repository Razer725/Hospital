from exceptions import PatientIdTypeError


class ConsoleHandler:
    def read_user_command(self):
        return input("Введите команду: ")

    def read_patient_id(self):
        patient_id = input("Введите ID пациента: ")
        if not patient_id.isdigit():
            raise PatientIdTypeError
        return patient_id

    def read_user_answer(self):
        return input("Желаете этого клиента выписать? (да/нет): ")

    def print_status(self, patient_status):
        print(f"Статус пациента: \"{patient_status}\"")

    def print_new_status(self, patient_new_status):
        print(f"Статус пациента: \"{patient_new_status}\"")

    def print_statistics(self, patients, patients_statuses):
        template = "    - в статусе \"{}\": {} чел."
        patients_statistics = [template.format(status[0], status[1]) for status in patients_statuses]
        print(f"В больнице на данный момент находится {len(patients)} чел., из них:",
              *patients_statistics,
              sep="\n")
