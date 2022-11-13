(function() {
    "use strict";
    const select = (el, all = false) => {
        el = el.trim()
        if (all) {
            return [...document.querySelectorAll(el)]
        } else {
            return document.querySelector(el)
        }
    }
    const on = (type, el, listener, all = false) => {
        if (all) {
            select(el, all).forEach(e => e.addEventListener(type, listener))
        } else {
            select(el, all).addEventListener(type, listener)
        }
    }
    if (select('.toggle-sidebar-btn')) {
        on('click', '.toggle-sidebar-btn', function(e) {
            select('body').classList.toggle('toggle-sidebar')
        })
    }
})();

$(document).ready(function(){
    const cart = document.querySelector(".cart");
    // Start when the document is ready
    if(document.readyState == "loading"){
        document.addEventListener("DOMContentLoaded", start);
    }else{
        start();
    }
    // ========================START=============================
    function start(){
        addEvents();
    }
    // ========================UPDATE & RENDER===================
    function update(){
        addEvents();
        updateTotal();
    }
    // =========================ADD==============================
    function addEvents(){
        // Xóa mặt hàng khỏi giỏ hàng
        let cartRemove_btns = document.querySelectorAll(".cart-remove");
        console.log(cartRemove_btns);
        cartRemove_btns.forEach(btn => {
            btn.addEventListener("click", handle_removeCartItem);
        });

        // Thay đổi số lượng mặt hàng
        let cartQuantity_inputs = document.querySelectorAll(".cart-quantity");
        cartQuantity_inputs.forEach(input => {
            input.addEventListener("change", handle_changeItemQuantity);
        })

        // Thêm mặt hàng vào giỏ hàng
        let addCart_btns = document.querySelectorAll(".add-cart");
        addCart_btns.forEach(btn => {
            btn.addEventListener("click", handle_addCartItem);
        });

        const buy_btn = document.querySelector(".btn-buy");
        buy_btn.addEventListener("click", handle_buyOrder);
    }
    // ====================Handle events functions================
    let itemsAdded = [];
    function handle_addCartItem(){
        let pro = this.parentElement;
        // console.log(pro)
        let title = pro.querySelector(".product-title").innerHTML;
        let price = pro.querySelector(".product-price").innerHTML;
        // console.log(title, price);

        let newToAdd = {
            title,
            price
        }

        // TMục xử lý mặt hàng đã tồn tại
        if(itemsAdded.find(el => el.title == newToAdd.title)){
            alert("Mặt hàng đã tồn tại trong giỏ hàng");
            return;
        }else{
            itemsAdded.push(newToAdd);
        }

        // Thêm sản phẩm vào giỏ hàng
        let cartBoxElement = cartBoxComponent(title, price);
        let newNode = document.createElement("div");
        newNode.innerHTML = cartBoxElement;
        const cartContent = cart.querySelector(".cart-content");
        cartContent.appendChild(newNode);
        update();
    }


    function handle_removeCartItem(){
        this.parentElement.remove();
        itemsAdded = itemsAdded.filter(el =>el.title != this.parentElement.querySelector(".cart-product-title").innerHTML)
        update();
    }

    function handle_changeItemQuantity(){
        if(isNaN(this.value) || this.value < 1){
            this.value = 1;
        }
        this.value = Math.floor(this.value); // Giữ ở số nguyên
        update();
    }

    function handle_buyOrder(){
        if(itemsAdded.length <= 0){
            alert("Chưa có mặt hàng nào được chọn");
            return;
        }
        const cartContent = cart.querySelector(".cart-content");
        cartContent.innerHTML = "";
        alert("Bạn đã đặt mua thành công");
        itemsAdded = [];
        update();
    }

    // ===================UPDATE & RENDER funstions===============
    function updateTotal(){
        let cartBoxes = document.querySelectorAll(".cart-box");
        const totalElement = cart.querySelector(".total-price");
        let total = 0;
        cartBoxes.forEach(cartBox => {
            let priceElement = cartBox.querySelector(".cart-price");
            let price = parseFloat(priceElement.innerHTML.replace(" ", ""));
            let quantity = cartBox.querySelector(".cart-quantity").value;
            total += price*quantity;
        });
        total = total.toFixed(0);
        totalElement.innerHTML = total;
    }




    // ========================HTML Components==================================
    function cartBoxComponent(title, price){
        return `<div class="cart-box">
                    <div class="detail-box">
                        <label class="cart-product-name">Tên hàng: </label>
                        <div class="cart-product-title">${title}</div>
                        <label class="cart-product-name">Giá: </label>
                        <div class="cart-price">${price}</div>
                        <label class="cart-product-name">Số lượng: </label>
                        <input type="number" value="1" class="cart-quantity cart-value">
                    </div>
                    <i class='bx bxs-trash cart-remove'></i>
                </div>`
    }
})

