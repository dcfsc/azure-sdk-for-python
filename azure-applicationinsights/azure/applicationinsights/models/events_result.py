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


class EventsResult(Model):
    """An event query result.

    :param aimessages: OData messages for this response.
    :type aimessages: list[~azure.applicationinsights.models.ErrorInfo]
    :param value:
    :type value: ~azure.applicationinsights.models.EventsResultData
    """

    _attribute_map = {
        'aimessages': {'key': '@ai\\.messages', 'type': '[ErrorInfo]'},
        'value': {'key': 'value', 'type': 'EventsResultData'},
    }

    def __init__(self, **kwargs):
        super(EventsResult, self).__init__(**kwargs)
        self.aimessages = kwargs.get('aimessages', None)
        self.value = kwargs.get('value', None)