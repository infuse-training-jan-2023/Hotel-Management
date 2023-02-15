import React from 'react';
import Container from 'react-bootstrap/esm/Container';
import Row from 'react-bootstrap/Row'
import Image from 'react-bootstrap/Image'
import Col from 'react-bootstrap/Col'
import Figure from 'react-bootstrap/Figure'
import { useNavigate } from 'react-router-dom'

function Services(){
    //const navigate = useNavigate();
    const myStyle={
        padding : '20px',
        height : '300px ',
        width :'20%',
        display: 'flex'
        
    }
    return(
        <Container className='min-vh-100 px-0'>
            <Row className='my-3'>
                <Col style={myStyle}>
                <Figure>
                <Figure.Image
                        src='https://img.freepik.com/free-photo/high-angle-wi-fi-router-with-vacuum-cleaner_23-2148779238.jpg'
                />
                <Figure.Caption className='text-center'>FREE WIFI</Figure.Caption>
                </Figure>
                </Col>

                <Col style={myStyle}>
                <Figure>
                <Figure.Image
                        src='https://images.pexels.com/photos/221457/pexels-photo-221457.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
                />
                <Figure.Caption className='text-center'>SWIMMING POOL</Figure.Caption>
                </Figure>
                </Col>

                <Col style={myStyle}>
                <Figure>
                <Figure.Image
                        src='https://img.freepik.com/free-photo/spa-composition-with-aromatherapy-body-care-items_169016-2261.jpg'
                />
                <Figure.Caption className='text-center'>SPA</Figure.Caption>
                </Figure>
                </Col>
                                
            </Row>
            <Row>
            <Col style={myStyle}>
                <Figure>
                <Figure.Image
                        src='https://img.freepik.com/free-photo/cast-iron-dumbbell-weights_1048-11523.jpg'
                />
                <Figure.Caption className='text-center'>GYM</Figure.Caption>
                </Figure>
                </Col>

                <Col style={myStyle}>
                <Figure>
                <Figure.Image
                        src='https://img.freepik.com/free-photo/parking_1127-2914.jpg'
                />
                <Figure.Caption className='text-center'>PARKING AREA</Figure.Caption>
                </Figure>
                </Col>
            </Row>
                
        </Container>

    );
}

export default Services;