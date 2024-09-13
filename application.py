from enums.command_type import CommandType


class Application:
    def __init__(self, hospital_commands, user_interaction):
        self.hospital_commands = hospital_commands
        self.user_interaction = user_interaction

    def run(self):
        user_command = None
        while user_command not in CommandType.STOP.value:
            user_command = self.user_interaction.request_user_command()
            self._execute(user_command)
        self.user_interaction.send_end_session()

    def _execute(self, command):
        if command in CommandType.GET_STATUS.value:
            self.hospital_commands.get_status()
        elif command in CommandType.STATUS_UP.value:
            self.hospital_commands.status_up()
        elif command in CommandType.STATUS_DOWN.value:
            self.hospital_commands.status_down()
        elif command in CommandType.DISCHARGE.value:
            self.hospital_commands.discharge()
        elif command in CommandType.CALCULATE_STATISTICS.value:
            self.hospital_commands.calculate_statistics()
        elif command in CommandType.STOP.value:
            pass
        else:
            self.user_interaction.send_unknown_command()
