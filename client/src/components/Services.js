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
            <Row>
                <Col style={myStyle}>
                <Figure>
                <Figure.Image
                        src='https://media.istockphoto.com/id/1189884884/vector/free-electromagnetic-wave-internet-wi-fi.jpg?s=1024x1024&w=is&k=20&c=OXpWcGVeQqIzMVtNLqZkaS_NqWT0nxFcTGY6MS51fpg='
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
                        src='https://media.istockphoto.com/id/1325095289/photo/still-life-closeup-of-a-tranquil-spa-arrangement.jpg?s=612x612&w=is&k=20&c=Cf7dJPP8bxzX8e76ayb5pEDhndUSOwnKY8c_l2s2hjs='
                />
                <Figure.Caption className='text-center'>SPA</Figure.Caption>
                </Figure>
                </Col>
                                
            </Row>
            <Row>
            <Col style={myStyle}>
                <Figure>
                <Figure.Image
                        src='https://images.unsplash.com/photo-1571902943202-507ec2618e8f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1075&q=80'
                />
                <Figure.Caption className='text-center'>GYM</Figure.Caption>
                </Figure>
                </Col>

                <Col style={myStyle}>
                <Figure>
                <Figure.Image
                        src='https://media.istockphoto.com/id/871756822/photo/car-park.jpg?s=612x612&w=is&k=20&c=c92errOkGhImXTF-rw8n3sOAilbvL8fdqCFU4ddjp4Q='
                />
                <Figure.Caption className='text-center'>PARKING AREA</Figure.Caption>
                </Figure>
                </Col>
            </Row>
                
        </Container>

    );
}

export default Services;