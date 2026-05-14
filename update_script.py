import os
import re

css_additions = """
        /* Professional Wizardry CSS */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
        .animate-float { animation: float 4s ease-in-out infinite; }
        
        .text-gradient {
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-image: linear-gradient(135deg, #0071A4, #8A1538);
        }

        .hover-magic {
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .hover-magic:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 25px -5px rgba(0, 113, 164, 0.15), 0 10px 10px -5px rgba(0, 113, 164, 0.04);
            border-color: rgba(0, 113, 164, 0.3);
        }

        .btn-magic {
            position: relative;
            overflow: hidden;
            z-index: 1;
        }
        .btn-magic::after {
            content: '';
            position: absolute;
            bottom: 0; left: 0; width: 100%; height: 100%;
            background-color: rgba(255,255,255,0.2);
            transform: translateY(100%);
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: -1;
        }
        .btn-magic:hover::after {
            transform: translateY(0);
        }
        
        /* Smooth underline animation for nav links */
        .nav-link-magic {
            position: relative;
        }
        .nav-link-magic::after {
            content: '';
            position: absolute;
            width: 0; height: 2px;
            bottom: -4px; left: 0;
            background-color: #0071A4;
            transition: width 0.3s ease;
        }
        .nav-link-magic:hover::after {
            width: 100%;
        }
"""

def update_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Add AOS CSS in head
    if 'aos.css' not in content:
        content = content.replace('</head>', '    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n</head>')
    
    # 2. Add custom CSS inside <style>
    if '.hover-magic' not in content:
        content = content.replace('</style>', css_additions + '\n    </style>')
        
    # 3. Add AOS JS and init at the end of body
    if 'aos.js' not in content:
        aos_init = """
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({
            duration: 800,
            once: true,
            offset: 50,
            easing: 'ease-out-cubic'
        });
    </script>
</body>"""
        content = content.replace('</body>', aos_init)

    # 4. Inject AOS attributes and magic classes (very naive regex replacements for common elements)
    
    # Nav links
    content = re.sub(r'class="([^"]*text-slate-600 font-medium transition hover:text-brandBlue[^"]*)"', r'class="\1 nav-link-magic"', content)
    
    # Hero H1
    content = content.replace('<h1 class="text-4xl font-extrabold', '<h1 data-aos="fade-up" class="text-4xl font-extrabold')
    content = content.replace('<h1 class="text-4xl md:text-5xl font-extrabold', '<h1 data-aos="fade-down" class="text-4xl md:text-5xl font-extrabold')
    
    # Hero p
    content = content.replace('<p class="mt-4 text-xl text-slate-300', '<p data-aos="fade-up" data-aos-delay="100" class="mt-4 text-xl text-slate-300')
    content = content.replace('<p class="text-lg text-slate-300', '<p data-aos="fade-up" data-aos-delay="100" class="text-lg text-slate-300')
    
    # Buttons
    content = re.sub(r'class="([^"]*bg-brandRed[^"]*px-8[^"]*)"', r'class="\1 btn-magic"', content)
    content = re.sub(r'class="([^"]*bg-brandBlue text-white[^"]*px-5 py-2.5[^"]*)"', r'class="\1 btn-magic"', content)
    
    # Cards / Grids
    content = re.sub(r'class="([^"]*p-6 border border-slate-100 rounded-xl shadow-sm hover:shadow-md transition[^"]*)"', r'class="\1 hover-magic" data-aos="fade-up"', content)
    content = re.sub(r'class="([^"]*bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex flex-col items-center text-center transition hover:shadow-md[^"]*)"', r'class="\1 hover-magic" data-aos="zoom-in"', content)
    content = re.sub(r'class="([^"]*bg-white p-8 rounded-2xl shadow-sm border border-slate-100 transition hover:shadow-md hover:border-brandBlue/30[^"]*)"', r'class="\1 hover-magic" data-aos="fade-up"', content)
    
    # Content sections
    content = content.replace('<h2 class="text-3xl font-bold', '<h2 data-aos="fade-right" class="text-3xl font-bold')
    
    # About Us List
    content = content.replace('<li class="flex items-start gap-4">', '<li data-aos="fade-left" class="flex items-start gap-4 hover-magic p-2 rounded-xl">')

    # Logos
    content = content.replace('<img src="assets/logo.png"', '<img src="assets/logo.png" class="animate-float"')

    with open(filepath, 'w') as f:
        f.write(content)

for f in ['index.html', 'about.html', 'contact.html', 'products.html']:
    update_file(f)
