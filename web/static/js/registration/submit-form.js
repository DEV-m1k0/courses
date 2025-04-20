/* ------------------------ Импорты из HTML разметки ------------------------ */

const btnSubmit = document.querySelector("#btnSubmit");

const inputs = document.querySelectorAll("input");

/* ------------------------ Дополнительные компоненты ----------------------- */

function checkValidationForm() {
    if (fieldUsername.classList.contains("is-valid") &&
        fieldEmail.classList.contains("is-valid") &&
        fieldPassword.classList.contains("is-valid") &&
        fieldPasswordCheck.classList.contains("is-valid")) {

        btnSubmit.disabled = false

    } else {
        btnSubmit.disabled = true
    }
}

/* ------------------------- Реализация функционала ------------------------- */

inputs.forEach(input => {
    input.addEventListener("input", (e) => {
        checkValidationForm()
    });
});