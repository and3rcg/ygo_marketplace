import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

import React from "react";
import ReactDOM from "react-dom";

import BaseApp from "./components/App";
import AppRouter from "./components/AppRouter"


// The index.js can be used to put "static" components of the website, such as header, footer,
// navbar, etc. Elements placed inside of a Route component will be rendered alongside any other
// "static" elements outside of the Router


const myElement = (
    <div>
        <BaseApp />
        <AppRouter />
        <h1>Fixed elements such as header, footer, etc should be put here!</h1>
        <h2>Pages to create:</h2>
        <ul>
            <li>Card list</li>
            <li>Login/register</li>
            <li>Card details</li>
        </ul>
    </div>
    );


ReactDOM.render(myElement, document.getElementById("app"));
