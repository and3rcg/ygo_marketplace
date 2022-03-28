import React, { Fragment } from 'react';
import { Nav, Navbar, Container } from 'react-bootstrap';
import { connect } from 'react-redux';

import { logout } from '../../actions/auth';

const WebsiteNavbar = ({ logout, isAuthenticated }) => {
    const guestLinks = () => (
        <Fragment>
            <li className="nav-item">
                <Nav.Link className="nav-link text-light" href="/login">
                    Login
                </Nav.Link>
            </li>
            <li className="nav-item">
                <Nav.Link className="nav-link text-light" href="/signup">
                    Sign Up
                </Nav.Link>
            </li>
        </Fragment>
    );

    const authLinks = () => (
        <li className="nav-item">
            <a className="nav-link text-light" href="/" onClick={logout}>
                Logout
            </a>
        </li>
    );

    return (
        <div>
            <Navbar className="container-fluid fixed-top bg-dark text-light font-weight-600">
                <Container>
                    <Nav.Link href="/" className="text-light">
                        YGO Marketplace
                    </Nav.Link>
                    <Nav>
                        <Nav.Link href="http://127.0.0.1:8000/api/card/9285" className="text-light">
                            API test
                        </Nav.Link>
                        <Nav.Link className="text-light" href="/detail/9284">
                            Card test
                        </Nav.Link>
                        {isAuthenticated ? authLinks() : guestLinks()}
                        <div className="text-light">(PH)Wishlist</div>
                    </Nav>
                </Container>
            </Navbar>
        </div>
    );
};

const mapStateToProps = (state) => ({
    isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { logout })(WebsiteNavbar);
