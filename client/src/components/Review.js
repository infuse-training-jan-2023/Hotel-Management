import React, { useState } from "react"

import { useNavigate } from "react-router-dom"
import Row from "react-bootstrap/Row"
import Button from "react-bootstrap/Button"
import Form from "react-bootstrap/Form"
import { useParams } from "react-router-dom"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faStar } from "@fortawesome/free-solid-svg-icons"
import OverlayTrigger from "react-bootstrap/OverlayTrigger"
import Tooltip from "react-bootstrap/Tooltip"

function Review() {
  const navigate = useNavigate()
  let { bid } = useParams()
  let [reviewParams, setReviewParams] = useState({})

  function addReviewParams(e) {
    const name = e.target.name
    const value = e.target.value
    setReviewParams({ ...reviewParams, [name]: value })
  }

  let postReview = async () => {
    try {
      let data = { ...reviewParams, booking_id: bid }
      const res = await fetch(`/api/review`, {
        method: "POST",
        body: JSON.stringify(data),
        headers: { "Content-type": "application/json charset=UTF-8" },
      })
      const msg = await res.json()
      navigate("/")
    } catch (e) {
      console.log(e)
    }
  }

  return (
    <Row className="vh-100 justify-content-center">
      <Form className="w-50 mx-auto p-5 m-5">
        <h3>How was your experience about the room?</h3>
        <Form.Group className="mb-3 align-middle" controlId="formBasicEmail">
          <Form.Control
            type="text"
            as="textarea"
            rows={3}
            placeholder="feedback"
            name="feedback"
            onChange={addReviewParams}
          />
        </Form.Group>
        <div key="inline-radio" className="mb-3">
          <Form.Check
            inline
            label="1"
            name="rating"
            type="radio"
            value="1"
            className="mx-2"
            id="inline-radio-1"
            onChange={addReviewParams}
          />
          <FontAwesomeIcon
            fade
            className="text-warning"
            style={{ marginRight: "20px", marginLeft: "-5px" }}
            icon={faStar}
            size="lg"
          />
          <Form.Check
            inline
            label="2"
            name="rating"
            type="radio"
            value="2"
            className="mx-2"
            id="inline-radio-3"
            onChange={addReviewParams}
          />
          <FontAwesomeIcon
            fade
            className="text-warning"
            style={{ marginRight: "20px", marginLeft: "-5px" }}
            icon={faStar}
            size="lg"
          />
          <Form.Check
            inline
            label="3"
            className="mx-2"
            name="rating"
            type="radio"
            value="3"
            id="inline-radio"
            onChange={addReviewParams}
          />
          <FontAwesomeIcon
            fade
            className="text-warning "
            icon={faStar}
            style={{ marginRight: "20px", marginLeft: "-5px" }}
            size="lg"
          />
          <Form.Check
            inline
            label="4"
            name="rating"
            type="radio"
            value="4"
            className="mx-2"
            id="inline-radio-4"
            onChange={addReviewParams}
          />
          <FontAwesomeIcon
            fade
            className="text-warning"
            style={{ marginRight: "20px", marginLeft: "-5px" }}
            icon={faStar}
            size="lg"
          />
          <Form.Check
            inline
            label="5"
            name="rating"
            type="radio"
            value="5"
            className="mx-2"
            id="inline-radio-5"
            onChange={addReviewParams}
          />
          <FontAwesomeIcon
            fade
            className="text-warning"
            style={{ marginRight: "20px", marginLeft: "-5px" }}
            icon={faStar}
            size="lg"
          />
        </div>
        <Button variant="primary" onClick={postReview}>
          Add review
        </Button>
      </Form>
    </Row>
  )
}

export default Review
