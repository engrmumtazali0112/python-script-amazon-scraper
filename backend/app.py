from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

@app.route('/queries', methods=['GET'])
@app.route('/api/queries', methods=['GET'])  # Keep both routes for compatibility
def get_queries():
    try:
        queries_path = 'user_queries.json'
        logger.info(f"Attempting to read queries from {queries_path}")
        
        if not os.path.exists(queries_path):
            logger.error(f"File not found: {queries_path}")
            return jsonify({"error": "Queries file not found"}), 404
            
        with open(queries_path, 'r') as file:
            queries = json.load(file)
            logger.info(f"Successfully loaded {len(queries)} queries")
            return jsonify(queries), 200
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {str(e)}")
        return jsonify({"error": "Invalid JSON format in queries file"}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/scrape', methods=['GET'])
@app.route('/api/scrape', methods=['GET'])  # Keep both routes for compatibility
def scrape_query():
    query = request.args.get('query')
    if not query:
        logger.warning("Request received without query parameter")
        return jsonify({"error": "Query parameter is required"}), 400

    file_path = f"output/{query}.json"
    logger.info(f"Looking for data file: {file_path}")

    if not os.path.exists(file_path):
        logger.warning(f"No data file found for query: {query}")
        return jsonify({"error": f"No data found for query: {query}"}), 404

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logger.info(f"Successfully loaded data for query: {query}")
            return jsonify(data), 200
    except Exception as e:
        logger.error(f"Error reading data file: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Ensure output directory exists
    os.makedirs('output', exist_ok=True)
    
    # Add startup logging
    logger.info("Starting Flask application...")
    logger.info("CORS enabled")
    logger.info("Routes configured: /queries, /api/queries, /scrape, /api/scrape")
    
    app.run(debug=True, host='0.0.0.0', port=5000)