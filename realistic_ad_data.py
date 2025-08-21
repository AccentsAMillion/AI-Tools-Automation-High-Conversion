"""
Realistic Ad Data Service
Provides realistic competitor ad data that mimics real API responses
"""

import random
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

class RealisticAdDataService:
    
    def __init__(self):
        self.platforms = ['Facebook', 'Instagram', 'LinkedIn', 'Google Ads', 'TikTok', 'Twitter']
        self.industries = ['Fitness', 'SaaS', 'E-commerce', 'Finance', 'Health', 'Education', 'Travel', 'Food']
        self.ad_formats = ['Video', 'Image', 'Carousel', 'Collection', 'Story']
        
        # Realistic brand names and companies
        self.brands = {
            'Fitness': ['FitLife Pro', 'GymBeast', 'FlexFit', 'PowerCore', 'MuscleTech', 'FitnessPal'],
            'SaaS': ['CloudSync', 'DataFlow', 'WorkSpace Pro', 'TeamConnect', 'AutoCRM', 'TaskMaster'],
            'E-commerce': ['ShopEasy', 'QuickBuy', 'MegaStore', 'FastShip', 'DealHunter', 'PrimeMart'],
            'Finance': ['MoneyWise', 'InvestSmart', 'CreditBoost', 'WealthBuilder', 'FinanceFlow', 'CashMax'],
            'Health': ['HealthFirst', 'WellnessPlus', 'VitalCare', 'MedAssist', 'HealthTracker', 'CureAll'],
            'Education': ['LearnFast', 'SkillBuilder', 'EduPro', 'KnowledgeHub', 'StudyMaster', 'BrainBoost']
        }
        
        # Realistic ad copy templates
        self.ad_templates = {
            'Fitness': [
                "🔥 Transform your body in just {timeframe}! Join {customer_count}+ people who've already seen amazing results. Get {discount}% OFF today!",
                "💪 Ready to get in the best shape of your life? Our proven system has helped {customer_count}+ people lose weight and build muscle. Start your transformation now!",
                "⚡ Stop making excuses! Our {timeframe} fitness program delivers real results. Join {customer_count}+ satisfied members today!",
                "🏋️ From couch to confident in {timeframe}! See why {customer_count}+ people choose us for their fitness journey. Limited time: {discount}% OFF!"
            ],
            'SaaS': [
                "🚀 Boost your productivity by {percentage}%! Join {customer_count}+ companies already using our platform. Start your free trial today!",
                "💼 Streamline your workflow and save {hours} hours per week. Trusted by {customer_count}+ businesses worldwide. Get started free!",
                "📈 Increase your revenue by {percentage}% with our proven system. Over {customer_count} companies can't be wrong. Try it free!",
                "⚡ Automate your {process} and focus on what matters. Join {customer_count}+ satisfied customers. Free trial available!"
            ],
            'E-commerce': [
                "🛍️ {product_name} - The #{ranking} bestseller! ⭐ {rating} stars from {review_count}+ customers. Get {discount}% OFF + free shipping!",
                "🔥 FLASH SALE: {product_name} now {discount}% OFF! Limited stock - {stock_count} left. Free shipping on orders over ${min_order}!",
                "✨ Discover why {customer_count}+ customers love {product_name}! Premium quality, unbeatable price. Shop now and save {discount}%!",
                "🎯 {product_name} - Perfect for {target_audience}! ⭐ {rating}/5 stars. Limited time: Buy 2, get 1 FREE!"
            ]
        }
    
    def get_winning_templates(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Generate realistic winning ad templates"""
        templates = []
        
        for i in range(limit):
            industry = random.choice(self.industries)
            platform = random.choice(self.platforms)
            brand = random.choice(self.brands.get(industry, ['Generic Brand']))
            
            template = {
                'id': i + 1,
                'name': f"{industry} {random.choice(['Conversion', 'Growth', 'Performance', 'Success'])} {random.choice(['Formula', 'System', 'Blueprint', 'Strategy'])}",
                'category': industry,
                'platform': platform,
                'template_copy': random.choice(self.ad_templates.get(industry, self.ad_templates['SaaS'])),
                'ctr': round(random.uniform(2.1, 8.5), 1),
                'conversion_rate': round(random.uniform(3.2, 15.8), 1),
                'roas': round(random.uniform(2.8, 8.2), 1),
                'use_count': random.randint(1200, 5000),
                'is_premium': random.choice([True, False]),
                'created_date': (datetime.now() - timedelta(days=random.randint(30, 365))).isoformat(),
                'last_updated': (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat()
            }
            templates.append(template)
        
        # Sort by performance (CTR * Conversion Rate)
        templates.sort(key=lambda x: x['ctr'] * x['conversion_rate'], reverse=True)
        
        return templates
    
    def get_competitor_ads(self, industry: str = None, platform: str = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Generate realistic competitor ads"""
        ads = []
        
        for i in range(limit):
            selected_industry = industry or random.choice(self.industries)
            selected_platform = platform or random.choice(self.platforms)
            brand = random.choice(self.brands.get(selected_industry, ['Generic Brand']))
            
            # Generate realistic ad copy
            template = random.choice(self.ad_templates.get(selected_industry, self.ad_templates['SaaS']))
            ad_copy = template.format(
                timeframe=random.choice(['30 days', '60 days', '90 days', '6 months']),
                customer_count=f"{random.randint(10, 500)}K",
                discount=random.randint(20, 70),
                percentage=random.randint(25, 200),
                hours=random.randint(5, 40),
                process=random.choice(['workflow', 'operations', 'marketing', 'sales']),
                product_name=f"{brand} {random.choice(['Pro', 'Plus', 'Premium', 'Elite'])}",
                ranking=random.randint(1, 5),
                rating=round(random.uniform(4.2, 4.9), 1),
                review_count=random.randint(500, 10000),
                stock_count=random.randint(5, 50),
                min_order=random.choice([50, 75, 100, 150]),
                target_audience=random.choice(['professionals', 'entrepreneurs', 'students', 'parents'])
            )
            
            ad = {
                'id': f"ad_{i+1}_{selected_platform.lower()}",
                'brand_name': brand,
                'headline': f"{brand} - {random.choice(['Revolutionary', 'Game-Changing', 'Industry-Leading', 'Award-Winning'])} {random.choice(['Solution', 'Platform', 'System', 'Tool'])}",
                'description': ad_copy,
                'platform': selected_platform,
                'industry': selected_industry,
                'ad_format': random.choice(self.ad_formats),
                'performance_score': round(random.uniform(6.5, 9.8), 1),
                'estimated_budget': f"${random.randint(5, 50)}K/month",
                'engagement_rate': round(random.uniform(2.1, 8.7), 1),
                'reach': f"{random.randint(100, 2000)}K",
                'impressions': f"{random.randint(500, 5000)}K",
                'clicks': f"{random.randint(25, 400)}K",
                'first_seen': (datetime.now() - timedelta(days=random.randint(1, 90))).isoformat(),
                'last_seen': (datetime.now() - timedelta(days=random.randint(0, 7))).isoformat(),
                'is_active': random.choice([True, True, True, False]),  # 75% active
                'target_demographics': {
                    'age_range': random.choice(['18-24', '25-34', '35-44', '45-54', '25-44']),
                    'gender': random.choice(['All', 'Male', 'Female']),
                    'locations': random.choice(['United States', 'United States, Canada', 'Global', 'North America'])
                },
                'call_to_action': random.choice(['Learn More', 'Sign Up', 'Get Started', 'Shop Now', 'Download', 'Try Free']),
                'landing_page_url': f"https://{brand.lower().replace(' ', '')}.com/{random.choice(['landing', 'signup', 'trial', 'offer'])}",
                'creative_elements': {
                    'has_video': random.choice([True, False]),
                    'has_carousel': random.choice([True, False]),
                    'color_scheme': random.choice(['Blue/White', 'Red/Black', 'Green/White', 'Purple/Gold', 'Orange/Black']),
                    'primary_emotion': random.choice(['Excitement', 'Trust', 'Urgency', 'Curiosity', 'Fear of Missing Out'])
                }
            }
            ads.append(ad)
        
        # Sort by performance score
        ads.sort(key=lambda x: x['performance_score'], reverse=True)
        
        return ads
    
    def get_ad_variations(self, base_template: str, product_description: str, count: int = 100) -> List[Dict[str, Any]]:
        """Generate realistic ad variations"""
        variations = []
        
        # Extract key elements from product description
        words = product_description.lower().split()
        product_type = 'app' if 'app' in words else 'product'
        
        # Variation templates
        variation_templates = [
            "🚀 {product_name} - The {adjective} {product_type} that {benefit}! Join {social_proof} satisfied users. {cta}!",
            "⚡ Transform your {area} with {product_name}! {benefit_statement}. Get started today!",
            "🎯 {product_name}: {unique_value_prop}. Trusted by {social_proof} users worldwide. {cta}!",
            "💪 Ready to {action}? {product_name} makes it easy! {benefit_statement}. Try it now!",
            "🔥 {product_name} - {social_proof} can't be wrong! {benefit_statement}. {cta}!",
            "✨ Discover the secret to {benefit}! {product_name} has helped {social_proof} achieve their goals.",
            "🌟 {product_name}: Where {benefit} meets {secondary_benefit}. Join the revolution!",
            "⭐ Why choose {product_name}? {reason_1}. {reason_2}. {reason_3}. Start your journey!"
        ]
        
        adjectives = ['revolutionary', 'game-changing', 'innovative', 'cutting-edge', 'advanced', 'smart', 'powerful']
        benefits = ['save time', 'boost productivity', 'achieve goals', 'get results', 'stay organized', 'improve performance']
        social_proofs = ['10K+', '25K+', '50K+', '100K+', '250K+', '500K+']
        ctas = ['Get Started', 'Try Free', 'Learn More', 'Sign Up', 'Download Now', 'Start Trial']
        
        for i in range(count):
            template = random.choice(variation_templates)
            
            variation_copy = template.format(
                product_name=f"FitPro {random.choice(['Elite', 'Pro', 'Plus', 'Max'])}",
                adjective=random.choice(adjectives),
                product_type=product_type,
                benefit=random.choice(benefits),
                social_proof=random.choice(social_proofs),
                cta=random.choice(ctas),
                area=random.choice(['fitness', 'health', 'lifestyle', 'routine']),
                benefit_statement=random.choice([
                    'Get results in just 15 minutes a day',
                    'Personalized plans that adapt to your schedule',
                    'AI-powered recommendations for maximum results',
                    'Track progress automatically and stay motivated'
                ]),
                unique_value_prop=random.choice([
                    'The only app you need for complete fitness',
                    'Personalized workouts that fit your busy schedule',
                    'AI-powered fitness coaching in your pocket',
                    'Transform your body with science-backed workouts'
                ]),
                action=random.choice(['get fit', 'transform your body', 'achieve your goals', 'stay healthy']),
                secondary_benefit=random.choice(['convenience', 'effectiveness', 'personalization', 'results']),
                reason_1=random.choice(['Personalized plans', 'Quick 15-min workouts', 'AI-powered coaching']),
                reason_2=random.choice(['Fits any schedule', 'Proven results', 'Easy to follow']),
                reason_3=random.choice(['Track progress', 'Stay motivated', 'Achieve goals faster'])
            )
            
            variation = {
                'id': i + 1,
                'generated_copy': variation_copy,
                'predicted_ctr': round(random.uniform(2.5, 9.2), 2),
                'predicted_conversion_rate': round(random.uniform(4.1, 16.8), 2),
                'predicted_roas': round(random.uniform(3.2, 7.8), 2),
                'confidence_score': round(random.uniform(0.75, 0.98), 2),
                'platform_optimized': random.choice(self.platforms),
                'target_audience': random.choice(['Busy Professionals', 'Fitness Enthusiasts', 'Health-Conscious Adults', 'Working Parents']),
                'emotional_tone': random.choice(['Motivational', 'Urgent', 'Trustworthy', 'Exciting', 'Aspirational']),
                'key_benefits': random.sample(['Time-saving', 'Personalized', 'Effective', 'Convenient', 'Results-driven', 'AI-powered'], 3),
                'estimated_performance': {
                    'reach': f"{random.randint(50, 500)}K",
                    'impressions': f"{random.randint(200, 2000)}K",
                    'clicks': f"{random.randint(10, 180)}K",
                    'cost_per_click': f"${round(random.uniform(0.45, 2.80), 2)}"
                }
            }
            variations.append(variation)
        
        # Sort by predicted performance (CTR * Conversion Rate)
        variations.sort(key=lambda x: x['predicted_ctr'] * x['predicted_conversion_rate'], reverse=True)
        
        return variations
    
    def get_cost_savings_analysis(self, variation_count: int) -> Dict[str, Any]:
        """Generate realistic cost savings analysis"""
        
        # Base costs for agencies/freelancers
        agency_cost_per_ad = random.randint(150, 400)
        freelancer_cost_per_ad = random.randint(75, 200)
        
        # Calculate savings
        agency_total = variation_count * agency_cost_per_ad
        freelancer_total = variation_count * freelancer_cost_per_ad
        
        # Our tool cost (much lower)
        tool_cost = random.randint(50, 150)  # Fixed monthly cost
        
        return {
            'variation_count': variation_count,
            'cost_comparison': {
                'agency': {
                    'cost_per_ad': agency_cost_per_ad,
                    'total_cost': agency_total,
                    'timeframe': 'monthly'
                },
                'freelancer': {
                    'cost_per_ad': freelancer_cost_per_ad,
                    'total_cost': freelancer_total,
                    'timeframe': 'monthly'
                },
                'our_tool': {
                    'cost_per_ad': round(tool_cost / variation_count, 2),
                    'total_cost': tool_cost,
                    'timeframe': 'monthly'
                }
            },
            'savings': {
                'vs_agency': {
                    'amount': agency_total - tool_cost,
                    'percentage': round(((agency_total - tool_cost) / agency_total) * 100, 1)
                },
                'vs_freelancer': {
                    'amount': freelancer_total - tool_cost,
                    'percentage': round(((freelancer_total - tool_cost) / freelancer_total) * 100, 1)
                }
            },
            'roi_scenarios': {
                'conservative': {
                    'monthly_savings': random.randint(3000, 8000),
                    'annual_savings': random.randint(36000, 96000),
                    'description': 'Based on replacing 1-2 agency campaigns per month'
                },
                'realistic': {
                    'monthly_savings': random.randint(8000, 18000),
                    'annual_savings': random.randint(96000, 216000),
                    'description': 'Based on replacing 3-5 agency campaigns per month'
                },
                'optimistic': {
                    'monthly_savings': random.randint(18000, 35000),
                    'annual_savings': random.randint(216000, 420000),
                    'description': 'Based on replacing entire marketing team for ad creation'
                }
            }
        }

