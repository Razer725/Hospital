class PatientIdTypeError(Exception):
    def __init__(self, msg="Ошибка. ID пациента должно быть числом (целым, положительным)", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class PatientMissingError(Exception):
    def __init__(self, msg="Ошибка. В больнице нет пациента с таким ID", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class StatusUpError(Exception):
    def __init__(self, msg, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class StatusDownError(Exception):
    def __init__(self, msg, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
