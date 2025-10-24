class LogicGate:                                                                                                        #no logic gates but there input
    def __init__(self):
        self.data: int | None = None
        self.name: str | None = None

    def __repr__(self):
        return f"LogicGate {self.data}"

    def set_data(self, data):
        self.data = data

    def set_name(self, name):
        self.name = name


class Wire:
    def __init__(self):
        self.logic_input: list[LogicGate] | None | str = None
        self.destination: LogicGate | None = None
        self.logic_calculation: str | None = None

    def set_logic_calculation(self, logic_calculation):
        self.logic_calculation = logic_calculation

    def set_destination(self, destination):
        self.destination = destination

    def set_logic_input(self, logic_input):
        self.logic_input = logic_input

    def is_ready(self) -> bool:
        try:
            if self.destination.name is not None and self.logic_input[0].data is not None and self.logic_input[1].data is not None:
                return True
            else:
                return False
        except AttributeError:
            if self.destination.name is not None and self.logic_input[0].isdigit() is True and self.logic_input[1].data is not None:
                return True
            elif self.destination.name is not None and self.logic_input[0].data is not None and self.logic_input[1].isdigit() is True:
                return True
            else:
                return False

