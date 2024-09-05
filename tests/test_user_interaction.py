from pytest_check import check, is_true, is_false
from unittest.mock import patch, call

import allure
import pytest

from exceptions import PatientIdTypeError


class TestUserInteraction:
# ----------------- Без использования unittest.mock -----------------------------------
    def test_request_patient_id(self, monkeypatch, user_interaction):
        monkeypatch.setattr('builtins.input', lambda _: "1")
        assert user_interaction.request_patient_id() == "1"

    def test_request_patient_id_when_id_zero(self, monkeypatch, user_interaction):
        monkeypatch.setattr('builtins.input', lambda _: "0")
        with pytest.raises(PatientIdTypeError):
            user_interaction.request_patient_id()

    def test_request_patient_id_when_id_negative(self, monkeypatch, user_interaction):
        monkeypatch.setattr('builtins.input', lambda _: "-1")
        with pytest.raises(PatientIdTypeError):
            user_interaction.request_patient_id()

    def test_request_patient_id_when_id_string(self, monkeypatch, user_interaction):
        monkeypatch.setattr('builtins.input', lambda _: "два")
        with pytest.raises(PatientIdTypeError):
            user_interaction.request_patient_id()

    def test_request_patient_id_when_id_float(self, monkeypatch, user_interaction):
        monkeypatch.setattr('builtins.input', lambda _: "1.1")
        with pytest.raises(PatientIdTypeError):
            user_interaction.request_patient_id()

    @pytest.mark.parametrize('user_input', ['yes', 'да'])
    def test_request_discharge_confirmation_when_answer_positive(self, monkeypatch, user_input, user_interaction):
        monkeypatch.setattr('builtins.input', lambda _: user_input)
        assert user_interaction.request_discharge_confirmation()

    @pytest.mark.parametrize('user_input', ['нет', 'a'])
    def test_request_discharge_confirmation_when_answer_negative(self, monkeypatch, user_input, user_interaction):
        monkeypatch.setattr('builtins.input', lambda _: user_input)
        assert not user_interaction.request_discharge_confirmation()

    def test_send_status(self, capfd, user_interaction):
        user_interaction.send_status("Болен")
        captured = capfd.readouterr()
        assert captured.out == 'Статус пациента: "Болен"\n'

    def test_send_patients_statistics(self, capfd, user_interaction):
        user_interaction.send_patients_statistics(100, [("Тяжело болен", 1), ("Болен", 5), ("Слегка болен", 50),
                                                        ("Готов к выписке", 44)])
        captured = capfd.readouterr()
        assert captured.out == ('В больнице на данный момент находится 100 чел., из них:\n'
                                '    - в статусе "Тяжело болен": 1 чел.\n'
                                '    - в статусе "Болен": 5 чел.\n'
                                '    - в статусе "Слегка болен": 50 чел.\n'
                                '    - в статусе "Готов к выписке": 44 чел.\n')




# ---------------- С использованием unittest mock ------------------------
    # @patch('builtins.input', return_value="1")
    # def test_request_patient_id(self, mock_input, user_interaction):
    #     assert user_interaction.request_patient_id() == "1"
    #
    # @patch('builtins.input', return_value="0")
    # def test_request_patient_id_when_id_zero(self, mock_input, user_interaction):
    #     with pytest.raises(PatientIdTypeError):
    #         user_interaction.request_patient_id()
    #
    # @patch('builtins.input', return_value="-1")
    # def test_request_patient_id_when_id_negative(self, mock_input, user_interaction):
    #     with pytest.raises(PatientIdTypeError):
    #         user_interaction.request_patient_id()
    #
    # @patch('builtins.input', return_value="два")
    # def test_request_patient_id_when_id_string(self, mock_input, user_interaction):
    #     with pytest.raises(PatientIdTypeError):
    #         user_interaction.request_patient_id()
    #
    # @patch('builtins.input', return_value="1.1")
    # def test_request_patient_id_when_id_float(self, mock_input, user_interaction):
    #     with pytest.raises(PatientIdTypeError):
    #         user_interaction.request_patient_id()
    #
    # @patch('builtins.print')
    # def test_send_patients_statistics(self, mock_print, user_interaction):
    #     user_interaction.send_patients_statistics(100, [("Тяжело болен", 1), ("Болен", 5), ("Слегка болен", 50), ("Готов к выписке", 44)])
    #
    #     assert mock_print.mock_calls == [call('В больнице на данный момент находится 100 чел., из них:',
    #                                           '    - в статусе "Тяжело болен": 1 чел.',
    #                                           '    - в статусе "Болен": 5 чел.',
    #                                           '    - в статусе "Слегка болен": 50 чел.',
    #                                           '    - в статусе "Готов к выписке": 44 чел.',
    #                                           sep='\n')]
    #
    # @patch('builtins.print')
    # def test_send_patients_statistics_when_no_patients(self, mock_print, user_interaction):
    #     user_interaction.send_patients_statistics(0, [])
    #     assert mock_print.mock_calls == [call('В больнице на данный момент находится 0 чел., из них:', sep='\n')]

# ----------------- С использованием soft assert ------------------------

    # @patch('builtins.input', side_effect=['yes', 'да'])
    # def test_request_discharge_confirmation_when_answer_positive(self, mock_input, user_interaction):
    #     is_true(user_interaction.request_discharge_confirmation())
    #     is_true(user_interaction.request_discharge_confirmation())
    #
    #
    # @patch('builtins.input', side_effect=['нет', 'a'])
    # def test_request_discharge_confirmation_when_answer_negative(self, mock_input, user_interaction):
    #     is_false(user_interaction.request_discharge_confirmation())
    #     is_false(user_interaction.request_discharge_confirmation())