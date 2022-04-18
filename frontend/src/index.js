import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';

import BaseApp from './App';
import store from './store';

// The index.js can be used to put "static" components of the website, such as header, footer,
// navbar, etc. Elements placed inside of a Route component will be rendered alongside any other
// "static" elements outside of the Router

const myElement = (
    <Provider store={store}>
        <div>
            <BaseApp />
            
        </div>
    </Provider>
);

ReactDOM.render(myElement, document.getElementById('app'));
