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
        self.authors = authors.SpigetAuthorsSection
        self.categories = categories.SpigetCategoriesSection
        self.resources = resources.SpigetResourcesSection
        self.search = search.SpigetSearchSection
        self.status = status.SpigetStatusSection
        self.webhook = webhook.SpigetWebhookSection
