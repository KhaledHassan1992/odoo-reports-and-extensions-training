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


################################################################################
# Split files by the model involved, either created or inherited.
#
# i.e. For model named <model_name>
# the following files may be created: <main_model>.py
#
# Filenames should use only [a-z0-9_]
# Use correct file permissions: folders 755 and files 644.
################################################################################

from . import model_name_subs
