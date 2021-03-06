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


class JobMaxRecurrence(Model):
    """JobMaxRecurrence.

    :param frequency: Gets or sets the frequency of recurrence (second,
     minute, hour, day, week, month). Possible values include: 'Minute',
     'Hour', 'Day', 'Week', 'Month'
    :type frequency: str or ~azure.mgmt.scheduler.models.RecurrenceFrequency
    :param interval: Gets or sets the interval between retries.
    :type interval: int
    """

    _attribute_map = {
        'frequency': {'key': 'frequency', 'type': 'RecurrenceFrequency'},
        'interval': {'key': 'interval', 'type': 'int'},
    }

    def __init__(self, *, frequency=None, interval: int=None, **kwargs) -> None:
        super(JobMaxRecurrence, self).__init__(**kwargs)
        self.frequency = frequency
        self.interval = interval
