from flask import Flask, render_template_string, send_from_directory, url_for
import os

app = Flask(__name__, static_folder='static')

# Serve static files (images)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

# Test route to check if image exists
@app.route('/test-image')
def test_image():
    image_path = os.path.join(app.static_folder, 'images', 'profile.jpg')
    alt_path = os.path.join(app.static_folder, 'profile.jpg')
    
    result = "<h2>🔍 Image Debug Information</h2>"
    result += f"<p><strong>App static folder:</strong> {app.static_folder}</p>"
    result += f"<p><strong>Current working directory:</strong> {os.getcwd()}</p>"
    
    if os.path.exists(image_path):
        result += f"<p>✅ <strong>Image found at:</strong> {image_path}</p>"
        result += f"<p>📊 <strong>File size:</strong> {os.path.getsize(image_path)} bytes</p>"
    elif os.path.exists(alt_path):
        result += f"<p>✅ <strong>Image found at:</strong> {alt_path}</p>"
        result += f"<p>📊 <strong>File size:</strong> {os.path.getsize(alt_path)} bytes</p>"
    else:
        result += f"<p>❌ <strong>Image NOT found at:</strong> {image_path}</p>"
        result += f"<p>❌ <strong>Also checked:</strong> {alt_path}</p>"
        
        # List what files exist in static folder
        if os.path.exists(app.static_folder):
            result += f"<p><strong>Files in static folder:</strong></p><ul>"
            for root, dirs, files in os.walk(app.static_folder):
                for file in files:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, app.static_folder)
                    result += f"<li>{rel_path}</li>"
            result += "</ul>"
    
    result += "<hr>"
    result += "<p><strong>Try these URLs:</strong></p>"
    result += "<ul>"
    result += "<li><a href='/static/images/profile.jpg'>/static/images/profile.jpg</a></li>"
    result += "<li><a href='/static/profile.jpg'>/static/profile.jpg</a></li>"
    result += "</ul>"
    
    return result

# Debug route for testing animations
@app.route('/debug')
def debug():
    return '''
    <h2>🔧 Portfolio Debug</h2>
    <p>✅ Flask app is running correctly</p>
    <p>✅ Routes are working</p>
    <p>📊 <strong>Portfolio Data loaded:</strong></p>
    <ul>
        <li>Name: ''' + PORTFOLIO_DATA['name'] + '''</li>
        <li>Experience items: ''' + str(len(PORTFOLIO_DATA['experience'])) + '''</li>
        <li>Projects: ''' + str(len(PORTFOLIO_DATA['projects'])) + '''</li>
        <li>Skills categories: ''' + str(len(PORTFOLIO_DATA['skills_data'])) + '''</li>
    </ul>
    <hr>
    <p><a href="/">← Back to Portfolio</a></p>
    '''

# Ultra-Advanced Portfolio Template with High-End Features
ADVANCED_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ name }} - Advanced Data Engineer Portfolio</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <script>
        // Fallback for Chart.js loading - Not needed anymore
        // if (typeof Chart === 'undefined') {
        //     const script = document.createElement('script');
        //     script.src = 'https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.min.js';
        //     document.head.appendChild(script);
        // }
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        :root {
            --primary: #00d4ff;
            --secondary: #ff006e;
            --accent: #8338ec;
            --success: #06ffa5;
            --warning: #ffbe0b;
            --dark: #0a0a0a;
            --card-bg: rgba(255, 255, 255, 0.05);
            --glass-border: rgba(255, 255, 255, 0.1);
            --text-primary: #ffffff;
            --text-secondary: rgba(255, 255, 255, 0.7);
            --gradient-1: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --gradient-2: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            --gradient-3: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            --gradient-4: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: #0a0a0a;
            color: var(--text-primary);
            overflow-x: hidden;
            line-height: 1.6;
        }

        /* Dynamic Background with Mesh Gradient */
        .mesh-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            background: radial-gradient(circle at 20% 80%, #120033 0%, transparent 50%),
                        radial-gradient(circle at 80% 20%, #000428 0%, transparent 50%),
                        radial-gradient(circle at 40% 40%, #2a0845 0%, transparent 50%),
                        linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
            animation: meshShift 20s ease infinite;
        }

        @keyframes meshShift {
            0%, 100% { filter: hue-rotate(0deg); }
            50% { filter: hue-rotate(90deg); }
        }

        /* 3D Floating Elements */
        .floating-elements {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        }

        .float-element {
            position: absolute;
            width: 4px;
            height: 4px;
            background: var(--primary);
            border-radius: 50%;
            animation: float3d 15s infinite ease-in-out;
            box-shadow: 0 0 20px var(--primary);
        }

        .float-element:nth-child(2n) { background: var(--secondary); box-shadow: 0 0 20px var(--secondary); animation-delay: -5s; }
        .float-element:nth-child(3n) { background: var(--accent); box-shadow: 0 0 20px var(--accent); animation-delay: -10s; }

        @keyframes float3d {
            0%, 100% { transform: translate3d(0, 100vh, 0) rotateY(0deg); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            50% { transform: translate3d(calc(100vw * var(--random-x, 0.5)), -100px, 50px) rotateY(360deg); }
        }

        /* Navigation */
        .nav-container {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000;
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 50px;
            padding: 0.5rem;
        }

        .nav {
            display: flex;
            gap: 0.5rem;
        }

        .nav-item {
            padding: 0.8rem 1.5rem;
            border-radius: 25px;
            text-decoration: none;
            color: var(--text-secondary);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            white-space: nowrap;
        }

        .nav-item:hover, .nav-item.active {
            color: var(--text-primary);
            background: var(--primary);
            transform: scale(1.05);
            box-shadow: 0 5px 20px rgba(0, 212, 255, 0.3);
        }

        /* Hero Section with 3D Elements */
        .hero {
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }

        .hero-content {
            text-align: center;
            z-index: 2;
            max-width: 800px;
            padding: 2rem;
        }

        .hero-avatar {
            width: 200px;
            height: 200px;
            margin: 0 auto 2rem;
            position: relative;
            perspective: 1000px;
        }

        .avatar-container {
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            animation: rotate3d 20s infinite linear;
        }

        .avatar-ring {
            position: absolute;
            border: 2px solid var(--primary);
            border-radius: 50%;
            animation: ringRotate 10s infinite linear;
        }

        .avatar-ring:nth-child(1) { width: 100%; height: 100%; border-color: var(--primary); }
        .avatar-ring:nth-child(2) { width: 120%; height: 120%; top: -10%; left: -10%; border-color: var(--secondary); animation-delay: -2s; }
        .avatar-ring:nth-child(3) { width: 140%; height: 140%; top: -20%; left: -20%; border-color: var(--accent); animation-delay: -4s; }

        @keyframes rotate3d {
            from { transform: rotateY(0deg) rotateX(15deg); }
            to { transform: rotateY(360deg) rotateX(15deg); }
        }

        @keyframes ringRotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(-360deg); }
        }

        .avatar-core {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 160px;
            height: 160px;
            background: var(--gradient-3);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
            box-shadow: 0 0 50px rgba(0, 212, 255, 0.5);
            animation: pulse 2s ease-in-out infinite alternate;
            background-image: url('data:image/jpeg;base64,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');
            background-size: cover;
            background-position: center;
            border: 4px solid rgba(255, 255, 255, 0.2);
        }

        @keyframes pulse {
            0% { box-shadow: 0 0 50px rgba(0, 212, 255, 0.5); }
            100% { box-shadow: 0 0 80px rgba(0, 212, 255, 0.8), 0 0 120px rgba(0, 212, 255, 0.3); }
        }

        .hero h1 {
            font-size: clamp(3rem, 8vw, 6rem);
            font-weight: 900;
            margin-bottom: 1rem;
            background: linear-gradient(45deg, var(--primary), var(--secondary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: textShimmer 3s ease-in-out infinite;
        }

        @keyframes textShimmer {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .hero .tagline {
            font-size: 1.5rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
            animation: fadeInUp 1s ease-out 0.5s both;
        }

        .hero .cta-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        .cta-btn {
            padding: 1rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            border: 2px solid transparent;
        }

        .cta-btn.primary {
            background: var(--gradient-3);
            color: white;
        }

        .cta-btn.secondary {
            background: transparent;
            border-color: var(--primary);
            color: var(--primary);
        }

        .cta-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
        }

        /* Stats Counter */
        .stats-section {
            padding: 6rem 2rem;
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            margin: 2rem;
            border-radius: 20px;
            border: 1px solid var(--glass-border);
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 3rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .stat-item {
            text-align: center;
            position: relative;
        }

        .stat-number {
            font-size: 3rem;
            font-weight: 900;
            color: var(--primary);
            display: block;
            font-family: 'JetBrains Mono', monospace;
        }

        .stat-label {
            font-size: 1.1rem;
            color: var(--text-secondary);
            margin-top: 0.5rem;
        }

        .section-title {
            font-size: 3rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 4rem;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* Enhanced Skills Visualization */
        .skills-section {
            padding: 6rem 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }

        .skills-container {
            display: block;
            width: 100%;
        }

        /* Skills Progress Bars */
        .skills-progress {
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 3rem;
            margin-bottom: 3rem;
            width: 100%;
            max-width: 1000px;
            margin-left: auto;
            margin-right: auto;
        }

        .skills-progress h3 {
            color: var(--text-primary);
            font-size: 1.8rem;
            margin-bottom: 2rem;
            text-align: center;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .skill-progress-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            transition: all 0.3s ease;
        }

        .skill-progress-item:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: translateX(10px);
        }

        .skill-info {
            display: flex;
            flex-direction: column;
            flex: 1;
        }

        .skill-name {
            color: var(--text-primary);
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }

        .skill-bar-container {
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            overflow: hidden;
            position: relative;
        }

        .skill-bar {
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            border-radius: 10px;
            position: relative;
            transition: width 2.5s cubic-bezier(0.4, 0, 0.2, 1);
            width: 0%;
        }

        .skill-bar::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            width: 30px;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
            animation: shimmer 2s infinite;
        }

        @keyframes shimmer {
            0% { transform: translateX(-30px); }
            100% { transform: translateX(200px); }
        }

        .skill-percentage {
            color: var(--primary);
            font-weight: 700;
            font-size: 1rem;
            margin-left: 1rem;
            min-width: 40px;
            text-align: right;
            font-family: 'JetBrains Mono', monospace;
        }

        /* Enhanced Skills Cloud */
        .skills-cloud {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .skill-category {
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .skill-category::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
        }

        .skill-category:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
        }

        .skill-category h4 {
            color: var(--text-primary);
            font-size: 1.3rem;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .skill-category-icon {
            width: 30px;
            height: 30px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 0.9rem;
        }

        .skill-tags-container {
            display: flex;
            flex-wrap: wrap;
            gap: 0.8rem;
        }

        .skill-tag {
            padding: 0.6rem 1.2rem;
            background: rgba(6, 182, 212, 0.1);
            border: 1px solid rgba(6, 182, 212, 0.3);
            border-radius: 20px;
            color: var(--primary);
            font-weight: 500;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .skill-tag::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s;
        }

        .skill-tag:hover::before {
            left: 100%;
        }

        .skill-tag:hover {
            transform: translateY(-3px) scale(1.05);
            border-color: var(--primary);
            box-shadow: 0 8px 20px rgba(6, 182, 212, 0.3);
            background: rgba(6, 182, 212, 0.2);
        }

        .skill-tag.expert { 
            border-color: var(--success); 
            color: var(--success);
            background: rgba(6, 255, 165, 0.1);
        }
        .skill-tag.expert:hover { 
            border-color: var(--success);
            background: rgba(6, 255, 165, 0.2);
            box-shadow: 0 8px 20px rgba(6, 255, 165, 0.3);
        }

        .skill-tag.advanced { 
            border-color: var(--primary); 
            color: var(--primary);
        }

        .skill-tag.intermediate { 
            border-color: var(--warning); 
            color: var(--warning);
            background: rgba(255, 190, 11, 0.1);
        }
        .skill-tag.intermediate:hover { 
            border-color: var(--warning);
            background: rgba(255, 190, 11, 0.2);
            box-shadow: 0 8px 20px rgba(255, 190, 11, 0.3);
        }

        /* Experience Timeline */
        .experience-section {
            padding: 6rem 2rem;
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            margin: 2rem;
            border-radius: 20px;
            border: 1px solid var(--glass-border);
        }

        .timeline {
            max-width: 1000px;
            margin: 0 auto;
            position: relative;
        }

        .timeline::before {
            content: '';
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(180deg, var(--primary), var(--secondary), var(--accent));
            transform: translateX(-50%);
        }

        .timeline-item {
            position: relative;
            margin: 3rem 0;
            opacity: 0;
            animation: slideInTimeline 0.8s ease-out forwards;
        }

        .timeline-item:nth-child(odd) {
            text-align: right;
            padding-right: calc(50% + 2rem);
        }

        .timeline-item:nth-child(even) {
            text-align: left;
            padding-left: calc(50% + 2rem);
        }

        .timeline-content {
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 15px;
            padding: 2rem;
            position: relative;
            transition: all 0.3s ease;
        }

        .timeline-content:hover {
            transform: scale(1.02);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }

        .timeline-dot {
            position: absolute;
            left: 50%;
            top: 2rem;
            width: 20px;
            height: 20px;
            background: var(--primary);
            border-radius: 50%;
            transform: translateX(-50%);
            box-shadow: 0 0 20px var(--primary);
            animation: pulse 2s ease-in-out infinite;
        }

        @keyframes slideInTimeline {
            from { opacity: 0; transform: translateY(50px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Projects Grid */
        .projects-section {
            padding: 6rem 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2rem;
        }

        .project-card {
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .project-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: var(--gradient-3);
        }

        .project-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }

        .project-icon {
            width: 60px;
            height: 60px;
            background: var(--gradient-3);
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .project-title {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color: var(--text-primary);
        }

        .project-description {
            color: var(--text-secondary);
            margin-bottom: 1.5rem;
            line-height: 1.6;
        }

        .project-tech {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
        }

        .tech-badge {
            padding: 0.3rem 0.8rem;
            background: rgba(0, 212, 255, 0.1);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 15px;
            font-size: 0.8rem;
            color: var(--primary);
        }

        .project-metrics {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1rem;
            margin-top: 1rem;
        }

        .metric {
            text-align: center;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
        }

        .metric-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--success);
            font-family: 'JetBrains Mono', monospace;
        }

        .metric-label {
            font-size: 0.8rem;
            color: var(--text-secondary);
            margin-top: 0.5rem;
        }

        /* Contact Section */
        .contact-section {
            padding: 6rem 2rem;
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            margin: 2rem;
            border-radius: 20px;
            border: 1px solid var(--glass-border);
        }

        .contact-container {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }

        .contact-methods {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .contact-method {
            padding: 2rem;
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 15px;
            transition: all 0.3s ease;
            text-decoration: none;
            color: inherit;
        }

        .contact-method:hover {
            transform: translateY(-5px);
            border-color: var(--primary);
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.2);
        }

        .contact-icon {
            width: 60px;
            height: 60px;
            background: var(--gradient-3);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1rem;
            font-size: 1.5rem;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-container {
                width: 90%;
                padding: 0.3rem;
            }
            
            .nav {
                justify-content: center;
                flex-wrap: wrap;
                gap: 0.3rem;
            }
            
            .nav-item {
                padding: 0.6rem 1rem;
                font-size: 0.9rem;
            }

            .hero h1 {
                font-size: 3rem;
            }

            .skills-container {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .skills-charts {
                grid-template-columns: 1fr;
            }

            .timeline::before {
                left: 20px;
            }

            .timeline-item {
                text-align: left !important;
                padding-left: 3rem !important;
                padding-right: 0 !important;
            }

            .timeline-dot {
                left: 20px;
                transform: translateX(-50%);
            }

            .projects-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Loading Animation */
        .loading-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: var(--dark);
            z-index: 9999;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 1;
            transition: opacity 0.5s ease;
        }

        .loading-spinner {
            width: 80px;
            height: 80px;
            border: 4px solid rgba(0, 212, 255, 0.1);
            border-left: 4px solid var(--primary);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .loaded .loading-overlay {
            opacity: 0;
            pointer-events: none;
        }

        /* Smooth Scrolling */
        html {
            scroll-behavior: smooth;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: var(--dark);
        }

        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, var(--primary), var(--secondary));
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(180deg, var(--secondary), var(--accent));
        }
    </style>
</head>
<body>
    <!-- Loading Overlay -->
    <div class="loading-overlay">
        <div class="loading-spinner"></div>
    </div>

    <!-- Dynamic Background -->
    <div class="mesh-background"></div>
    
    <!-- Floating Elements -->
    <div class="floating-elements" id="floatingElements"></div>

    <!-- Navigation -->
    <div class="nav-container">
        <nav class="nav">
            <a href="#hero" class="nav-item active">Home</a>
            <a href="#stats" class="nav-item">Stats</a>
            <a href="#skills" class="nav-item">Skills</a>
            <a href="#experience" class="nav-item">Experience</a>
            <a href="#projects" class="nav-item">Projects</a>
            <a href="#contact" class="nav-item">Contact</a>
        </nav>
    </div>

    <!-- Hero Section -->
    <section id="hero" class="hero">
        <div class="hero-content">
            <div class="hero-avatar">
                <div class="avatar-container">
                    <div class="avatar-ring"></div>
                    <div class="avatar-ring"></div>
                    <div class="avatar-ring"></div>
                    <div class="avatar-core" id="profileAvatar">
                        <i class="fas fa-database" id="fallbackIcon"></i>
                    </div>
                </div>
            </div>
            <h1>{{ name }}</h1>
            <p class="tagline">{{ tagline }}</p>
            <div class="cta-buttons">
                <a href="#projects" class="cta-btn primary">
                    <i class="fas fa-rocket"></i> View My Work
                </a>
                <a href="#contact" class="cta-btn secondary">
                    <i class="fas fa-envelope"></i> Get In Touch
                </a>
            </div>
        </div>
    </section>

    <!-- Stats Section -->
    <section id="stats" class="stats-section">
        <div class="stats-grid">
            <div class="stat-item">
                <span class="stat-number" data-count="4">0</span>
                <div class="stat-label">Years Experience</div>
            </div>
            <div class="stat-item">
                <span class="stat-number" data-count="15">0</span>
                <div class="stat-label">TB Data Migrated</div>
            </div>
            <div class="stat-item">
                <span class="stat-number" data-count="10">0</span>
                <div class="stat-label">M+ Daily Transactions</div>
            </div>
            <div class="stat-item">
                <span class="stat-number" data-count="99.9">0</span>
                <div class="stat-label">% Data Accuracy</div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="skills-section">
        <h2 class="section-title">Technical Expertise</h2>
        
        <!-- Skills Progress Bars -->
        <div class="skills-progress">
            <h3><i class="fas fa-chart-line"></i> Core Competencies</h3>
            <div class="skill-progress-item">
                <div class="skill-info">
                    <div class="skill-name">Python & Data Engineering</div>
                    <div class="skill-bar-container">
                        <div class="skill-bar" data-width="95"></div>
                    </div>
                </div>
                <div class="skill-percentage">95%</div>
            </div>
            <div class="skill-progress-item">
                <div class="skill-info">
                    <div class="skill-name">AWS Cloud Architecture</div>
                    <div class="skill-bar-container">
                        <div class="skill-bar" data-width="90"></div>
                    </div>
                </div>
                <div class="skill-percentage">90%</div>
            </div>
            <div class="skill-progress-item">
                <div class="skill-info">
                    <div class="skill-name">Apache Spark & Big Data</div>
                    <div class="skill-bar-container">
                        <div class="skill-bar" data-width="88"></div>
                    </div>
                </div>
                <div class="skill-percentage">88%</div>
            </div>
            <div class="skill-progress-item">
                <div class="skill-info">
                    <div class="skill-name">Real-time Data Processing</div>
                    <div class="skill-bar-container">
                        <div class="skill-bar" data-width="85"></div>
                    </div>
                </div>
                <div class="skill-percentage">85%</div>
            </div>
            <div class="skill-progress-item">
                <div class="skill-info">
                    <div class="skill-name">Database Design & Optimization</div>
                    <div class="skill-bar-container">
                        <div class="skill-bar" data-width="92"></div>
                    </div>
                </div>
                <div class="skill-percentage">92%</div>
            </div>
        </div>

        <div class="skills-container">
            <div class="skills-cloud">
                <div class="skill-category">
                    <h4>
                        <div class="skill-category-icon"><i class="fab fa-python"></i></div>
                        Programming & Frameworks
                    </h4>
                    <div class="skill-tags-container">
                        <span class="skill-tag expert">Python</span>
                        <span class="skill-tag expert">PySpark</span>
                        <span class="skill-tag expert">Apache Spark</span>
                        <span class="skill-tag expert">SQL</span>
                        <span class="skill-tag advanced">Machine Learning</span>
                    </div>
                </div>
                
                <div class="skill-category">
                    <h4>
                        <div class="skill-category-icon"><i class="fas fa-cloud"></i></div>
                        Cloud & Big Data
                    </h4>
                    <div class="skill-tags-container">
                        <span class="skill-tag expert">AWS</span>
                        <span class="skill-tag expert">Azure</span>
                        <span class="skill-tag expert">Databricks</span>
                        <span class="skill-tag expert">Kafka</span>
                        <span class="skill-tag expert">Airflow</span>
                        <span class="skill-tag advanced">DBT</span>
                    </div>
                </div>
                
                <div class="skill-category">
                    <h4>
                        <div class="skill-category-icon"><i class="fas fa-database"></i></div>
                        Databases
                    </h4>
                    <div class="skill-tags-container">
                        <span class="skill-tag expert">PostgreSQL</span>
                        <span class="skill-tag expert">Snowflake</span>
                        <span class="skill-tag advanced">MongoDB</span>
                        <span class="skill-tag expert">AWS Aurora</span>
                        <span class="skill-tag expert">Redshift</span>
                    </div>
                </div>
                
                <div class="skill-category">
                    <h4>
                        <div class="skill-category-icon"><i class="fas fa-tools"></i></div>
                        DevOps & Tools
                    </h4>
                    <div class="skill-tags-container">
                        <span class="skill-tag advanced">Docker</span>
                        <span class="skill-tag advanced">Terraform</span>
                        <span class="skill-tag advanced">Kubernetes</span>
                        <span class="skill-tag expert">Glue</span>
                        <span class="skill-tag expert">Athena</span>
                    </div>
                </div>
                
                <div class="skill-category">
                    <h4>
                        <div class="skill-category-icon"><i class="fas fa-chart-bar"></i></div>
                        Analytics & BI
                    </h4>
                    <div class="skill-tags-container">
                        <span class="skill-tag advanced">PowerBI</span>
                        <span class="skill-tag advanced">Tableau</span>
                        <span class="skill-tag intermediate">Iceberg</span>
                        <span class="skill-tag expert">Delta Lake</span>
                        <span class="skill-tag advanced">Unity Catalog</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Experience Timeline -->
    <section id="experience" class="experience-section">
        <h2 class="section-title">Professional Journey</h2>
        <div class="timeline">
            {% for exp in experience %}
            <div class="timeline-item" style="animation-delay: {{ loop.index0 * 0.2 }}s;">
                <div class="timeline-dot"></div>
                <div class="timeline-content">
                    <h3>{{ exp.title }}</h3>
                    <div class="experience-meta">{{ exp.company }} | {{ exp.period }}</div>
                    <p>{{ exp.description }}</p>
                    <ul>
                        {% for achievement in exp.achievements %}
                        <li>{{ achievement }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
            {% endfor %}
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects-section">
        <h2 class="section-title">Featured Projects</h2>
        <div class="projects-grid">
            {% for project in projects %}
            <div class="project-card">
                <div class="project-icon">
                    <i class="{{ project.icon }}"></i>
                </div>
                <h3 class="project-title">{{ project.name }}</h3>
                <p class="project-description">{{ project.description }}</p>
                <div class="project-tech">
                    {% for tech in project.technologies %}
                    <span class="tech-badge">{{ tech }}</span>
                    {% endfor %}
                </div>
                <div class="project-metrics">
                    {% for metric in project.metrics %}
                    <div class="metric">
                        <div class="metric-value">{{ metric.value }}</div>
                        <div class="metric-label">{{ metric.label }}</div>
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% endfor %}
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact-section">
        <div class="contact-container">
            <h2 class="section-title">Let's Build Something Amazing</h2>
            <p style="font-size: 1.2rem; color: var(--text-secondary); margin-bottom: 2rem;">
                Ready to discuss your next data engineering project? Let's connect!
            </p>
            <div class="contact-methods">
                <a href="mailto:{{ contact.email }}" class="contact-method">
                    <div class="contact-icon">
                        <i class="fas fa-envelope"></i>
                    </div>
                    <h4>Email</h4>
                    <p>{{ contact.email }}</p>
                </a>
                <a href="{{ contact.linkedin }}" target="_blank" class="contact-method">
                    <div class="contact-icon">
                        <i class="fab fa-linkedin"></i>
                    </div>
                    <h4>LinkedIn</h4>
                    <p>Connect professionally</p>
                </a>
                <a href="tel:{{ contact.phone }}" class="contact-method">
                    <div class="contact-icon">
                        <i class="fas fa-phone"></i>
                    </div>
                    <h4>Phone</h4>
                    <p>{{ contact.phone }}</p>
                </a>
                <div class="contact-method">
                    <div class="contact-icon">
                        <i class="fas fa-map-marker-alt"></i>
                    </div>
                    <h4>Location</h4>
                    <p>{{ contact.location }}</p>
                </div>
            </div>
        </div>
    </section>

    <script>
        // Initialize the page
        document.addEventListener('DOMContentLoaded', function() {
            console.log('🚀 Portfolio loading...');
            
            // Load profile image
            loadProfileImage();
            
            // Remove loading overlay
            setTimeout(() => {
                document.body.classList.add('loaded');
                console.log('✅ Loading overlay removed');
            }, 1500);

            // Generate floating elements
            generateFloatingElements();
            console.log('✅ Floating elements generated');
            
            // Setup navigation
            setupNavigation();
            console.log('✅ Navigation setup complete');
            
            // Setup counters
            setupCounters();
            console.log('✅ Counters setup complete');
            
            // Setup skill progress bars
            setupSkillBars();
            console.log('✅ Skill bars setup complete');
            
            // Setup intersection observer for animations
            setupScrollAnimations();
            console.log('✅ Scroll animations setup complete');
            
            console.log('🎉 Portfolio initialization complete!');
        });

        // Setup skill progress bars animation
        function setupSkillBars() {
            const skillBars = document.querySelectorAll('.skill-bar');
            console.log(`Found ${skillBars.length} skill bars to animate`);
            
            const animateSkillBar = (bar) => {
                const targetWidth = bar.dataset.width;
                console.log(`Animating skill bar to ${targetWidth}%`);
                setTimeout(() => {
                    bar.style.width = targetWidth + '%';
                }, 300);
            };
            
            // Trigger animation when in view
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !entry.target.dataset.animated) {
                        console.log('Skill bar entered view, starting animation');
                        entry.target.dataset.animated = 'true';
                        animateSkillBar(entry.target);
                    }
                });
            }, { threshold: 0.2 });
            
            skillBars.forEach((bar, index) => {
                bar.style.width = '0%'; // Start from 0
                console.log(`Setting up observer for skill bar ${index + 1}: ${bar.dataset.width}%`);
                observer.observe(bar);
            });
        }

        // Load profile image with multiple fallback attempts
        function loadProfileImage() {
            const avatar = document.getElementById('profileAvatar');
            const fallbackIcon = document.getElementById('fallbackIcon');
            
            // Try multiple image paths
            const imagePaths = [
                '/static/images/profile.jpg',
                './static/images/profile.jpg',
                'static/images/profile.jpg',
                '/static/profile.jpg'
            ];
            
            let imageLoaded = false;
            let currentPath = 0;
            
            function tryNextImage() {
                if (currentPath >= imagePaths.length || imageLoaded) {
                    if (!imageLoaded) {
                        console.log('Profile image not found in any location, using fallback icon');
                        fallbackIcon.style.display = 'flex';
                        avatar.style.color = 'white';
                    }
                    return;
                }
                
                const img = new Image();
                img.onload = function() {
                    // Image loaded successfully
                    imageLoaded = true;
                    avatar.style.backgroundImage = `url(${imagePaths[currentPath]})`;
                    avatar.classList.add('image-loaded');
                    fallbackIcon.style.display = 'none';
                    console.log(`✅ Profile image loaded from: ${imagePaths[currentPath]}`);
                };
                img.onerror = function() {
                    console.log(`❌ Failed to load: ${imagePaths[currentPath]}`);
                    // Try next path
                    currentPath++;
                    tryNextImage();
                };
                img.src = imagePaths[currentPath];
            }
            
            tryNextImage();
        }

        // Generate floating elements
        function generateFloatingElements() {
            const container = document.getElementById('floatingElements');
            for (let i = 0; i < 50; i++) {
                const element = document.createElement('div');
                element.className = 'float-element';
                element.style.left = Math.random() * 100 + '%';
                element.style.animationDelay = Math.random() * 15 + 's';
                element.style.setProperty('--random-x', Math.random());
                container.appendChild(element);
            }
        }

        // Initialize charts
        function initializeCharts() {
            // Wait for Chart.js to be fully loaded
            if (typeof Chart === 'undefined') {
                setTimeout(initializeCharts, 100);
                return;
            }

            // Skills Chart
            const skillsCanvas = document.getElementById('skillsChart');
            if (skillsCanvas) {
                const skillsCtx = skillsCanvas.getContext('2d');
                new Chart(skillsCtx, {
                    type: 'radar',
                    data: {
                        labels: ['Python', 'AWS', 'Spark', 'Kafka', 'ML', 'SQL'],
                        datasets: [{
                            label: 'Skill Level',
                            data: [95, 90, 85, 80, 75, 95],
                            backgroundColor: 'rgba(0, 212, 255, 0.2)',
                            borderColor: '#00d4ff',
                            pointBackgroundColor: '#00d4ff',
                            pointBorderColor: '#fff',
                            pointHoverBackgroundColor: '#fff',
                            pointHoverBorderColor: '#00d4ff',
                            borderWidth: 2
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { display: false }
                        },
                        scales: {
                            r: {
                                beginAtZero: true,
                                max: 100,
                                ticks: { 
                                    display: false,
                                    stepSize: 20
                                },
                                grid: { color: 'rgba(255, 255, 255, 0.2)' },
                                pointLabels: { 
                                    color: '#ffffff',
                                    font: { size: 12 }
                                }
                            }
                        }
                    }
                });
            }

            // Experience Chart
            const expCanvas = document.getElementById('experienceChart');
            if (expCanvas) {
                const expCtx = expCanvas.getContext('2d');
                new Chart(expCtx, {
                    type: 'doughnut',
                    data: {
                        labels: ['Data Engineering', 'Cloud Architecture', 'Database Admin', 'ML/Analytics'],
                        datasets: [{
                            data: [40, 30, 20, 10],
                            backgroundColor: ['#00d4ff', '#ff006e', '#8338ec', '#06ffa5'],
                            borderWidth: 2,
                            borderColor: '#0a0a0a'
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { 
                                position: 'bottom',
                                labels: { 
                                    color: '#ffffff',
                                    font: { size: 11 },
                                    padding: 15
                                }
                            }
                        }
                    }
                });
            }

            // Projects Chart
            const projCanvas = document.getElementById('projectsChart');
            if (projCanvas) {
                const projCtx = projCanvas.getContext('2d');
                new Chart(projCtx, {
                    type: 'bar',
                    data: {
                        labels: ['ETL Pipelines', 'Real-time', 'Migration', 'Analytics'],
                        datasets: [{
                            label: 'Projects Completed',
                            data: [12, 8, 5, 10],
                            backgroundColor: 'rgba(0, 212, 255, 0.8)',
                            borderColor: '#00d4ff',
                            borderWidth: 1,
                            borderRadius: 5
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { display: false }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                ticks: { 
                                    color: '#ffffff',
                                    font: { size: 11 }
                                },
                                grid: { color: 'rgba(255, 255, 255, 0.1)' }
                            },
                            x: {
                                ticks: { 
                                    color: '#ffffff',
                                    font: { size: 10 }
                                },
                                grid: { color: 'rgba(255, 255, 255, 0.1)' }
                            }
                        }
                    }
                });
            }

            // Cloud Growth Chart
            const cloudCanvas = document.getElementById('cloudChart');
            if (cloudCanvas) {
                const cloudCtx = cloudCanvas.getContext('2d');
                new Chart(cloudCtx, {
                    type: 'line',
                    data: {
                        labels: ['2020', '2021', '2022', '2023', '2024'],
                        datasets: [{
                            label: 'Data Processed (TB)',
                            data: [5, 12, 25, 45, 70],
                            borderColor: '#00d4ff',
                            backgroundColor: 'rgba(0, 212, 255, 0.2)',
                            fill: true,
                            tension: 0.4,
                            borderWidth: 3,
                            pointBackgroundColor: '#00d4ff',
                            pointBorderColor: '#fff',
                            pointBorderWidth: 2
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { display: false }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                ticks: { 
                                    color: '#ffffff',
                                    font: { size: 11 }
                                },
                                grid: { color: 'rgba(255, 255, 255, 0.1)' }
                            },
                            x: {
                                ticks: { 
                                    color: '#ffffff',
                                    font: { size: 11 }
                                },
                                grid: { color: 'rgba(255, 255, 255, 0.1)' }
                            }
                        }
                    }
                });
            }
        }

        // Setup navigation
        function setupNavigation() {
            const navItems = document.querySelectorAll('.nav-item');
            
            navItems.forEach(item => {
                item.addEventListener('click', function(e) {
                    e.preventDefault();
                    navItems.forEach(nav => nav.classList.remove('active'));
                    this.classList.add('active');
                    
                    const target = document.querySelector(this.getAttribute('href'));
                    target.scrollIntoView({ behavior: 'smooth' });
                });
            });
        }

        // Setup counters
        function setupCounters() {
            const counters = document.querySelectorAll('[data-count]');
            console.log(`Found ${counters.length} counters to animate`);
            
            const animateCounter = (counter) => {
                const target = parseFloat(counter.dataset.count);
                console.log(`Animating counter to ${target}`);
                const increment = target / 50;
                let current = 0;
                
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        if (target % 1 === 0) {
                            counter.textContent = Math.floor(target);
                        } else {
                            counter.textContent = target.toFixed(1);
                        }
                        console.log(`Counter animation complete: ${target}`);
                        clearInterval(timer);
                    } else {
                        if (target % 1 === 0) {
                            counter.textContent = Math.floor(current);
                        } else {
                            counter.textContent = current.toFixed(1);
                        }
                    }
                }, 40);
            };
            
            // Trigger animation when in view
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !entry.target.dataset.animated) {
                        console.log('Counter entered view, starting animation');
                        entry.target.dataset.animated = 'true';
                        // Force start animation immediately
                        animateCounter(entry.target);
                    }
                });
            }, { threshold: 0.3 });
            
            counters.forEach((counter, index) => {
                counter.textContent = '0'; // Reset to 0
                console.log(`Setting up observer for counter ${index + 1}: ${counter.dataset.count}`);
                observer.observe(counter);
            });
        }

        // Setup scroll animations
        function setupScrollAnimations() {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            }, { threshold: 0.1 });

            document.querySelectorAll('.timeline-item, .project-card, .skill-tag').forEach(el => {
                el.style.opacity = '0';
                el.style.transform = 'translateY(50px)';
                el.style.transition = 'all 0.8s ease';
                observer.observe(el);
            });
        }

        // Add parallax effect
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const parallax = document.querySelector('.mesh-background');
            const speed = scrolled * 0.5;
            parallax.style.transform = `translateY(${speed}px)`;
        });
    </script>
</body>
</html>'''

# Sobin Babu's Portfolio Data (Based on Resume)
PORTFOLIO_DATA = {
    'name': 'Sobin Babu',
    'tagline': '🚀 Senior Data Engineer | Cloud Data Specialist | 4+ Years Building Scalable Data Solutions',
    'skills_data': {
        'Programming & Frameworks': ['Python', 'PySpark', 'Apache Spark', 'SQL', 'Machine Learning'],
        'Cloud & Big Data': ['AWS', 'Azure', 'Databricks', 'Kafka', 'Airflow', 'DBT'],
        'Databases': ['PostgreSQL', 'Snowflake', 'MongoDB', 'AWS Aurora', 'Redshift'],
        'DevOps & Tools': ['Docker', 'Terraform', 'Kubernetes', 'Glue', 'Athena'],
        'Analytics & BI': ['PowerBI', 'Tableau', 'Iceberg', 'Delta Lake', 'Unity Catalog']
    },
    'experience': [
        {
            'title': 'Senior Consultant Data Engineer',
            'company': 'IBS Software Ltd., UK',
            'period': 'Nov 2021 – Feb 2025',
            'description': 'Leading data engineering initiatives for airline loyalty systems, processing 10M+ daily transactions with 99.9% accuracy.',
            'achievements': [
                'Built Kafka-Spark pipeline processing 10M+ daily transactions with 99.9% accuracy',
                'Designed serverless batch pipeline reducing ingestion failures by 85%',
                'Implemented real-time Databricks pipeline improving campaign responsiveness by 60%',
                'Optimized Snowflake ELT pipeline reducing reporting latency by 70%',
                'Automated data validation reducing downstream issues by 50%'
            ]
        },
        {
            'title': 'Database Architect',
            'company': 'IBS Software (India) & Cognizant',
            'period': '2011 – 2021',
            'description': 'Administered enterprise databases and led major data migration projects with zero downtime.',
            'achievements': [
                'Led migration of 15+ TB airline data to AWS Aurora with zero downtime',
                'Achieved 30% improvement in query performance post-migration',
                'Administered PostgreSQL and AWS Aurora for transactional workloads',
                'Created interactive Tableau dashboards for data-driven insights',
                'Implemented automated backup and replication systems'
            ]
        }
    ],
    'projects': [
        {
            'name': 'Real-Time Loyalty Processing System',
            'description': 'Enterprise-scale Kafka-Spark pipeline handling millions of daily loyalty transactions with real-time validation and fraud detection.',
            'technologies': ['Apache Kafka', 'Spark', 'AWS', 'Python', 'PostgreSQL'],
            'icon': 'fas fa-stream',
            'metrics': [
                {'value': '10M+', 'label': 'Daily Transactions'},
                {'value': '99.9%', 'label': 'Data Accuracy'},
                {'value': '40%', 'label': 'Efficiency Gain'}
            ]
        },
        {
            'name': 'Enterprise Data Migration to Cloud',
            'description': 'Seamless migration of 15+ TB of critical airline reservation data from on-premises to AWS Aurora using advanced ETL techniques.',
            'technologies': ['AWS DMS', 'Pentaho', 'AWS Aurora', 'PostgreSQL', 'Python'],
            'icon': 'fas fa-cloud-upload-alt',
            'metrics': [
                {'value': '15TB', 'label': 'Data Migrated'},
                {'value': '0', 'label': 'Downtime'},
                {'value': '30%', 'label': 'Performance Boost'}
            ]
        },
        {
            'name': 'Medallion Architecture Pipeline',
            'description': 'Real-time Azure Databricks pipeline using Delta Lake and Structured Streaming for airline loyalty insights with comprehensive data governance.',
            'technologies': ['Azure Databricks', 'Delta Lake', 'Unity Catalog', 'Structured Streaming', 'Python'],
            'icon': 'fas fa-layer-group',
            'metrics': [
                {'value': '60%', 'label': 'Response Time'},
                {'value': '100%', 'label': 'Data Lineage'},
                {'value': '85%', 'label': 'Failure Reduction'}
            ]
        },
        {
            'name': 'Serverless ETL Framework',
            'description': 'Automated batch processing framework using AWS Lambda, Glue, and EventBridge for daily airline data ingestion with comprehensive monitoring.',
            'technologies': ['AWS Lambda', 'AWS Glue', 'EventBridge', 'S3', 'DynamoDB', 'Redshift'],
            'icon': 'fas fa-cogs',
            'metrics': [
                {'value': '100%', 'label': 'Automation'},
                {'value': '85%', 'label': 'Error Reduction'},
                {'value': '50%', 'label': 'Time Saved'}
            ]
        }
    ],
    'contact': {
        'email': 'sobinbabu@hotmail.com',
        'linkedin': 'https://linkedin.com/in/sobin-babu',
        'phone': '+44 7555084364',
        'location': 'Manchester, UK'
    }
}

@app.route('/')
def index():
    return render_template_string(ADVANCED_TEMPLATE, **PORTFOLIO_DATA)

@app.route('/api/portfolio')
def api_portfolio():
    from flask import jsonify
    return jsonify(PORTFOLIO_DATA)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)