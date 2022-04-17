"""All models for Spiget API, taken from documentation."""
from base64 import b64decode
from dataclasses import dataclass, field
from typing import Any, Dict, List, Literal, Optional

from dataclasses_json import (
    DataClassJsonMixin,
    LetterCase,
    config,
    dataclass_json,
)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Model(DataClassJsonMixin):
    """Base model for all models."""


class Base64Encoded(Model):
    """Base64 encoded text model. Use ``.decode()`` to get original text."""

    #: Base64 encoded text.
    text: str

    def decode(self) -> str:
        """Decode encoded text.

        Returns:
            Decoded text.
        """
        return b64decode(self.text.encode("utf-8")).decode("utf-8")


class Icon(Model):
    #: Relative URL to the image.
    url: Optional[str] = None
    #: Base64-Encoded image data.
    data: Optional[Base64Encoded] = field(
        default=None,
        metadata=config(
            encoder=Base64Encoded,
            decoder=Base64Encoded,
        ),
    )


class IdReference(Model):
    #: ID of the Another Object.
    id: Optional[int] = None


class IdAndUUIDReference(IdReference):
    #: UUID of the Another Object.
    uuid: Optional[str] = None


class Category(Model):
    #: Category ID.
    id: Optional[int] = None
    #: Category name.
    name: Optional[str] = None


class Author(Model):
    #: ID of the author.
    id: Optional[int] = None
    #: Author name.
    name: Optional[str] = None
    icon: Optional[Icon] = None


class ResourceRating(Model):
    #: Number of ratings.
    count: Optional[int] = None
    #: Average rating.
    average: Optional[float] = None


class ResourceReview(Model):
    author: Optional[Author] = None
    rating: Optional[ResourceRating] = None
    #: Base64-Encoded Review message.
    message: Optional[Base64Encoded] = field(
        default=None,
        metadata=config(
            encoder=Base64Encoded,
            decoder=Base64Encoded,
        ),
    )
    #: Base64-Encoded message the author responded with.
    response_message: Optional[Base64Encoded] = field(
        default=None,
        metadata=config(
            encoder=Base64Encoded,
            decoder=Base64Encoded,
        ),
    )
    #: Version name the review was posted for.
    version: Optional[str] = None
    #: Review timestamp.
    date: Optional[int] = None


class ResourceUpdate(Model):
    #: Update ID.
    id: Optional[int] = None
    #: Update title.
    title: Optional[str] = None
    #: Base64-Encoded description of the update.
    description: Optional[Base64Encoded] = field(
        default=None,
        metadata=config(
            encoder=Base64Encoded,
            decoder=Base64Encoded,
        ),
    )
    #: Update timestamp.
    date: Optional[int] = None
    #: Amount of likes for this update.
    likes: Optional[int] = None


class ResourceVersion(Model):
    #: Version ID.
    id: Optional[int] = None
    #: Version UUID.
    uuid: Optional[str] = None
    #: Version name (e.g. v1.0).
    name: Optional[str] = None
    #: Timestamp of the version's release date.
    release_date: Optional[int] = None
    #: Amount of downloads.
    downloads: Optional[int] = None
    rating: Optional[ResourceRating] = None


class ResourceFile(Model):
    #: File extension.
    type: Optional[Literal["jar", "zip", "sk", "external"]] = None
    #: File size.
    size: Optional[float] = None
    #: File size-unit (KB, MB, GB).
    size_unit: Optional[str] = None
    #: Relative URL to the file.
    url: Optional[str] = None
    #: URL of external downloads.
    external_url: Optional[str] = None


class Resource(Model):
    #: ID of the Resource.
    id: Optional[int] = None
    #: Name of the Resource.
    name: Optional[str] = None
    #: Tag line of the Resource.
    tag: Optional[str] = None
    #: Contributors of the Resource.
    contributors: Optional[str] = None
    #: Number of likes.
    likes: Optional[int] = None
    file: Optional[ResourceFile] = None
    #: List with Tested Versions of the Resource.
    tested_versions: Optional[List[str]] = None
    #: Map of external and custom links in the resource description.
    links: Optional[Dict[str, str]] = None
    rating: Optional[ResourceRating] = None
    #: Release timestamp.
    release_date: Optional[int] = None
    #: Update timestamp.
    update_date: Optional[int] = None
    #: Amount of downloads.
    downloads: Optional[int] = None
    #: Whether this resource is external (not hosted on SpigotMC.org).
    external: Optional[bool] = None
    icon: Optional[Icon] = None
    #: Whether the resource is a premium resource.
    premium: Optional[bool] = None
    #: Price of the resource (only if the resource is premium).
    price: Optional[float] = None
    #: Price Currency of the resource (only if the resource is premium).
    currency: Optional[str] = None
    author: Optional[IdReference] = None
    category: Optional[IdReference] = None
    version: Optional[IdAndUUIDReference] = None
    #: List of review IDs on this resource - only present if directly requesting the resource.
    reviews: Optional[List[IdReference]] = None
    #: List of version IDs of this resource - only present if directly requesting the resource.
    versions: Optional[List[IdReference]] = None
    #: List of update IDs of this resource - only present if directly requesting the resource.
    updates: Optional[List[IdReference]] = None
    #: Base64-encoded description HTML.
    description: Optional[Base64Encoded] = field(
        default=None,
        metadata=config(
            encoder=Base64Encoded,
            decoder=Base64Encoded,
        ),
    )
    #: Base64-encoded documentation HTML (from the Documentation tab).
    documentation: Optional[Base64Encoded] = field(
        default=None,
        metadata=config(
            encoder=Base64Encoded,
            decoder=Base64Encoded,
        ),
    )
    #: Source Code link of the Resource.
    source_code_link: Optional[str] = None
    #: Donation link of the Resource.
    donation_link: Optional[str] = None
