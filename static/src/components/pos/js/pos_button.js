odoo.define("owl_custom.SampleButton", function(require){
"use strict";

    const PosComponent = require("point_of_sale.PosComponent");
    const ProductScreen = require("point_of_sale.ProductScreen"); 
    const Registries = require("point_of_sale.Registries")

    class SampleButton extends PosComponent {

    }

    SampleButton.template = "SampleButton";
    ProductScreen.addControlButton({
        component: SampleButton,
        position: ["before", "OrderlineCustomerNoteButton"],
    })

    Registries.Component.add(SampleButton);

    return SampleButton;

});