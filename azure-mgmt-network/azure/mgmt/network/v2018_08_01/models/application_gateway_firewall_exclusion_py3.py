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


class ApplicationGatewayFirewallExclusion(Model):
    """Allow to exclude some variable satisfy the condition for the WAF check.

    All required parameters must be populated in order to send to Azure.

    :param match_variable: Required. The variable to be excluded.
    :type match_variable: str
    :param selector_match_operator: Required. When matchVariable is a
     collection, operate on the selector to specify which elements in the
     collection this exclusion applies to.
    :type selector_match_operator: str
    :param selector: Required. When matchVariable is a collection, operator
     used to specify which elements in the collection this exclusion applies
     to.
    :type selector: str
    """

    _validation = {
        'match_variable': {'required': True},
        'selector_match_operator': {'required': True},
        'selector': {'required': True},
    }

    _attribute_map = {
        'match_variable': {'key': 'matchVariable', 'type': 'str'},
        'selector_match_operator': {'key': 'selectorMatchOperator', 'type': 'str'},
        'selector': {'key': 'selector', 'type': 'str'},
    }

    def __init__(self, *, match_variable: str, selector_match_operator: str, selector: str, **kwargs) -> None:
        super(ApplicationGatewayFirewallExclusion, self).__init__(**kwargs)
        self.match_variable = match_variable
        self.selector_match_operator = selector_match_operator
        self.selector = selector
