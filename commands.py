from enum import Enum


class Commands(Enum):
    STOP = "stop", "стоп"
    GET_STATUS = "узнать статус пациента", "get status"
    STATUS_UP = "повысить статус пациента", "status up"
    STATUS_DOWN = "понизить статус пациента", "status down"
    DISCHARGE = "выписать пациента", "discharge"
    CALCULATE_STATISTICS = "рассчитать статистику", "calculate statistics"
