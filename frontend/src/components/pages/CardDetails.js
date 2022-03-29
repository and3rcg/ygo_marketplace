import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
// import { connect } from 'react-redux';

import axiosInstance from '../../axios';

import './styles/CardDetails.css';

const API_URL = 'http://127.0.0.1:8000/api';

// grab isAuthenticated from the Redux store
function CardDetails() {
    const [cardData, setCardData] = useState([]);
    let { id } = useParams();

    useEffect(() => {
        axiosInstance.get(`${API_URL}/card/${id}/`).then((response) => setCardData(response.data));
    }, []);

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
