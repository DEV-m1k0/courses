/* ------------------------- Импорты с HTML разметки ------------------------ */

const fieldUsername = document.querySelector('#id_username');
const labelUsername = document.querySelector("#username-label")
const elementUsernameHelp = document.getElementById('username-help');

/* --------------------------- Полезные компоненты -------------------------- */

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

/* ---------------------------- Валидация логина ---------------------------- */

const prevUsernameHelpText = elementUsernameHelp.innerText;
const incorrectUsernameHelpText = "Ваш логин должен содержать минимум 4 символа, латинские буквы и цифры!"

fieldUsername.addEventListener('focusin', (e) => {
    changeFocuseOfText(elementUsernameHelp, labelUsername)
})
fieldUsername.addEventListener('focusout', (e) => {
    changeFocuseOfText(elementUsernameHelp, labelUsername)
})

fieldUsername.addEventListener('input', (e) => {

    // Динамическая проверка валидности введеного логина
    const reg = /^[a-zA-Z0-9]+$/
    if (fieldUsername.value.length > 3 && reg.test(fieldUsername.value)) {
        fieldUsername.classList.remove("is-invalid")
        if (!fieldUsername.classList.contains("is-valid")) {
            fieldUsername.classList.add("is-valid")
        }
        elementUsernameHelp.innerText = ""
    } else {
        fieldUsername.classList.remove("is-valid")
        if (!fieldUsername.classList.contains("is-invalid")) {
            fieldUsername.classList.add("is-invalid")
        }
    }

    // Изменение вспомогательного текста под полем с логином
    if (fieldUsername.value.length == 0) {
        elementUsernameHelp.innerText = prevUsernameHelpText
    } else if (fieldUsername.value.length > 0 && !fieldUsername.classList.contains('is-valid')) {
        elementUsernameHelp.innerText = incorrectUsernameHelpText
    }
})

