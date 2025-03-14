let uname = document.getElementById('id_username')
let fname = document.getElementById('id_first_name')
fname.focus()

function getCSRFToken() {
    let csrfToken = document.querySelector("[name=csrfmiddlewaretoken]");
    return csrfToken ? csrfToken.value : "";
}


let button = document.querySelector('.btn');
button.disabled = true

function validateFieldOnBlur(element, feedbackElement, errorMessage) {
    element.addEventListener('blur', (e) => {
        element.classList.remove('is-valid');
        if (e.target.value === '') {
            element.classList.add('is-invalid');
            feedbackElement.textContent = errorMessage;
            feedbackElement.style.display = "block";
            button.disabled = true

        }
    });
}




let hints = document.querySelectorAll('[id^="hint_id"')
hints.forEach(hint => {
    hint.classList.add('hidden');
})


let uname_element = document.getElementById('id_username');
let uname_feedback = document.querySelector('.uname');
uname_element.addEventListener('input', (e) => {
    uname_value = e.target.value;
    fetch('/authentication/usernamevalidate/', {
        method: 'POST',
        body: JSON.stringify({
            username: uname_value,

        }),
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':getCSRFToken()
        },
        credentials:'same-origin',
    }).then(res => res.json()).then(data => {
        uname_feedback.style.display = "none";
        uname_feedback.textContent = "";
        if (data.user_name_len_error) {
            uname_element.classList.add('is-invalid')
            uname_feedback.textContent = data.user_name_len_error
            uname_feedback.style.display = "block";


        }
        if (data.user_name_error) {

            uname_element.classList.add('is-invalid')
            uname_feedback.textContent = data.user_name_error
            uname_feedback.style.display = "block";
            button.disabled = true





        }
        if (data.user_name_char_error) {

            uname_element.classList.add('is-invalid')
            uname_feedback.textContent = data.user_name_char_error
            uname_feedback.style.display = "block";
            button.disabled = true



        }
        if ((!data.user_name_char_error && !data.user_name_error && !data.user_name_len_error)) {
            uname_element.classList.remove('is-invalid');
            uname_element.classList.add('is-valid');
            uname_feedback.style.display = "none";


        }

    })

})

validateFieldOnBlur(uname_element, uname_feedback, "This field is required");


let phone_element = document.getElementById('id_phone');
let phone_feedback = document.querySelector('.phone');

phone_element.addEventListener('input', (e) => {
    phone_value = e.target.value;
    fetch('/authentication/phonevalidate/', {
        method: 'POST',
        credentials:'same-origin',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':getCSRFToken()
        },
        body: JSON.stringify({phone: phone_value}),
    }).then(res => res.json()).then(data => {
        phone_feedback.style.display = "none";
        phone_feedback.textContent = "";

        if (data.phone_error) {
            phone_element.classList.add('is-invalid');
            phone_feedback.textContent = data.phone_error
            phone_feedback.style.display = 'block';
            button.disabled = true

        } else {
            phone_element.classList.remove('is-invalid');
            phone_element.classList.add('is-valid');
            phone_feedback.style.display = 'none';

        }
    })
})

validateFieldOnBlur(phone_element, phone_feedback, "This field is required");

let email_element = document.getElementById('id_email');
let email_feedback = document.querySelector('.email');

email_element.addEventListener('input', (e) => {
    email_value = e.target.value;
    fetch('/authentication/emailvalidate/', {
        method: 'POST',
        body: JSON.stringify({
            email: email_value,
        }),
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':getCSRFToken()
        },
        credentials:'same-origin',
    }).then(res => res.json()).then(data => {
        email_feedback.style.display = "none";
        email_feedback.textContent = "";

        if (data.email_error) {
            email_element.classList.add('is-invalid');
            email_feedback.textContent = data.email_error
            email_feedback.style.display = 'block';
        } else {
            email_element.classList.remove('is-invalid');
            email_element.classList.add('is-valid');
            email_feedback.style.display = 'none';

        }
    })
})


validateFieldOnBlur(email_element, email_feedback, "This field is required");


let pwd_element = document.getElementById('id_password1');
let pwd_feedback = document.querySelector('.pwd1');

pwd_element.addEventListener('input', (e) => {
    pwd_value = e.target.value;
    fetch('/authentication/pwdvalidate/', {
        method: 'POST',
        body: JSON.stringify({
            password: pwd_value,
        }),
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':getCSRFToken()
        },
        credentials:'same-origin',
    }).then(res => res.json()).then(data => {
        pwd_feedback.style.display = "none";
        pwd_feedback.textContent = "";

        if (data.pwd_error) {
            pwd_element.classList.add('is-invalid');
            pwd_feedback.textContent = data.pwd_error
            pwd_feedback.style.display = 'block';
            button.disabled = true

        } else {
            pwd_element.classList.remove('is-invalid');
            pwd_element.classList.add('is-valid');
            pwd_feedback.style.display = 'none';

        }
    })
})

validateFieldOnBlur(pwd_element, pwd_feedback, "This field is required");



let pwd2_element = document.getElementById('id_password2');
let pwd2_feedback = document.querySelector('.pwd2');

pwd2_element.addEventListener('input', (e) => {
    let pwd2_value = e.target.value;
    let pwd_value = document.getElementById('id_password1').value; // Original password


    pwd2_feedback.textContent = "";
    pwd2_feedback.style.display = "none";


    if (pwd2_value !== pwd_value) {
        pwd2_element.classList.add('is-invalid');
        pwd2_element.classList.remove('is-valid');
        pwd2_feedback.textContent = "Passwords do not match";
        pwd2_feedback.style.display = "block";
        return;
    } else {
        pwd2_element.classList.remove('is-invalid');
    }


    fetch('/authentication/pwdvalidate/', {
        body: JSON.stringify({
            password: pwd_value,
            repassword: pwd2_value,
        }),
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':getCSRFToken()
        },
        credentials:'same-origin',
        method: 'POST',
    }).then(res => res.json()).then(data => {

        pwd2_feedback.textContent = "";
        pwd2_feedback.style.display = "none";

        if (data.pwd_match_error) {
            pwd2_element.classList.add('is-invalid');
            pwd2_element.classList.remove('is-valid');
            pwd2_feedback.textContent = data.pwd_match_error;
            pwd2_feedback.style.display = 'block';
            button.disabled = true

        } else {
            pwd2_element.classList.remove('is-invalid');
            pwd2_element.classList.add('is-valid');
            button.disabled = false

        }
    });
});



validateFieldOnBlur(pwd2_element, pwd2_feedback, "This field is required");