document.addEventListener("DOMContentLoaded", function () {

    let alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.classList.add("fade");
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
});