"""API section with name ``resources``."""
from spiget_orm.models.resources import Resource
from spiget_orm.raw import _raw_api_answer


class SpigetResourcesSection:
    """Resources API section for class."""

    def __init__(self):
        """__init__ method."""
        self.prefix_url = "resources/"

    def resource_details(self, resource_id: int) -> Resource:
        """Get a resource by its ID.

        Args:
            resource_id: Recource ID.

        Returns:
            ``Resource`` model.
        """
        raw_answer = _raw_api_answer(self.prefix_url + str(resource_id))
        return Resource.from_dict(raw_answer.json())
