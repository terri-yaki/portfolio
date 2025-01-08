// loader, toTop, etc.
const loader = document.getElementById('loader');
const body = document.body;
const themeToggle = document.getElementById('themeToggle');
const toTopBtn = document.getElementById('toTop');
const header = document.getElementById('header');

// Loader
window.addEventListener('load', () => {
  setTimeout(() => {
    loader.classList.add('hidden');
  }, 500);
});

// Dark/Light Mode Toggle
themeToggle.addEventListener('click', () => {
  body.classList.toggle('dark-mode');
  header.classList.toggle('dark-mode');
  loader.classList.toggle('dark-mode');
});

// Go to top button
window.addEventListener('scroll', () => {
  if (window.scrollY > 300) {
    toTopBtn.classList.add('show');
  } else {
    toTopBtn.classList.remove('show');
  }
});
toTopBtn.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Mobile Nav Controls
const menuToggle = document.getElementById('menuToggle');
const mobileNav = document.getElementById('mobileNav');
const closeBtn = document.getElementById('closeBtn');
const navLinks = document.querySelectorAll('.mobile-nav-links a');

// Open mobile nav
menuToggle.addEventListener('click', () => {
  mobileNav.classList.add('open');
});

// Close mobile nav
closeBtn.addEventListener('click', () => {
  mobileNav.classList.remove('open');
});

navLinks.forEach(link => {
  link.addEventListener('click', () => {
    mobileNav.classList.remove('open');
  });
});
