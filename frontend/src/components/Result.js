import React from 'react';

const Result = ({ result }) => {
    return (
        <div style={{ marginTop: '20px', border: '1px solid black', padding: '10px' }}>
            <h2>Selected Product Details</h2>
            <p><strong>Title:</strong> {result.title}</p>
            <p><strong>Reviews:</strong> {result.reviews}</p>
            <p><strong>Price:</strong> {result.price}</p>
            <img src={result.image_url} alt={result.title} width="100" />
        </div>
    );
};

export default Result;
