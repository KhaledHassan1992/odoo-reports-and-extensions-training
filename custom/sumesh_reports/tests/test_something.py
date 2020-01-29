# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2019 Openfellas (http://openfellas.com) All Rights Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsibility of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# guarantees and support are strongly advised to contract support@openfellas.com
#
##############################################################################

from odoo.tests.common import HttpCase, TransactionCase


class SomethingCase(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(SomethingCase, self).setUp(*args, **kwargs)

        # TODO Replace this for something useful or delete this method
        self.do_something_before_all_tests()

    def tearDown(self, *args, **kwargs):
        # TODO Replace this for something useful or delete this method
        self.do_something_after_all_tests()

        return super(SomethingCase, self).tearDown(*args, **kwargs)

    def test_something(self):
        """First line of docstring appears in test logs.

        Other lines do not.

        Any method starting with ``test_`` will be tested.
        """
        pass
