from application import Application
from console import Console
from hospital_commands import HospitalCommands
from user_interaction import UserInteraction
from hospital import Hospital

if __name__ == '__main__':
    console = Console()
    user_interaction = UserInteraction(console)
    hospital = Hospital()
    hospital_commands = HospitalCommands(hospital, user_interaction)
    application = Application(hospital_commands, user_interaction)
    application.run()
