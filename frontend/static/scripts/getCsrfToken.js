import React from "react";

function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !=='') {
        let myPattern = /(^| )csrftoken=([^;]+)/gm;  // replace csrftoken for the name of the cookie you want
        let websiteCookie = document.cookie
        let tokenData = myPattern.exec(websiteCookie)

        // console.log(tokenData[0]) to see the cookie's data after the regexp match
        let cookieValue = tokenData[0].split('=')[1]
    }
    return cookieValue
};

const csrfToken = getCSRFToken();

const CSRFTokenElement = (
    <input type="hidden" name="csrfmiddlewaretoken" value={csrfToken}/>
);

export default CSRFTokenElement
