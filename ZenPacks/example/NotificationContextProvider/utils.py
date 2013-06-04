##############################################################################
#
# Copyright (C) Zenoss, Inc. 2013, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

import datetime

from zenoss.protocols.jsonformat import to_dict
from zope.interface import implements

from Products.ZenModel.interfaces import INotificationContextProvider


class MyNotificationContextProvider(object):
    implements(INotificationContextProvider)

    def updateContext(self, signal, context):
        '''
        Provide additional context to notifications.
        '''
        # Get information about the event summary.
        event = to_dict(signal)['event']

        # Get information about the event occurrence.
        occurrence = event_dict['occurrence'][0]

        # Add something to the context.
        context['utcnow'] = str(datetime.datetime.utcnow())
