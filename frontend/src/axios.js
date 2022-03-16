import axios from 'axios';

const baseURL = 'localhost:8000/api/'  // API url

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const axiosInstance = axios.create({
  baseURL: baseURL,
  timeout: 3000, // timeout in ms to avoid system hanging
  headers: {
      // ternary operator (inline conditional)
      Authorization: localStorage.getItem('access_token') ? 'JWT ' + localStorage.getItem('access_token') : null,
      'content-type': 'application/json',
      accept:'application/json',
      "X-CSRFToken":'eloo',
  },
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken',
});

export default axiosInstance