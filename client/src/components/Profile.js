import React, {useState, useEffect} from 'react';
import Card from 'react-bootstrap/Card';
import Button  from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import { useNavigate } from 'react-router-dom'
import Container from 'react-bootstrap/esm/Container';
function Profile(){
    const navigate = useNavigate();
    // let email = JSON.parse(localStorage.getItem('email')) || ""
    let [uid, setUid] = useState('')
    let [email, setEmail] = useState(JSON.parse(localStorage.getItem('email')) || "")
    let [cancel, setCancel] = useState({})
    const [userBookings, setUserBookings] = useState([])

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
    useEffect(() => {
        email && getAllUserBookings()
      }, [email, cancel]);

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

    async function cancelOrder(e){
        try{
            const bid = e.target.name
            //alert(bid)
            const res = await fetch(`/api/booking`, {method: 'PUT', body:JSON.stringify({id:bid}), headers: {'Content-type': 'application/json charset=UTF-8',}}  )
            const msg = await res.json()
            setCancel(msg)
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
            <hr ></hr>
                            {   

              userBookings.length? userBookings.map((item, idx)=>{
    
               if(Date.parse((item.check_out.$date)) > Date.now() && item.isCancelled==false) {
                  return (<Card  className='my-2 bg-light' height="2rem" key={idx}>
                    <Card.Body>
                        <Row>
                            <Col sm={6}>
                                <Card.Title>Guest Name: {item.guest_name}</Card.Title>
                                <Card.Text>Registered Email: {item.customer_email}</Card.Text>
                                <Card.Text>Check In: {item.check_in.$date.split('T')[0]}</Card.Text>
                                <Card.Text>Check Out: {item.check_out.$date.split('T')[0]}</Card.Text>
                                <Card.Text>Total Amount: Rs. {item.total_amount}/-</Card.Text>
                            </Col>
                            <Col> </Col>  
                            <Col ><Button className='my-3' name={item._id['$oid']} onClick={downloadInvoice}>Invoice</Button></Col>
                            <Col ><Button variant="danger" name={item._id['$oid']} className='my-3' onClick={cancelOrder}>Cancel</Button></Col>
                           <Col> </Col>  
                        </Row>
                    </Card.Body>
                </Card>)
                }}):<p className='text-center'>None</p>
            }    


            <h4 className='my-3 text-center'>PREVIOUS</h4>
            <hr></hr>
            {   

              userBookings.map((item, idx)=>{
    
               if(Date.parse((item.check_out.$date)) < Date.now() || item.isCancelled==true) {
                  return (<Card  className='my-2 bg-light ' height="2rem" key={idx}>
                    <Card.Body>
                        <Row>
                            <Col sm={8}>
                            <Card.Title>Guest Name: {item.guest_name}</Card.Title>
                                <Card.Text>Registered Email: {item.customer_email}</Card.Text>
                                <Card.Text>Check In: {item.check_in.$date.split('T')[0]}</Card.Text>
                                <Card.Text>Check Out: {item.check_out.$date.split('T')[0]}</Card.Text>
                                <Card.Text>Total Amount: Rs. {item.total_amount}/-</Card.Text>
                            </Col>  
                            <Col ><Button variant="info" className='my-3' onClick={()=>navigate(`/review/${item._id['$oid']}`)}>Review</Button></Col>
                            <Col ><Button className='my-3' name={item._id['$oid']} onClick={downloadInvoice}>Invoice</Button></Col>
                        </Row>
                    </Card.Body>
                </Card>)
                }})
            } 
            {!userBookings.length  && <p className='text-center'>None</p>}
            </Row>
            

        </Container>
    );
}

export default Profile;