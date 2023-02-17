import React, {useState, useEffect} from "react"
import { useNavigate } from "react-router-dom";

import Container from "react-bootstrap/esm/Container"
import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Form from 'react-bootstrap/Form'
import Carousel from 'react-bootstrap/Carousel';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faTv, faWifi, faMusic,  faWineGlass, faCouch, faHotTub, faAirFreshener } from '@fortawesome/free-solid-svg-icons'
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Tooltip from 'react-bootstrap/Tooltip';


function App(){
  const [rooms, setRooms] = useState([])
  const [loading, setLoading] = useState(true)
  let getTomorrowsDate = ()=>{
    let tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    return tomorrow.toISOString().split("T")[0]
  }
  const [filters, setFilters] = useState({check_out:getTomorrowsDate(), check_in:new Date().toISOString().split("T")[0]})
  console.log(filters)
  let images = [{msg:"Relaxation at a beautiful peak", url:"https://images.pexels.com/photos/1134176/pexels-photo-1134176.jpeg?cs=srgb&dl=pexels-boonkong-boonpeng-1134176.jpg&fm=jpg&w=1920&h=1281"},
        {msg:"It's a home away from home.", url:"https://images.pexels.com/photos/460537/pexels-photo-460537.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},
        {msg:"Impeccable service.", url:"https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"}
    ]
  const navigate = useNavigate();

  let amenities_components = {
    tv: faTv,  
    speaker:faMusic,
    couch:faCouch,
    wifi:faWifi,
    jacuzzi:faHotTub,
    wine:faWineGlass,
    ac: faAirFreshener
  }
  
  let getRooms = async ()=>{
    try{
      const res = await fetch("/api/get-available-rooms",{
        method:"POST", 
        body:JSON.stringify(filters),
        headers: {'Content-type': 'application/json charset=UTF-8',}
      })
      const msg = await res.json()
      setRooms(msg)
      console.log(msg)
      return msg
    }
    catch(e)
      {console.log(e)}
  }

  function applyFilters(e) {
    const name = e.target.name
    const value = e.target.value
    setFilters({...filters, [name]: value})
    //getRooms()
  }


  useEffect(()=>{
    setLoading(true)
    getRooms()
    setLoading(false)
    console.log()
  }, [filters])

  if(loading) 
    return <p>loading</p>
  return(
    <Container fluid className="min-vh-100">   
      <Carousel >
          {images.map((item, idx)=>{
              return (<Carousel.Item key={idx}>
              <img
                className="d-block"
                src={item.url}
                alt={item.key}
                style={{height: "80vh", width:"100vw"}}
              />
              <Carousel.Caption className="display-3 bg-gray text-white "><span  >{item.msg}</span >     </Carousel.Caption>
            </Carousel.Item>)
          })}
        </Carousel>  
      
      <Row className="align-items-center mx-1 my-3 justify-content-center  bg-dark p-2 bg-opacity-25">
        
        <Col xs="auto">
          <Form.Label className="fs-5" htmlFor="inlineFormInput">Price above <span>₹{filters.price|| 1000}</span></Form.Label>
          <Form.Range id="price" name="price" min="1000" max="10000" defaultValue='1000' onChange={applyFilters} step='100'/>
        </Col>
        <Col xs="auto">
          <Form.Label className="fs-5" htmlFor="inlineFormInput">Room type </Form.Label>
          <Form.Select aria-label="room type" name="room_type" id="room_type" onClick={applyFilters} >
            <option value="any">Any</option>
            <option value="single">Single</option>
            <option value="double">Double</option>
            <option value="penthouse">Penthouse</option>
          </Form.Select>
        </Col>

        <Col xs="auto">
          <Form.Label className="fs-5" htmlFor="inlineFormInput">Check-in date</Form.Label>

          <Form.Control type="date"
              name="check_in"
              min={new Date().toISOString().split("T")[0]}
              max={filters.check_out ? new Date(filters.check_out).toISOString().split("T")[0]: ""}
              onChange={applyFilters}
              defaultValue={new Date().toISOString().split("T")[0]}
              required />
        </Col>

        <Col xs="auto my-3">
          <Form.Label className="fs-5" htmlFor="inlineFormInput">Check-out date</Form.Label>

          <Form.Control type="date"
              name="check_out"
              disabled={filters.check_in === "" ? true: false}
              min={getTomorrowsDate()}
              defaultValue={getTomorrowsDate()}
              onChange={applyFilters}
              required />
        </Col>
      </Row>

      <Row xs={1} md={3} lg={4} className="g-4">
        {rooms.map((room, idx) => (
          <Col>
            <Card role='button'  key={idx} onClick={() => {navigate(`/viewroom/${room._id['$oid']}`, {state:{check_in: filters.check_in, check_out: filters.check_out}})}}>
              <Card.Img variant="top" src={room.images[0]} />
              <Card.Body>
                <Card.Title className="text-capitalize">{room.title}</Card.Title>
                <Card.Text >
                  <p>Capacity: {room["capacity"]}</p>
                  <p>Amenities: 
                    {room['amenities'].map((item, idx)=>{
                      return ( 
                        <OverlayTrigger placement="bottom" overlay={<Tooltip>{item}</Tooltip>} >
                          <FontAwesomeIcon fade className='px-2'icon={amenities_components[item]} size="sm" />
                        </OverlayTrigger>)
                    })}
                  </p>
                </Card.Text>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
      {(rooms.length === 0) && <h3 className="position-absolute top-50 start-50 translate-middle">No results found</h3>}
    </Container>
  )
}
export default App