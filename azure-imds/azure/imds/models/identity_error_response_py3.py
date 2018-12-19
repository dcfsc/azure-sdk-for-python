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
from msrest.exceptions import HttpOperationError


class IdentityErrorResponse(Model):
    """This is the response from an Identity operation in the case an error
    occurs.

    :param error: Error code. Possible values include: 'invalid_request',
     'unauthorized_client', 'access_denied', 'unsupported_response_type',
     'invalid_scope', 'server_error', 'service_unavailable', 'bad_request',
     'forbidden', 'not_found', 'method_not_allowed', 'too_many_requests'
    :type error: str or ~azure.imds.models.Error
    :param error_description: Error message indicating why the operation
     failed.
    :type error_description: str
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'str'},
        'error_description': {'key': 'error_description', 'type': 'str'},
    }

    def __init__(self, *, error=None, error_description: str=None, **kwargs) -> None:
        super(IdentityErrorResponse, self).__init__(**kwargs)
        self.error = error
        self.error_description = error_description


class IdentityErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'IdentityErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(IdentityErrorResponseException, self).__init__(deserialize, response, 'IdentityErrorResponse', *args)