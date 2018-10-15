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


class Account(Model):
    """Represents a user account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar user_name: Gets the name of the account owner
    :vartype user_name: str
    :ivar email: Gets the email associated with this account
    :vartype email: str
    :ivar keys: Gets the api keys associated with this account
    :vartype keys:
     ~azure.cognitiveservices.vision.customvision.training.models.ApiKeys
    :ivar quotas: Gets the quotas associated with this account
    :vartype quotas:
     ~azure.cognitiveservices.vision.customvision.training.models.AccountQuota
    """

    _validation = {
        'user_name': {'readonly': True},
        'email': {'readonly': True},
        'keys': {'readonly': True},
        'quotas': {'readonly': True},
    }

    _attribute_map = {
        'user_name': {'key': 'UserName', 'type': 'str'},
        'email': {'key': 'Email', 'type': 'str'},
        'keys': {'key': 'Keys', 'type': 'ApiKeys'},
        'quotas': {'key': 'Quotas', 'type': 'AccountQuota'},
    }

    def __init__(self, **kwargs):
        super(Account, self).__init__(**kwargs)
        self.user_name = None
        self.email = None
        self.keys = None
        self.quotas = None