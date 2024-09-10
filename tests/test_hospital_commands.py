from unittest.mock import MagicMock

from exceptions import PatientIdTypeError
from hospital import Hospital
from hospital_commands import HospitalCommands


class TestHospitalCommands:
    def test_get_status(self):
        user_interaction = MagicMock()
        user_interaction.request_patient_id = MagicMock(return_value=1)
        hospital_commands = HospitalCommands(Hospital([0, 1, 2]), user_interaction)
        hospital_commands.get_status()
        user_interaction.send_status.assert_called_once_with('Тяжело болен')

    def test_get_status_when_id_type_invalid(self):
        user_interaction = MagicMock()
        user_interaction.request_patient_id = MagicMock(side_effect=PatientIdTypeError)
        hospital_commands = HospitalCommands(Hospital([0, 1, 2]), user_interaction)
        hospital_commands.get_status()
        user_interaction.send_message.assert_called_once_with(
            "Ошибка. ID пациента должно быть числом (целым, положительным)")

    def test_get_status_when_patient_missing(self):
        user_interaction = MagicMock()
        user_interaction.request_patient_id = MagicMock(return_value=10)
        hospital_commands = HospitalCommands(Hospital([0, 1, 2]), user_interaction)
        hospital_commands.get_status()
        user_interaction.send_message.assert_called_once_with("Ошибка. В больнице нет пациента с таким ID")

    def test_status_up(self):
        user_interaction = MagicMock()
        user_interaction.request_patient_id = MagicMock(return_value=1)
        hospital_commands = HospitalCommands(Hospital([1, 1, 2]), user_interaction)
        hospital_commands.status_up()
        user_interaction.send_new_status.assert_called_once_with("Слегка болен")

    def test_status_up_with_max_status_when_discharge_confirmed(self):
        user_interaction = MagicMock()
        user_interaction.request_patient_id = MagicMock(return_value=1)
        hospital_commands = HospitalCommands(Hospital([3, 1, 2]), user_interaction)
        hospital_commands.status_up()
        user_interaction.request_discharge_confirmation = MagicMock(return_value=True)
        user_interaction.send_discharged.assert_called_once()

    def test_status_up_with_max_status_when_discharge_declined(self):
        user_interaction = MagicMock()
        user_interaction.request_patient_id = MagicMock(return_value=1)
        user_interaction.request_discharge_confirmation = MagicMock(return_value=False)
        hospital_commands = HospitalCommands(Hospital([3, 1, 2]), user_interaction)
        hospital_commands.status_up()
        user_interaction.send_status_not_changed.assert_called_once()
