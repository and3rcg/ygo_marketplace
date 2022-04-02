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
        <div>
            <div className="container d-flex flex-row p-5">
                <div>
                    <img src={cardData.image_url} className="img-responsive" />
                    <p className="text-center text-muted">* Imagem meramente ilustrativa</p>
                </div>
                <div className="px-4">
                    <h1>{cardData.name}</h1>
                    <p className="cardEffect">{cardData.description}</p>
                </div>
            </div>
        </div>
    );
}

export default CardDetails;
