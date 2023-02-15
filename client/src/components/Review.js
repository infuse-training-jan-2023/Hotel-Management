import React, { useState, useEffect } from 'react';

import { useNavigate } from 'react-router-dom'
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form'
import { useParams, useLocation } from 'react-router-dom'


function Review(){
    const navigate = useNavigate();
    let { bid } = useParams(); 
    let [reviewParams, setReviewParams] = useState({})

    function addReviewParams(e) {
        const name = e.target.name
        const value = e.target.value
        setReviewParams({...reviewParams, [name]: value})
    }

    let sendFeedback = async ()=>{
        try{
          alert(bid)
          let data = {...reviewParams, booking_id:bid}
          console.log(data)
          const res = await fetch(`/api/review`,{
            method:"POST", 
            body:JSON.stringify(data),
            headers: {'Content-type': 'application/json charset=UTF-8',}
          })
          const msg = await res.json()
          console.log(msg)
          navigate('/')
        }
        catch(e)
          {console.log(e)}
      }


    return(
        <Row className='vh-100 justify-content-center' >
        <Form className='w-50 mx-auto p-5 m-5'>
            <h3>How was your experience about the room?</h3>
          <Form.Group className="mb-3 align-middle" controlId="formBasicEmail" >
            <Form.Control type="text" placeholder="feedback" name="feedback" onChange={addReviewParams}/>
          </Form.Group>
            <div key='inline-radio' className="mb-3">
            <Form.Check inline label="1" name="stars" type='radio' value ='1' id='inline-radio-1' onChange={addReviewParams}/>
            <Form.Check inline label="3" name="stars" type='radio' value ='2' id='inline-radio-3' onChange={addReviewParams}/>
            <Form.Check inline label="2" name="stars" type='radio' value ='3' id='inline-radio-2' onChange={addReviewParams}/>
            <Form.Check inline label="4" name="stars" type='radio' value ='4' id='inline-radio-4' onChange={addReviewParams}/>
            <Form.Check inline label="5" name="stars" type='radio' value ='5' id='inline-radio-5' onChange={addReviewParams}/>
            </div>
          <Button variant="primary" type="submit" onClick={sendFeedback}>Add review</Button>
        </Form>
        <p>{JSON.stringify(reviewParams)}</p>
        </Row>

    );
}

export default Review