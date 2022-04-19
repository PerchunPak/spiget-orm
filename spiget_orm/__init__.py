"""Source folder of all project."""
from spiget_orm.authors import SpigetAuthorsSection
from spiget_orm.categories import SpigetCategoriesSection
from spiget_orm.resources import SpigetResourcesSection
from spiget_orm.search import SpigetSearchSection
from spiget_orm.status import SpigetStatusSection
from spiget_orm.webhook import SpigetWebhookSection

__all__ = [
    "SpigetAuthorsSection",
    "SpigetCategoriesSection",
    "SpigetResourcesSection",
    "SpigetSearchSection",
    "SpigetStatusSection",
    "SpigetWebhookSection",
]
