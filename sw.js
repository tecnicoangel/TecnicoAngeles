const CACHE_NAME = 'tecnicoangeles-v1';
const ASSETS = [
  './',
  './index.html',
  './Servicio.html',
  './Producto.html',
  './contactos.html',
  './login.html',
  './registro.html',
  './Manual de Convivencia.html',
  './Cableado Estructurado RED.html',
  './Formulario para el cliente realice su pago .html',
  './styles/styles.css',
  './imgA/Logo.png',
  './favicon.ico'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS);
    })
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => {
      return response || fetch(e.request);
    })
  );
});