import React, { useEffect } from 'react';
import { connect } from 'react-redux';

//
import { checkAuthenticated, load_user } from '../actions/auth';

// layout components
import Navbar from './layout/Navbar';
import WebsiteFooter from './layout/Footer';

const Layout = (props) => {
    useEffect(() => {
        props.checkAuthenticated();
        props.load_user();
    });

    return (
        <div>
            <Navbar />
            <WebsiteFooter />
            {props.children}
        </div>
    );
};

export default connect(null, { checkAuthenticated, load_user })(Layout);
