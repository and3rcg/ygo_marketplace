import React, { useState, useEffect } from 'react';
import { Modal, Button } from 'react-bootstrap';

import axiosInstance from '../../axios';

function OrderCardModal(props) {
    const [show, setShow] = useState(false);
    const [cardData, setCardData] = useState({});
    const [amount, setAmount] = useState(1);

    const handleShow = () => setShow(true);
    const handleClose = () => setShow(false);
    // TODO: put a spinner in handleOrder to wait for a 201 response by the API
    // const handleOrder = () => setShow(false);
    const handleAmountChange = (event) => setAmount(event.target.value);

    // API request:
    // TODO: make a function to DRY the auth'd API calls!
    const API_URL = 'http://127.0.0.1:8000/api';

    useEffect(() => {
        axiosInstance
            .get(`${API_URL}/on_sale/${props.id}`)
            .then((response) => setCardData(response.data));
    }, []);

    const handleOrder = (event) => {
        event.preventDefault();
        axiosInstance
            .post(`${API_URL}/on_sale/${props.id}/add_to_cart/`, { amount: amount })
            .then((response) => console.log(response));
    };

    return (
        <div>
            <Button variant="primary" onClick={handleShow}>
                Order
            </Button>

            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Confirm order</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <h2>{cardData.card_name}</h2>
                    <h3>Select amount to order:</h3>
                    {/* TODO: add onSubmit={handleOrder} to the form tag in the JSX below */}
                    <form onSubmit={handleOrder}>
                        <div className="form-group">
                            <label>
                                <input type="number" onChange={handleAmountChange} value={amount} />
                            </label>
                        </div>
                        ({cardData.amount} left)
                        <h3>Total price: USD {amount * cardData.price}</h3>
                        <Modal.Footer>
                            <Button variant="primary" type="submit">
                                Add to cart
                            </Button>
                        </Modal.Footer>
                    </form>
                </Modal.Body>
            </Modal>
        </div>
    );
}

export default OrderCardModal;
