// /** @odoo-module */
// import { PosOrderline } from "@point_of_sale/app/models/pos_orderline_model";
// import { patch } from "@web/core/utils/patch";
//
// // patch(orderline.prototype),{
// patch(PosOrderline.prototype, {
//     getDisplayData() {
//         return {
//             ...super.getDisplayData(),
//             product_owner: this.product_id.product_tmpl_id.product_owner_id,
//         };
//     },
// });



// /** @odoo-module */
// import { patch } from "@web/core/utils/patch";
// import { PosStore } from "@point_of_sale/app/store/pos_store";
// patch(PosStore.prototype, {
//    getReceiptHeaderData() {
//        return {
//            ...super.getReceiptHeaderData(...arguments),
//            partner: this.get_order().get_partner(),
//            // product_owner:this.product_id.product_tmpl_id.product_owner_id,
//
//        };
//    },
// });