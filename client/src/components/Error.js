import React from "react"

import { useNavigate } from "react-router-dom"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faExclamationTriangle } from "@fortawesome/free-solid-svg-icons"
import Button from "react-bootstrap/Button"
import Row from "react-bootstrap/esm/Row"

function Error() {
  const navigate = useNavigate()

  return (
    <Row className="w-50 mx-auto py-5 my-5 text-center">
      <FontAwesomeIcon
        className="text-warning"
        icon={faExclamationTriangle}
        size="5x"
        beatFade
      />
      <div className="display-6 my-5">Unable to find page</div>
      <Button onClick={() => navigate("/")}>Go to home page</Button>
    </Row>
  )
}

export default Error
