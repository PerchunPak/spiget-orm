"""Backend package. Not a part of the public API."""
from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Base(DataClassJsonMixin):
    """Base model for all models."""
