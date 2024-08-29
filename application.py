from commands import Commands


class Application:
    def __init__(self, hospital, data_handler):
        self.hospital = hospital
        self.data_handler = data_handler

    def run(self):
        user_command = None
        while user_command not in Commands.STOP.value:
            user_command = self.data_handler.read_user_command()
            self._execute(user_command)
        self.data_handler.print_end_session()

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
            self.data_handler.print_unknown_command()
