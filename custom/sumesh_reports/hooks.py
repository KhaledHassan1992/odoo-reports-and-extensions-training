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


def pre_init_hook(cr):
    """Loaded before installing the module.

    None of this module's DB modifications will be available yet.

    If you plan to raise an exception to abort install, put all code inside a
    ``with cr.savepoint():`` block to avoid broken databases.

    :param openerp.sql_db.Cursor cr:
        Database cursor.
    """
    raise NotImplementedError


def post_init_hook(cr, registry):
    """Loaded after installing the module.

    This module's DB modifications will be available.

    :param openerp.sql_db.Cursor cr:
        Database cursor.

    :param openerp.modules.registry.RegistryManager registry:
        Database registry, using v7 api.
    """
    raise NotImplementedError


def uninstall_hook(cr, registry):
    """Loaded before uninstalling the module.

    This module's DB modifications will still be available. Raise an exception
    to abort uninstallation.

    :param openerp.sql_db.Cursor cr:
        Database cursor.

    :param openerp.modules.registry.RegistryManager registry:
        Database registry, using v7 api.
    """
    raise NotImplementedError


def post_load():
    """Loaded before any model or data has been initialized.

    This is ok as the post-load hook is for server-wide
    (instead of registry-specific) functionalities.

    This is very useful to create monkey patches for odoo.

    Note: You do not have access to database cursor here.
    """
    raise NotImplementedError
