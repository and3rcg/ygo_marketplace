import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"

import CardDetails from "./CardDetails";


// This component will house all routes of the app.

function AppRouter() {
    
    return(
        <div>
            <Router>
                <Routes>
                    <Route path="" element={<h1>Home page</h1>}/>
                    <Route path="detail/:id" element={<CardDetails />}/>
                </Routes>
            </Router>
        </div>
        )
}

export default AppRouter


// Route example: add more of these if you need more paths
// <Route path="/join" element={<RoomJoinPage />}/>
// Don't forget to add these paths to the Django URLs so it won't block you from going there!