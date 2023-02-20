import React, { useState, useEffect } from "react"
import Button from "react-bootstrap/Button"
import Form from "react-bootstrap/Form"
import Row from "react-bootstrap/Row"
import { useNavigate } from "react-router-dom"

function Login() {
  const navigate = useNavigate()
  let [email, setEmail] = useState("")

  useEffect(() => {
    localStorage.setItem("email", JSON.stringify(email))
  }, [email])

  return (
    <Row className="vh-10 justify-content-center">
      <Form className="w-50 mx-auto p-5 m-5 bg-light shadow-5 text-center">
        <h3 className="text-center">LOG IN</h3>
        <Form.Group className="mb-3 align-middle" controlId="formBasicEmail">
          <Form.Control
            type="email"
            placeholder="Email"
            size={2}
            onChange={(e) => setEmail(e.target.value)}
          />
        </Form.Group>
        <Button
          variant="primary"
          type="submit"
          onClick={() => {
            navigate("/bookings")
            window.location.reload()
          }}
        >
          Login
        </Button>
      </Form>
    </Row>
  )
}

export default Login
