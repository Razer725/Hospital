from exceptions import PatientIdTypeError, PatientMissingError


class HospitalCommands:
    def __init__(self, hospital, user_interaction):
        self.hospital = hospital
        self.user_interaction = user_interaction

    def get_status(self):
        try:
            patient_id = self.user_interaction.request_patient_id()
            status = self.hospital.get_status(patient_id)
            self.user_interaction.send_status(status)
        except (PatientMissingError, PatientIdTypeError) as e:
            self.user_interaction.send_message(e)

    def status_up(self):
        try:
            patient_id = self.user_interaction.request_patient_id()
            if self.hospital.can_status_up(patient_id):
                self.hospital.status_up(patient_id)
                new_status = self.hospital.get_status(patient_id)
                self.user_interaction.send_new_status(new_status)
            else:
                if self.user_interaction.request_discharge_confirmation():
                    self.hospital.discharge(patient_id)
                    self.user_interaction.send_discharged()
                else:
                    self.user_interaction.send_status_not_changed()
        except (PatientMissingError, PatientIdTypeError) as e:
            self.user_interaction.send_message(e)

    def status_down(self):
        try:
            patient_id = self.user_interaction.request_patient_id()
            if self.hospital.can_status_down(patient_id):
                self.hospital.status_down(patient_id)
                new_status = self.hospital.get_status(patient_id)
                self.user_interaction.send_new_status(new_status)
            else:
                self.user_interaction.send_status_down_denied()
        except (PatientMissingError, PatientIdTypeError) as e:
            self.user_interaction.send_message(e)

    def discharge(self):
        try:
            patient_id = self.user_interaction.request_patient_id()
            self.hospital.discharge(patient_id)
            self.user_interaction.send_discharged()
        except (PatientMissingError, PatientIdTypeError) as e:
            self.user_interaction.send_message(e)

    def calculate_statistics(self):
        patients_statuses = self.hospital.get_patients_statuses()
        patients_count = self.hospital.get_patients_count()
        self.user_interaction.send_patients_statistics(patients_count, patients_statuses)
