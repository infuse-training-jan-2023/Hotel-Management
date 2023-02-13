import React from 'react';
import Carousel from 'react-bootstrap/Carousel';
import Container from 'react-bootstrap/esm/Container';
import { useNavigate } from 'react-router-dom'
function Home(){
    //const navigate = useNavigate();
    let images = [{msg:"Awesome rooms", url:"https://images.pexels.com/photos/2635038/pexels-photo-2635038.jpeg?cs=srgb&dl=pexels-terry-magallanes-2635038.jpg&fm=jpg&w=1920&h=1282 "},
        {msg:"Stunning view", url:"https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281"},
        {msg:"Best service", url:"https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"}
    ]
    return(
    <Container fluid className='min-vh-100'>
      <Carousel >
        {images.map((item, idx)=>{
            return (<Carousel.Item key={idx}>
            <img
              className="d-block"
              src={item.url}
              alt={item.key}
              style={{height: "80vh", width:"100vw"}}
            />
            <Carousel.Caption>
              <h2>{item.msg}</h2>
            </Carousel.Caption>
          </Carousel.Item>)
        })}
      </Carousel>        
    </Container>  
    
    );
}

export default Home;