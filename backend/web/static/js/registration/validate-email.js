/* ------------------------- Импорты с HTML разметки ------------------------ */

const fieldEmail = document.getElementById('id_email')
const elementEmailHelp = document.getElementById('email-help')
const labelEmail = document.getElementById('email-label')

// alert("")

/* --------------------------- Дополнительные компоненты -------------------------- */

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

/* ---------------------------- Валидация почты ---------------------------- */

fieldEmail.addEventListener('focusin', (e) => {
    changeFocuseOfText(elementEmailHelp, labelEmail)
})
fieldEmail.addEventListener('focusout', (e) => {
    changeFocuseOfText(elementEmailHelp, labelEmail)
})

const prevEmailHelpText = elementEmailHelp.innerText
const incorrectEmailHelpText = "Пример правильной почты: email@email.email"

fieldEmail.addEventListener('input', (e) => {

    // Динамическая проверка валидности введеной почты
    const reg = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
    if (fieldEmail.value.length > 3 && reg.test(fieldEmail.value)) {
        fieldEmail.classList.remove("is-invalid")
        if (!fieldEmail.classList.contains("is-valid")) {
            fieldEmail.classList.add("is-valid")
        }
        elementEmailHelp.innerText = ""
    } else {
        fieldEmail.classList.remove("is-valid")
        if (!fieldEmail.classList.contains("is-invalid")) {
            fieldEmail.classList.add("is-invalid")
        }
    }

    // Изменение вспомогательного текста под полем с логином
    if (fieldEmail.value.length == 0) {
        elementEmailHelp.innerText = prevEmailHelpText
    } else if (fieldEmail.value.length > 0 && !fieldEmail.classList.contains('is-valid')) {
        elementEmailHelp.innerText = incorrectEmailHelpText
    }
})

