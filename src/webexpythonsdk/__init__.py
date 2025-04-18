"""Community-developed Python SDK for the Webex APIs.

Copyright (c) 2016-2024 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import logging


from ._metadata import (
    __author__,
    __author_email__,
    __copyright__,
    __description__,
    __download_url__,
    __license__,
    __title__,
    __url__,
    __version__,
)
from .api import WebexAPI
from .exceptions import (
    AccessTokenError,
    ApiError,
    ApiWarning,
    MalformedResponse,
    RateLimitError,
    RateLimitWarning,
    webexpythonsdkException,
    webexpythonsdkWarning,
)
from .models.dictionary import dict_data_factory
from .models.immutable import (
    AccessToken,
    AdminAuditEvent,
    AttachmentAction,
    Event,
    GuestIssuerToken,
    immutable_data_factory,
    License,
    Meeting,
    MeetingInvitee,
    MeetingRegistrant,
    MeetingTemplate,
    Membership,
    Message,
    Organization,
    Person,
    Recording,
    Role,
    Room,
    RoomMeetingInfo,
    RoomTab,
    Team,
    TeamMembership,
    Webhook,
    WebhookEvent,
)
from .models.simple import simple_data_factory, SimpleDataModel
from .utils import WebexDateTime


# Initialize Package Logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
