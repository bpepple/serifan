import platform
from collections import OrderedDict
from typing import Optional
from urllib.parse import urlencode

import requests

from serifan import __version__, comics_list, exceptions


class Session:
    """
    Session to request api endpoints
    """

    def __init__(self) -> None:
        self.header = {
            "User-Agent": f"Serifan/{__version__} ({platform.system()}; {platform.release()})"
        }
        self.api_url = "https://api.shortboxed.com/comics/v1/{}"

    def call(self, endpoint, params=None):
        """
        Method to make request for api endpoints.
        :param str endpoint: The endpoint to request information from.
        :param dict params: Parameters to add to the request.
        """
        if params is None:
            params = {}

        url = self.api_url.format("/".join(str(e) for e in endpoint))

        try:
            response = requests.get(url, params=params, headers=self.header)
        except requests.exceptions.ConnectionError as e:
            raise exceptions.ApiError("Connection error: {}".format(repr(e)))

        return response.json()

    def new_releases(self) -> comics_list.ComicsList:
        """
        Method to request a list of this weeks current new release comics.

        :return: A list of :class:`Comic` objects.
        :rtype: ComicsList
        """
        return comics_list.ComicsList(self.call(["new"], params={}))

    def previous_releases(self) -> comics_list.ComicsList:
        """
        Method to request a list of the previous weeks released comics.

        :return: A list of :class:`Comic` objects.
        :rtype: ComicsList
        """
        return comics_list.ComicsList(self.call(["previous"], params={}))

    def future_releases(self) -> comics_list.ComicsList:
        return comics_list.ComicsList(self.call(["future"], params={}))
