"""API section with name ``authors``."""
from typing import List, Literal, Optional

from spiget_orm.models import Author, Resource, ResourceReview
from spiget_orm.raw import _params_parser, _raw_api_answer


class SpigetAuthorsSection:
    """Authors API section class."""

    def __init__(self):
        """__init__ method."""
        self.prefix_url = "authors/"

    def author_list(
        self,
        *,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> List[Author]:
        """Get a list of available authors.

        Note: This only includes members involved with resources, either being their author or having reviewed a resource.

        Args:
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by. (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List of authors.
        """
        additional_params = _params_parser(
            ("size", size), ("page", page), ("sort", sort), ("fields", ",".join(fields) if fields else None)
        )
        raw_answer = _raw_api_answer(self.prefix_url + additional_params)
        return [Author.from_dict(resource.json()) for resource in raw_answer.json()]

    def author_details(self, author: int) -> Author:
        """Get details about an author.

        Args:
            author: Author ID.

        Returns:
            Author Model.
        """
        raw_answer = _raw_api_answer(self.prefix_url + str(author))
        return Author.from_dict(raw_answer.json())

    def author_resources(
        self,
        author: int,
        *,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> List[Resource]:
        """Get a list of resources by an author.

        WARN: At now, this is not returning some fields from Resource model.
        This includes: description, versions, updates, reviews, price.

        Args:
            author: Author ID.
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by. (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List with Resource models.
        """
        additional_params = _params_parser(
            ("size", size), ("page", page), ("sort", sort), ("fields", ",".join(fields) if fields else None)
        )
        raw_answer = _raw_api_answer(self.prefix_url + str(author) + "/resources" + additional_params)
        return [Resource.from_dict(resource.json()) for resource in raw_answer.json()]

    def author_reviews(
        self,
        author: int,
        *,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> List[ResourceReview]:
        """Get an author's reviews left on resources.

        Args:
            author: Author ID.
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by. (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List with ResourceReview models.
        """
        additional_params = _params_parser(
            ("size", size), ("page", page), ("sort", sort), ("fields", ",".join(fields) if fields else None)
        )
        raw_answer = _raw_api_answer(self.prefix_url + str(author) + "/reviews" + additional_params)
        return [ResourceReview.from_dict(review.json()) for review in raw_answer.json()]

    def author_search(
        self,
        query: str,
        *,
        field: Literal["name"],
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> List[Author]:
        """Search for authors.

        Args:
            query: Search query.
            field: Field to search in.
            size: Size of the returned array.
            page: Page index.
            sort: Field to sort by. (Use a +/- prefix for ascending/descending order).
            fields: Fields to return.

        Returns:
            List with Author models.
        """
        additional_params = _params_parser(
            ("field", field),
            ("size", size),
            ("page", page),
            ("sort", sort),
            ("fields", ",".join(fields) if fields else None),
        )
        raw_answer = _raw_api_answer("search/authors/" + query + additional_params)
        return [Author.from_dict(author.json()) for author in raw_answer.json()]
