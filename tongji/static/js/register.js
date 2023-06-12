"use strict"

function register() {
    let auth;
    const checkbox1 = document.querySelector('input[name="checkbox1"]');
    const checkbox2 = document.querySelector('input[name="checkbox2"]');
    if (checkbox1.checked) {
        auth = 1;
    } else if (checkbox2.checked) {
        auth = 2;
    } else {
        auth = 0;
    }
    let name = document.querySelector("#name").value;
    let email = document.querySelector("#email").value;
    let password = document.querySelector("#password").value;
    let password1 = document.querySelector("#password1").value;
    let error = document.querySelector("#error");
    error.textContent = "";
    if (!/^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/.test(email)) {
        error.textContent = "邮箱不符合格式";
        document.querySelector("#email").classList.add("input-err")
        return;
    }
    document.querySelector("#email").classList.remove("input-err")
    if (name === '') {
        error.textContent = "用户名不能为空";
        document.querySelector("#name").classList.add("input-err")
        return;
    }
    document.querySelector("#name").classList.remove("input-err")
    if (password !== password1) {
        error.textContent = "两次输入密码不一致";
        document.querySelector("#password1").classList.add("input-err")
        return;
    }
    document.querySelector("#password1").classList.remove("input-err")
    if (password === '') {
        error.textContent = "密码不能为空";
        document.querySelector("#password").classList.add("input-err")
        return;
    }
    error.textContent = '';
    document.querySelector("#password").classList.remove("input-err")
    ajax({
        type: "POST",
        url: "/api/register",
        data: {
            email,
            name,
            password,
            auth
        },
        success(res) {
            window.location.href = res.location;
        },
        fail(err) {
            error.textContent = err.status;
        }
    })
}

function handleCheckboxClick(event) {
    const checkbox1 = document.querySelector('input[name="checkbox1"]');
    const checkbox2 = document.querySelector('input[name="checkbox2"]');
    
    if (event.target === checkbox1 && checkbox2.checked) {
      checkbox2.checked = false;
    } else if (event.target === checkbox2 && checkbox1.checked) {
      checkbox1.checked = false;
    }
  }
  