from flask import Blueprint, request, jsonify
import json
import random
import re
from src.services.realistic_ad_data import RealisticAdDataService

automatic_ads_bp = Blueprint('automatic_ads', __name__)
ad_data_service = RealisticAdDataService()

@automatic_ads_bp.route("/step1/analyze-product", methods=["POST"])
def analyze_product():
    """Step 1: Analyze product description"""
    try:
        data = request.get_json()
        product_description = data.get('product_description', '')
        
        if not product_description:
            return jsonify({'success': False, 'error': 'Product description is required'}), 400
        
        # AI-powered analysis (simulated)
        analysis = {
            'product_name': extract_product_name(product_description),
            'target_audience': extract_target_audience(product_description),
            'main_benefit': extract_main_benefit(product_description),
            'industry': extract_industry(product_description),
            'key_features': extract_key_features(product_description),
            'competitive_advantages': extract_competitive_advantages(product_description)
        }
        
        return jsonify({
            'success': True,
            'message': 'Product analysis completed successfully',
            'analysis': analysis
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@automatic_ads_bp.route("/step2/winning-templates", methods=["GET"])
def get_winning_templates():
    """Step 2: Get winning ad templates"""
    try:
        limit = request.args.get('limit', 10, type=int)
        templates = ad_data_service.get_winning_templates(limit)
        
        return jsonify({
            'success': True,
            'message': 'Choose a winning template or competitor ad to duplicate',
            'templates': templates,
            'total': len(templates)
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@automatic_ads_bp.route("/step2/competitor-ads-for-duplication", methods=["GET"])
def get_competitor_ads():
    """Step 2: Get competitor ads for duplication"""
    try:
        industry = request.args.get('industry')
        platform = request.args.get('platform')
        limit = request.args.get('limit', 10, type=int)
        
        competitor_ads = ad_data_service.get_competitor_ads(industry, platform, limit)
        
        return jsonify({
            'success': True,
            'message': 'Competitor ads loaded successfully',
            'competitor_ads': competitor_ads,
            'total': len(competitor_ads)
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@automatic_ads_bp.route("/step3/generate-variations", methods=["POST"])
def generate_variations():
    """Step 3: Generate ad variations"""
    try:
        data = request.get_json()
        product_description = data.get('product_description', '')
        variation_count = data.get('variation_count', 10)
        template_id = data.get('template_id')
        platform = data.get('platform', 'Facebook')
        
        # Generate variations using the realistic data service
        variations = ad_data_service.get_ad_variations(
            base_template='', 
            product_description=product_description, 
            count=int(variation_count)
        )
        
        return jsonify({
            'success': True,
            'message': f'Generated {len(variations)} ad variations successfully',
            'variations': variations,
            'total_generated': len(variations),
            'platform': platform,
            'estimated_time_saved': f"{random.randint(20, 80)} hours"
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@automatic_ads_bp.route("/step4/cost-savings", methods=["POST"])
def calculate_cost_savings():
    """Step 4: Calculate cost savings"""
    try:
        data = request.get_json()
        variation_count = data.get('variation_count', 10)
        
        savings_analysis = ad_data_service.get_cost_savings_analysis(int(variation_count))
        
        return jsonify({
            'success': True,
            'message': 'Cost savings calculated successfully',
            'savings_analysis': savings_analysis
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Helper functions for product analysis
def extract_product_name(description):
    """Extract or generate product name from description"""
    words = description.split()
    if 'app' in description.lower():
        return f"{random.choice(['Fit', 'Health', 'Wellness', 'Power', 'Smart'])}Pro"
    elif 'software' in description.lower() or 'platform' in description.lower():
        return f"{random.choice(['Work', 'Team', 'Business', 'Smart', 'Pro'])}Flow"
    else:
        return f"{random.choice(['Smart', 'Pro', 'Elite', 'Premium', 'Advanced'])}{random.choice(['Solution', 'System', 'Tool'])}"

def extract_target_audience(description):
    """Extract target audience from description"""
    if 'professional' in description.lower():
        return 'Busy Professionals'
    elif 'business' in description.lower():
        return 'Business Owners'
    elif 'student' in description.lower():
        return 'Students'
    elif 'parent' in description.lower():
        return 'Working Parents'
    else:
        return 'Health-Conscious Adults'

def extract_main_benefit(description):
    """Extract main benefit from description"""
    if 'save time' in description.lower() or 'quick' in description.lower():
        return 'Save time and increase efficiency'
    elif 'fitness' in description.lower() or 'workout' in description.lower():
        return 'Get fit and stay healthy'
    elif 'productivity' in description.lower():
        return 'Boost productivity and performance'
    else:
        return 'Achieve your goals faster'

def extract_industry(description):
    """Extract industry from description"""
    desc_lower = description.lower()
    if any(word in desc_lower for word in ['fitness', 'workout', 'health', 'exercise']):
        return 'Fitness'
    elif any(word in desc_lower for word in ['software', 'platform', 'saas', 'tool']):
        return 'SaaS'
    elif any(word in desc_lower for word in ['shop', 'store', 'product', 'buy']):
        return 'E-commerce'
    elif any(word in desc_lower for word in ['finance', 'money', 'investment', 'banking']):
        return 'Finance'
    elif any(word in desc_lower for word in ['education', 'learning', 'course', 'training']):
        return 'Education'
    else:
        return 'Technology'

def extract_key_features(description):
    """Extract key features from description"""
    features = []
    desc_lower = description.lower()
    
    if 'ai' in desc_lower or 'artificial intelligence' in desc_lower:
        features.append('AI-Powered')
    if 'personal' in desc_lower:
        features.append('Personalized')
    if 'track' in desc_lower:
        features.append('Progress Tracking')
    if 'mobile' in desc_lower or 'app' in desc_lower:
        features.append('Mobile App')
    if 'quick' in desc_lower or 'fast' in desc_lower:
        features.append('Quick Results')
    
    if not features:
        features = ['Easy to Use', 'Effective', 'Time-Saving']
    
    return features[:3]

def extract_competitive_advantages(description):
    """Extract competitive advantages from description"""
    advantages = []
    desc_lower = description.lower()
    
    if '15' in description or 'quick' in desc_lower:
        advantages.append('Only 15 minutes needed')
    if 'personal' in desc_lower:
        advantages.append('Fully personalized experience')
    if 'ai' in desc_lower:
        advantages.append('Advanced AI technology')
    if 'professional' in desc_lower:
        advantages.append('Designed for busy professionals')
    
    if not advantages:
        advantages = ['Industry-leading features', 'Proven results', 'Easy to use']
    
    return advantages[:3]

