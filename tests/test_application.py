import builtins
from unittest.mock import patch, MagicMock, call
from application import Application
from hospital import Hospital
from hospital_commands import HospitalCommands
from mocks.mock_console import MockConsole
from user_interaction import UserInteraction


class TestApplication:
    def test_base_case(self):
        console = MockConsole()
        hospital = Hospital([1, 1, 0, 2, 1])
        user_interaction = UserInteraction(console)
        hospital_commands = HospitalCommands(hospital, user_interaction)
        application = Application(hospital_commands, user_interaction)

        console.add_expected_request_and_response('Введите команду: ', 'узнать статус пациента')
        console.add_expected_request_and_response('Введите ID пациента: ', '1')
        console.add_expected_output_message('Статус пациента: "Болен"')

        console.add_expected_request_and_response('Введите команду: ', 'повысить статус пациента')
        console.add_expected_request_and_response('Введите ID пациента: ', '1')
        console.add_expected_output_message('Новый статус пациента: "Слегка болен"')

        console.add_expected_request_and_response('Введите команду: ', 'понизить статус пациента')
        console.add_expected_request_and_response('Введите ID пациента: ', '2')
        console.add_expected_output_message('Новый статус пациента: "Тяжело болен"')

        console.add_expected_request_and_response('Введите команду: ', 'рассчитать статистику')
        console.add_expected_output_message("В больнице на данный момент находится 5 чел., из них:")
        console.add_expected_output_message('    - в статусе "Тяжело болен": 2 чел.')
        console.add_expected_output_message('    - в статусе "Болен": 1 чел.')
        console.add_expected_output_message('    - в статусе "Слегка болен": 2 чел.')

        console.add_expected_request_and_response('Введите команду: ', 'стоп')
        console.add_expected_output_message('Сеанс завершён.')
        application.run()

        console.verify_all_calls_have_been_made()
        assert hospital._patients == [2, 0, 0, 2, 1]
