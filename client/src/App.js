import React from "react"
import { BrowserRouter, Route, Routes } from "react-router-dom"

import "./App.css"
import "bootstrap/dist/css/bootstrap.min.css"

import NavigationBar from "./components/NavigationBar"
import Room from "./components/Room"
import Error from "./components/Error"
import Home from "./components/Home"
import Bookroom from "./components/Bookroom"
import Login from "./components/Login"
import Bookings from "./components/Bookings"
import Review from "./components/Review"
import Services from "./components/Services"
import About from "./components/About"

import Container from "react-bootstrap/esm/Container"
import Footer from "./components/Footer"
function App() {
  return (
    <Container fluid className="px-0">
      <NavigationBar />
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/bookings" element={<Bookings />} />
          <Route path="/room/:rid" element={<Room />} />
          <Route path="/bookroom/" element={<Bookroom />} />
          <Route path="/review/:bid" element={<Review />} />
          <Route path="/services" element={<Services />} />
          <Route path="/about" element={<About />} />
          <Route path="*" element={<Error />} />
        </Routes>
      </BrowserRouter>
      <Footer />
    </Container>
  )
}
export default App
