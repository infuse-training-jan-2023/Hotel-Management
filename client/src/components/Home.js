import React, {useState, useEffect} from "react"
import { useNavigate } from "react-router-dom";

import Container from "react-bootstrap/esm/Container"
import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Form from 'react-bootstrap/Form'
import Carousel from 'react-bootstrap/Carousel';

import placeholder from'../placeholder.png'

function App(){
  const [rooms, setRooms] = useState([])
  const [loading, setLoading] = useState(true)
  const [filters, setFilters] = useState({})
  let images = [{msg:"Awesome rooms", url:"https://images.pexels.com/photos/2635038/pexels-photo-2635038.jpeg?cs=srgb&dl=pexels-terry-magallanes-2635038.jpg&fm=jpg&w=1920&h=1282 "},
        {msg:"Stunning view", url:"https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281"},
        {msg:"Best service", url:"https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"}
    ]
  const navigate = useNavigate();
  
  let getRooms = async ()=>{
    try{
      const res = await fetch("/api/search",{
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
              <Carousel.Caption>
                <h2>{item.msg}</h2>
              </Carousel.Caption>
            </Carousel.Item>)
          })}
        </Carousel>  
      
      <Row className="align-items-center p-2 my-3 justify-content-center bg-light shadow-5">
        
        <Col xs="auto">
          <Form.Label htmlFor="inlineFormInput">Price<span>{filters.price}</span></Form.Label>
          <Form.Range id="price" name="price" min="1000" max="7000" defaultValue='1000' onChange={applyFilters} step='100'/>
        </Col>
        <Col xs="auto">
          <Form.Label htmlFor="inlineFormInput">Room type </Form.Label>
          <Form.Select aria-label="room type" name="room_type" id="room_type" onClick={applyFilters}>
            <option value="single">Single</option>
            <option value="double">Double</option>
            <option value="penthouse">Penthouse</option>
          </Form.Select>
        </Col>

        <Col xs="auto">
          <Form.Label htmlFor="inlineFormInput">Check-in date</Form.Label>

          <Form.Control type="date"
              name="check_in"
              min={new Date().toISOString().split("T")[0]}
              onChange={applyFilters}
              required />
        </Col>

        <Col xs="auto">
          <Form.Label htmlFor="inlineFormInput">Check-out date</Form.Label>

          <Form.Control type="date"
              name="check_out"
              disabled={filters.startdate === "" ? true: false}
              min={filters.startdate ? new Date(filters.startdate).toISOString().split("T")[0]: ""}
              onChange={applyFilters}
              required />
        </Col>
      </Row>
      {/* <p>{JSON.stringify(filters)}</p>   */}
      {/* <h3 className="my-3">Available Rooms</h3> */}
      <Row xs={1} md={3} lg={4} className="g-4">
        {rooms.map((room, idx) => (
          <Col>
            <Card role='button'  key={idx} onClick={() => {navigate(`/viewroom/${room._id['$oid']}`, {state:{check_in: filters.check_in, check_out: filters.check_out}})}}>
              <Card.Img variant="top" src={placeholder} />
              <Card.Body>
                <Card.Title>{room.type}</Card.Title>
                <Card.Text >
                  {/* {JSON.stringify(room)} */}
                  <h4 className="text-uppercase">{
                      room["room_type"]
                  }</h4>
                  {<p>Capacity: {room["capacity"]}</p>}
                  {
                    <p>Amenities: {room["amenities"].map(amenity => (
                      <span>{amenity}, </span>
                    ))}</p>
                  }
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