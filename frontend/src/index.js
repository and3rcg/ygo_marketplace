import React from "react";
import MyComponent from "./components/App";
import ReactDOM from "react-dom";


const appDiv = document.getElementById("app");
const myElement = <MyComponent />;
ReactDOM.render(myElement, appDiv);