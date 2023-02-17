import React, {useState, useEffect} from 'react';
import Card from 'react-bootstrap/Card';
import Button  from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import { useNavigate } from 'react-router-dom'
import Container from 'react-bootstrap/esm/Container';
import Badge from 'react-bootstrap/Badge'
import Modal from 'react-bootstrap/Modal';
function Profile(){
    const navigate = useNavigate();
    // let email = JSON.parse(localStorage.getItem('email')) || ""
    let [bid, setBid] = useState('')
    let [email, setEmail] = useState(JSON.parse(localStorage.getItem('email')) || "")
    let [cancel, setCancel] = useState({})
    const [userBookings, setUserBookings] = useState([])

    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    let handleLogout = () => {
        //setUid('')
        setEmail('')
        // localStorage.removeItem('uid');
        
        localStorage.removeItem('email');
        navigate('/')
        window.location.reload()
    }

    // let getUserDetail = async ()=>{
    //     try{
    //         if (localStorage.getItem("uid") === null) {
    //             // alert('new')
    //             console.log(email)
    //             const res = await fetch(`/api/user?email=${email}`)
    //             const msg = await res.json()
    //             // alert(msg._id['$oid'])
    //             setUid(msg._id['$oid'])
    //             localStorage.setItem('uid', JSON.stringify(msg._id['$oid']));
    //             console.log(msg)
    //             return msg
    //         }
    //         else{
    //             console.log(JSON.parse(localStorage.getItem('uid')))
    //         setUid(JSON.parse(localStorage.getItem('uid')))
    //         // alert('old')
    //         }
    //     }
    //     catch(e)
    //         {console.log(e)}
          
    // }

    let getAllUserBookings = async ()=>{
        try{
            // alert(uid)
            //console.log(uid)
            console.log('in fetch')
            
            const res = await fetch(`/api/booking?customer_email=${email}`)
            const msg = await res.json()
            // console.log(uid)
            console.log(msg)
            setUserBookings(msg);
            // console.log(`length: ${userBookings} type: ${typeof userBookings}`)
            return msg
        }
        catch(e)
            {console.log(e)}
    }
    // useEffect(() => {
    //     getUserDetail()
    //   }, []);
    // useEffect(() => {
    //     uid && getAllUserBookings()
    //   }, [uid]);


    function humanizeDate(date_str) {
        let month = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
      
        var date_arr = date_str.split('-');
        
        return month[Number(date_arr[1]) - 1] + " " + Number(date_arr[2]) + ", " + date_arr[0]
      }


    useEffect(() => {
        email && getAllUserBookings()
      }, [email, cancel, show]);

    // let downloadInvoice = async ()=> {
    //     console.log('get bill')
    //     const res = await fetch(`/api/invoice?id=${email}`)
    //     const msg = await res.json()
    // }

    async function downloadInvoice(e) {
        try{
            const bid = e.target.name
            //alert(bid)
            const res = await fetch(`/api/invoice?id=${bid}`)
            const blob = await res.blob()
            const url = window.URL.createObjectURL(new Blob([blob], {type: 'application/pdf'}))
            window.open(url, '_blank')
        }
        catch(e){
            console.log(e)
        }
    }

    async function cancelOrder(){ 
        // handleShow()
        try{
            
            alert(bid)
           
            const res = await fetch(`/api/booking`, {method: 'PUT', body:JSON.stringify({id:bid}), headers: {'Content-type': 'application/json charset=UTF-8',}}  )
            const msg = await res.json()
            setCancel(msg)

            handleClose()
           
        }
        catch(e){
            console.log(e)     
        }
    }

    return(
        <Container className="w-75">
            <Row className='my-2 px-3 h-50' >
                <Col className='fs-3 text-center font-weight-bold '><span>Your Bookings</span></Col>
                {/* <Col xs={2} ><Button variant="danger" onClick={handleLogout}>Logout</Button></Col> */}
            <h4 className='my-3 text-center'>CURRENT</h4>
            {   
              userBookings.length? userBookings.map((item, idx)=>{
               if(Date.parse((item.check_out.$date)) > Date.now() && item.isCancelled==false) {
                  return (<Card  className='my-2 bg-light  mx-auto' height="2rem" key={idx}>
                    <Card.Body>
                        <Row>
                            <Col sm={9}>
                                <Card.Title>Guest Name: {item.guest_name}</Card.Title>
                                <p className='my-1'><span>Registered Email: </span>{item.customer_email}</p>
                                <p className='my-1'><span>Date: </span>{humanizeDate(item.check_in.$date.split('T')[0])} <span>To</span> {humanizeDate(item.check_out.$date.split('T')[0])}</p>
        
                                <p className='my-1'><span>Total Amount: ₹ </span>{item.total_amount}/-</p>
                            </Col>
                            <Col ><Button className='my-3' name={item._id['$oid']} onClick={downloadInvoice}>Invoice</Button></Col>
                            <Col ><Button variant="danger" name={item._id['$oid']} className='my-3' onClick={(e)=>{setBid(e.target.name);handleShow()}}>Cancel</Button></Col>
                        </Row>
                    </Card.Body>
                </Card>)
                }}):<p className='text-center'>None</p>
            }    


            <h4 className='my-3 text-center'>PREVIOUS</h4>
            {   
              userBookings.length? userBookings.map((item, idx)=>{
                if(Date.parse((item.check_out.$date)) < Date.now() || item.isCancelled==true) {
                  return (<Card  className='my-2 bg-light  mx-auto' height="2rem" key={idx}>
                    <Card.Body>
                        <Row>
                            <Col sm={9}>
                                <Card.Title>Guest Name: {item.guest_name}</Card.Title>
                                <p className='my-1'><span>Registered Email: </span>{item.customer_email}</p>
                                <p className='my-1'><span>Check In: </span>{item.check_in.$date.split('T')[0]}</p>
                                <p className='my-1'><span>Check Out: </span>{item.check_out.$date.split('T')[0]}</p>
                                <p className='my-1'><span>Total Amount: ₹ </span>{item.total_amount}/-</p>
                            </Col>
                            <Col >{!item.isCancelled ? <Button variant="info" onClick={()=>navigate(`/review/${item._id['$oid']}`)}>Review</Button>: <Button  role="button" variant='secondary' disabled className='align-middle'>Cancelled</Button>}</Col>
                            <Col ><Button name={item._id['$oid']} onClick={downloadInvoice}>Invoice</Button></Col>
                        </Row>
                    </Card.Body>
                </Card>)
                }}):<p className='text-center'>None</p>
            } 
            </Row>
            

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Modal heading</Modal.Title>
        </Modal.Header>
        <Modal.Body>Do you really want to confirm the cancellation made? </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="danger" onClick={cancelOrder}>
            Confirm cancellation
          </Button>
        </Modal.Footer>
      </Modal>

        </Container>
    );
}

export default Profile;