import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
// import {useNavigate} from 'react-router-dom';

import axiosInstance from '../../axios';

const API_URL = 'http://127.0.0.1:8000/api';

function ProfileEdit() {
    const [profileData, setProfileData] = useState({});
    const [AddressData, setAddressData] = useState({});

    useEffect(() => {
        axiosInstance
            .get(`${API_URL}/auth/users/me/`)
            .then((response) => setProfileData(response.data));
    }, []);

    const handleChange = (evt) => {
        setProfileData({ ...profileData, [evt.target.name]: evt.target.value });
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        axiosInstance.put(`${API_URL}/auth/users/me/`, profileData).then((response) => {
            if (response.status == 200) {
                alert('Profile updated successfully!');
            } else {
                alert('Invalid data.');
            }
        });
    };

    return (
        <div className="container p-5">
            <h1>Update profile: {profileData.username}</h1>

            <form className="container mt-4" onSubmit={handleSubmit}>
                <div className="row">
                    <div className="form-group col-sm">
                        <label for="exampleInputEmail1">First name</label>
                        <input
                            type="text"
                            className="form-control"
                            name="first_name"
                            placeholder={profileData.first_name}
                            onChange={handleChange}
                        />
                    </div>

                    <div className="form-group col-sm">
                        <label for="exampleInputPassword1">Last name</label>
                        <input
                            type="text"
                            className="form-control"
                            name="last_name"
                            placeholder={profileData.last_name}
                            onChange={handleChange}
                        />
                    </div>
                </div>

                <div className="form-group">
                    <label for="exampleInputPassword1">Bio</label>
                    <input
                        type="text"
                        className="form-control"
                        name="bio"
                        placeholder={profileData.bio}
                        onChange={handleChange}
                    />
                </div>
                <button type="submit" className="btn btn-success mt-3">
                    Save
                </button>
            </form>
            <div className="container-fluid mt-5">
                <h1>Address details:</h1>
            </div>
        </div>
    );
}
// placeholder code
export default ProfileEdit;
