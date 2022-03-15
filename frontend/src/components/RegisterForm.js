import React from "react";
import CSRFTokenElement from "../../static/scripts/getCsrfToken";


function RegisterUser () {
    

    return (
        <div class="card h-100 align-items-center">
            <div class="card-body">
                <h3>Register</h3>
                <div className="form-group row">
                    <label htmlFor="full_name">Full name:</label>
                    <input type="text" name="full_name" id="fullname"/>
                </div>
                <div className="form-group row">
                    <label htmlFor="username">User name:</label>
                    <input type="text" name="username" id="username"/>
                </div>
                <div className="form-group row">
                    <label htmlFor="email">E-mail:</label>
                    <input type="email" name="email" id="email"/>
                </div>
                <div className="form-group row">
                    <label htmlFor="password">Password: </label>
                    <input type="password" name="password" id="passwd"/>
                </div>
                <button type="submit" className="btn btn-success">Register</button>
            </div>
        </div>
    )
    // return JSX with a form, with CSRFTokenElement inside!
}

export default RegisterUser
