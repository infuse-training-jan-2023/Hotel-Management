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
      }, [email]);

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

    return(
        <Container className="">
            <Row className='my-2 px-3 h-50' >
                <Col xs={10}><h3>Bookings</h3></Col>
                {/* <Col xs={2} ><Button variant="danger" onClick={handleLogout}>Logout</Button></Col> */}
            <h4 className='my-3'>Current booking</h4>
            {
                userBookings.map((item, idx)=>{
                    return (<Card  className='mx-auto my-2 w-75 '  key={idx}>
                    <Card.Body className='py-2'>
                        <Row>
                            <Col sm={8}>
                                <Card.Title>{item.guest_name}</Card.Title>
                                <Card.Text>{item.total_amount}</Card.Text>
                                <Card.Text>{item.special_request}</Card.Text>
                            </Col>  
                            <Col ><Button variant="info" className='my-3' onClick={()=>navigate(`/review/${item._id['$oid']}`)}>Review</Button></Col>
                           <Col ><Button className='my-3' name={item._id['$oid']} onClick={downloadInvoice}>Invoice</Button></Col>
                        </Row>
                    </Card.Body>
                </Card>)
                })
            } 
            {!userBookings.length  && <h5 className='text-center'>No bookings made</h5>}
            </Row>
            

        </Container>
    );
}

export default Profile;