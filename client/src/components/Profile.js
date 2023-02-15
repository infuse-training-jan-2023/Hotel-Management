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
    let downloadInvoice = async ()=> {
        console.log('get bill')
    }

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


    return(
        <Container className="min-vh-100">
            <Row className='my-2'>
                <Col xs={10} style={{padding : '10px'}}><h3></h3></Col>
                <Col xs={2} ><Button variant="danger" onClick={handleLogout}>Logout</Button></Col>
            {uid}
            </Row>

            <h3>Previous Booking</h3>
            {   
            
                
                userBookings.map((item, idx)=>{
                    return (<Card  className='my-2' height="2rem" key={idx}>
                    <Card.Body>
                        <Row>
                            <Col sm={10}>
                                <Card.Title>{item.guest_name}</Card.Title>
                                <Card.Text>{item.total_amount}</Card.Text>
                                <Card.Text>{item.special_request}</Card.Text>
                            </Col>  
                            <Col ><Button variant="info" className='my-3' onClick={()=>navigate(`/review/${item._id['$oid']}`)}>Review</Button></Col>
                           <Col ><Button className='my-3' onClick={downloadInvoice}>Invoice</Button></Col>
                        </Row>
                    </Card.Body>
                </Card>)
                })
            } 
            

        </Container>
    );
}

export default Profile;