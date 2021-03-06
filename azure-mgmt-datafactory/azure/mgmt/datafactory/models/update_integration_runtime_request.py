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


class UpdateIntegrationRuntimeRequest(Model):
    """Update integration runtime request.

    :param auto_update: Enables or disables the auto-update feature of the
     self-hosted integration runtime. See
     https://go.microsoft.com/fwlink/?linkid=854189. Possible values include:
     'On', 'Off'
    :type auto_update: str or
     ~azure.mgmt.datafactory.models.IntegrationRuntimeAutoUpdate
    :param update_delay_offset: The time offset (in hours) in the day, e.g.,
     PT03H is 3 hours. The integration runtime auto update will happen on that
     time.
    :type update_delay_offset: str
    """

    _attribute_map = {
        'auto_update': {'key': 'autoUpdate', 'type': 'str'},
        'update_delay_offset': {'key': 'updateDelayOffset', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(UpdateIntegrationRuntimeRequest, self).__init__(**kwargs)
        self.auto_update = kwargs.get('auto_update', None)
        self.update_delay_offset = kwargs.get('update_delay_offset', None)
