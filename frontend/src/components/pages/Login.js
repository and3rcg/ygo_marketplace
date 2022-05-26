import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { connect } from 'react-redux';
import { login } from '../../actions/auth';

const Login = ({ login, isAuthenticated }) => {
    const navigate = useNavigate();
    const initialFormData = Object.freeze({
        username: '',
        password: '',
    });

    useEffect(() => {
        document.title = 'Login | ' + document.title;
    }, []);

    const [formData, setFormData] = useState(initialFormData);
    const { username, password } = formData;

    const handleChange = (event) => {
        setFormData({ ...formData, [event.target.name]: event.target.value });
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        login(username, password);
    };

    if (isAuthenticated) {
        navigate('/');
    }

    return (
        <div>
            <form className="container mt-4" onSubmit={handleSubmit}>
                <div className="form-group">
                    <label for="exampleInputEmail1">Username</label>
                    <input
                        type="text"
                        className="form-control"
                        name="username"
                        placeholder="Username"
                        onChange={handleChange}
                    />
                </div>

                <div className="form-group">
                    <label for="exampleInputPassword1">Password</label>
                    <input
                        type="password"
                        className="form-control"
                        name="password"
                        placeholder="Password"
                        onChange={handleChange}
                    />
                </div>

                <button type="submit" className="btn btn-primary">
                    Log in
                </button>
            </form>
        </div>
    );
};

const mapStateToProps = (state) => ({
    isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { login })(Login);
