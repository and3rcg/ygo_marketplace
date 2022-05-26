import React from 'react';
import './styles/CardThumbnail.css';

function CardThumbnail(props) {
    const usdFormat = (value) => {
        return `US$ ${parseFloat(value).toFixed(2)}`;
    };
    return (
        <div className="flex-col">
            <div className="card">
                <a href={`/detail/${props.id}`}>
                    <img className="img-thumbnail height:auto" src={props.image} alt={props.name} />
                </a>
                <div className="card-body row">
                    <h5 className="card-name">{props.name}</h5>
                    <p>
                        Starting at:{' '}
                        <span className="price fw-bolder">{usdFormat(props.price)}</span>
                    </p>
                    <p className="">{props.amount} left</p>
                </div>
            </div>
        </div>
    );
}

export default CardThumbnail;
