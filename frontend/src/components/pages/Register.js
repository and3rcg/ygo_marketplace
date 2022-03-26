import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../../axios';
// import CSRFTokenElement from "../../static/scripts/getCsrfToken";

function RegisterPage() {
    const navigate = useNavigate();
    const initialFormData = Object.freeze({
        email: '',
        username: '',
        first_name: '',
        last_name: '',
        password: '',
    });

    useEffect(() => {
        document.title = 'Register | ' + document.title;
    }, []);

    const [formData, setFormData] = useState(initialFormData);

    const handleSubmit = (event) => {
        event.preventDefault();
        // TODO remove this console.log later for security
        console.log(formData);

        axiosInstance
            .post('auth/users/', formData)
            .then((response) => {
                console.log(response);
                response.status == '201' ? navigate('/login') : console.log('Invalid data.');
            })
            .catch((err) => console.log(err));
    };

    const handleChange = (evt) => {
        setFormData({ ...formData, [evt.target.id]: evt.target.value });
    };

    return (
        <div>
            <form className="container mt-5" onSubmit={handleSubmit}>
                <div className="form-group">
                    <label for="exampleInputEmail1">Username</label>
                    <input
                        type="text"
                        className="form-control"
                        id="username"
                        placeholder="User name"
                        onChange={handleChange}
                    />
                </div>

                <div className="form-group">
                    <label for="exampleInputEmail1">E-mail address</label>
                    <input
                        type="email"
                        className="form-control"
                        id="email"
                        aria-describedby="emailHelp"
                        placeholder="E-mail"
                        onChange={handleChange}
                    />
                    <small id="emailHelp" className="form-text text-muted">
                        We'll never share your email with anyone else.
                    </small>
                </div>

                <div className="form-group">
                    <label for="exampleInputEmail1">First name</label>
                    <input
                        type="text"
                        className="form-control"
                        id="first_name"
                        aria-describedby="emailHelp"
                        placeholder="First name"
                        onChange={handleChange}
                    />
                </div>

                <div className="form-group">
                    <label for="exampleInputEmail1">Last name</label>
                    <input
                        type="text"
                        className="form-control"
                        id="last_name"
                        aria-describedby="emailHelp"
                        placeholder="Last name"
                        onChange={handleChange}
                    />
                </div>

                <div className="form-group">
                    <label for="exampleInputPassword1">Password</label>
                    <input
                        type="password"
                        className="form-control"
                        id="password"
                        placeholder="Password"
                        onChange={handleChange}
                    />
                </div>

                <div className="form-group">
                    <label for="exampleInputPassword1">Confirm Password</label>
                    <input
                        type="password"
                        className="form-control"
                        id="re_password"
                        onChange={handleChange}
                    />
                </div>

                <button type="submit" className="btn btn-primary mt-3">
                    Register
                </button>
            </form>
        </div>
    );
}

export default RegisterPage;
