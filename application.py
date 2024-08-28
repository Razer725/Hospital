from commands import Commands
from hospital import Hospital

class Application:
    def __init__(self):
        self.hospital = Hospital()

    def run(self):
        user_command = None
        while user_command not in Commands.STOP.value:
            user_command = self.hospital.console_handler.read_user_command()
            self._execute(user_command)
        print("Сеанс завершён.")

    def _execute(self, command):
        if command in Commands.GET_STATUS.value:
            self.hospital.get_status()
        elif command in Commands.STATUS_UP.value:
            self.hospital.status_up()
        elif command in Commands.STATUS_DOWN.value:
            self.hospital.status_down()
        elif command in Commands.DISCHARGE.value:
            self.hospital.discharge()
        elif command in Commands.CALCULATE_STATISTICS.value:
            self.hospital.calculate_statistics()
        elif command in Commands.STOP.value:
            pass
        else:
            print("Неизвестная команда! Попробуйте ещё раз")


if __name__ == '__main__':
    Application().run()
