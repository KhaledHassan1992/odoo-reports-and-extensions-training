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

# 1: imports of python lib
import logging

# 2: import of known third party lib

# 3:  imports of odoo
from odoo import models

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib

_logger = logging.getLogger(__name__)


class ModelName(models.Model):
    # Private attributes
    _inherit = 'model.name'
    _description = 'Model Name'

    # Default methods
    # --> the default method pattern is _default_<field_name>


    # Fields declarations


    # compute and search fields, in the same order that fields declaration
    # --> the compute method pattern is _compute_<field_name>
    # --> the inverse method pattern is _inverse_<field_name>
    # --> the search method pattern is _search_<field_name>


    # Constraints and onchanges
    # --> the onchange method pattern is _onchange_<field_name>
    # --> the constraint method pattern is _check_<constraint_name>


    # CRUD methods


    # Action methods
    # -->  an object action method is prefix with action_
    # --> Its decorator is @api.multi, but since it use only one record, 
	#     add self.ensure_one() at the beginning of the method.


    # Business methods