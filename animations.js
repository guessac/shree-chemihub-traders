// Initialize AOS (Animate On Scroll)
document.addEventListener('DOMContentLoaded', function() {
    // Dynamically load AOS CSS
    const aosCss = document.createElement('link');
    aosCss.rel = 'stylesheet';
    aosCss.href = 'https://unpkg.com/aos@2.3.1/dist/aos.css';
    document.head.appendChild(aosCss);

    // Add AOS attributes dynamically to existing elements BEFORE initializing AOS
    
    // Headings (Fly in from bottom or sides, not down which looks like flying out)
    document.querySelectorAll('h1').forEach(el => el.setAttribute('data-aos', 'fade-up'));
    document.querySelectorAll('h2').forEach(el => el.setAttribute('data-aos', 'fade-up'));
    
    // Hero Paragraphs
    document.querySelectorAll('header p, .hero p').forEach((el, index) => {
        el.setAttribute('data-aos', 'fade-up');
        el.setAttribute('data-aos-delay', (100 * (index + 1)).toString());
    });

    // Cards and Grids
    document.querySelectorAll('.border-slate-100, .shadow-sm').forEach((el, index) => {
        // Apply magic classes and fly-in effect
        if(!el.classList.contains('nav') && !el.tagName.toLowerCase().includes('nav') && !el.closest('nav')) {
            el.classList.add('hover-magic');
            el.setAttribute('data-aos', 'fade-up');
            el.setAttribute('data-aos-delay', (100 * (index % 4)).toString());
        }
    });
    
    // Buttons
    document.querySelectorAll('a[href]').forEach(el => {
        if(el.classList.contains('bg-brandRed') || el.classList.contains('bg-brandBlue')) {
            el.classList.add('btn-magic');
        } else if(el.classList.contains('text-slate-600') && !el.classList.contains('block')) {
            el.classList.add('nav-link-magic');
        }
    });
    
    // (Logo Float removed to prevent mobile visibility issues)

    // Dynamically load AOS JS and then init
    const aosJs = document.createElement('script');
    aosJs.src = 'https://unpkg.com/aos@2.3.1/dist/aos.js';
    aosJs.onload = function() {
        AOS.init({
            duration: 800,
            once: true, // Whether animation should happen only once - while scrolling down
            offset: 50, // Offset (in px) from the original trigger point
            easing: 'ease-out-cubic'
        });
    };
    document.body.appendChild(aosJs);
});

// Global function to toggle brand categories
window.toggleCategory = function(categoryId, btnElement) {
    const content = document.getElementById(categoryId);
    if (content) {
        if (content.classList.contains('expanded')) {
            content.classList.remove('expanded');
            if (btnElement) btnElement.innerHTML = 'View Products <i data-lucide="chevron-down" class="w-4 h-4 inline-block ml-1"></i>';
        } else {
            content.classList.add('expanded');
            if (btnElement) btnElement.innerHTML = 'Hide Products <i data-lucide="chevron-up" class="w-4 h-4 inline-block ml-1"></i>';
        }
        if (window.lucide) {
            window.lucide.createIcons();
        }
    }
};

// Global functions for Modals
window.openModal = function(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('hidden');
        // Small delay to allow display:block to apply before adding opacity class
        setTimeout(() => {
            modal.classList.add('active');
        }, 10);
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }
};

window.closeModal = function(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
        // Wait for transition to finish before hiding
        setTimeout(() => {
            modal.classList.add('hidden');
        }, 300);
        document.body.style.overflow = ''; // Restore background scrolling
    }
};
