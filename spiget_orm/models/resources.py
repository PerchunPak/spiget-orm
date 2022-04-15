"""Models for section with name Recources."""
from base64 import b64decode
from dataclasses import dataclass, field
from typing import Dict, List, Literal, Optional

from dataclasses_json import (
    DataClassJsonMixin,
    LetterCase,
    config,
    dataclass_json,
)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ResourceFile(DataClassJsonMixin):
    """File model for some fields."""

    #: File extension.
    type: Literal[".jar", ".zip", ".sk", "external"]
    #: File size.
    size: float
    #: File size-unit (KB, MB, GB).
    size_unit: str
    #: Relative URL to the file.
    url: str
    #: URL of external downloads.
    external_url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ResourceRating(DataClassJsonMixin):
    """Rating model for some fields."""

    #: Number of ratings.
    count: int
    #: Average rating.
    average: float


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Icon(DataClassJsonMixin):
    """Icon model for some fields."""

    #: Relative URL to the image.
    url: str
    #: Base64-Encoded image data.
    data: str
    #: Uknown parametr returned from Spiget.
    info: str
    #: Uknown parametr returned from Spiget.
    hash: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class IdReference(DataClassJsonMixin):
    """Id-Reference to another object."""

    #: ID.
    id: int
    #: Rarely used UUID.
    uuid: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Base64Encoded(DataClassJsonMixin):
    """Base64 encoded text model. Use ``.decode()`` to get original text."""

    #: Base64 encoded text.
    text: str

    def decode(self) -> str:
        """Decode encoded text.

        Returns:
            Decoded text.
        """
        return b64decode(self.text.encode("utf-8")).decode("utf-8")


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Resource(DataClassJsonMixin):
    """Resource model. Almost same with version in docs."""

    #: Id of the Resource.
    id: int
    #: Name of the Resource.
    name: str
    #: Tag line of the Resource.
    tag: str
    #: Contributors.
    contributors: str
    #: Number of likes.
    likes: int
    #: File of the Resource.
    file: ResourceFile
    #: Tested versions.
    tested_versions: List[str]
    #: Map of external and custom links in the resource description.
    links: Dict[str, str]
    #: Rating of the Resource.
    rating: ResourceRating
    #: Release timestamp.
    release_date: int
    #: Update timestamp.
    update_date: int
    #: Amount of downloads.
    downloads: int
    #: Whether this resource is external (not hosted on SpigotMC.org).
    external: bool
    #: Icon of the Resource.
    icon: Icon
    #: Whether the resource is a premium resource.
    premium: bool
    #: Base64-encoded description HTML. Use ``.decode()`` to decode.
    description: Optional[Base64Encoded] = field(
        default=None,
        metadata=config(
            encoder=Base64Encoded,
            decoder=Base64Encoded,
        ),
    )
    #: Base64-encoded documentation HTML (from the Documentation tab). Use ``.decode()`` to decode.
    documentation: Optional[Base64Encoded] = field(
        default=None,
        metadata=config(
            encoder=Base64Encoded,
            decoder=Base64Encoded,
        ),
    )
    #: Price of the resource (only if the resource is premium).
    price: Optional[int] = None
    #: Price Currency of the resource (only if the resource is premium).
    currency: Optional[str] = None
    #: List of review IDs on this resource - only present if directly requesting the resource.
    reviews: Optional[List[IdReference]] = None
    #: List of version IDs of this resource - only present if directly requesting the resource.
    versions: Optional[List[IdReference]] = None
    #: List of update IDs of this resource - only present if directly requesting the resource.
    updates: Optional[List[IdReference]] = None
