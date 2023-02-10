import React, {useState, useEffect} from "react";
import './App.css';
function App(){
  const [rooms, setRooms] = useState([])
  const [discount, setDiscount] = useState(0)
  const [loading, setLoading] = useState(true)
  const [filters, setFilters] = useState({checkin: null, checkout: null , room_type:null, price:null })
  let getRooms = async ()=>{
    try{
      const res = await fetch("/api/search",{
        method:"POST", 
        body:JSON.stringify(filters),
        headers: {'Content-type': 'application/json; charset=UTF-8',}
      })
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

  function applyFilters(e) {
    const name = e.target.name;
    const value = e.target.value;
    setFilters({...filters, [name]: value})
    //getRooms()
  }

  useEffect(()=>{
    setLoading(true)
    getRooms()
    // getDiscount()
    setLoading(false)
    console.log()
  }, [filters])

  if(loading) 
    return <p>loading</p>
  return(
    <div className="App">
		<div>
			
			<div>
      <fieldset>
          <legend>Filter</legend>
              <label for="price">Price: </label><input type="range" id="price" name="price" min="1000" max="10000" onChange={applyFilters} step='100'/>
          <label for="room_type">Room type:</label>
            <select name="room_type" id="room_type" onChange={applyFilters}>
              <option value="single">single</option>
              <option value="double">double</option>
              <option value="penthouse">penthouse</option>
          </select>
          <label for="checkin">Start Date:</label>
          <input
            type="date"
            name="checkin"
            min={new Date().toISOString().split("T")[0]}
            onChange={applyFilters}
            required
          />
          <label for="checkout">End Date:</label>
          <input
            type="date"
            name="checkout"
            disabled={filters.startdate === "" ? true: false}
            min={filters.startdate ? new Date(filters.startdate).toISOString().split("T")[0]: ""}
            onChange={applyFilters}
            required
          />
      </fieldset>
      <p>{JSON.stringify(filters)}</p>  
    </div>
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