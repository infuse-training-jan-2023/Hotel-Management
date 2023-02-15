import Container from 'react-bootstrap/esm/Container';
import { useParams, useLocation, useNavigate } from 'react-router-dom'
import React, {useState, useEffect, useId} from "react"
import Carousel from 'react-bootstrap/Carousel';
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Tooltip from 'react-bootstrap/Tooltip';

import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Form from 'react-bootstrap/Form'
import Badge from 'react-bootstrap/Badge';
import Card from 'react-bootstrap/Card';
import '../App.css'
import Button  from 'react-bootstrap/Button';

import ReactDOM from 'react-dom'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faStar, faTv, faWifi,  faMusic, faWineGlass, faCouch, faHotTub, faAirFreshener } from '@fortawesome/free-solid-svg-icons'


// library.add(faBatteryHalf, faBatteryFull, faPrint);

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
          const res = await fetch(`/api/rooms?room_id=${rid}`)
          const msg = await res.json()
          setRoom(msg)
          setAmenities(msg.amenities)
          setImgs(msg.images)
          return msg
        }
        catch(e)
          {console.log(e)}
    }

    let amenities_components = {
      tv: faTv,  
      speaker:faMusic,
      couch:faCouch,
      wifi:faWifi,
      jacuzzi:faHotTub,
      wine:faWineGlass,
      ac: faAirFreshener
    }

    let getRoomReviews = async ()=>{
        try{
          const res = await fetch(`/api/reviews_of_room?room_id=${rid}`)
          const msg = await res.json()
          setReviews(msg)
        }
        catch(e)
          {console.log(e)}
      }
      useEffect(()=>{
        setLoading(true)
        setCheckin(location.state.check_in || Date.now());
        setCheckout(location.state.check_out || Date.now());
        getRoom()
        getRoomReviews()
        setLoading(false)
      }, [])


    if(loading) 
      return <p>loading</p>
    return(
        <Container className='min-vh-120'>
            <Row xs={1} lg={2} className="g-4 py-2">
            <Col>
            <Carousel >
                {images.map((item, idx)=>{
                    return (<Carousel.Item key={idx}>
                    <img
                    className="d-block"
                    src={item}
                    alt={idx}
                    style={{height: "90vh"}}
                    />
                </Carousel.Item>)
                })}
            </Carousel> 
            </Col>
            <Col>
                <p className="fs-3 text-capitalize"> {room.room_type} room </p>
                <p className='fs-6'> <span>Room price:</span> Rs. {room.price}/-</p>
                <p className='fs-6'> <span>Room capacity: </span> {room.capacity}</p>
                <p className='fs-6'> <span>Amenities: </span> 
                    {amenities.map((item, idx)=>{
                      return ( 
                        <OverlayTrigger placement="bottom" overlay={<Tooltip>{item}</Tooltip>} >
                          <FontAwesomeIcon fade className='px-2'icon={amenities_components[item]} size="lg" />
                        </OverlayTrigger>)
                    })
                    }
                </p>
                <p>{room.description}</p>
                <Button className='my-3 btn-lg btn-success' onClick={() => {navigate("/bookroom", {state:{room_id:rid, check_in: check_in, check_out: check_out, room_price:room.price}})}}>Book now</Button>
                    
                <p className='fs-4 '>Reviews</p>
                {
                    reviews.map((item, idx)=>{
                        return(
                            <Card  key={idx} className='my-2 bg-light shadow-5'>
                                <Card.Body>
                                    <Card.Title>{item.guest_name}</Card.Title>
                                    <Card.Subtitle className="mb-2 text-muted">

                                      {
                                        [...Array(item.rating)].map((e, i) => <FontAwesomeIcon className='text-warning' icon={faStar} />)
                                      }

                                    </Card.Subtitle>
                                    <Card.Text className='fw-lighter'>{item.feedback}</Card.Text>
                                </Card.Body>
                            </Card>
                        )
                    })   
                    
                }
                {!reviews.length && <p>No reviews to show</p>}
            </Col>
        </Row>
        </Container>

    );
}

export default Viewroom