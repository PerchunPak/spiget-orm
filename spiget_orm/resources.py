"""API section with name ``resources``."""
from typing import List, Literal, Optional

from requests.models import Response

from spiget_orm.models import (
    Resource,
    ResourceAuthor,
    ResourceForVersion,
    ResourceReview,
    ResourceUpdate,
    ResourceVersion,
)
from spiget_orm.raw import _params_parser, _raw_api_answer


class SpigetResourcesSection:
    """Resources API section for class."""

    def __init__(self):
        """__init__ method."""
        self.prefix_url = "resources/"

    def resource_list(
        self,
        *,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> List[Resource]:
        """Get a list of available resources (premium and free).

        Args:
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List of ``Resource`` models.
        """
        additional_params = _params_parser(
            ("size", size), ("page", page), ("sort", sort), ("fields", ",".join(fields) if fields else None)
        )
        raw_answer = _raw_api_answer(self.prefix_url + additional_params)
        return [Resource.from_dict(resource.json()) for resource in raw_answer.json()]

    def resources_for_versions(
        self,
        versions: List[str],
        *,
        method: Optional[Literal["any", "all"]] = None,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> ResourceForVersion:
        """Get resources for the specified version(s).

        Args:
            versions: List with version(s).
            method: Method to use to check for versions.
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List of ``Resource`` models.
        """
        additional_params = _params_parser(
            ("method", method),
            ("size", size),
            ("page", page),
            ("sort", sort),
            ("fields", ",".join(fields) if fields else None),
        )
        raw_answer = _raw_api_answer(self.prefix_url + "resources/for/" + ",".join(versions) + additional_params)
        return ResourceForVersion.from_dict(raw_answer.json())

    def free_resource_list(
        self,
        *,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> List[Resource]:
        """Get a list of available free resources.

        Args:
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List of ``Resource`` models.
        """
        additional_params = _params_parser(
            ("size", size), ("page", page), ("sort", sort), ("fields", ",".join(fields) if fields else None)
        )
        raw_answer = _raw_api_answer(self.prefix_url + "free/" + additional_params)
        return [Resource.from_dict(resource.json()) for resource in raw_answer.json()]

    def new_resources(
        self,
        *,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> List[Resource]:
        """Get all new resources.

        Args:
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List of ``Resource`` models.
        """
        additional_params = _params_parser(
            ("size", size), ("page", page), ("sort", sort), ("fields", ",".join(fields) if fields else None)
        )
        raw_answer = _raw_api_answer(self.prefix_url + "new/" + additional_params)
        return [Resource.from_dict(resource.json()) for resource in raw_answer.json()]

    def premium_resources_list(
        self,
        *,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> List[Resource]:
        """Get a list of available premium resources.

        Args:
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List of ``Resource`` models.
        """
        additional_params = _params_parser(
            ("size", size), ("page", page), ("sort", sort), ("fields", ",".join(fields) if fields else None)
        )
        raw_answer = _raw_api_answer(self.prefix_url + "premium/" + additional_params)
        return [Resource.from_dict(resource.json()) for resource in raw_answer.json()]

    def resource_details(self, resource_id: int) -> Resource:
        """Get a resource by its ID.

        Args:
            resource_id: Resource ID.

        Returns:
            ``Resource`` model.
        """
        raw_answer = _raw_api_answer(self.prefix_url + str(resource_id))
        return Resource.from_dict(raw_answer.json())

    def resource_author(self, resource: int) -> ResourceAuthor:
        """Get the resource author.

        Args:
            resource: Resource ID.

        Returns:
            ``ResourceAuthor`` model.
        """
        raw_answer = _raw_api_answer(self.prefix_url + str(resource) + "/author")
        return ResourceAuthor.from_dict(raw_answer.json())

    def resource_download(self, resource: int) -> Response:
        """Download a resource.

         This either redirects to spiget's CDN server (cdn.spiget.org) for a direct download
         of files hosted on spigotmc.org or to the URL of externally hosted resources.
         The external field of a resource should be checked before downloading, to not receive any unexpected data.

        Args:
            resource: Resource ID.

        Returns:
            ``requests.models.Response`` model.
        """
        return _raw_api_answer(self.prefix_url + str(resource) + "/download", allow_redirects=True)

    def resource_reviews(
        self,
        resource: int,
        *,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> List[ResourceReview]:
        """Get a list of reviews for a resource.

        Args:
            resource: Resource ID.
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List of ``ResourceReview`` models.
        """
        additional_params = _params_parser(
            ("size", size), ("page", page), ("sort", sort), ("fields", ",".join(fields) if fields else None)
        )
        raw_answer = _raw_api_answer(self.prefix_url + str(resource) + "/reviews" + additional_params)
        return [ResourceReview.from_dict(review.json()) for review in raw_answer.json()]

    def resource_updates(
        self,
        resource: int,
        *,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> List[ResourceUpdate]:
        """Get a list of updates for a resource.

        Args:
            resource: Resource ID.
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List of ``ResourceUpdate`` models.
        """
        additional_params = _params_parser(
            ("size", size), ("page", page), ("sort", sort), ("fields", ",".join(fields) if fields else None)
        )
        raw_answer = _raw_api_answer(self.prefix_url + str(resource) + "/updates" + additional_params)
        return [ResourceUpdate.from_dict(update.json()) for update in raw_answer.json()]

    def last_resource_update(
        self,
        resource: int,
        *,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> ResourceUpdate:
        """Get a latest of updates for a resource.

        Args:
            resource: Resource ID.
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List of ``ResourceUpdate`` models.
        """
        additional_params = _params_parser(
            ("size", size), ("page", page), ("sort", sort), ("fields", ",".join(fields) if fields else None)
        )
        raw_answer = _raw_api_answer(self.prefix_url + str(resource) + "/updates/latest" + additional_params)
        return ResourceUpdate.from_dict(raw_answer.json())

    def resource_versions(
        self,
        resource: int,
        *,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> List[ResourceVersion]:
        """Get a list of versions for a resource.

        Args:
            resource: Resource ID.
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List of ``ResourceUpdate`` models.
        """
        additional_params = _params_parser(
            ("size", size), ("page", page), ("sort", sort), ("fields", ",".join(fields) if fields else None)
        )
        raw_answer = _raw_api_answer(self.prefix_url + str(resource) + "/updates" + additional_params)
        return [ResourceVersion.from_dict(update.json()) for update in raw_answer.json()]

    def last_resource_version(
        self,
        resource: int,
        *,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> ResourceVersion:
        """Get a latest of versions for a resource.

        Args:
            resource: Resource ID.
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List of ``ResourceVersion`` models.
        """
        additional_params = _params_parser(
            ("size", size), ("page", page), ("sort", sort), ("fields", ",".join(fields) if fields else None)
        )
        raw_answer = _raw_api_answer(self.prefix_url + str(resource) + "/versions/latest" + additional_params)
        return ResourceVersion.from_dict(raw_answer.json())

    def resource_version(self, resource: int, version: int) -> ResourceVersion:
        """Get a version of a resource.

        Args:
            resource: Resource ID.
            version: Version ID.

        Returns:
            ``ResourceVersion`` model.
        """
        raw_answer = _raw_api_answer(self.prefix_url + str(resource) + "/versions/" + str(version))
        return ResourceVersion.from_dict(raw_answer.json())

    def resource_version_download(self, resource: int, version: int) -> Response:
        """Download a specific resource version.

        Note: This only redirects to the stored download location and might not download a file (i.e. for external resources).

        Args:
            resource: Resource ID.
            version: Version ID.

        Returns:
            ``ResourceVersion`` model.
        """
        raw_answer = _raw_api_answer(
            self.prefix_url + str(resource) + "/versions/" + str(version) + "/download", allow_redirects=True
        )
        return raw_answer

    def resource_search(
        self,
        query: str,
        *,
        field: Literal["name", "tag"],
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> List[Resource]:
        """Search for resources.

        Args:
            query: Search query.
            field: Field to search in.
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List of ``Resource`` models.
        """
        additional_params = _params_parser(
            ("field", field),
            ("size", size),
            ("page", page),
            ("sort", sort),
            ("fields", ",".join(fields) if fields else None),
        )
        raw_answer = _raw_api_answer(self.prefix_url + "search/" + field + "/" + query + additional_params)
        return [Resource.from_dict(resource.json()) for resource in raw_answer.json()]
