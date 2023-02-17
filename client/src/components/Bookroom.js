import React, { useEffect, useState } from 'react';
import { useParams, useLocation, useNavigate } from 'react-router-dom'
import Button from 'react-bootstrap/esm/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Container from 'react-bootstrap/esm/Container';
import Form from 'react-bootstrap/Form'
import Badge from 'react-bootstrap/Badge';
import Modal from 'react-bootstrap/Modal';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCheckCircle, faCircleInfo } from '@fortawesome/free-solid-svg-icons'
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Tooltip from 'react-bootstrap/Tooltip';



function Bookroom(){
    const navigate = useNavigate();
    const location = useLocation(); 
    // let uid = JSON.parse(localStorage.getItem('uid')) || ""
    let email = JSON.parse(localStorage.getItem('email')) || ""
    // const [checkin, setCheckin] = useState(0)
    // const [checkout, setCheckout] = useState(0)
    const [rid, setRid] = useState(0)
    const [addons, setAddons] = useState([])
    const [discount, setDiscount] = useState(10)
    const [select_addons, setSelectAddons] = useState([])
    const [total_amount, setTotalAmount] = useState(0)
    const [guest_name, setGuestName] = useState('')
    const [phone_number, setPhoneNumber] = useState('')
    const [special_request, setSpecialRequest] = useState('')
    const [modalShow, setModalShow] = useState(false);
    const [modalData, setModalData] = useState({})
    const [buttonDisabled, setButtonDisabled] = useState(false);
    const check_in = new Date(location.state.check_in).toISOString().split("T")[0]
    const check_out= new Date(location.state.check_out).toISOString().split("T")[0] 
    console.log(`checkin ${check_in} checkout ${check_out}`)
    let performBooking = async ()=>{
        try{
            let data = {room_id:rid, 
                customer_email: email, 
                check_in,
                check_out,
                add_ons: select_addons, 
                guest_name: guest_name, 
                phone_number: phone_number, 
                discount: discount,
                special_request:special_request, 
                room_price:location.state.room_price}
            console.log(`checkin: ${data.check_in}`)
            console.log(`checkout: ${data.check_out}`)
            console.log(data)
            const res = await fetch(`/api/booking`,{
                method:"POST", 
                body:JSON.stringify(data),
                headers: {'Content-type': 'application/json charset=UTF-8',}
            })
            const msg = await res.json()
            console.log(msg)
            setButtonDisabled(true)
            setModalData(data)
            setModalShow(true)
            //navigate('/profile')
            }
          catch(e)
            {console.log(e)}
    }

    let getAddons = async ()=>{
        try{
            const res = await fetch(`/api/addons`)
            const msg = await res.json()
            //const msg=[{name:'swimming pool', cost:300}, {name:'gym', cost:200}, {name:'sauna', cost:500}]
            console.log(msg)
            setAddons(msg)
        }
        catch(e)
            {console.log(e)}
    }

    function addAddons(e) {
        const idx = e.target.name

        if(e.target.checked)
        {
            setSelectAddons(arr => [...arr,addons[idx]])    
            console.log("add")
        }
        else{
         //   select_addons.splice(select_addons.findIndex(({name}) => name == addons[idx].name), 1)   
           console.log("remove")
           setSelectAddons(select_addons.filter(function(service){return service.name !=  addons[idx].name;}))
          
        }
    }

    

    let getDiscount = async ()=>{
        try{
        const res = await fetch(`/api/loyalty-discount?customer_email=${email}`)
        const msg = await res.json()
        setDiscount(msg.discount)
        }
        catch(e)
        {console.log(e)}
    }

    function get_total_amount(){
        // var check_in =location.state.check_in
        // var check_out =location.state.check_out
        let diffDays=0

        const date1 = new Date(check_in);
        const date2 = new Date(check_out);
        const diffTime = Math.abs(date2 - date1);
        if(diffTime==0){
            diffDays =1
            console.log("diffDays: "+diffDays)
        }
        else{
          diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 
        }
        //return location.state.room_price
       
        
        var initialValue=0
        var add_ons_cost = select_addons.reduce((accumulator, service) => accumulator + service.price,initialValue)
        

        setTotalAmount((diffDays*location.state.room_price) + add_ons_cost)
       // return (diffDays*location.state.room_price) + add_ons_cost

    }

    useEffect(()=>{
        console.log(`start: ${location.state.check_in} end: ${location.state.check_out}`)
        // setCheckin(location.state.checkin);
        // setCheckout(location.state.checkout);
        setRid(location.state.room_id);
        getAddons()
        getDiscount()
        get_total_amount()
       
    },[total_amount , select_addons])

    return(
        <Container className='min-vh-100 px-0'>

            <Row className="align-items-center bg-light shadow-5 p-2 my-3 justify-content-center">
            <h4>Booking details</h4>
            <Col xs="auto">
            <Form.Label htmlFor="inlineFormInput">Check-in date</Form.Label>
                <Form.Control type="date"
                    name="checkin"
                    value={check_in}
                    disabled
                    required />
            </Col>
            <Col xs="auto">
            <Form.Label htmlFor="inlineFormInput">Check-out date</Form.Label>
                <Form.Control type="date"
                    name="checkout"
                    value={check_out}
                    disabled
                    required />
            </Col>
            <Col xs="auto">
                <Form.Label htmlFor="inlineFormInput">Add-ons</Form.Label>
                {addons.map((item, idx)=>{
                    return <p><Form.Check inline key={idx} label={item.name} name={idx} type='checkbox'  id='radio-{idx}' onChange={addAddons}/> <span>₹{item.price}</span></p>
                })}
            </Col>
        </Row>

        <Row className="align-items-center bg-light shadow-5 p-2 my-3">
            <h4>Guest details</h4>
            <Col xs="auto">
                <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                    <Form.Label>Name</Form.Label>
                    <Form.Control type="text" placeholder="name" required onChange={(e)=>setGuestName(e.target.value)}/>
                </Form.Group>
            </Col>
            <Col xs="auto">
                <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                    <Form.Label>Email</Form.Label>
                    <Form.Control disabled type="email" defaultValue={email} placeholder="name@example.com" />
                </Form.Group>
            </Col>
            <Col xs="auto">
                <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                    <Form.Label>Phone number</Form.Label>
                    <Form.Control type="phone" required placeholder="10 digit mobile" pattern='[0-9]{10}' onChange={(e)=>setPhoneNumber(e.target.value)}/>
                </Form.Group>
            </Col>
            <Col xs="auto">
                <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                    <Form.Label>Special request</Form.Label>
                    <Form.Control type="text" required placeholder="requirements" onChange={(e)=>setSpecialRequest(e.target.value)} />
                </Form.Group>
            </Col>
        </Row>

        <Row className="align-items-center bg-light shadow-5 p-2 my-3">
        <h4>Payment details</h4>
            <Col xs="auto">
                <p><span>Room Price: ₹</span>{location.state.room_price}</p>
                {select_addons.map((item, idx)=>{
                    return <p><span>{item.name}:  </span>+ ₹{item.price}</p>
                })}
                <p><span>Total Amount: ₹</span>{total_amount}</p>
                <OverlayTrigger placement="right" overlay={<Tooltip>Loyalty discount obtained after placing {discount>0?discount/10:0} bookings.</Tooltip>} >
                    <p><span>Discount(if applicable): </span><Badge pill bg='success'>-₹{discount}</Badge><FontAwesomeIcon fade className='px-2'icon={faCircleInfo} size="lg" /></p>
                </OverlayTrigger>
                <p></p> 
                <p><span>Grand Total: ₹</span>{total_amount - discount}</p>
                <Button className='btn-lg btn-success' disabled={buttonDisabled} onClick={performBooking}>Confirm booking</Button>
            </Col>  
        </Row>
        <Modal backdrop="static"  show = {modalShow} aria-labelledby="contained-modal-title-vcenter">
            <Modal.Header>
                <Modal.Title id="contained-modal-title-vcenter" className='text-center'>
                Booking confirmation
                </Modal.Title>
            </Modal.Header>
            <Modal.Body className="show-grid">
                <Container>
                <Row className='my-3 text-center'>
                    <FontAwesomeIcon beat className='text-success' icon={faCheckCircle} size='5x' />
                </Row>
                <Row>
                    <Col >
                        <p><span>Guest name:</span> {modalData.guest_name}</p>
                        <p><span>Contact:</span> {modalData.phone_number}</p>
                        <p><span>Check In:</span> {modalData.check_in}</p>
                        <p><span>Check Out:</span> {modalData.check_out}</p>
                        <p><span>Special request: </span>{modalData.special_request}</p>
                    </Col>

                    <Col>
                        <p><span>Room Price: ₹</span>{location.state.room_price}</p>
                        {select_addons.map((item, idx)=>{
                            return <p><span>{item.name}:  </span>+ ₹{item.price}</p>
                        })}
                        <p><span>Total Amount: ₹</span>{total_amount}</p>
                        <OverlayTrigger placement="right" overlay={<Tooltip>Loyalty discount obtained after placing {discount>0?discount/10:0} bookings.</Tooltip>} >
                            <p><span>Discount(if applicable): </span><Badge pill bg='success'>-₹{discount}</Badge><FontAwesomeIcon fade className='px-2'icon={faCircleInfo} size="lg" /></p>
                        </OverlayTrigger>
                        <p></p> 
                        <p><span>Grand Total: ₹</span>{total_amount - discount}</p>           
                    </Col>

                </Row>
                </Container>
            </Modal.Body>
            <Modal.Footer className='justify-content-center'>
                <Button variant="danger" onClick={()=>navigate('/')}>Go to homepage</Button> 
            </Modal.Footer>
        </Modal>
        </Container>
    );
}

export default Bookroom