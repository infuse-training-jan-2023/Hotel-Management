import React from 'react';

import { useNavigate } from 'react-router-dom'

function Error(){
    const navigate = useNavigate();

    return(
        <div className="position-absolute top-50 start-50 translate-middle">
            <span class="display-1 d-block">404</span>
            <div class="mb-4 lead">Unable to find page</div>
            <a onClick={() => navigate('/')} >Go to home page</a>
        </div>

    );
}

export default Error;