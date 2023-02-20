import React, { useState, useEffect } from "react"

import Container from "react-bootstrap/esm/Container"
import Card from "react-bootstrap/Card"
import Col from "react-bootstrap/Col"
import Row from "react-bootstrap/Row"
import Figure from "react-bootstrap/Figure"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import {
  faTv,
  faWifi,
  faMusic,
  faWineGlass,
  faCouch,
  faHotTub,
  faAirFreshener,
} from "@fortawesome/free-solid-svg-icons"
import OverlayTrigger from "react-bootstrap/OverlayTrigger"
import Tooltip from "react-bootstrap/Tooltip"

function App() {
  const [rooms, setRooms] = useState([])
  const [loading, setLoading] = useState(true)

  const myStyle = {
    padding: "50px",
    height: "300px ",
    width: "20%",
    display: "flex",
  }
  let amenities_components = {
    tv: faTv,
    speaker: faMusic,
    couch: faCouch,
    wifi: faWifi,
    jacuzzi: faHotTub,
    wine: faWineGlass,
    ac: faAirFreshener,
  }

  let getAllRooms = async () => {
    try {
      const res = await fetch("/api/rooms")
      const roomsData = await res.json()
      setRooms(roomsData)
      return roomsData
    } catch (e) {
      console.log(e)
    }
  }

  useEffect(() => {
    setLoading(true)
    getAllRooms()
    setLoading(false)
  }, [])

  if (loading) return <p>loading</p>
  return (
    <Container fluid>
      <div className="fs-3 text-center font-weight-bold my-3">
        Variety of rooms
      </div>
      <Row xs={1} md={3} lg={4} className="g-4 mx-3">
        {rooms.map((room, idx) => (
          <Col>
            <Card key={idx}>
              <Card.Img variant="top" src={room.images[0]} />
              <Card.Body>
                <Card.Title className="text-capitalize">
                  {room.title}
                </Card.Title>
                <Card.Text>
                  <p>Capacity: {room["capacity"]}</p>
                  <p>Price: ₹{room["price"]}</p>
                  <p>
                    Amenities:
                    {room["amenities"].map((item, idx) => {
                      return (
                        <OverlayTrigger
                          placement="bottom"
                          overlay={<Tooltip>{item}</Tooltip>}
                        >
                          <FontAwesomeIcon
                            fade
                            className="px-2"
                            icon={amenities_components[item]}
                            size="sm"
                          />
                        </OverlayTrigger>
                      )
                    })}
                  </p>
                </Card.Text>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
      {rooms.length === 0 && (
        <h3 className="position-absolute top-50 start-50 translate-middle">
          No results found
        </h3>
      )}
      <Container>
        <div className="fs-3 text-center font-weight-bold my-3">
          Other services
        </div>
        <Row>
          <Col style={myStyle}>
            <Figure>
              <Figure.Image src="https://img.freepik.com/free-photo/high-angle-wi-fi-router-with-vacuum-cleaner_23-2148779238.jpg" />
              <Figure.Caption className="text-center fs-5">
                Free WIFI
              </Figure.Caption>
            </Figure>
          </Col>

          <Col style={myStyle}>
            <Figure>
              <Figure.Image
                style={{ height: "125%", width: "100%" }}
                src="https://images.pexels.com/photos/221457/pexels-photo-221457.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
              />
              <Figure.Caption className="text-center fs-5">
                Swimming Pool
              </Figure.Caption>
            </Figure>
          </Col>

          <Col style={myStyle}>
            <Figure>
              <Figure.Image src="https://img.freepik.com/free-photo/spa-composition-with-aromatherapy-body-care-items_169016-2261.jpg" />
              <Figure.Caption className="text-center fs-5">
                Spa & Wellness Center
              </Figure.Caption>
            </Figure>
          </Col>
        </Row>
        <Row>
          <Col style={myStyle}>
            <Figure>
              <Figure.Image src="https://img.freepik.com/free-photo/cast-iron-dumbbell-weights_1048-11523.jpg" />
              <Figure.Caption className="text-center fs-5">
                Gym & Fitness Studio
              </Figure.Caption>
            </Figure>
          </Col>

          <Col style={myStyle}>
            <Figure>
              <Figure.Image src="https://img.freepik.com/free-photo/parking_1127-2914.jpg" />
              <Figure.Caption className="text-center fs-5">
                Parking Area
              </Figure.Caption>
            </Figure>
          </Col>
        </Row>
      </Container>
    </Container>
  )
}
export default App
