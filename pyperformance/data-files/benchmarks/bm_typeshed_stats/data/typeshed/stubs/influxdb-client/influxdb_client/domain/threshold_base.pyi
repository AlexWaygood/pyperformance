from _typeshed import Incomplete

class ThresholdBase:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, level: Incomplete | None = ..., all_values: Incomplete | None = ...) -> None: ...
    @property
    def level(self): ...
    @level.setter
    def level(self, level) -> None: ...
    @property
    def all_values(self): ...
    @all_values.setter
    def all_values(self, all_values) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
