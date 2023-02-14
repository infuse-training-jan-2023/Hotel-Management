import React, {useState, useEffect} from "react"

import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

function NavigationBar() {
  let [uid, setUid] = useState('')

  useEffect(()=>{
    const uid = JSON.parse(localStorage.getItem('uid'));
    console.log(uid)
    if (uid) 
      setUid(uid);
        
  }, [])

  return (
    <Navbar collapseOnSelect expand="lg" bg="dark" variant='dark'>
      <Container>
        <Navbar.Brand href="/">Hotel management</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href='/services'>Services</Nav.Link>
            <Nav.Link href="/search" >About us</Nav.Link>
          </Nav>
          <Nav>
            {uid ? <Nav.Link href="/profile">Profile</Nav.Link> : <Nav.Link href="/login">Login</Nav.Link>}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavigationBar;