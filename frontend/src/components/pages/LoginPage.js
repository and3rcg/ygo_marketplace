import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../../axios';

function LoginPage() {
    const navigate = useNavigate();
    const initialFormData = Object.freeze({
        username: '',
        password: '',
    });

    useEffect(() => {
        document.title = 'Login | ' + document.title;
    }, []);

    const [formData, setFormData] = useState(initialFormData);

    const handleChange = (event) => {
        setFormData({ ...formData, [event.target.id]: event.target.value });
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        // TODO remove this console.log later for security
        console.log(formData);

        axiosInstance.post('token/', formData).then((response) => {
            console.log(response);

            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);

            axiosInstance.defaults.headers['Authorization'] =
                'JWT ' + localStorage.getItem('access_token');

            response.status == '200' ? navigate('/') : navigate('/login');
        });
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <div class="form-group">
                    <label for="exampleInputEmail1">Username</label>
                    <input
                        type="text"
                        class="form-control"
                        id="username"
                        placeholder="Username"
                        onChange={handleChange}
                    />
                </div>

                <div class="form-group">
                    <label for="exampleInputPassword1">Password</label>
                    <input
                        type="password"
                        class="form-control"
                        id="password"
                        placeholder="Password"
                        onChange={handleChange}
                    />
                </div>

                <button type="submit" class="btn btn-primary">
                    Register
                </button>
            </form>
        </div>
    );
}

export default LoginPage;
