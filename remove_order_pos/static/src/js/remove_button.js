/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Orderline } from "@point_of_sale/app/components/orderline/orderline";


patch(ProductScreen.prototype,{
    setup(){
        super.setup(...arguments)
        console.log(" product screen ready")
    },
    async onButtonClick(){
        console.log("all clear button is ready")

        const order=this.pos.getOrder();
        console.log(order.id,"this order")

        for (const line of order.getOrderlines()) {
            order.removeOrderline(line)
        }

    }
})


patch(Orderline.prototype,{

    setup(){
        super.setup(...arguments)
        console.log("order line ready")
    },

    async onButtonLine(){
        console.log("line button is ready")
        const line=this.props.line
        const order=line.order_id
        order.removeOrderline(line)

    }

})

