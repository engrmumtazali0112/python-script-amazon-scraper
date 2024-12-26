import React, { useState, useEffect } from 'react';
import Table from './components/Table';
import Result from './components/Result';

const App = () => {
    const [query, setQuery] = useState('');
    const [queries, setQueries] = useState([]);
    const [data, setData] = useState([]);
    const [selectedResult, setSelectedResult] = useState(null);

    useEffect(() => {
        // Fetch available queries from the backend
        fetch('http://localhost:5000/queries')
            .then(response => response.json())
            .then(data => setQueries(data))
            .catch(error => console.error('Error fetching queries:', error));
    }, []);

    const handleScrape = () => {
        if (!query) return;

        // Fetch scraped data for the selected query
        fetch(`http://localhost:5000/scrape?query=${query}`)
            .then(response => response.json())
            .then(data => setData(data))
            .catch(error => console.error('Error fetching data:', error));
    };

    const handleResultClick = (item) => {
        setSelectedResult(item);
    };

    return (
        <div>
            <h1>Amazon Product Scraper</h1>
            <select onChange={(e) => setQuery(e.target.value)}>
                <option value="">Select a query</option>
                {queries.map((q, index) => (
                    <option key={index} value={q}>
                        {q}
                    </option>
                ))}
            </select>
            <button onClick={handleScrape}>Scrape</button>
            <Table data={data} onResultClick={handleResultClick} />
            {selectedResult && <Result result={selectedResult} />}
        </div>
    );
};

export default App;
