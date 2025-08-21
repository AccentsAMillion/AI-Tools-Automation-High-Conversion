#!/usr/bin/env python3
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import random
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Serve static files
@app.route('/')
def serve_index():
    return send_from_directory('/home/ubuntu/automatic-ads-frontend-enhanced', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('/home/ubuntu/automatic-ads-frontend-enhanced', filename)

# API Routes
@app.route('/api/automatic/step1/analyze-product', methods=['POST'])
def analyze_product():
    try:
        data = request.get_json()
        product_description = data.get('product_description', '')
        
        # Simulate product analysis
        analysis = {
            'industry': 'Fitness & Health',
            'target_audience': 'Busy professionals aged 25-45',
            'key_benefits': ['Time-efficient', 'Personalized', 'AI-powered'],
            'competitors': ['Nike Training Club', 'Peloton', 'MyFitnessPal'],
            'market_size': 'Large',
            'competition_level': 'High'
        }
        
        return jsonify({
            'success': True,
            'analysis': analysis
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/automatic/step2/winning-templates', methods=['GET'])
def get_winning_templates():
    try:
        templates = [
            {
                'id': 'template_1',
                'name': 'Problem-Solution Framework',
                'category': 'High Converting',
                'template_copy': 'Tired of [PROBLEM]? Our [SOLUTION] helps [TARGET_AUDIENCE] achieve [BENEFIT] in just [TIME_FRAME]. Join [SOCIAL_PROOF] who have already transformed their [AREA].',
                'ctr': 4.2,
                'conversion_rate': 12.8,
                'roas': 3.4,
                'use_count': 15420
            },
            {
                'id': 'template_2',
                'name': 'Social Proof Amplifier',
                'category': 'Viral',
                'template_copy': '[NUMBER] [TARGET_AUDIENCE] can\'t be wrong! Discover why [PRODUCT] is the #1 choice for [BENEFIT]. Limited time: [OFFER]',
                'ctr': 3.8,
                'conversion_rate': 10.5,
                'roas': 2.9,
                'use_count': 12350
            },
            {
                'id': 'template_3',
                'name': 'Urgency Creator',
                'category': 'High Converting',
                'template_copy': 'Only [TIME_LEFT] left! [PRODUCT] is helping [TARGET_AUDIENCE] [ACHIEVE_GOAL]. Don\'t miss out on [BENEFIT] - [CTA]',
                'ctr': 5.1,
                'conversion_rate': 15.2,
                'roas': 4.1,
                'use_count': 18750
            },
            {
                'id': 'template_4',
                'name': 'Before & After Story',
                'category': 'Emotional',
                'template_copy': 'From [BEFORE_STATE] to [AFTER_STATE] in just [TIME_FRAME]. See how [PRODUCT] transformed [CUSTOMER_TYPE]\'s [LIFE_AREA]. Your turn next!',
                'ctr': 3.5,
                'conversion_rate': 11.3,
                'roas': 3.2,
                'use_count': 9840
            },
            {
                'id': 'template_5',
                'name': 'Expert Endorsement',
                'category': 'Authority',
                'template_copy': 'Recommended by [EXPERT_TYPE]: "[PRODUCT] is the most effective [SOLUTION_TYPE] I\'ve seen for [TARGET_AUDIENCE]." Try it risk-free today!',
                'ctr': 4.0,
                'conversion_rate': 13.7,
                'roas': 3.8,
                'use_count': 11200
            }
        ]
        
        return jsonify({
            'success': True,
            'templates': templates
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/automatic/step2/competitor-ads-for-duplication', methods=['GET'])
def get_competitor_ads():
    try:
        industry = request.args.get('industry', 'Fitness & Health')
        
        competitor_ads = [
            {
                'id': 'comp_1',
                'brand_name': 'FitQuick Pro',
                'platform': 'Facebook',
                'industry': 'Fitness & Health',
                'headline': 'Get Fit in 15 Minutes Daily',
                'description': 'Busy schedule? No problem! Our AI creates personalized 15-minute workouts that fit your lifestyle. Join 50,000+ professionals who stay fit without gym memberships.',
                'performance_score': 9,
                'estimated_budget': '$5,000-10,000/month',
                'engagement_rate': 8.5,
                'reach': '2.5M',
                'is_active': True
            },
            {
                'id': 'comp_2',
                'brand_name': 'WorkoutWise',
                'platform': 'Instagram',
                'industry': 'Fitness & Health',
                'headline': 'AI Personal Trainer in Your Pocket',
                'description': 'Stop wasting hours at the gym. Our smart app creates custom workouts based on your schedule, fitness level, and goals. 7-day free trial!',
                'performance_score': 8,
                'estimated_budget': '$3,000-7,000/month',
                'engagement_rate': 7.2,
                'reach': '1.8M',
                'is_active': True
            },
            {
                'id': 'comp_3',
                'brand_name': 'QuickFit Solutions',
                'platform': 'LinkedIn',
                'industry': 'Fitness & Health',
                'headline': 'Executive Fitness Made Simple',
                'description': 'Designed for busy executives: Science-backed 15-minute workouts that deliver results. No equipment needed. Used by Fortune 500 leaders.',
                'performance_score': 7,
                'estimated_budget': '$2,000-5,000/month',
                'engagement_rate': 6.8,
                'reach': '800K',
                'is_active': False
            },
            {
                'id': 'comp_4',
                'brand_name': 'SmartFit AI',
                'platform': 'TikTok',
                'industry': 'Fitness & Health',
                'headline': 'This App Knows Your Body Better Than You Do',
                'description': 'Revolutionary AI analyzes your movement patterns and creates perfect workouts. See why 100K+ users are obsessed. Download free!',
                'performance_score': 9,
                'estimated_budget': '$8,000-15,000/month',
                'engagement_rate': 12.3,
                'reach': '5.2M',
                'is_active': True
            }
        ]
        
        return jsonify({
            'success': True,
            'competitor_ads': competitor_ads
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/automatic/step3/generate-variations', methods=['POST'])
def generate_variations():
    try:
        data = request.get_json()
        variation_count = int(data.get('variation_count', 10))
        product_description = data.get('product_description', '')
        template_id = data.get('template_id', '')
        platform = data.get('platform', 'Facebook')
        
        # Generate realistic variations
        variations = []
        base_copies = [
            "Transform your fitness routine with AI-powered 15-minute workouts designed for busy professionals. Join thousands who've revolutionized their health!",
            "Stop making excuses! Our smart fitness app creates personalized workouts that fit your hectic schedule. Results guaranteed in just 15 minutes daily.",
            "Busy professional? Get fit without the gym! AI-powered workouts adapt to your schedule and fitness level. Try free for 7 days!",
            "Finally, a fitness solution that works with your busy life. Personalized 15-minute AI workouts deliver real results. Join the revolution!",
            "Ditch the gym membership! Our AI creates custom 15-minute workouts for busy professionals. See why 50,000+ users are obsessed.",
            "Time-crunched? Our AI fitness coach creates perfect 15-minute workouts for your lifestyle. Transform your health starting today!",
            "Revolutionary AI fitness app for busy professionals. Get personalized 15-minute workouts that actually work. Free trial available!",
            "No time for the gym? No problem! AI-powered 15-minute workouts designed specifically for busy professionals. Start your transformation!",
            "Breakthrough fitness technology for busy people. AI creates personalized 15-minute workouts that fit any schedule. Try it free!",
            "The fitness app that understands your busy life. AI-powered 15-minute workouts deliver maximum results in minimum time."
        ]
        
        for i in range(min(variation_count, len(base_copies))):
            variation = {
                'id': i + 1,
                'generated_copy': base_copies[i],
                'predicted_ctr': round(random.uniform(2.5, 6.0), 1),
                'predicted_conversion_rate': round(random.uniform(8.0, 18.0), 1),
                'predicted_roas': round(random.uniform(2.0, 5.0), 1),
                'target_audience': 'Busy professionals aged 25-45',
                'emotional_tone': random.choice(['Motivational', 'Urgent', 'Empowering', 'Solution-focused']),
                'confidence_score': round(random.uniform(0.75, 0.95), 2),
                'platform_optimized': platform,
                'estimated_cpc': round(random.uniform(0.50, 2.50), 2)
            }
            variations.append(variation)
        
        # Sort by predicted performance
        variations.sort(key=lambda x: x['predicted_roas'], reverse=True)
        
        return jsonify({
            'success': True,
            'variations': variations,
            'total_generated': len(variations)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/automatic/step4/cost-savings', methods=['POST'])
def calculate_cost_savings():
    try:
        data = request.get_json()
        variation_count = int(data.get('variation_count', 10))
        
        # Cost calculations
        agency_cost_per_ad = random.randint(150, 400)
        freelancer_cost_per_ad = random.randint(75, 200)
        our_tool_cost_per_ad = 0.50
        
        cost_comparison = {
            'agency': {
                'cost_per_ad': agency_cost_per_ad,
                'total_cost': agency_cost_per_ad * variation_count
            },
            'freelancer': {
                'cost_per_ad': freelancer_cost_per_ad,
                'total_cost': freelancer_cost_per_ad * variation_count
            },
            'our_tool': {
                'cost_per_ad': our_tool_cost_per_ad,
                'total_cost': our_tool_cost_per_ad * variation_count
            }
        }
        
        # ROI scenarios
        agency_savings = cost_comparison['agency']['total_cost'] - cost_comparison['our_tool']['total_cost']
        freelancer_savings = cost_comparison['freelancer']['total_cost'] - cost_comparison['our_tool']['total_cost']
        
        roi_scenarios = {
            'conservative': {
                'monthly_savings': int(agency_savings * 0.5),
                'annual_savings': int(agency_savings * 0.5 * 12),
                'description': 'Using 50% fewer agency services'
            },
            'realistic': {
                'monthly_savings': int(agency_savings * 0.8),
                'annual_savings': int(agency_savings * 0.8 * 12),
                'description': 'Replacing 80% of agency work'
            },
            'optimistic': {
                'monthly_savings': int(agency_savings),
                'annual_savings': int(agency_savings * 12),
                'description': 'Complete agency replacement'
            }
        }
        
        savings_analysis = {
            'cost_comparison': cost_comparison,
            'roi_scenarios': roi_scenarios,
            'time_saved_hours': variation_count * 2,  # 2 hours per ad
            'break_even_ads': max(1, int(97 / (agency_cost_per_ad - our_tool_cost_per_ad)))  # Assuming $97 monthly subscription
        }
        
        return jsonify({
            'success': True,
            'savings_analysis': savings_analysis
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

