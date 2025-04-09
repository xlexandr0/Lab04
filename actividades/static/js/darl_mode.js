// Obtiene el botón para activar el modo oscuro
const darkModeToggle = document.getElementById('darkModeToggle');

// Verifica si el usuario ya tiene configurado el modo oscuro
if (localStorage.getItem('darkMode') === 'true') {
    document.body.classList.add('dark-mode');
}

// Función para alternar entre modo claro y oscuro
darkModeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    
    // Guarda la preferencia en localStorage
    if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('darkMode', 'true');
    } else {
        localStorage.setItem('darkMode', 'false');
    }
});
