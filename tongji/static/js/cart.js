"use strict"

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".cart-item").forEach(item => {
        calc(item);
    })
    selall(true);
})

function selall(checked) {
    let checks = document.querySelectorAll(".col-check input");
    checks.forEach(check => {
        check.checked = checked;
    })
}

function del(e) {
    e = e.target;
    e = e.parentNode.parentNode.parentNode;

    // 获取自定义属性的值
    var itemName = e.querySelector('.name').innerText;
    var itemPrice = e.querySelector('.col-price span').innerText;
    var orderId = e.querySelector('.col-action a').getAttribute('data-idorder');

    // 创建包含要发送的数据的对象
    var data = {
        name: itemName,
        price: itemPrice,
        idorder: orderId
    };

    // 发送AJAX请求
    fetch('/del_cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            // 请求成功处理逻辑
            e.remove();
            resum();
            recount();
            recheck();
        } else {
            // 请求失败处理逻辑
            console.error('请求失败');
        }
    })
    .catch(error => {
        console.error('发生错误:', error);
    });
}




function minus(e) {
    e = e.target;
    let v = e.parentNode.children[1]
    if (v.value <= 1) return
    v.value--;
    calc(e.parentNode.parentNode.parentNode);
}

function plus(e) {
    e = e.target;
    e.parentNode.children[1].value++;
    calc(e.parentNode.parentNode.parentNode);
    resum();
}

function calc(item) {
    let count = item.querySelector(".col-price span").textContent;
    let val = item.querySelector(".col-num .num").value;
    let total = item.querySelector(".col-total span");
    total.textContent = val * count;
    resum();
}

function resum() {
    let totals = document.querySelectorAll(".cart-item");
    let resum = 0;
    totals = [...totals].filter(total =>
        total.querySelector(".col-check input").checked && total
    );
    totals.forEach(total => {
        total = total.querySelector(".col-total span").textContent;
        resum += Number(total);
    })
    document.querySelector(".total-price em").textContent = resum;
}

function recount() {
    let items = document.querySelectorAll(".cart-item")
    document.querySelectorAll(".cart-total span")[0].textContent = items.length;
}

function recheck() {
    let checks = document.querySelectorAll(".cart-item .col-check .check-box")
    checks = [...checks].filter(check => check.checked && check);
    document.querySelectorAll(".cart-total span")[1].textContent = checks.length;
    resum();
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector(".list-head .col-check input").click();
    recount();
    recheck();
    // resum();
})

function logout() {
    ajax({
        type: "POST",
        url: "/api/logout",
        success(res) {
            window.location.href = "/"
        },
        fail(err) {

        }
    })
}