/*
 * Copyright (c) 2019 Openfellas (http://openfellas.com) All Rights Reserved.
 *
 * WARNING: This program as such is intended to be used by professional
 * programmers who take the whole responsibility of assessing all potential
 * consequences resulting from its eventual inadequacies and bugs
 * End users who are looking for a ready-to-use solution with commercial
 * guarantees and support are strongly advised to contract support@openfellas.com
*/

odoo.define('website_module_name.objectName', function(require){
    "use strict";

    var base = require('web_editor.base');
    base.ready().done(function() {
        // Script that will be loaded when document is ready
    });

    function methodToExport () {
        // This method will be exported as
        // require('module_name.object_name').methodToExport
    }

    return {
        methodToExport: methodToExport
    };

});