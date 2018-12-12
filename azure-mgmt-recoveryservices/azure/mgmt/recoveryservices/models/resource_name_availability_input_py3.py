# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ResourceNameAvailabilityInput(Model):
    """Resource information, as sent to the regional resource provider from Global
    RP.

    :param type:
    :type type: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, type: str=None, name: str=None, **kwargs) -> None:
        super(ResourceNameAvailabilityInput, self).__init__(**kwargs)
        self.type = type
        self.name = name