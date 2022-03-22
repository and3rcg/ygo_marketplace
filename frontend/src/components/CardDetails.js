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

    console.log(cardData.image_url);

    return (
        <div className="container d-flex flex-row">
            <img src={cardData.image_url} className="p-5" />
            <div className="p-5">
                <h1>{cardData.name}</h1>
                <p className="cardEffect">{cardData.description}</p>
            </div>
        </div>
    );
}

export default CardDetails;
