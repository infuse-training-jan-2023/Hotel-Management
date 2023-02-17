import React from 'react';
import Container from 'react-bootstrap/esm/Container';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form'
import Row from 'react-bootstrap/Row'
import Image from 'react-bootstrap/Image'
import { useNavigate } from 'react-router-dom'

function Footer(){
    return (
        <div class="container">
            <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
            <span><img className='w-25 inline' src="../../hotel.png" /></span>
            <p class="col-md-4 mb-0 text-muted">&copy; 2023 The New View, Inc</p>

            <a href="/" class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
            </a>

            </footer>
        </div>
    )
}

export default Footer;