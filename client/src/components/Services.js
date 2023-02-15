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
        <div style={{backgroundColor : '#f4f6f6', height : '900px',padding :'40px'}}>
        <Container className='min-vh-120'>
            <Row>
                <h2 className='text-center fst-italic' style={{paddingBottom:'20px'}}>Services & Add Ons</h2>
            </Row>
            <Row>
                <Col style={myStyle}>
                <Figure>
                <Figure.Image style={{height :'90%'}}
                        src='https://cdn.pixabay.com/photo/2021/03/27/12/32/free-wifi-icon-6128369_1280.png'
                />
                <Figure.Caption className='text-center fs-5'>Free WIFI</Figure.Caption>
                </Figure>
                </Col>

                <Col style={myStyle}>
                <Figure>
                <Figure.Image style={{height :'90%'}}
                        src='https://images.pexels.com/photos/221457/pexels-photo-221457.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
                />
                <Figure.Caption className='text-center fs-5'>Swimming Pool</Figure.Caption>
                </Figure>
                </Col>

                <Col style={myStyle}>
                <Figure>
                <Figure.Image style={{height :'90%'}}   
                        src='https://img.freepik.com/free-photo/spa-concept-beauty-fashion-concept-with-spa-set-perfumed-flowers-water-relaxation-zen-spa-setting-flat-lay-with-bowl-bath-salt-flowers-towel-natural-soap-top-view_1150-44593.jpg?w=1060&t=st=1676443664~exp=1676444264~hmac=154dfa4d23baebc76473c171c722bcf11d0aae304c374b536e5a552fe8c948a3'
                />
                <Figure.Caption className='text-center fs-5'>Spa & Wellness Center</Figure.Caption>
                </Figure>
                </Col>
                                
            </Row>
            <Row>
            <Col style={myStyle}>
                <Figure>
                <Figure.Image 
                        src='https://images.unsplash.com/photo-1571902943202-507ec2618e8f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1075&q=80'
                />
                <Figure.Caption className='text-center fs-5'>Gym & Fitness Studio</Figure.Caption>
                </Figure>
                </Col>

                <Col style={myStyle}>
                <Figure>
                <Figure.Image style={{height :'135%'}}
                        src='https://images.unsplash.com/photo-1506521781263-d8422e82f27a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80'
                />
                <Figure.Caption className='text-center fs-5'>Parking Area</Figure.Caption>
                </Figure>
                </Col>
            </Row>
                
        </Container>
        </div>   

    );
}

export default Services;