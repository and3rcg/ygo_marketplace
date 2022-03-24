import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../../axios';

function Logout() {
    const navigate = useNavigate();
    useEffect(() => {
        const response = axiosInstance.post('/logout/', {
            refresh_token: localStorage.getItem('refresh_token'),
        });
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        axiosInstance.defaults.headers['Authorization'] = null;
        navigate('/login');
    });
    return <div>Logout</div>;
}

export default Logout;
