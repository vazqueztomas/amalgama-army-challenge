class ArmyError(Exception):
    pass


class InsufficientGold(ArmyError):
    pass


class TransformationError(ArmyError):
    pass
