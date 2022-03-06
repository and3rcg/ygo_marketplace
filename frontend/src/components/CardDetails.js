import React from "react";
import Button from "react-bootstrap/Button"

function CardDetails () {
    const card = fetch('http://127.0.0.1:8000/api/card/9285')
    .then(response => response.json())
    .then(data => console.log(data));

    
    return(
        <div>
            <Button>
                xok
            </Button>
        </div>
    )
}
export default CardDetails

