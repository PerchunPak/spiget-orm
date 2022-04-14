"""Source folder of all project."""
from spiget_orm import authors, categories, resources, search, status, webhook


class SpigetAPI:
    """Main class to access all other classes.

    Attributes:
        authors: API section with name ``authors``.
        categories: API section with name ``categories``.
        resources: API section with name ``resources``.
        search: API section with name ``search``.
        status: API section with name ``status``.
        webhook: API section with name ``webhook``.
    """

    def __init__(self):
        """__init__ method."""
        self.authors = authors
        self.categories = categories
        self.resources = resources
        self.search = search
        self.status = status
        self.webhook = webhook
