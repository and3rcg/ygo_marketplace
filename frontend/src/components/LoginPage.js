import React, { useState } from 'react';
import axiosInstance from '../axios';

function LoginPage() {
    const initialFormData = Object.freeze({
        username: '',
        password: '',
    });

    const [formData, setFormData] = useState(initialFormData);

    const handleChange = (evt) => {
        setFormData({ ...formData, [evt.target.id]: evt.target.value });
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(formData);
        axiosInstance.post('token/', formData).then((response) => {
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            axiosInstance.defaults.headers['Authorization'] =
                'JWT ' + localStorage.getItem('access_token');
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
