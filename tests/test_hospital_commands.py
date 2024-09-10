from unittest.mock import MagicMock

import pytest

from exceptions import PatientIdTypeError, PatientMissingError
from hospital import Hospital
from hospital_commands import HospitalCommands
from tests.conftest import user_interaction
from user_interaction import UserInteraction


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
        user_interaction.send_message.assert_called_once_with("Ошибка. ID пациента должно быть числом (целым, положительным)")

    def test_get_status_when_patient_missing(self):
        user_interaction = MagicMock()
        user_interaction.request_patient_id = MagicMock(return_value=10)
        hospital_commands = HospitalCommands(Hospital([0, 1, 2]), user_interaction)
        hospital_commands.get_status()
        user_interaction.send_message.assert_called_once_with("Ошибка. В больнице нет пациента с таким ID")

