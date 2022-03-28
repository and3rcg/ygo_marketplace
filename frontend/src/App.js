import React from 'react';
import Layout from './components/Layout';
import AppRouter from './components/AppRouter';

function BaseApp() {
    return (
        <div>
            <AppRouter />
            <Layout />
        </div>
    );
}

export default BaseApp;
