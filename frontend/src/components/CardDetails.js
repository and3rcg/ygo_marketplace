import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './styles/CardDetails.css';
import axiosInstance from '../axios';

function CardDetails() {
    const [cardData, setCardData] = useState([]);
    let { id } = useParams();

    useEffect(() => {
        axiosInstance
            .get(`card/${id}/`)
            .then((response) => setCardData(response.data));
    }, []);

    // testing the useParams() hook
    // let dict_test = useParams();
    // console.log(dict_test);
    // console.log(document.cookie);

    return (
        <div className="container">
            <h1>{cardData.name}</h1>
            <p className="cardEffect">{cardData.description}</p>
            <img src="/images/raye.jpg" />
        </div>
    );
}

export default CardDetails;
