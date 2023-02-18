import React from "react"
import "../App.css"
function Footer() {
  return (
    <container className="hotelfooter  flex-grow-0">
      <footer className="d-flex flex-wrap justify-content-between align-items-center py-3 mx-3 my-4 border-top">
        <span>
          <img className="w-25 inline" src="../../hotel.png" alt="logo" />
        </span>
        <p class="col-md-4 mb-0 text-muted">&copy; 2023 The New View, Inc</p>

        <a
          href="/"
          class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none"
        >
          {" "}
        </a>
      </footer>
    </container>
  )
}

export default Footer
