import React, {useState, useEffect} from "react";
import './App.css';
function App(){
  const [rooms, setRooms] = useState([])
  const [discount, setDiscount] = useState(0)
  const [loading, setLoading] = useState(true)

  let min_date = new Date();
  console.log(min_date);

  
  var d = new Date();
  d.setMonth(d.getMonth() +2);
  console.log(d)

  let getRooms = async ()=>{
    try{
      const res = await fetch("/api/search")
      const msg = await res.json()
      setRooms(msg)
      console.log(msg);
      return msg
    }
    catch(e)
      {console.log(e)}
  }

  let getDiscount = async ()=>{
    try{
      const res = await fetch('/api/loyalty-discount?id=63e52044ba29b6d46527fe8b', {method: "GET"} )
      const msg = await res.json()
      setDiscount(msg.discount)
      console.log(msg);
    }
    catch(e)
      {console.log(e)}
  }

  useEffect(()=>{
    setLoading(true)
    getRooms()
    getDiscount()
    setLoading(false)
  }, [])

  if(loading) 
    return <p>loading</p>
  return(
    <div className="App">
		<div>
			<label for="price">price: </label><input type="range" id="price" name="price" min="1000" max="10000"/>
			<label for="roomtype">room type:</label>
				<select name="roomtype" id="roomtype">
					<option value="single">single</option>
					<option value="double">double</option>
					<option value="penthouse">penthouse</option>
			</select>
			<label for="checkin">Check in: </label><input type="date" id="checkin" name="checkin" min={min_date} max={d}/>
			<label for="checkout">Check out: </label><input type="date" id="checkout" name="checkout" min={min_date} max={d}/>
		</div>
		<div>
			{rooms.map((room, id)=>{
				return <div className="card" key="{id}">{JSON.stringify(room)}</div>
			})}
		</div>
    <h2>discount: {discount}</h2>
    </div>
  )
}
export default App