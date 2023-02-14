import React, {useState, useEffect} from "react"
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { useNavigate } from 'react-router-dom'

import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css'


import NavigationBar from './components/NavigationBar'
import Viewroom from "./components/Viewroom"
import Error from "./components/Error"
import Home from "./components/Home"
import Bookroom from "./components/Bookroom"
import Login from "./components/Login"
import Profile from "./components/Profile"
import Review from "./components/Review"
import Services from "./components/Services"

import Container from "react-bootstrap/esm/Container"
function App(){
    //const navigate = useNavigate();
  const [rooms, setRooms] = useState([])
//   const [discount, setDiscount] = useState(0)
  const [loading, setLoading] = useState(true)
  const [filters, setFilters] = useState({checkin: null, checkout: null , room_type:null, price:null })
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

//   let getDiscount = async ()=>{
//     try{
//       const res = await fetch('/api/loyalty-discount?id=63e52044ba29b6d46527fe8b', {method: "GET"} )
//       const msg = await res.json()
//       setDiscount(msg)
//       console.log(msg)
//     }
//     catch(e)
//       {console.log(e)}
//   }

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
    <Container fluid >
        <NavigationBar/>
        <BrowserRouter>
            <Routes>
                <Route exact path='/' element={<Home/>} />
                <Route path="/login" element={<Login/>} />
                <Route path="/profile" element={<Profile/>} />
                <Route path="/viewroom/:rid" element={<Viewroom/>} />
                <Route path="/bookroom/" element={<Bookroom />} />
                <Route path="/review/:rid" element={<Review />} />
                <Route path="/services" element={<Services />} />
                <Route path="/about" element={<About />} />
                <Route path="*" element={<Error/>} />
            </Routes>
        </BrowserRouter>
        
    </Container>
  )
}
export default App