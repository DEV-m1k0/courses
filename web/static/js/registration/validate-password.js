/* ------------------------- Импорты с HTML разметки ------------------------ */

const fieldPassword = document.getElementById('id_password')
const elementPasswordHelp = document.getElementById('password-help')
const elementPasswordSecureCheckHelp = document.getElementById('password-secure-check')

const fieldPasswordCheck = document.getElementById('id_password_check')
const fieldPasswordCheckHelp = document.getElementById('password_check-help')

/* ------------------------ Дополнительные компоненты ----------------------- */

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

/* ---------- Валидация для проверки правильности введенного пароля --------- */

fieldPasswordCheck.addEventListener("input", (e) => {
    if (fieldPasswordCheck.value == fieldPassword.value) {
        switchValidField(fieldPasswordCheck)
        switchValidField(fieldPassword)
    }
})

/* ---------------------- Валидация пароля пользователя --------------------- */

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


