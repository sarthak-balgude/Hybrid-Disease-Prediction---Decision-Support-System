// --- THREE.JS BACKGROUND ---
function initBackground() {
    const container = document.getElementById('canvas-container');
    const scene = new THREE.Scene();
    
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 40;

    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio); 
    container.appendChild(renderer.domElement);

    const geometry = new THREE.BufferGeometry();
    const particles = 250; 
    const positions = [];
    
    for (let i = 0; i < particles; i++) {
        const r = 50;
        const theta = Math.random() * Math.PI * 2;
        const phi = Math.acos(Math.random() * 2 - 1);
        
        const x = r * Math.sin(phi) * Math.cos(theta);
        const y = r * Math.sin(phi) * Math.sin(theta);
        const z = r * Math.cos(phi);
        
        positions.push(x, y, z);
    }

    geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));

    const material = new THREE.PointsMaterial({ 
        color: 0x38bdf8, 
        size: 0.7, 
        transparent: true,
        opacity: 0.9, 
        blending: THREE.AdditiveBlending,
        depthWrite: false
    });

    const points = new THREE.Points(geometry, material);
    scene.add(points);

    let mouseX = 0;
    let mouseY = 0;
    
    document.addEventListener('mousemove', (event) => {
        mouseX = (event.clientX - window.innerWidth / 2) * 0.0005;
        mouseY = (event.clientY - window.innerHeight / 2) * 0.0005;
    });

    document.addEventListener('touchmove', (event) => {
        if(event.touches.length > 0) {
            mouseX = (event.touches[0].clientX - window.innerWidth / 2) * 0.001;
            mouseY = (event.touches[0].clientY - window.innerHeight / 2) * 0.001;
        }
    }, { passive: true });

    function animate() {
        requestAnimationFrame(animate);
        points.rotation.y += 0.0010;
        points.rotation.x += 0.0006;
        points.rotation.y += mouseX * 0.05;
        points.rotation.x += mouseY * 0.05;
        renderer.render(scene, camera);
    }
    animate();

    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });
}

// --- UI LOGIC ---

function showModal(modalId, panelId) {
    const modal = document.getElementById(modalId);
    const panel = document.getElementById(panelId);
    modal.classList.remove('hidden');
    modal.style.display = 'flex';
    setTimeout(() => {
        modal.classList.remove('opacity-0');
        panel.classList.remove('scale-95');
    }, 10);
}

function hideModal(modalId, panelId, callback) {
    const modal = document.getElementById(modalId);
    const panel = document.getElementById(panelId);
    modal.classList.add('opacity-0');
    panel.classList.add('scale-95');
    setTimeout(() => {
        modal.classList.add('hidden');
        modal.style.display = 'none';
        if(callback) callback();
    }, 300);
}

// Login Logic
function toggleLogin() {
    const modal = document.getElementById('login-modal');
    if (modal.classList.contains('hidden')) {
        showModal('login-modal', 'login-panel');
    } else {
        hideModal('login-modal', 'login-panel');
    }
}

function handleAuth(e) {
    e.preventDefault();
    const btn = e.target.querySelector('button');
    const checkbox = document.getElementById('login-agree');
    
    if (!checkbox.checked) {
        alert("Please agree to the Terms & Conditions and Privacy Policy to continue.");
        return;
    }

    const originalText = btn.innerText;
    btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Authenticating...';
    btn.classList.add('opacity-75', 'cursor-not-allowed');
    
    setTimeout(() => {
        btn.classList.remove('bg-sky-600', 'hover:bg-sky-500');
        btn.classList.add('bg-emerald-600', 'hover:bg-emerald-500');
        btn.innerHTML = '<i class="fas fa-check"></i> Success';
        
        setTimeout(() => {
            alert("Welcome back! Redirecting to dashboard...");
            window.location.reload(); 
        }, 800);
    }, 1200);
}

// Modal Open/Close Logic
function openFAQ(e) { if(e) e.preventDefault(); showModal('faq-modal', 'faq-panel'); }
function closeFAQ() { hideModal('faq-modal', 'faq-panel'); }

function openContact(e) { if(e) e.preventDefault(); showModal('contact-modal', 'contact-panel'); }
function closeContact() { hideModal('contact-modal', 'contact-panel'); }

function openTerms(e) { if(e) e.preventDefault(); showModal('terms-modal', 'terms-panel'); }
function closeTerms() { hideModal('terms-modal', 'terms-panel'); }

function openPrivacy(e) { if(e) e.preventDefault(); showModal('privacy-modal', 'privacy-panel'); }
function closePrivacy() { hideModal('privacy-modal', 'privacy-panel'); }

function openDisclaimer(e) { if(e) e.preventDefault(); showModal('disclaimer-modal', 'disclaimer-panel'); }
function closeDisclaimer() { hideModal('disclaimer-modal', 'disclaimer-panel'); }

function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
}

// Init
window.addEventListener('DOMContentLoaded', initBackground);