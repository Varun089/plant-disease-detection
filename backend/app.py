"""Plant Disease Detection - Flask Backend Application

Main Flask application for the Plant Disease Detection system.
Provides REST API endpoints for image prediction, sensor data handling,
and recommendations.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'uploads')

# Enable CORS
CORS(app)

# Initialize REST API
api = Api(app)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import routes and models
from routes.api import PredictAPI, SensorDataAPI, RecommendationsAPI

# Register API endpoints
api.add_resource(PredictAPI, '/api/predict')
api.add_resource(SensorDataAPI, '/api/sensor-data')
api.add_resource(RecommendationsAPI, '/api/recommendations')

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Plant Disease Detection API',
        'version': '1.0.0'
    }), 200

@app.route('/api/info', methods=['GET'])
def api_info():
    """API information endpoint"""
    return jsonify({
        'name': 'Plant Disease Detection API',
        'version': '1.0.0',
        'description': 'ML system for detecting abiotic plant stresses',
        'endpoints': {
            'predict': '/api/predict (POST)',
            'sensor_data': '/api/sensor-data (POST)',
            'recommendations': '/api/recommendations (GET)',
            'health': '/api/health (GET)'
        }
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f'Internal server error: {error}')
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Run Flask app
    app.run(
        host=os.getenv('FLASK_HOST', '0.0.0.0'),
        port=int(os.getenv('FLASK_PORT', 5000)),
        debug=os.getenv('FLASK_ENV', 'development') == 'development'
    )
"""
