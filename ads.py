from flask import Blueprint, request, jsonify
from src.models.ad import db, Ad, GeneratedAd
from src.models.user import User
import json
import random
import re

ads_bp = Blueprint('ads', __name__)

# Sample competitor ads data for demonstration
SAMPLE_COMPETITOR_ADS = [
    {
        "title": "Revolutionary Fitness App",
        "description": "Transform your body in 30 days",
        "ad_copy": "🔥 Get fit in just 30 days! Our AI-powered fitness app creates personalized workouts just for you. Join 1M+ users who've transformed their bodies. Download now and get your first week FREE! 💪",
        "keywords": "fitness, workout, AI, personalized, transformation",
        "platform": "Facebook",
        "competitor_name": "FitTech Pro",
        "estimated_spend": 15000.0,
        "performance_score": 8.5
    },
    {
        "title": "Premium Coffee Subscription",
        "description": "Artisan coffee delivered monthly",
        "ad_copy": "☕ Discover the world's finest coffee beans delivered to your door. Hand-selected by expert roasters. First bag only $9.99! Free shipping. Cancel anytime. Taste the difference quality makes.",
        "keywords": "coffee, subscription, artisan, premium, delivery",
        "platform": "Google",
        "competitor_name": "Bean Masters",
        "estimated_spend": 8500.0,
        "performance_score": 7.8
    },
    {
        "title": "Online Marketing Course",
        "description": "Master digital marketing in 6 weeks",
        "ad_copy": "🚀 From Zero to Marketing Hero in 6 weeks! Learn Facebook Ads, Google Ads, SEO & more. 10,000+ students. 4.9★ rating. Limited time: 70% OFF! Enroll now and transform your career.",
        "keywords": "marketing, course, digital, Facebook ads, Google ads, SEO",
        "platform": "Facebook",
        "competitor_name": "Marketing Mastery",
        "estimated_spend": 25000.0,
        "performance_score": 9.2
    },
    {
        "title": "Smart Home Security",
        "description": "24/7 home monitoring system",
        "ad_copy": "🏠 Protect what matters most. Our smart security system monitors your home 24/7. Easy DIY installation. No contracts. Professional monitoring from $19.99/month. Get peace of mind today!",
        "keywords": "security, smart home, monitoring, DIY, protection",
        "platform": "Google",
        "competitor_name": "SecureHome Plus",
        "estimated_spend": 12000.0,
        "performance_score": 8.1
    }
]

def initialize_sample_data():
    """Initialize database with sample competitor ads if empty"""
    if Ad.query.filter_by(is_competitor_ad=True).count() == 0:
        for ad_data in SAMPLE_COMPETITOR_ADS:
            ad = Ad(
                title=ad_data["title"],
                description=ad_data["description"],
                ad_copy=ad_data["ad_copy"],
                keywords=ad_data["keywords"],
                platform=ad_data["platform"],
                competitor_name=ad_data["competitor_name"],
                estimated_spend=ad_data["estimated_spend"],
                performance_score=ad_data["performance_score"],
                is_competitor_ad=True
            )
            db.session.add(ad)
        db.session.commit()

@ads_bp.route('/competitor-ads', methods=['GET'])
def get_competitor_ads():
    """Get all competitor ads with optional filtering"""
    initialize_sample_data()
    
    platform = request.args.get('platform')
    keyword = request.args.get('keyword')
    
    query = Ad.query.filter_by(is_competitor_ad=True)
    
    if platform:
        query = query.filter(Ad.platform.ilike(f'%{platform}%'))
    
    if keyword:
        query = query.filter(Ad.keywords.ilike(f'%{keyword}%'))
    
    ads = query.order_by(Ad.performance_score.desc()).all()
    
    return jsonify({
        'success': True,
        'ads': [ad.to_dict() for ad in ads],
        'total': len(ads)
    })

@ads_bp.route('/generate-ad', methods=['POST'])
def generate_ad():
    """Generate AI-powered ad copy based on product description"""
    data = request.get_json()
    
    if not data or 'product_description' not in data:
        return jsonify({'success': False, 'error': 'Product description is required'}), 400
    
    product_description = data['product_description']
    platform = data.get('platform', 'Facebook')
    user_id = data.get('user_id', 1)  # Default user for demo
    
    # Simple AI simulation - in a real app, this would use actual AI models
    generated_copy = generate_ai_ad_copy(product_description, platform)
    predicted_score = random.uniform(6.0, 9.5)
    
    # Save to database
    generated_ad = GeneratedAd(
        user_id=user_id,
        product_description=product_description,
        generated_copy=generated_copy,
        platform=platform,
        predicted_score=predicted_score
    )
    
    db.session.add(generated_ad)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'generated_ad': generated_ad.to_dict()
    })

@ads_bp.route('/generate-variations', methods=['POST'])
def generate_ad_variations():
    """Generate multiple variations of an ad"""
    data = request.get_json()
    
    if not data or 'product_description' not in data:
        return jsonify({'success': False, 'error': 'Product description is required'}), 400
    
    product_description = data['product_description']
    platform = data.get('platform', 'Facebook')
    user_id = data.get('user_id', 1)
    count = min(data.get('count', 5), 10)  # Limit to 10 variations
    
    variations = []
    
    for i in range(count):
        generated_copy = generate_ai_ad_copy(product_description, platform, variation=i+1)
        predicted_score = random.uniform(6.0, 9.5)
        
        generated_ad = GeneratedAd(
            user_id=user_id,
            product_description=product_description,
            generated_copy=generated_copy,
            platform=platform,
            predicted_score=predicted_score
        )
        
        db.session.add(generated_ad)
        variations.append(generated_ad.to_dict())
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'variations': variations,
        'count': len(variations)
    })

@ads_bp.route('/my-ads', methods=['GET'])
def get_user_ads():
    """Get all ads generated by the user"""
    user_id = request.args.get('user_id', 1)
    
    ads = GeneratedAd.query.filter_by(user_id=user_id).order_by(GeneratedAd.created_at.desc()).all()
    
    return jsonify({
        'success': True,
        'ads': [ad.to_dict() for ad in ads],
        'total': len(ads)
    })

@ads_bp.route('/analyze-competitor', methods=['POST'])
def analyze_competitor():
    """Analyze a specific competitor's ad strategy"""
    data = request.get_json()
    
    if not data or 'competitor_name' not in data:
        return jsonify({'success': False, 'error': 'Competitor name is required'}), 400
    
    competitor_name = data['competitor_name']
    
    # Find competitor ads
    ads = Ad.query.filter(Ad.competitor_name.ilike(f'%{competitor_name}%')).all()
    
    if not ads:
        return jsonify({'success': False, 'error': 'No ads found for this competitor'}), 404
    
    # Analyze competitor strategy
    analysis = {
        'competitor_name': competitor_name,
        'total_ads': len(ads),
        'avg_performance_score': sum(ad.performance_score for ad in ads) / len(ads),
        'total_estimated_spend': sum(ad.estimated_spend for ad in ads if ad.estimated_spend),
        'platforms': list(set(ad.platform for ad in ads)),
        'top_keywords': extract_top_keywords([ad.keywords for ad in ads if ad.keywords]),
        'best_performing_ad': max(ads, key=lambda x: x.performance_score).to_dict(),
        'ads': [ad.to_dict() for ad in ads]
    }
    
    return jsonify({
        'success': True,
        'analysis': analysis
    })

def generate_ai_ad_copy(product_description, platform, variation=1):
    """Simulate AI ad copy generation"""
    
    # Simple templates based on platform
    facebook_templates = [
        "🚀 {product}! Transform your life today. Join thousands who've already discovered the difference. Limited time offer - don't miss out! 💪",
        "✨ Introducing {product} - the game-changer you've been waiting for! See results in days, not months. Try it risk-free now! 🔥",
        "🎯 Ready for a change? {product} delivers real results. Trusted by experts. Special launch price - 50% OFF! Get yours today! 💯",
        "💡 {product} is here! Revolutionary approach, proven results. Join the movement. Free trial available - no commitment required! 🌟",
        "🔥 Don't settle for ordinary. {product} gives you extraordinary results. Limited stock available. Order now and save big! ⚡"
    ]
    
    google_templates = [
        "{product} - Get Results Fast. Proven solution trusted by thousands. Free shipping. 30-day guarantee. Order today!",
        "Transform Your Life with {product}. Expert-recommended. Fast delivery. Special offer: Buy 2, Get 1 Free!",
        "{product} - The Smart Choice. Compare prices and save. Free consultation available. Call now!",
        "Discover {product} - Premium Quality, Affordable Price. Fast results guaranteed. Limited time discount!",
        "Professional {product} Solutions. Trusted by industry leaders. Free quote. Same-day service available."
    ]
    
    # Extract key product name/type from description
    product_name = extract_product_name(product_description)
    
    if platform.lower() == 'facebook':
        template = facebook_templates[(variation - 1) % len(facebook_templates)]
    else:
        template = google_templates[(variation - 1) % len(google_templates)]
    
    return template.format(product=product_name)

def extract_product_name(description):
    """Extract a product name or type from description"""
    # Simple extraction - in a real AI system, this would be more sophisticated
    words = description.lower().split()
    
    # Look for common product indicators
    product_indicators = ['app', 'software', 'course', 'service', 'product', 'tool', 'system', 'platform']
    
    for word in words:
        if word in product_indicators:
            return word.title()
    
    # If no indicator found, use first few words
    return ' '.join(words[:2]).title()

def extract_top_keywords(keyword_lists):
    """Extract top keywords from a list of keyword strings"""
    all_keywords = []
    
    for keyword_string in keyword_lists:
        if keyword_string:
            keywords = [k.strip() for k in keyword_string.split(',')]
            all_keywords.extend(keywords)
    
    # Count frequency and return top 5
    keyword_count = {}
    for keyword in all_keywords:
        keyword_count[keyword] = keyword_count.get(keyword, 0) + 1
    
    return sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)[:5]

