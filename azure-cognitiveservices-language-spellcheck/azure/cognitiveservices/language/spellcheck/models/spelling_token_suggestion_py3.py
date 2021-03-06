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


class SpellingTokenSuggestion(Model):
    """SpellingTokenSuggestion.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param suggestion: Required.
    :type suggestion: str
    :ivar score:
    :vartype score: float
    :ivar ping_url_suffix:
    :vartype ping_url_suffix: str
    """

    _validation = {
        'suggestion': {'required': True},
        'score': {'readonly': True},
        'ping_url_suffix': {'readonly': True},
    }

    _attribute_map = {
        'suggestion': {'key': 'suggestion', 'type': 'str'},
        'score': {'key': 'score', 'type': 'float'},
        'ping_url_suffix': {'key': 'pingUrlSuffix', 'type': 'str'},
    }

    def __init__(self, *, suggestion: str, **kwargs) -> None:
        super(SpellingTokenSuggestion, self).__init__(**kwargs)
        self.suggestion = suggestion
        self.score = None
        self.ping_url_suffix = None
