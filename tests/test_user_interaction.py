from unittest.mock import patch, call

import pytest

from exceptions import PatientIdTypeError


class TestUserInteraction:
    @patch('builtins.input', return_value="1")
    def test_request_patient_id(self, mock_input, user_interaction):
        assert user_interaction.request_patient_id() == "1"

    @patch('builtins.input', side_effect=['0', '-1', 'два'])  # Спросить тут про параметризацию с моками и софт ассерты
    def test_request_patient_id_when_id_invalid(self, mock_input, user_interaction):
        with pytest.raises(PatientIdTypeError):
            user_interaction.request_patient_id()

        with pytest.raises(PatientIdTypeError):
            user_interaction.request_patient_id()

        with pytest.raises(PatientIdTypeError):
            user_interaction.request_patient_id()

    @patch('builtins.input', side_effect=['yes', 'да'])
    def test_request_discharge_confirmation_when_answer_positive(self, mock_input, user_interaction):
        assert user_interaction.request_discharge_confirmation()
        assert user_interaction.request_discharge_confirmation()

    @patch('builtins.input', side_effect=['нет', 'a'])
    def test_request_discharge_confirmation_when_answer_negative(self, mock_input, user_interaction):
        assert not user_interaction.request_discharge_confirmation()
        assert not user_interaction.request_discharge_confirmation()

    @patch('builtins.print')
    def test_send_status(self, mock_print, user_interaction):
        user_interaction.send_status("Болен")
        assert mock_print.mock_calls == [call(f"Статус пациента: \"Болен\"")]

    def test_send_status_without_mocking(self, capfd, user_interaction):  # без мока
        user_interaction.send_status("Болен")
        captured = capfd.readouterr()
        assert captured.out == 'Статус пациента: "Болен"\n'

    @patch('builtins.print')
    def test_send_patients_statistics(self, mock_print, user_interaction):
        user_interaction.send_patients_statistics(100, [("Тяжело болен", 1), ("Болен", 5), ("Слегка болен", 50), ("Готов к выписке", 44)])
        assert mock_print.mock_calls == [call('В больнице на данный момент находится 100 чел., из них:',
                                              '    - в статусе "Тяжело болен": 1 чел.',
                                              '    - в статусе "Болен": 5 чел.',
                                              '    - в статусе "Слегка болен": 50 чел.',
                                              '    - в статусе "Готов к выписке": 44 чел.',
                                              sep='\n')]

    @patch('builtins.print')
    def test_send_patients_statistics_when_no_patients(self, mock_print, user_interaction):
        user_interaction.send_patients_statistics(0, [])
        assert mock_print.mock_calls == [call('В больнице на данный момент находится 0 чел., из них:', sep='\n')]

