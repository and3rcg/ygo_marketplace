import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// app components
import CardDetails from './pages/CardDetails';
import RegisterPage from './pages/Register';
import LoginPage from './pages/Login';
import ProfileEdit from './pages/ProfileEdit';
import HomePage from './pages/HomePage';
import UserProfile from './pages/UserProfile';

// This component will house all routes of the app.

function AppRouter() {
    return (
        <div>
            <Router>
                <Routes>
                    <Route path="" element={<HomePage />} />
                    <Route path="detail/:id" element={<CardDetails />} />
                    <Route path="login" element={<LoginPage />} />
                    <Route path="profile/edit" element={<ProfileEdit />} />
                    <Route path="register" element={<RegisterPage />} />
                    <Route path="user/:username" element={<UserProfile />} />
                </Routes>
            </Router>
        </div>
    );
}

export default AppRouter;

// Route example: add more of these if you need more paths
// <Route path="/join" element={<RoomJoinPage />}/>
// Don't forget to add these paths to the Django URLs so it won't block you from going there!
// <Route path="register" element={<RegistrationForm />}/>
// import RegistrationForm from "./RegistrationForm";

// <Route path="logout" element={<Logout />} />
// <Route path=":username" element={<UserProfile />} />
//
