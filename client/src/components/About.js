import React from 'react';
import Container from 'react-bootstrap/esm/Container';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form'
import Row from 'react-bootstrap/Row'
import Image from 'react-bootstrap/Image'
import { useNavigate } from 'react-router-dom'

function About(){
    const myStyle={
        marginTop:'40px',
        width : '80%',
        display : 'flex',
        alignItems : 'center',
        padding : '10px',
        justifyContent : 'space-between',
        flexWrap :'wrap'
    }
    return(
       
        <Container className='min-vh-100'>   
        <Row> 
           <Image src="https://static01.nyt.com/images/2019/07/21/travel/29checkin-vancouver1/17f45183dc304c8a80697200b69b45a9-articleLarge.jpg?quality=75&auto=webp&disable=upscale" width='100%'></Image>
         
        </Row>
        
            <div style={myStyle}>
            <h5>Our Story</h5>    
            <p >
                Our journey began in 1985, with a simple goal of providing a relaxing space for travellers. But with time, with everyone's support we are where we are today.
                We at THE NEW VIEW hotels are committed to providing our guests with best in class services in the industry. Acknowledged and praised, we aspire to continously improve experiences of the guests that stay with us.
            </p>
            </div>

            <div>
            <h5>Contact Us</h5>    
            <p >
                <ul>
                    <li>Proprietor : John Doe</li>
                    <li>Phone No.: 9842252248</li>
                    <li>Email : thenewview@gmail.com</li>
                </ul>  
            </p>
            </div>
     
      
        </Container>

    );
}

export default About;