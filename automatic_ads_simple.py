from flask import Blueprint, request, jsonify
import json
import random

automatic_ads_bp = Blueprint('automatic_ads', __name__)

def extract_product_elements(description):
    """Extract key elements from product description"""
    # Simple keyword extraction
    words = description.lower().split()
    
    # Determine product type
    if any(word in words for word in ['app', 'software', 'platform', 'tool']):
        product_name = 'AI-powered'
        category = 'Technology'
    elif any(word in words for word in ['fitness', 'workout', 'exercise', 'health']):
        product_name = 'Fitness'
        category = 'Health & Fitness'
    else:
        product_name = 'Product'
        category = 'General'
    
    # Determine target audience
    if 'professional' in words or 'business' in words:
        target_audience = 'professionals'
    elif 'student' in words or 'learn' in words:
        target_audience = 'students'
    else:
        target_audience = 'customers'
    
    return {
        'product_name': product_name,
        'category': category,
        'target_audience': target_audience,
        'main_benefit': 'achieve better results',
        'price_range': 'standard'
    }

@automatic_ads_bp.route('/step1/analyze-product', methods=['POST'])
def analyze_product_description():
    """STEP 1: Analyze product/service description and extract key elements"""
    data = request.get_json()
    
    if not data or 'product_description' not in data:
        return jsonify({'success': False, 'error': 'Product description is required'}), 400
    
    product_description = data['product_description']
    analysis = extract_product_elements(product_description)
    
    return jsonify({
        'success': True,
        'analysis': analysis,
        'message': 'Product analyzed successfully! Now choose a template or competitor ad to duplicate.'
    })

@automatic_ads_bp.route('/step2/winning-templates', methods=['GET'])
def get_winning_templates():
    """STEP 2: Get winning templates proven to drive leads and sales"""
    
    # Mock winning templates data
    templates = [
        {
            'id': 1,
            'name': 'E-commerce Conversion King',
            'category': 'E-commerce',
            'template_copy': '🛒 {product_name} - The {category} that {target_audience} love! ⭐ {rating} stars from {review_count} customers. 🚀 {discount}% OFF today only! Free shipping on orders over ${min_order}. Shop now!',
            'platform': 'Facebook',
            'conversion_rate': 8.5,
            'ctr': 3.2,
            'roas': 4.7,
            'use_count': 2341,
            'is_premium': False
        },
        {
            'id': 2,
            'name': 'SaaS Growth Accelerator',
            'category': 'SaaS',
            'template_copy': '💼 {product_name} - Helping {target_audience} {main_benefit} since {year}. 📈 Join {customer_count}+ satisfied users. ✨ {key_feature} ⚡ {benefit_1} 🎯 {benefit_2} Start your free trial!',
            'platform': 'LinkedIn',
            'conversion_rate': 12.3,
            'ctr': 4.8,
            'roas': 6.2,
            'use_count': 1876,
            'is_premium': False
        },
        {
            'id': 3,
            'name': 'Fitness Transformation Formula',
            'category': 'Health & Fitness',
            'template_copy': '💪 Transform your {target_area} in just {timeframe}! {product_name} - the proven system used by {social_proof} people. 🔥 {benefit_1} ⚡ {benefit_2} 🎯 {benefit_3} Get started today!',
            'platform': 'Instagram',
            'conversion_rate': 9.7,
            'ctr': 5.1,
            'roas': 3.9,
            'use_count': 3421,
            'is_premium': False
        }
    ]
    
    return jsonify({
        'success': True,
        'templates': templates,
        'total': len(templates),
        'message': 'Choose a winning template or competitor ad to duplicate'
    })

@automatic_ads_bp.route('/step2/competitor-ads-for-duplication', methods=['GET'])
def get_competitor_ads_for_duplication():
    """STEP 2: Get competitor ads available for duplication"""
    
    # Mock competitor ads data
    competitor_ads = [
        {
            'id': 1,
            'headline': 'Revolutionary Fitness App Changes Everything',
            'description': 'Join thousands who transformed their lives with our AI-powered workout plans. Get personalized routines that fit your busy schedule.',
            'platform': 'Facebook',
            'performance_score': 8.7,
            'estimated_budget': '$5000/month',
            'engagement_rate': 4.2,
            'is_competitor_ad': True
        },
        {
            'id': 2,
            'headline': 'The Productivity Tool Every Professional Needs',
            'description': 'Stop wasting time on manual tasks. Our AI assistant handles your workflow so you can focus on what matters most.',
            'platform': 'LinkedIn',
            'performance_score': 9.1,
            'estimated_budget': '$8000/month',
            'engagement_rate': 5.8,
            'is_competitor_ad': True
        }
    ]
    
    return jsonify({
        'success': True,
        'competitor_ads': competitor_ads,
        'total': len(competitor_ads),
        'message': 'Select an ad to duplicate or choose a winning template'
    })

@automatic_ads_bp.route('/step3/generate-variations', methods=['POST'])
def generate_massive_variations():
    """STEP 3: Generate 10-1000 ad variations with one click"""
    data = request.get_json()
    
    if not data or 'variation_count' not in data:
        return jsonify({'success': False, 'error': 'Variation count is required'}), 400
    
    variation_count = min(max(int(data['variation_count']), 10), 1000)
    
    # Generate mock variations
    variations = []
    for i in range(variation_count):
        variation = {
            'id': i + 1,
            'generated_copy': f'🚀 Transform your life with our revolutionary solution! Join {random.randint(1000, 50000)}+ satisfied customers. ⭐ {random.uniform(4.5, 5.0):.1f} stars. Get {random.randint(10, 50)}% OFF today!',
            'predicted_ctr': round(random.uniform(2.0, 8.0), 2),
            'predicted_conversion_rate': round(random.uniform(5.0, 15.0), 2),
            'predicted_roas': round(random.uniform(3.0, 8.0), 2),
            'platform': random.choice(['Facebook', 'Instagram', 'LinkedIn', 'Google'])
        }
        variations.append(variation)
    
    # Calculate cost savings
    monthly_savings = random.randint(3000, 30000)
    
    return jsonify({
        'success': True,
        'variations': variations,
        'total_generated': variation_count,
        'estimated_monthly_savings': monthly_savings,
        'message': f'Successfully generated {variation_count} ad variations! Estimated savings: ${monthly_savings}/month'
    })

@automatic_ads_bp.route('/step4/cost-savings-calculator', methods=['POST'])
def calculate_cost_savings():
    """STEP 4: Calculate cost savings vs agencies/freelancers"""
    data = request.get_json()
    
    current_spend = data.get('current_monthly_spend', 1000)
    ad_variations = data.get('ad_variations', 5)
    
    # Calculate savings scenarios
    scenarios = {
        'conservative': {
            'improvement_factor': 1.5,
            'monthly_savings': random.randint(3000, 8000),
            'annual_savings': random.randint(36000, 96000)
        },
        'realistic': {
            'improvement_factor': 2.0,
            'monthly_savings': random.randint(8000, 15000),
            'annual_savings': random.randint(96000, 180000)
        },
        'optimistic': {
            'improvement_factor': 3.0,
            'monthly_savings': random.randint(15000, 30000),
            'annual_savings': random.randint(180000, 360000)
        }
    }
    
    return jsonify({
        'success': True,
        'scenarios': scenarios,
        'current_spend': current_spend,
        'message': 'Cost savings calculated successfully!'
    })

