document.addEventListener('DOMContentLoaded', function() {
    // Make sure the hamburger menu works
    const hamburgerBtn = document.querySelector('.navbar-hamburger');
    const navMenu = document.querySelector('.navbar-menu');
    const body = document.body;
    
    if (hamburgerBtn) {
        console.log("Hamburger button found"); // Debug message
        hamburgerBtn.addEventListener('click', function(event) {
            event.stopPropagation(); // Prevent event bubbling
            console.log("Hamburger clicked"); // Debug message
            navMenu.classList.toggle('active');
            hamburgerBtn.classList.toggle('active');
            body.classList.toggle('menu-active');
        });
    }
    
    // Close menu when clicking menu items
    const menuItems = document.querySelectorAll('.navbar-menu .navbar-item');
    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            navMenu.classList.remove('active');
            hamburgerBtn.classList.remove('active');
        });
    });
    
    // Detect if device is mobile
    const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    
    if (isMobile) {
        // Add touch-specific classes to the body
        document.body.classList.add('touch-device');
        
        // Make problem cards tappable
        const problemCards = document.querySelectorAll('.problem-card');
        problemCards.forEach(card => {
            const viewDetailsBtn = card.querySelector('.btn-secondary');
            
            if (viewDetailsBtn) {
                card.addEventListener('touchstart', function() {
                    this.classList.add('touch-active');
                });
                
                card.addEventListener('touchend', function(event) {
                    this.classList.remove('touch-active');
                    // Don't trigger if they're tapping the view details button
                    if (event.target !== viewDetailsBtn && !viewDetailsBtn.contains(event.target)) {
                        viewDetailsBtn.click();
                    }
                });
            }
        });
        
        // Add smooth scrolling with inertia for touch devices
        const scrollLinks = document.querySelectorAll('a[href^="#"]');
        scrollLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    e.preventDefault();
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }
});