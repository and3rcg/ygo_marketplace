import React, { useEffect, useState } from 'react';

import axiosInstance from '../../axios';
import CardThumbnail from './CardThumbnail';

import './styles/HomePage.css';

function HomePage() {
    const [cardList, setCardList] = useState([]);

    useEffect(() => {
        axiosInstance.get('on_sale/').then((res) => setCardList(res.data));
    }, []);

    return (
        <div className="container">
            <h1>Cards on sale: </h1>
            <div className="card-list">
                {cardList.map((card) => (
                    <div className="flex-item">
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

export default HomePage;
