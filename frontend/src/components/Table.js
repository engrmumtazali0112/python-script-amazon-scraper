import React from 'react';
import './Table.css'; // Import the CSS file

const Table = ({ data }) => {
    if (!Array.isArray(data) || data.length === 0) {
        return <p>No data available or an error occurred while fetching data.</p>;
    }

    return (
        <div className="grid-container">
            {data.map((item, index) => (
                <a
                    href={item.product_link || "#"} // Use product_link or a placeholder if not available
                    target="_blank" // Open the link in a new tab
                    rel="noopener noreferrer" // Prevent security vulnerabilities
                    className="card-link"
                    key={index}
                >
                    <div className="card">
                        <img
                            src={item.image_url || "https://via.placeholder.com/150"}
                            alt={item.title || "No Image"}
                            className="product-image"
                        />
                        <div className="card-content">
                            <h3 className="product-title">{item.title || "N/A"}</h3>
                            <p className="product-reviews">
                                <strong>Reviews:</strong> {item.reviews || "N/A"}
                            </p>
                            <p className="product-price">
                                <strong>Price:</strong> {item.price || "N/A"}
                            </p>
                        </div>
                    </div>
                </a>
            ))}
        </div>
    );
};

export default Table;
