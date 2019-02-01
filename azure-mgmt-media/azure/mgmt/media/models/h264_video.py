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

from .video import Video


class H264Video(Video):
    """Describes all the properties for encoding a video with the H.264 codec.

    All required parameters must be populated in order to send to Azure.

    :param label: An optional label for the codec. The label can be used to
     control muxing behavior.
    :type label: str
    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param key_frame_interval: The distance between two key frames, thereby
     defining a group of pictures (GOP). The value should be a non-zero integer
     in the range [1, 30] seconds, specified in ISO 8601 format. The default is
     2 seconds (PT2S).
    :type key_frame_interval: timedelta
    :param stretch_mode: The resizing mode - how the input video will be
     resized to fit the desired output resolution(s). Default is AutoSize.
     Possible values include: 'None', 'AutoSize', 'AutoFit'
    :type stretch_mode: str or ~azure.mgmt.media.models.StretchMode
    :param scene_change_detection: Whether or not the encoder should insert
     key frames at scene changes. If not specified, the default is false. This
     flag should be set to true only when the encoder is being configured to
     produce a single output video.
    :type scene_change_detection: bool
    :param complexity: Tells the encoder how to choose its encoding settings.
     The default value is Balanced. Possible values include: 'Speed',
     'Balanced', 'Quality'
    :type complexity: str or ~azure.mgmt.media.models.H264Complexity
    :param layers: The collection of output H.264 layers to be produced by the
     encoder.
    :type layers: list[~azure.mgmt.media.models.H264Layer]
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'key_frame_interval': {'key': 'keyFrameInterval', 'type': 'duration'},
        'stretch_mode': {'key': 'stretchMode', 'type': 'StretchMode'},
        'scene_change_detection': {'key': 'sceneChangeDetection', 'type': 'bool'},
        'complexity': {'key': 'complexity', 'type': 'H264Complexity'},
        'layers': {'key': 'layers', 'type': '[H264Layer]'},
    }

    def __init__(self, **kwargs):
        super(H264Video, self).__init__(**kwargs)
        self.scene_change_detection = kwargs.get('scene_change_detection', None)
        self.complexity = kwargs.get('complexity', None)
        self.layers = kwargs.get('layers', None)
        self.odatatype = '#Microsoft.Media.H264Video'
