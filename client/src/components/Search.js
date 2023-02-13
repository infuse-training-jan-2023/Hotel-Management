import React, {useState, useEffect} from "react"
import { useNavigate } from "react-router-dom";

import Container from "react-bootstrap/esm/Container"
import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Form from 'react-bootstrap/Form'
import placeholder from'../placeholder.png'

function App(){
  const [rooms, setRooms] = useState([])
  const [discount, setDiscount] = useState(0)
  const [loading, setLoading] = useState(true)
  const [filters, setFilters] = useState({})
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
      <h3 className="my-3">Filter</h3>
      <Row className="align-items-center border border-secondary rounded p-2 my-3 justify-content-center">
        
        <Col xs="auto">
          <Form.Label htmlFor="inlineFormInput">Price above <span>{filters.price}</span></Form.Label>
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
      <p>{JSON.stringify(filters)}</p>  

      <Row xs={1} md={3} lg={4} className="g-4">
        {rooms.map((room, idx) => (
          <Col>
            <Card role='button'  key={idx} onClick={() => {navigate(`/viewroom/${room._id['$oid']}`, {state:{check_in: filters.checkin, check_out: filters.checkout}})}}>
              <Card.Img variant="top" src={placeholder} />
              <Card.Body>
                <Card.Title>{room.type}</Card.Title>
                <Card.Text>
                  {JSON.stringify(room)}
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