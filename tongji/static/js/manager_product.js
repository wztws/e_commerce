function recheck() {
    let checks = document.querySelectorAll(".cart-item .col-check .check-box")
    checks = [...checks].filter(check => check.checked && check);
    document.querySelectorAll(".cart-total span")[1].textContent = checks.length;
    resum();
}