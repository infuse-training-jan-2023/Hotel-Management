import React, { useEffect, useState } from 'react';
import { useParams, useLocation, useNavigate } from 'react-router-dom'
import Button from 'react-bootstrap/esm/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Container from 'react-bootstrap/esm/Container';
import Form from 'react-bootstrap/Form'

function Bookroom(){
    const navigate = useNavigate();
    const location = useLocation(); 
    const [uid, setUid] = useState('')
    const [checkin, setCheckin] = useState(0)
    const [checkout, setCheckout] = useState(0)
    const [rid, setRid] = useState(0)
    const [addons, setAddons] = useState([])
    const [discount, setDiscount] = useState(0)
    const [select_addons, setSelectAddons] = useState([])
    let performBooking = async ()=>{
        try{

            console.log(`uid: ${uid} rid:${rid} start: ${checkin} end: ${checkout}`)

            let data = {room_id:rid, user_id: uid, checkin: checkin, checkout: checkout, addons: select_addons}
            const res = await fetch(`/api/booking`,{
                method:"POST", 
                body:JSON.stringify(data),
                headers: {'Content-type': 'application/json charset=UTF-8',}
            })
            const msg = await res.json()
            console.log(msg)
            navigate('/profile')
          }
          catch(e)
            {console.log(e)}
    }

    let getAddons = async ()=>{
        try{
            // const res = await fetch(`/api/addons`)
            // const msg = await res.json()
            const msg=[{name:'swimming pool', cost:300}, {name:'gym', cost:200}, {name:'sauna', cost:500}]
            console.log(msg)
            setAddons(msg)
        }
        catch(e)
            {console.log(e)}
    }

    function addAddons(e) {
        const idx = e.target.name
        setSelectAddons(arr => [...arr, addons[idx]])
    }

    let getDiscount = async ()=>{
        try{
        const res = await fetch('/api/loyalty-discount?id=63e670f601343886816b44c7', {method: "GET"} )
        const msg = await res.json()
        setDiscount(msg)
        console.log(msg)
        }
        catch(e)
        {console.log(e)}
    }

    useEffect(()=>{
        const uid = JSON.parse(localStorage.getItem('uid'));
        console.log(uid)
        if (uid) 
            setUid(uid);
        console.log(`uid: ${uid} rid:${rid} start: ${location.statecheckin} end: ${location.state.checkout}`)
        setCheckin(location.state.checkin);
        setCheckout(location.state.checkout);
        setRid(location.state.room_id);
        getAddons()
        getDiscount()
    },[])

    return(
        <Container className='min-vh-100'>

            <Row className="align-items-center border border-secondary rounded p-2 my-3 justify-content-center">
            <h4>Booking details</h4>
            <Col xs="auto">
            <Form.Label htmlFor="inlineFormInput">Check-in date</Form.Label>
                <Form.Control type="date"
                    name="checkin"
                    min={new Date().toISOString().split("T")[0]}
                    onChange={(e)=>setCheckin(e.target.value)}
                    defaultValue={checkin}
                    required />
            </Col>
            <Col xs="auto">
            <Form.Label htmlFor="inlineFormInput">Check-out date</Form.Label>
                <Form.Control type="date"
                    name="checkout"
                    disabled={checkin === "" ? true: false}
                    min={checkin ? new Date(checkin).toISOString().split("T")[0]: ""}
                    onChange={(e)=>setCheckout(e.target.value)}
                    defaultValue={checkout}
                    required />
            </Col>
            <Col xs="auto">
                <Form.Label htmlFor="inlineFormInput">Add-ons</Form.Label>
                {addons.map((item, idx)=>{
                    return <p><Form.Check inline key={idx} label={item.name} name={idx} type='checkbox'  id='radio-{idx}' onChange={addAddons}/> <span>₹{item.cost}</span></p>
                })}
            </Col>
        </Row>

        <Row className="align-items-center border border-secondary rounded p-2 my-3">
            <h4>Guest details</h4>
            <Col xs="auto">
                <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                    <Form.Label>Name</Form.Label>
                    <Form.Control type="text" placeholder="name" />
                </Form.Group>
            </Col>
            <Col xs="auto">
                <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                    <Form.Label>Email</Form.Label>
                    <Form.Control type="email" placeholder="name@example.com" />
                </Form.Group>
            </Col>
            <Col xs="auto">
                <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                    <Form.Label>Phone number</Form.Label>
                    <Form.Control type="phone" placeholder="985xxx2358" />
                </Form.Group>
            </Col>
            <Col xs="auto">
                <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                    <Form.Label>Special request</Form.Label>
                    <Form.Control type="text" placeholder="any special needs" />
                </Form.Group>
            </Col>
        </Row>

        <Row className="align-items-center border border-secondary rounded p-2 my-3">
        <h4>Payment details</h4>
            <Col xs="auto">
                <p><span>Total amount:</span></p>
                <p><span>Discount(if applicable):</span>{discount}</p> 
                <p><span>Grand total:</span></p>
                <Button onClick={performBooking}>Confirm booking</Button>
            </Col>  
        </Row>
        </Container>
    );
}

export default Bookroom