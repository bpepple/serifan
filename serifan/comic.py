"""
Comic module.

This module provides the following classes:

- Comic
- ComicSchema
"""
from marshmallow import INCLUDE, Schema, fields, post_load


class Comic:
    """
    The Comic object contains information for an issue.

    :param `**kwargs`: The keyword arguments is used for setting comic data.
    """

    def __init__(self, **kwargs):
        """Intialize a new Comic."""
        for k, v in kwargs.items():
            setattr(self, k, v)


class ComicSchema(Schema):
    """Schema for Comic api."""

    publisher = fields.Str()
    description = fields.Str()
    title = fields.Str()
    price = fields.Str()
    creators = fields.Str()
    release_date = fields.Date(format="%Y-%m-%d")
    diamond_id = fields.Str()

    class Meta:
        """Any unknown fields will be included."""

        unknown = INCLUDE

    @post_load
    def make_object(self, data, **kwargs):
        """
        Make the comic object.

        :param data: Data from Shortboxed response.
        :return: :class:`Comic` object
        :rtype: Comic
        """
        return Comic(**data)
