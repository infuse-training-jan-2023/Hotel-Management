import React, {useState, useEffect} from "react"

import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

function NavigationBar() {
  let [uid, setUid] = useState('')
  let [email, setEmail] = useState('')

  useEffect(()=>{
    const email = JSON.parse(localStorage.getItem('email'));
    console.log(email)
    if (email) 
      setEmail(email);
        
  }, [])

  return (
    <Navbar collapseOnSelect expand="lg" bg="dark" variant='dark'>
      <Container>
        <Navbar.Brand href="/" className="fst-italic fw-bold">THE NEW VIEW</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto">
  
           
          </Nav>
          <Nav>
            <Nav.Link href="/about" >About Us</Nav.Link>
            <Nav.Link href='/services'>Services</Nav.Link>
          </Nav>
          <Nav className="fs-5">
            {email ? <Nav.Link href="/profile">Profile</Nav.Link> : <Nav.Link href="/login">Login</Nav.Link>}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavigationBar;