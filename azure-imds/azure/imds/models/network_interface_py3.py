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


class NetworkInterface(Model):
    """This contains data about the network interface.

    :param ipv4: This contains the IPv4 address.
    :type ipv4: ~azure.imds.models.NetworkInterfaceIpv4
    :param ipv6: This contains the IPv6 address.
    :type ipv6: ~azure.imds.models.NetworkInterfaceIpv6
    :param mac_address: This is the MAC address of the interface.
    :type mac_address: str
    """

    _attribute_map = {
        'ipv4': {'key': 'ipv4', 'type': 'NetworkInterfaceIpv4'},
        'ipv6': {'key': 'ipv6', 'type': 'NetworkInterfaceIpv6'},
        'mac_address': {'key': 'macAddress', 'type': 'str'},
    }

    def __init__(self, *, ipv4=None, ipv6=None, mac_address: str=None, **kwargs) -> None:
        super(NetworkInterface, self).__init__(**kwargs)
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.mac_address = mac_address