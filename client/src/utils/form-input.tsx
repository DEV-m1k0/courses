import { useState } from "react";

interface InputProps {
    label: string;
    inputId?: string;
    helpText: string;
    placeholder?: string;
    type: string;
    value?: string;
    onChange?: (value: string) => void;
}

const InputField = ({ label, inputId, helpText, placeholder, type, value, onChange }: InputProps) => {
    const [isFocused, setIsFocused] = useState(false);
    
    const handleFocus = () => setIsFocused(true);
    const handleBlur = () => setIsFocused(false);

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (onChange) {
            onChange(e.target.value);
        }
    }

    return (
        <div className="my-4">
            <label htmlFor={inputId} className={`text-warning ${isFocused ? 'fw-bold' : ''}`}>{label}</label>
            <input 
                className="form-control"
                type={type}
                placeholder={placeholder || ""}
                onFocus={handleFocus}
                onBlur={handleBlur}
                value={value}
                onChange={handleInputChange}
            />
            <small className={`${isFocused ? 'text-warning' : 'text-warning-emphasis' }`}>{helpText}</small>
        </div>
    )
}

export default InputField;