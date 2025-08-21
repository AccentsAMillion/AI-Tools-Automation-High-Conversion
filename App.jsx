import React from 'react'
import './App.css'
import { Button } from './components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './components/ui/card'
import { Badge } from './components/ui/badge'
import { 
  Zap, 
  Target, 
  TrendingUp, 
  Clock, 
  DollarSign, 
  Users, 
  CheckCircle, 
  Star,
  ArrowRight,
  Play,
  BarChart3,
  Lightbulb,
  Shield,
  Rocket
} from 'lucide-react'

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      {/* Navigation */}
      <nav className="bg-white/80 backdrop-blur-md border-b border-gray-200 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
                <Zap className="w-5 h-5 text-white" />
              </div>
              <span className="text-xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                Automatic Ads
              </span>
            </div>
            <div className="hidden md:flex items-center space-x-8">
              <a href="#features" className="text-gray-600 hover:text-gray-900 transition-colors">Features</a>
              <a href="#how-it-works" className="text-gray-600 hover:text-gray-900 transition-colors">How It Works</a>
              <a href="#pricing" className="text-gray-600 hover:text-gray-900 transition-colors">Pricing</a>
              <Button className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700">
                Try Free Now
              </Button>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative overflow-hidden py-20 lg:py-32">
        <div className="absolute inset-0 bg-gradient-to-r from-blue-600/10 to-purple-600/10"></div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <Badge className="mb-6 bg-blue-100 text-blue-800 hover:bg-blue-200">
              🚀 Built on $100M+ Ad Spend Learnings
            </Badge>
            <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold text-gray-900 mb-6">
              Create{' '}
              <span className="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                1000s of Winning Ads
              </span>
              <br />
              By Duplicating Your{' '}
              <span className="bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
                Competitor's Top Ads
              </span>
              <br />
              In Seconds
            </h1>
            <p className="text-xl md:text-2xl text-gray-600 mb-8 max-w-4xl mx-auto leading-relaxed">
              Without any tech skills, or wasting thousands on agencies, freelancers, or spending hours on creating ads with ChatGPT or crappy AI tools.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
              <Button 
                size="lg" 
                className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-lg px-8 py-4 h-auto"
              >
                <Play className="w-5 h-5 mr-2" />
                Try Automatic Ads Free
              </Button>
              <Button 
                variant="outline" 
                size="lg" 
                className="text-lg px-8 py-4 h-auto border-2"
              >
                Watch Demo Video
              </Button>
            </div>
            <div className="flex flex-wrap justify-center items-center gap-8 text-sm text-gray-500">
              <div className="flex items-center">
                <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
                No Credit Card Required
              </div>
              <div className="flex items-center">
                <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
                30-60 Second Setup
              </div>
              <div className="flex items-center">
                <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
                Save $3-30k/Month
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Problem Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              The Problem With Traditional Ad Creation
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Most businesses struggle with expensive, time-consuming ad creation that delivers unpredictable results.
            </p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            <Card className="text-center p-8 border-2 border-red-200 bg-red-50">
              <CardHeader>
                <div className="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <DollarSign className="w-8 h-8 text-red-600" />
                </div>
                <CardTitle className="text-red-800">Expensive Agencies</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-red-700">
                  Agencies charge $150-400 per ad, with minimum monthly retainers of $5,000-15,000. 
                  Most small businesses can't afford this premium pricing.
                </p>
              </CardContent>
            </Card>
            <Card className="text-center p-8 border-2 border-orange-200 bg-orange-50">
              <CardHeader>
                <div className="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <Clock className="w-8 h-8 text-orange-600" />
                </div>
                <CardTitle className="text-orange-800">Time-Consuming Process</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-orange-700">
                  Creating effective ads manually takes 4-8 hours per variation. Testing 100 headlines 
                  manually would take weeks of full-time work.
                </p>
              </CardContent>
            </Card>
            <Card className="text-center p-8 border-2 border-yellow-200 bg-yellow-50">
              <CardHeader>
                <div className="w-16 h-16 bg-yellow-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <Target className="w-8 h-8 text-yellow-600" />
                </div>
                <CardTitle className="text-yellow-800">Unpredictable Results</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-yellow-700">
                  Without competitor insights, you're shooting in the dark. 90% of ads fail because 
                  they don't follow proven patterns that actually work.
                </p>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Solution Section */}
      <section id="how-it-works" className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              Here's How Automatic Ads Works
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Our revolutionary 4-step process turns competitor intelligence into winning ads in seconds.
            </p>
          </div>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            <Card className="text-center p-6 hover:shadow-lg transition-shadow border-2 hover:border-blue-200">
              <CardHeader>
                <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-2xl font-bold text-blue-600">1</span>
                </div>
                <CardTitle className="text-blue-800">Describe Your Product</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">
                  Simply describe your product or service. Our AI analyzes your input to understand 
                  your market and identify relevant competitors.
                </p>
              </CardContent>
            </Card>
            <Card className="text-center p-6 hover:shadow-lg transition-shadow border-2 hover:border-purple-200">
              <CardHeader>
                <div className="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-2xl font-bold text-purple-600">2</span>
                </div>
                <CardTitle className="text-purple-800">Select Winning Template</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">
                  Choose from our library of proven templates or select a competitor ad to duplicate. 
                  All templates are backed by real performance data.
                </p>
              </CardContent>
            </Card>
            <Card className="text-center p-6 hover:shadow-lg transition-shadow border-2 hover:border-green-200">
              <CardHeader>
                <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-2xl font-bold text-green-600">3</span>
                </div>
                <CardTitle className="text-green-800">Generate Variations</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">
                  Generate 10-1000 ad variations with one click. Each variation is optimized for 
                  different audiences, emotions, and platforms.
                </p>
              </CardContent>
            </Card>
            <Card className="text-center p-6 hover:shadow-lg transition-shadow border-2 hover:border-orange-200">
              <CardHeader>
                <div className="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-2xl font-bold text-orange-600">4</span>
                </div>
                <CardTitle className="text-orange-800">Save Thousands</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">
                  Deploy your winning ads and save $3-30k/month on agencies, freelancers, 
                  and entire marketing teams. Saved money = made money.
                </p>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              Why Automatic Ads Works So Well
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Built on the exact same framework we use with elite 8-figure clients. Everything's automated, optimized, and simplified.
            </p>
          </div>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <Card className="p-6 hover:shadow-lg transition-shadow">
              <CardHeader>
                <Lightbulb className="w-12 h-12 text-blue-600 mb-4" />
                <CardTitle>No Creative Talent Needed</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">
                  Our AI handles all the creative work. You don't need design skills, copywriting experience, 
                  or marketing expertise to create professional ads.
                </p>
              </CardContent>
            </Card>
            <Card className="p-6 hover:shadow-lg transition-shadow">
              <CardHeader>
                <BarChart3 className="w-12 h-12 text-purple-600 mb-4" />
                <CardTitle>No Media Buying Skills</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">
                  Skip the learning curve of Facebook Ads Manager, Google Ads, and other platforms. 
                  Our system optimizes for each platform automatically.
                </p>
              </CardContent>
            </Card>
            <Card className="p-6 hover:shadow-lg transition-shadow">
              <CardHeader>
                <Shield className="w-12 h-12 text-green-600 mb-4" />
                <CardTitle>No Tech Skills Required</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">
                  Simple point-and-click interface that anyone can use. No coding, no complex setups, 
                  no technical knowledge required.
                </p>
              </CardContent>
            </Card>
            <Card className="p-6 hover:shadow-lg transition-shadow">
              <CardHeader>
                <Rocket className="w-12 h-12 text-red-600 mb-4" />
                <CardTitle>No Manual Testing</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">
                  Stop testing 100 headlines manually. Our AI generates and ranks variations based on 
                  proven performance patterns from successful campaigns.
                </p>
              </CardContent>
            </Card>
            <Card className="p-6 hover:shadow-lg transition-shadow">
              <CardHeader>
                <Zap className="w-12 h-12 text-yellow-600 mb-4" />
                <CardTitle>Everything Automated</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">
                  From competitor analysis to ad generation to performance prediction - everything 
                  happens automatically in 30-60 seconds.
                </p>
              </CardContent>
            </Card>
            <Card className="p-6 hover:shadow-lg transition-shadow">
              <CardHeader>
                <TrendingUp className="w-12 h-12 text-indigo-600 mb-4" />
                <CardTitle>Optimized & Simplified</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">
                  Every feature is designed for maximum results with minimum effort. Clean interface, 
                  clear workflows, and instant results.
                </p>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Results Section */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              Here's How It Works In Real Numbers
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Let's say you're running 5 ad variations a month, spending $1,000/month.
            </p>
          </div>
          <div className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl p-8 md:p-12 text-white">
            <div className="grid md:grid-cols-2 gap-12 items-center">
              <div>
                <h3 className="text-2xl md:text-3xl font-bold mb-6">
                  If even one of those converts 2x better...
                </h3>
                <p className="text-xl mb-8 text-blue-100">
                  You just increased your revenue without touching your ad budget.
                </p>
                <p className="text-lg text-blue-100 mb-8">
                  That's what Automatic Ads unlocks: more results, less work.
                </p>
                <div className="space-y-4">
                  <div className="flex items-center">
                    <CheckCircle className="w-6 h-6 text-green-400 mr-3" />
                    <span className="text-lg">Lower cost per lead</span>
                  </div>
                  <div className="flex items-center">
                    <CheckCircle className="w-6 h-6 text-green-400 mr-3" />
                    <span className="text-lg">Lower cost per acquisition</span>
                  </div>
                  <div className="flex items-center">
                    <CheckCircle className="w-6 h-6 text-green-400 mr-3" />
                    <span className="text-lg">Higher ROAS</span>
                  </div>
                  <div className="flex items-center">
                    <CheckCircle className="w-6 h-6 text-green-400 mr-3" />
                    <span className="text-lg">Less stress</span>
                  </div>
                </div>
              </div>
              <div className="bg-white/10 backdrop-blur-sm rounded-xl p-8">
                <h4 className="text-xl font-semibold mb-6">Monthly Savings Breakdown</h4>
                <div className="space-y-4">
                  <div className="flex justify-between items-center">
                    <span>Agency Costs:</span>
                    <span className="font-bold text-red-300">$15,000</span>
                  </div>
                  <div className="flex justify-between items-center">
                    <span>Freelancer Costs:</span>
                    <span className="font-bold text-orange-300">$8,000</span>
                  </div>
                  <div className="flex justify-between items-center">
                    <span>Automatic Ads:</span>
                    <span className="font-bold text-green-300">$150</span>
                  </div>
                  <hr className="border-white/20" />
                  <div className="flex justify-between items-center text-xl font-bold">
                    <span>You Save:</span>
                    <span className="text-green-300">$14,850/month</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Social Proof Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              Trusted by 10,000+ Marketers
            </h2>
            <p className="text-xl text-gray-600">
              Join thousands of businesses already saving time and money with Automatic Ads.
            </p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            <Card className="p-6">
              <CardContent className="pt-6">
                <div className="flex items-center mb-4">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="w-5 h-5 text-yellow-400 fill-current" />
                  ))}
                </div>
                <p className="text-gray-600 mb-4">
                  "Automatic Ads saved us $12,000 per month on agency fees. We're getting better results 
                  than ever before with half the effort."
                </p>
                <div className="flex items-center">
                  <div className="w-10 h-10 bg-blue-500 rounded-full flex items-center justify-center text-white font-bold mr-3">
                    SM
                  </div>
                  <div>
                    <p className="font-semibold">Sarah Martinez</p>
                    <p className="text-sm text-gray-500">Marketing Director, TechStart</p>
                  </div>
                </div>
              </CardContent>
            </Card>
            <Card className="p-6">
              <CardContent className="pt-6">
                <div className="flex items-center mb-4">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="w-5 h-5 text-yellow-400 fill-current" />
                  ))}
                </div>
                <p className="text-gray-600 mb-4">
                  "I was spending 20 hours a week creating ads. Now I generate 100 variations in 2 minutes. 
                  This tool is a game-changer."
                </p>
                <div className="flex items-center">
                  <div className="w-10 h-10 bg-green-500 rounded-full flex items-center justify-center text-white font-bold mr-3">
                    MJ
                  </div>
                  <div>
                    <p className="font-semibold">Mike Johnson</p>
                    <p className="text-sm text-gray-500">Founder, E-commerce Plus</p>
                  </div>
                </div>
              </CardContent>
            </Card>
            <Card className="p-6">
              <CardContent className="pt-6">
                <div className="flex items-center mb-4">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="w-5 h-5 text-yellow-400 fill-current" />
                  ))}
                </div>
                <p className="text-gray-600 mb-4">
                  "Our ROAS improved by 340% after switching to Automatic Ads. The competitor intelligence 
                  feature is incredibly powerful."
                </p>
                <div className="flex items-center">
                  <div className="w-10 h-10 bg-purple-500 rounded-full flex items-center justify-center text-white font-bold mr-3">
                    LC
                  </div>
                  <div>
                    <p className="font-semibold">Lisa Chen</p>
                    <p className="text-sm text-gray-500">CMO, Growth Agency</p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section id="pricing" className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              Simple, Transparent Pricing
            </h2>
            <p className="text-xl text-gray-600">
              Choose the plan that fits your business needs. All plans include our core features.
            </p>
          </div>
          <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
            <Card className="p-8 border-2">
              <CardHeader className="text-center">
                <CardTitle className="text-2xl">Starter</CardTitle>
                <CardDescription>Perfect for small businesses</CardDescription>
                <div className="mt-4">
                  <span className="text-4xl font-bold">$97</span>
                  <span className="text-gray-500">/month</span>
                </div>
              </CardHeader>
              <CardContent>
                <ul className="space-y-3">
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    Up to 100 ad variations/month
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    Competitor ad intelligence
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    Winning templates library
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    Basic analytics
                  </li>
                </ul>
                <Button className="w-full mt-6" variant="outline">
                  Start Free Trial
                </Button>
              </CardContent>
            </Card>
            <Card className="p-8 border-2 border-blue-500 relative">
              <Badge className="absolute -top-3 left-1/2 transform -translate-x-1/2 bg-blue-500">
                Most Popular
              </Badge>
              <CardHeader className="text-center">
                <CardTitle className="text-2xl">Professional</CardTitle>
                <CardDescription>For growing businesses</CardDescription>
                <div className="mt-4">
                  <span className="text-4xl font-bold">$197</span>
                  <span className="text-gray-500">/month</span>
                </div>
              </CardHeader>
              <CardContent>
                <ul className="space-y-3">
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    Up to 500 ad variations/month
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    Advanced competitor intelligence
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    Premium templates
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    Advanced analytics & reporting
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    Priority support
                  </li>
                </ul>
                <Button className="w-full mt-6 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700">
                  Start Free Trial
                </Button>
              </CardContent>
            </Card>
            <Card className="p-8 border-2">
              <CardHeader className="text-center">
                <CardTitle className="text-2xl">Enterprise</CardTitle>
                <CardDescription>For agencies & large teams</CardDescription>
                <div className="mt-4">
                  <span className="text-4xl font-bold">$497</span>
                  <span className="text-gray-500">/month</span>
                </div>
              </CardHeader>
              <CardContent>
                <ul className="space-y-3">
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    Unlimited ad variations
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    White-label options
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    Custom integrations
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    Dedicated account manager
                  </li>
                  <li className="flex items-center">
                    <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                    24/7 priority support
                  </li>
                </ul>
                <Button className="w-full mt-6" variant="outline">
                  Contact Sales
                </Button>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Final CTA Section */}
      <section className="py-20 bg-gradient-to-r from-blue-600 to-purple-600">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">
            Ready to Scale Your Ads Faster, Smarter, and With Less Work?
          </h2>
          <p className="text-xl text-blue-100 mb-8">
            You can get started in just 30-60 seconds and have the tool create winning ads every day, 
            week or month for you automatically.
          </p>
          <p className="text-lg text-blue-100 mb-8">
            Which means you're now able to scale your ads faster, smarter, and with less work. 
            So you can have the freedom and have more choices to do whatever you want whenever you want 
            and never worry about creating new ads again.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <Button 
              size="lg" 
              className="bg-white text-blue-600 hover:bg-gray-100 text-lg px-8 py-4 h-auto"
            >
              <Rocket className="w-5 h-5 mr-2" />
              Start Your Free Trial Now
            </Button>
            <Button 
              variant="outline" 
              size="lg" 
              className="border-white text-white hover:bg-white hover:text-blue-600 text-lg px-8 py-4 h-auto"
            >
              Schedule a Demo
            </Button>
          </div>
          <p className="text-sm text-blue-200 mt-6">
            The choice is yours... Join 10,000+ marketers already saving time and money.
          </p>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center space-x-2 mb-4">
                <div className="w-8 h-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
                  <Zap className="w-5 h-5 text-white" />
                </div>
                <span className="text-xl font-bold">Automatic Ads</span>
              </div>
              <p className="text-gray-400">
                AI-powered competitor ad intelligence platform that helps businesses create winning ads in seconds.
              </p>
            </div>
            <div>
              <h3 className="font-semibold mb-4">Product</h3>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-white transition-colors">Features</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Pricing</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Templates</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Integrations</a></li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold mb-4">Company</h3>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-white transition-colors">About</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Blog</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Careers</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Contact</a></li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold mb-4">Support</h3>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-white transition-colors">Help Center</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Documentation</a></li>
                <li><a href="#" className="hover:text-white transition-colors">API Reference</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Status</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400">
            <p>&copy; 2025 Automatic Ads. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}

export default App

