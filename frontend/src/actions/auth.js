import {
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    USER_LOADED_SUCCESS,
    USER_LOADED_FAIL,
    AUTHENTICATED_SUCCESS,
    AUTHENTICATED_FAIL,
    LOGOUT,
} from './types';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api';

// check if there is an access token in the local storage

export const checkAuthenticated = () => async (dispatch) => {
    if (localStorage.getItem('access_token')) {
        const config = {
            headers: {
                'Content-Type': 'application/json',
                Accept: 'application/json',
            },
        };

        const body = JSON.stringify({ token: localStorage.getItem('access_token') });

        try {
            const res = await axios.post(`${API_URL}/auth/jwt/verify/`, body, config);
            if (res.data.code != 'token_not_valid') {
                dispatch({ type: AUTHENTICATED_SUCCESS });
            } else {
                dispatch({ type: AUTHENTICATED_FAIL });
            }
        } catch (err) {
            dispatch({ type: AUTHENTICATED_FAIL });
        }
    } else {
        dispatch({ type: AUTHENTICATED_FAIL });
    }
};

export const load_user = () => async (dispatch) => {
    if (localStorage.getItem('access_token')) {
        const config = {
            headers: {
                'Content-Type': 'application/json',
                Authorization: `JWT ${localStorage.getItem('access_token')}`,
                Accept: 'application/json',
            },
        };

        try {
            const res = await axios.get(`${API_URL}/auth/users/me/`, config);
            // localStorage.setItem('payload', JSON.stringify(res.data));

            dispatch({
                type: USER_LOADED_SUCCESS,
                payload: res.data,
            });
        } catch (err) {
            dispatch({
                type: USER_LOADED_FAIL,
            });
        }
    } else {
        dispatch({
            type: USER_LOADED_FAIL,
        });
    }
};

export const login = (username, password) => async (dispatch) => {
    const config = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const body = JSON.stringify({ username, password });

    try {
        const res = await axios.post(`${API_URL}/auth/jwt/create/`, body, config);

        dispatch({
            type: LOGIN_SUCCESS,
            payload: res.data,
        });

        dispatch(load_user());
    } catch (err) {
        dispatch({
            type: LOGIN_FAIL,
        });
    }
};

export const logout = () => async (dispatch) => {
    dispatch({ type: LOGOUT });
};
