import React, {useState, useEffect} from 'react';
import Card from 'react-bootstrap/Card';
import Button  from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import { useNavigate } from 'react-router-dom'
import Container from 'react-bootstrap/esm/Container';
function Profile(){
    const navigate = useNavigate();
    let [uid, setUid] = useState(JSON.parse(localStorage.getItem('uid')))
    let downloadInvoice = async ()=> {
        console.log('get bill')
    }

    let handleLogout = () => {
        setUid('')
        localStorage.removeItem('uid');
        navigate('/')
        window.location.reload()
    }

    return(
        <Container className="min-vh-100">
            <Row className='my-2'>
                <Col xs={10}><h3>Bookings</h3></Col>
                <Col xs={2} ><Button variant="danger" onClick={handleLogout}>Logout</Button></Col>
            
            <h4>Current booking</h4>
            </Row>
            {
                <Card  className='my-2' height="2rem">
                    <Card.Body>
                        <Row>
                            <Col sm={10}>
                                <Card.Title>room_type</Card.Title>
                                <Card.Text>checkin checkout</Card.Text>
                            </Col>
                           <Col ><Button variant="danger" className='my-3' onClick={downloadInvoice}>Cancel</Button></Col>
                           <Col ><Button className='my-3' onClick={downloadInvoice}>Invoice</Button></Col>
                            
                        </Row>
                        
                    </Card.Body>
                </Card>
            }
            <hr/>
            <h4>Past bookings</h4>
            {
                <Card  className='my-2' height="2rem">
                    <Card.Body>
                        <Row>
                            <Col sm={10}>
                                <Card.Title>room_type</Card.Title>
                                <Card.Text>checkin checkout</Card.Text>
                            </Col>
                           <Col ><Button variant="info" className='my-3' onClick={downloadInvoice}>Review</Button></Col>
                           <Col ><Button className='my-3' onClick={downloadInvoice}>Invoice</Button></Col>
                        </Row>
                        
                    </Card.Body>
                </Card>
            }
        </Container>
    );
}

export default Profile;