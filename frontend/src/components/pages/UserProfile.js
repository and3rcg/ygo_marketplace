import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import axiosInstance from '../../axios';

import CardThumbnail from './CardThumbnail';

const API_URL = 'http://127.0.0.1:8000/api';

function UserProfile() {
    let { username } = useParams();
    const [cardList, setCardList] = useState([]);

    useEffect(() => {
        axiosInstance
            .get(`${API_URL}/on_sale/?username=${username}`)
            .then((res) => setCardList(res.data));
    }, []);

    return (
        <div className="container">
            <h1>Cards on sale: {username}</h1>
            <div className="row">
                {cardList.map((card) => (
                    <div className="col">
                        <CardThumbnail
                            name={card.card_name}
                            price={card.price}
                            image={card.img}
                            id={card.card}
                            amount={card.amount}
                        />
                    </div>
                ))}
            </div>
        </div>
    );
}

export default UserProfile;
