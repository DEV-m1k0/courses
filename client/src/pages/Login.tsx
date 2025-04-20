import InputField from "../utils/form-input.tsx";
import Header from "../components/Header";
import "../styles/form/base-form.css"
import "../styles/form/sizing-form.css"
import { useState } from "react";


interface FormProps {
    username:  "";
    password: "";
}


function Login() {

    const initialFormValues: FormProps = {
        username: "",
        password: ""
    }

    const [values, setValues] = useState(initialFormValues);

    const handleValueChange = (field: keyof FormProps, newValue: string) => {
        setValues(prevValues => ({
            ...prevValues,
            [field]: newValue
        }))
    }

    const isButtonEnabled = values.username.trim().length > 0 && values.password.trim().length > 0;



    return (
        <>
            <Header/>
            <form className="p-4 rounded">
                <h2 className="text-warning">Вход в аккаунт</h2>

                <hr className="text-warning" />

                <InputField
                    label="Логин:"
                    helpText="Введите логин"
                    type="text"
                    onChange={(newValue) => handleValueChange('username', newValue)}
                />

                <InputField
                    label="Пароль:"
                    helpText="Введите пароль"
                    type="password"
                    onChange={(newValue) => handleValueChange('password', newValue)}
                />

                <button id="btnLogin" className="btn btn-primary w-100" type="button" disabled={!isButtonEnabled}>Войти</button>
            </form>
        </>
    )
}

export default Login;