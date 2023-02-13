import Container from 'react-bootstrap/esm/Container';
import { useParams, useLocation, useNavigate } from 'react-router-dom'
import React, {useState, useEffect, useId} from "react"
import Carousel from 'react-bootstrap/Carousel';

import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Form from 'react-bootstrap/Form'
import Badge from 'react-bootstrap/Badge';
import Card from 'react-bootstrap/Card';
import '../App.css'
import Button  from 'react-bootstrap/Button';
function Viewroom(){
    const navigate = useNavigate();
    let { rid } = useParams(); 
    const location = useLocation(); 
    const [room, setRoom] = useState({})
    const [loading, setLoading] = useState(true)
    const [reviews, setReviews] = useState([])
    const [images, setImgs] = useState([])
    const [amenities, setAmenities] = useState([])
    const [check_in, setCheckin] = useState(0)
    const [check_out, setCheckout] = useState(0)
    let getRoom = async ()=>{
        try{
          const res = await fetch(`/api/room?room_id=${rid}`)
          const msg = await res.json()
          setRoom(msg)
          setAmenities(msg.amenities)
          setImgs(msg.images)
          return msg
        }
        catch(e)
          {console.log(e)}
      }

    let getRoomReviews = async ()=>{
        try{
          //const res = await fetch(`/api/reviews/${rid}`)
          //const msg = await res.json()
          let  msg=[{customer_name:"bob", rating: 4, feedback: "good service"}, {customer_name:"harry", rating: 5, feedback: "luxurious stay"}, {customer_name:"tom", rating: 2, feedback: "expensive"}]
          setReviews(msg)
        }
        catch(e)
          {console.log(e)}
      }
      useEffect(()=>{
        setLoading(true)
        setCheckin(location.state.check_in);
        setCheckout(location.state.check_out);
        getRoom()
        getRoomReviews()
        setLoading(false)
      }, [])


    if(loading) 
      return <p>loading</p>
    return(
        <Container className='min-vh-100'>
            <Row xs={1} lg={2} className="g-4 py-2">
            
            <Col>
            <Carousel >
                {images.map((item, idx)=>{
                    return (<Carousel.Item key={idx}>
                    <img
                    className="d-block"
                    src={item}
                    alt={idx}
                    style={{height: "80vh"}}
                    />
                    <Carousel.Caption>
                    <h2>{item.msg}</h2>
                    </Carousel.Caption>
                </Carousel.Item>)
                })}
            </Carousel> 
            </Col>
            <Col>
                <h3>{room.type}</h3>
                <p><span>Room price: </span>{room.price}</p>
                <p><span>Room capacity: </span>{room.capacity}</p>
                <p><span>Amenities: </span>
                    {amenities.map((item, idx)=><><Badge key={idx} bg="info">{item} </Badge><span> </span></>)}
                </p>
                <Button className='my-3' onClick={() => {navigate("/bookroom", {state:{room_id:rid, check_in: check_in, check_out: check_out}})}}>Book now</Button>
                    
                <h5>Reviews</h5>
                {
                    reviews.map((item, idx)=>{
                        return(
                            <Card  key={idx} className='my-2'>
                                <Card.Body>
                                    <Card.Title>{item.customer_name}</Card.Title>
                                    <Card.Subtitle className="mb-2 text-muted">{item.rating}<span> stars</span></Card.Subtitle>
                                    <Card.Text>{item.feedback}</Card.Text>
                                </Card.Body>
                            </Card>
                        )
                    })   
                    
                }
            </Col>
        </Row>
        </Container>

    );
}

export default Viewroom