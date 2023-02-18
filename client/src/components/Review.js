import React, { useState } from "react"

import { useNavigate } from "react-router-dom"
import Row from "react-bootstrap/Row"
import Button from "react-bootstrap/Button"
import Form from "react-bootstrap/Form"
import { useParams } from "react-router-dom"

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
      navigate("/profile")
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
            id="inline-radio-1"
            onChange={addReviewParams}
          />
          <Form.Check
            inline
            label="2"
            name="rating"
            type="radio"
            value="2"
            id="inline-radio-3"
            onChange={addReviewParams}
          />
          <Form.Check
            inline
            label="3"
            name="rating"
            type="radio"
            value="3"
            id="inline-radio-2"
            onChange={addReviewParams}
          />
          <Form.Check
            inline
            label="4"
            name="rating"
            type="radio"
            value="4"
            id="inline-radio-4"
            onChange={addReviewParams}
          />
          <Form.Check
            inline
            label="5"
            name="rating"
            type="radio"
            value="5"
            id="inline-radio-5"
            onChange={addReviewParams}
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
