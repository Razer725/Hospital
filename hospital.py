from collections import Counter
from console_handler import ConsoleHandler
from exceptions import PatientIdTypeError, PatientMissingError
from patient_db import PatientDB


class Hospital:
    def __init__(self, db:PatientDB, data_handler:ConsoleHandler):
        self.db = db
        self.data_handler = data_handler

    def get_status(self):
        try:
            patient_id = self.data_handler.read_patient_id()
            status = self.db.get_status(patient_id)
            self.data_handler.print_status(status)
        except (PatientMissingError, PatientIdTypeError) as e:
            self.data_handler.print_error(e)

    def status_up(self):
        try:
            patient_id = self.data_handler.read_patient_id()
            if self.db.can_status_up(patient_id):
                self.db.status_up(patient_id)
                new_status = self.db.get_status(patient_id)
                self.data_handler.print_new_status(new_status)
            else:
                if self.data_handler.confirm_discharge():
                    self.db.discharge(patient_id)
                    self.data_handler.print_discharged()
                else:
                    self.data_handler.print_not_discharged()
        except (PatientMissingError, PatientIdTypeError) as e:
            self.data_handler.print_error(e)

    def status_down(self):
        try:
            patient_id = self.data_handler.read_patient_id()
            if self.db.can_status_down(patient_id):
                self.db.status_down(patient_id)
                new_status = self.db.get_status(patient_id)
                self.data_handler.print_new_status(new_status)
            else:
                self.data_handler.print_status_down_denied()
        except (PatientMissingError, PatientIdTypeError) as e:
            self.data_handler.print_error(e)

    def discharge(self):
        try:
            patient_id = self.data_handler.read_patient_id()
            self.db.discharge(patient_id)
            self.data_handler.print_discharged()
        except (PatientMissingError, PatientIdTypeError) as e:
            self.data_handler.print_error(e)

    def calculate_statistics(self):
        patients_statuses = self.db.get_patients_statuses()
        patients_count = self.db.get_patients_count()
        self.data_handler.print_patients_statistics(patients_count, patients_statuses)
