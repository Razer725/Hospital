from application import Application
from console_handler import ConsoleHandler
from hospital import Hospital
from patient_db import PatientDB

if __name__ == '__main__':
    console_handler = ConsoleHandler()
    db = PatientDB()
    hospital = Hospital(db, console_handler)
    application = Application(hospital, console_handler)
    application.run()
