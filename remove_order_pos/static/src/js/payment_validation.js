/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Orderline } from "@point_of_sale/app/components/orderline/orderline";
import OrderPaymentValidation from "@point_of_sale/app/utils/order_payment_validation";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import {clickPayButton} from "../../../../../addons/point_of_sale/static/tests/pos/tours/utils/product_screen_util";



patch(clickPayButton().prototype,{
    clickPayButton(){
        super.clickPayButton()
        console.log("payment validation is ready")
    }
})



patch(PaymentScreen.prototype,{
    setup(){
        super.setup(...arguments)
        console.log("payment screen 123467890")

    },
    clickPartnerButton(){
        super.clickPartnerButton(...arguments)
        console.log("partner is ready")
    }

})
