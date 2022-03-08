import React from 'react';
import { Nav, Navbar, Container } from 'react-bootstrap';
// import "./styles/Navbar.css";


function WebsiteNavbar() {
    return(
        <div>
            <Navbar bg="dark" expand="lg" variant="dark" sticky="top">
                <Container>
                    <Navbar.Brand>YGO Marketplace</Navbar.Brand>
                    <Nav>
                        <Nav.Link href="http://127.0.0.1:8000/api/card/9285">API test</Nav.Link>
                        <div className="text-light">(PH)Wishlist
                        (PH)Login</div>
                    </Nav>
                </Container>
            </Navbar>
        </div>
    )
}

export default WebsiteNavbar;