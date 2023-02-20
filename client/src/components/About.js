import React from "react"
import Container from "react-bootstrap/esm/Container"
import Row from "react-bootstrap/Row"
import Image from "react-bootstrap/Image"

function About() {
  return (
    <Container className="min-vh-100 my-2">
      <Row>
        <Image
          src="https://r2imghtlak.mmtcdn.com/r2-mmt-htl-image/htl-imgs/202103161731226897-549d5be89b9a11ec8bdd0a58a9feac02.jpg?&output-quality=75&downsize=520:350&crop=520:350;2,0&output-format=jpg&downsize=821:550&crop=821:550"
          width="100%"
        ></Image>
      </Row>

      <div>
        <h5>Our Story</h5>
        <p>
          Our journey began in 1985, with a simple goal of providing a relaxing
          space for travellers. But with time, with everyone's support we are
          where we are today. We at THE NEW VIEW hotels are committed to
          providing our guests with best in class services in the industry.
          Acknowledged and praised, we aspire to continously improve experiences
          of the guests that stay with us.
        </p>
      </div>

      <div>
        <h5>Contact Us</h5>
        <p>
          <ul>
            <li>Proprietor : John Doe</li>
            <li>Phone No.: 9842252248</li>
            <li>Email : thenewview@gmail.com</li>
          </ul>
        </p>
      </div>
    </Container>
  )
}

export default About
