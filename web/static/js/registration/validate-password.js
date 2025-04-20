/* ------------------------- Импорты с HTML разметки ------------------------ */

const fieldPassword = document.getElementById('id_password')
const elementPasswordHelp = document.getElementById('password-help')
const elementPasswordSecureCheckHelp = document.getElementById('password-secure-check')
const labelPassword = document.querySelector("#password-label")

const fieldPasswordCheck = document.getElementById('id_password_check')
const fieldPasswordCheckHelp = document.getElementById('password_check-help')
const labelPasswordCheck = document.querySelector("#password_check-label")

/* ------------------------ Дополнительные компоненты ----------------------- */

// Функция для изменения цвета текста для поля, которое находится в фокусе
function changeFocuseOfText (helpText, label) {
    if (helpText.classList.contains("text-warning-emphasis")) {
        helpText.classList.remove("text-warning-emphasis")
        helpText.classList.add("text-warning")
        label.classList.add("fw-bold");
    } else {
        helpText.classList.remove("text-warning")
        helpText.classList.add("text-warning-emphasis")
        label.classList.remove("fw-bold");
    }
}

// Функция для очистки цвета у текста
function removeAllTagsFromSecureCheckHelp(element) {
    element.classList.remove("text-warning")
    element.classList.remove("text-danger")
    element.classList.remove("text-success")
}

// Функция для изменения состояния валидности поля
function switchValidField(field) {
    if (field.classList.contains("is-valid")) {
        field.classList.remove("is-valid")
        field.classList.add("is-invalid")
    } else {
        field.classList.remove("is-invalid")
        field.classList.add("is-valid")
    }
}

/* ---------------------- Валидация пароля пользователя --------------------- */

fieldPassword.addEventListener('focusin', (e) => {
    changeFocuseOfText(elementPasswordHelp, labelPassword)
})
fieldPassword.addEventListener('focusout', (e) => {
    changeFocuseOfText(elementPasswordHelp, labelPassword)
})

const prevPasswordHelpText = elementPasswordHelp.innerText
const updatedPasswordHelpText = "Введите более надежный пароль"


fieldPassword.addEventListener('input', (e) => {

    removeAllTagsFromSecureCheckHelp(elementPasswordSecureCheckHelp)

    // Динамическая проверка валидности введеного пароля
    const mediumSecureReg = /^(?=.*[\da-zA-Z])(?=.*[^a-zA-Z0-9]).{6,}$/

    const goodSecureReg = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?\d)(?=.*?[!@#$%^&*_+=\-]).{8,}$/

    if (goodSecureReg.test(fieldPassword.value)) {
        elementPasswordSecureCheckHelp.innerText = "Надежный"
        elementPasswordSecureCheckHelp.classList.add("text-success")
    } else if (mediumSecureReg.test(fieldPassword.value)) {
        elementPasswordSecureCheckHelp.innerText = "Средний"
        elementPasswordSecureCheckHelp.classList.add("text-warning")
        elementPasswordHelp.innerText = ""
    } else {
        elementPasswordSecureCheckHelp.innerText = "Слабый"
        elementPasswordSecureCheckHelp.classList.add("text-danger")
    }

    // Изменение вспомогательного текста под полем с логином
    if (fieldPassword.value.length == 0) {
        elementPasswordHelp.innerText = prevPasswordHelpText
    } else if (fieldPassword.value.length > 0 && elementPasswordSecureCheckHelp.innerText == "Слабый") {
        elementPasswordHelp.innerText = updatedPasswordHelpText
    }
})

/* ---------- Валидация для проверки правильности введенного пароля --------- */

fieldPasswordCheck.addEventListener('focusin', (e) => {
    changeFocuseOfText(fieldPasswordCheckHelp, labelPasswordCheck)
})
fieldPasswordCheck.addEventListener('focusout', (e) => {
    changeFocuseOfText(fieldPasswordCheckHelp, labelPasswordCheck)
})

fieldPasswordCheck.addEventListener("input", (e) => {
    if (fieldPasswordCheck.value == fieldPassword.value && elementPasswordSecureCheckHelp.innerText != "Слабый") {
        switchValidField(fieldPasswordCheck)
        switchValidField(fieldPassword)
        fieldPasswordCheckHelp.innerText = ""
    }
})