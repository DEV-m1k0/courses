import "../styles/header.css";
import { Link } from "react-router-dom"

export default function Header() {
    let link = <></>
    if (document.URL.includes("login")) {
        link = <Link to='/' className="btn btn-primary">Home</Link>
    } else {
        link = <Link to='/login/' className="btn btn-primary">Login</Link>
    }
    return (
        <>
            <div className="d-flex justify-content-between py-3" id="header">
                <div className="">
                    <Link to="/">
                        <img className="img-fluid" src="/kg-logo.png" id="header-logo-img"/>
                    </Link>
                </div>
                <div className="align-content-center">
                    {link}
                </div>
            </div>
            <hr className="text-white"/>
        </>
    )
}