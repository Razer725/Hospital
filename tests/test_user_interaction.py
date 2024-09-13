import pytest

from exceptions import PatientIdTypeError


class TestUserInteraction:
    def test_request_patient_id(self, monkeypatch, user_interaction):
        monkeypatch.setattr('builtins.input', lambda _: "1")
        assert user_interaction.request_patient_id() == "1"

    @pytest.mark.parametrize("patient_id", ["0", "-1", "два", "1.1"])
    def test_request_patient_id_with_invalid_id_type(self, monkeypatch, user_interaction, patient_id):
        monkeypatch.setattr('builtins.input', lambda _: patient_id)
        with pytest.raises(PatientIdTypeError):
            user_interaction.request_patient_id()

    @pytest.mark.parametrize('user_input', ['yes', 'да'])
    def test_request_discharge_confirmation_when_answer_positive(self, monkeypatch, user_input, user_interaction):
        monkeypatch.setattr('builtins.input', lambda _: user_input)
        assert user_interaction.request_discharge_confirmation()

    @pytest.mark.parametrize('user_input', ['нет', 'не нужно'])
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
