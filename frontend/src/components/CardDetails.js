import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import "./styles/CardDetails.css";


function CardDetails () {
    const [cardData, setCardData] = useState([]);
    let { id } = useParams();
    
    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/card/${id}`)
        .then((response) => response.json())
        .then((response) => {setCardData(response)})
        }, []);
        
    document.title = `${cardData.card_name} | Yu-Gi-Oh! Marketplace`;

    // testing the useParams() hook
    let dict_test = useParams();
    console.log(dict_test);
    
    
    return(
        <div className="container">
            <h1>{cardData.card_name}</h1>
            <p className="cardEffect">{cardData.card_description}</p>
        </div>
    )
}


// TODO: create a commit, merge and push after setting up the AppRouter.js file!

export default CardDetails