import React, { useEffect, useState } from 'react';

import axiosInstance from '../../axios';
import CardThumbnail from './CardThumbnail';

function HomePage() {
    const [cardList, setCardList] = useState([]);

    useEffect(() => {
        axiosInstance.get('on_sale/').then((res) => setCardList(res.data));
    }, []);

    return (
        <div className="container">
            <h1>Cards on sale: </h1>
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

export default HomePage;
