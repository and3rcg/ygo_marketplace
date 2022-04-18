import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
// import { connect } from 'react-redux';

import axiosInstance from '../../axios';

import './styles/CardDetails.css';

const API_URL = 'http://127.0.0.1:8000/api';

// grab isAuthenticated from the Redux store
function CardDetails() {
    const [cardData, setCardData] = useState([]);
    const [sellersData, setSellersData] = useState([]);

    // TODO: DRY this function!
    const usdFormat = (value) => {
        return `US$ ${parseFloat(value).toFixed(2)}`;
    };

    // create sellers state
    let { id } = useParams();

    useEffect(() => {
        axiosInstance
            .get(`${API_URL}/on_sale/?card_id=${id}`)
            .then((response) => setSellersData(response.data));
        axiosInstance.get(`${API_URL}/card/${id}/`).then((response) => setCardData(response.data));
    }, []);
    console.log(sellersData);

    return (
        <div>
            <div className="container">
                <div className="row">
                    <div className="col">
                        <img src={cardData.image_url} className="img-fluid w-50 mx-auto d-block" />
                        <p className="text-center text-muted">* For illustration purposes only</p>
                    </div>
                    <div className="col">
                        <h1>{cardData.name}</h1>
                        <p className="cardEffect">{cardData.description}</p>
                        {/* put this table in an if statement to avoid blank tables */}
                        <h2>Sellers:</h2>
                        <table className="table table-striped">
                            <tbody>
                                {sellersData.map((product) => (
                                    <tr>
                                        <th scope="row">
                                            <a href={`/user/${product.seller_name}`}>
                                                {product.seller_name}
                                            </a>
                                        </th>
                                        <td>{product.condition}</td>
                                        <td>{product.region}</td>
                                        <td>{product.set}</td>
                                        <td>{usdFormat(product.price)}</td>
                                        <td>(PH) Buy</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                        {/* end table */}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default CardDetails;
