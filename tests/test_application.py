import builtins
from unittest.mock import patch, MagicMock, call
from application import Application
from hospital import Hospital
from hospital_commands import HospitalCommands
from user_interaction import UserInteraction


class TestApplication:
    @patch('builtins.input', side_effect=["узнать статус пациента", "200", "status up", "2", "status down", "3",
                                          "discharge", "4", "рассчитать статистику", "стоп"])
    @patch('builtins.print')
    def test_base_case(self, mock_print, mock_input):
        user_interaction = UserInteraction()
        hospital = Hospital()
        hospital_commands = HospitalCommands(hospital, user_interaction)
        application = Application(hospital_commands, user_interaction)
        application.run()

        assert mock_print.mock_calls == [
            call('Статус пациента: "Болен"'),
            call('Новый статус пациента: "Слегка болен"'),
            call('Новый статус пациента: "Тяжело болен"'),
            call('Пациент выписан из больницы'),
            call('В больнице на данный момент находится 199 чел., из них:',
                 '    - в статусе "Тяжело болен": 1 чел.',
                 '    - в статусе "Болен": 197 чел.',
                 '    - в статусе "Слегка болен": 1 чел.', sep='\n'),
            call('Сеанс завершён.')]


