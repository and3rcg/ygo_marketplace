import React from 'react';
import { Nav, Navbar, Container } from 'react-bootstrap';
// import "./styles/Navbar.css";


function WebsiteNavbar() {
    return(
        <div>
            <Navbar className="container-fluid fixed-top bg-dark text-light font-weight-600">
                <Container>
                    <Navbar.Brand className="text-light">YGO Marketplace</Navbar.Brand>
                    <Nav>
                        <Nav.Link href="http://127.0.0.1:8000/api/card/9285"  className="text-light">API test</Nav.Link>
                        <div className="text-light">(PH)Wishlist
                        (PH)Login</div>
                    </Nav>
                </Container>
            </Navbar>
        </div>
    )
}

export default WebsiteNavbar;