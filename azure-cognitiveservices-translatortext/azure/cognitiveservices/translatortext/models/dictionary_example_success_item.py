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


class DictionaryExampleSuccessItem(Model):
    """DictionaryExampleSuccessItem.

    :param normalized_source:
    :type normalized_source: str
    :param normalized_target:
    :type normalized_target: str
    :param examples:
    :type examples:
     list[~azure.cognitiveservices.translatortext.models.DictionaryExampleSuccessItemExamplesItem]
    """

    _attribute_map = {
        'normalized_source': {'key': 'normalizedSource', 'type': 'str'},
        'normalized_target': {'key': 'normalizedTarget', 'type': 'str'},
        'examples': {'key': 'examples', 'type': '[DictionaryExampleSuccessItemExamplesItem]'},
    }

    def __init__(self, **kwargs):
        super(DictionaryExampleSuccessItem, self).__init__(**kwargs)
        self.normalized_source = kwargs.get('normalized_source', None)
        self.normalized_target = kwargs.get('normalized_target', None)
        self.examples = kwargs.get('examples', None)