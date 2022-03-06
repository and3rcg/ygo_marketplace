import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom"
import MyComponent from "./components/App";
import CardDetails from "./components/CardDetails";
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.min.css';


// The index.js can be used to put "static" components of the website, such as header, footer,
// navbar, etc. Elements placed inside of a Route component will be rendered alongside any other
// "static" elements outside of the Router


const myElement = (
    <div>
        <h1>Fixed elements such as header, footer, etc should be put here!</h1>
        <h2>Pages to create:</h2>
        <ul>
            <li>Card list</li>
            <li>Login/register</li>
            <li>Card details</li>
        </ul>
        <button type="button" class="btn btn-primary">fixed button</button>
        <Router>
            <Routes>
                <Route path="" element={<MyComponent />}/>
                <Route path="details" element={<CardDetails />}/>
            </Routes>
        </Router>
    </div>
    );


ReactDOM.render(myElement, document.getElementById("app"));


// Route example: add more of these if you need more paths
// <Route path="/join" element={<RoomJoinPage />}/>
// Don't forget to add these paths to the Django URLs so it won't block you from going there!
