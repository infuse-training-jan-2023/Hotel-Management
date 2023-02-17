import React, {useState, useEffect} from "react"
import { useNavigate } from "react-router-dom";

import Container from "react-bootstrap/esm/Container"
import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faTv, faWifi, faMusic,  faWineGlass, faCouch, faHotTub, faAirFreshener } from '@fortawesome/free-solid-svg-icons'
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Tooltip from 'react-bootstrap/Tooltip';
import placeholder from'../placeholder.png'



function App(){
  const [rooms, setRooms] = useState([])
  const [loading, setLoading] = useState(true)

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
      const res = await fetch("/api/get-all-rooms")
      const msg = await res.json()
      setRooms(msg)
      console.log(msg)
      return msg
    }
    catch(e)
      {console.log(e)}
  }



  useEffect(()=>{
    setLoading(true)
    getRooms()
    setLoading(false)
    console.log()
  }, [])

  if(loading) 
    return <p>loading</p>
  return(
    <Container fluid >   
    <div className='fs-3 text-center font-weight-bold my-3'>Variety of rooms</div>
      <Row xs={1} md={3} lg={4} className="g-4 mx-3">
        {rooms.map((room, idx) => (
          <Col>
            <Card  key={idx}>
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