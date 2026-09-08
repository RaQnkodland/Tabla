// Datos trasladados del programa Python original.
const elementos = [[1, 'H', 'Hidrógeno', 1.008, 'no metal', 1, 1], [2, 'He', 'Helio', 4.003, 'gas noble', 1, 18], [3, 'Li', 'Litio', 6.941, 'metal alcalino', 2, 1], [4, 'Be', 'Berilio', 9.012, 'alcalinotérreo', 2, 2], [5, 'B', 'Boro', 10.81, 'metaloide', 2, 13], [6, 'C', 'Carbono', 12.01, 'no metal', 2, 14], [7, 'N', 'Nitrógeno', 14.01, 'no metal', 2, 15], [8, 'O', 'Oxígeno', 16.0, 'no metal', 2, 16], [9, 'F', 'Flúor', 19.0, 'halógeno', 2, 17], [10, 'Ne', 'Neón', 20.18, 'gas noble', 2, 18], [11, 'Na', 'Sodio', 22.99, 'metal alcalino', 3, 1], [12, 'Mg', 'Magnesio', 24.31, 'alcalinotérreo', 3, 2], [13, 'Al', 'Aluminio', 26.98, 'post-transición', 3, 13], [14, 'Si', 'Silicio', 28.09, 'metaloide', 3, 14], [15, 'P', 'Fósforo', 30.97, 'no metal', 3, 15], [16, 'S', 'Azufre', 32.07, 'no metal', 3, 16], [17, 'Cl', 'Cloro', 35.45, 'halógeno', 3, 17], [18, 'Ar', 'Argón', 39.95, 'gas noble', 3, 18], [19, 'K', 'Potasio', 39.1, 'metal alcalino', 4, 1], [20, 'Ca', 'Calcio', 40.08, 'alcalinotérreo', 4, 2], [21, 'Sc', 'Escandio', 44.96, 'transición', 4, 3], [22, 'Ti', 'Titanio', 47.87, 'transición', 4, 4], [23, 'V', 'Vanadio', 50.94, 'transición', 4, 5], [24, 'Cr', 'Cromo', 52.0, 'transición', 4, 6], [25, 'Mn', 'Manganeso', 54.94, 'transición', 4, 7], [26, 'Fe', 'Hierro', 55.85, 'transición', 4, 8], [27, 'Co', 'Cobalto', 58.93, 'transición', 4, 9], [28, 'Ni', 'Níquel', 58.69, 'transición', 4, 10], [29, 'Cu', 'Cobre', 63.55, 'transición', 4, 11], [30, 'Zn', 'Zinc', 65.38, 'transición', 4, 12], [31, 'Ga', 'Galio', 69.72, 'post-transición', 4, 13], [32, 'Ge', 'Germanio', 72.63, 'metaloide', 4, 14], [33, 'As', 'Arsénico', 74.92, 'metaloide', 4, 15], [34, 'Se', 'Selenio', 78.97, 'no metal', 4, 16], [35, 'Br', 'Bromo', 79.9, 'halógeno', 4, 17], [36, 'Kr', 'Kriptón', 83.8, 'gas noble', 4, 18], [37, 'Rb', 'Rubidio', 85.47, 'metal alcalino', 5, 1], [38, 'Sr', 'Estroncio', 87.62, 'alcalinotérreo', 5, 2], [39, 'Y', 'Itrio', 88.91, 'transición', 5, 3], [40, 'Zr', 'Circonio', 91.22, 'transición', 5, 4], [41, 'Nb', 'Niobio', 92.91, 'transición', 5, 5], [42, 'Mo', 'Molibdeno', 95.95, 'transición', 5, 6], [43, 'Tc', 'Tecnecio', 98.0, 'transición', 5, 7], [44, 'Ru', 'Rutenio', 101.1, 'transición', 5, 8], [45, 'Rh', 'Rodio', 102.9, 'transición', 5, 9], [46, 'Pd', 'Paladio', 106.4, 'transición', 5, 10], [47, 'Ag', 'Plata', 107.9, 'transición', 5, 11], [48, 'Cd', 'Cadmio', 112.4, 'transición', 5, 12], [49, 'In', 'Indio', 114.8, 'post-transición', 5, 13], [50, 'Sn', 'Estaño', 118.7, 'post-transición', 5, 14], [51, 'Sb', 'Antimonio', 121.8, 'metaloide', 5, 15], [52, 'Te', 'Telurio', 127.6, 'metaloide', 5, 16], [53, 'I', 'Yodo', 126.9, 'halógeno', 5, 17], [54, 'Xe', 'Xenón', 131.3, 'gas noble', 5, 18], [55, 'Cs', 'Cesio', 132.9, 'metal alcalino', 6, 1], [56, 'Ba', 'Bario', 137.3, 'alcalinotérreo', 6, 2], [72, 'Hf', 'Hafnio', 178.5, 'transición', 6, 4], [73, 'Ta', 'Tantalio', 180.9, 'transición', 6, 5], [74, 'W', 'Wolframio', 183.8, 'transición', 6, 6], [75, 'Re', 'Renio', 186.2, 'transición', 6, 7], [76, 'Os', 'Osmio', 190.2, 'transición', 6, 8], [77, 'Ir', 'Iridio', 192.2, 'transición', 6, 9], [78, 'Pt', 'Platino', 195.1, 'transición', 6, 10], [79, 'Au', 'Oro', 197.0, 'transición', 6, 11], [80, 'Hg', 'Mercurio', 200.6, 'transición', 6, 12], [81, 'Tl', 'Talio', 204.4, 'post-transición', 6, 13], [82, 'Pb', 'Plomo', 207.2, 'post-transición', 6, 14], [83, 'Bi', 'Bismuto', 209.0, 'post-transición', 6, 15], [84, 'Po', 'Polonio', 209.0, 'post-transición', 6, 16], [85, 'At', 'Astato', 210.0, 'halógeno', 6, 17], [86, 'Rn', 'Radón', 222.0, 'gas noble', 6, 18], [87, 'Fr', 'Francio', 223.0, 'metal alcalino', 7, 1], [88, 'Ra', 'Radio', 226.0, 'alcalinotérreo', 7, 2], [104, 'Rf', 'Rutherfordio', 267.0, 'transición', 7, 4], [105, 'Db', 'Dubnio', 268.0, 'transición', 7, 5], [106, 'Sg', 'Seaborgio', 269.0, 'transición', 7, 6], [107, 'Bh', 'Bohrio', 270.0, 'transición', 7, 7], [108, 'Hs', 'Hassio', 277.0, 'transición', 7, 8], [109, 'Mt', 'Meitnerio', 278.0, 'desconocido', 7, 9], [110, 'Ds', 'Darmstadtio', 281.0, 'desconocido', 7, 10], [111, 'Rg', 'Roentgenio', 282.0, 'desconocido', 7, 11], [112, 'Cn', 'Copernicio', 285.0, 'transición', 7, 12], [113, 'Nh', 'Nihonio', 286.0, 'desconocido', 7, 13], [114, 'Fl', 'Flerovio', 289.0, 'desconocido', 7, 14], [115, 'Mc', 'Moscovio', 290.0, 'desconocido', 7, 15], [116, 'Lv', 'Livermorio', 293.0, 'desconocido', 7, 16], [117, 'Ts', 'Tenesino', 294.0, 'desconocido', 7, 17], [118, 'Og', 'Oganesón', 294.0, 'desconocido', 7, 18], [57, 'La', 'Lantano', 138.9, 'lantánido', 9, 3], [58, 'Ce', 'Cerio', 140.1, 'lantánido', 9, 4], [59, 'Pr', 'Praseodimio', 140.9, 'lantánido', 9, 5], [60, 'Nd', 'Neodimio', 144.2, 'lantánido', 9, 6], [61, 'Pm', 'Prometio', 145.0, 'lantánido', 9, 7], [62, 'Sm', 'Samario', 150.4, 'lantánido', 9, 8], [63, 'Eu', 'Europio', 152.0, 'lantánido', 9, 9], [64, 'Gd', 'Gadolinio', 157.3, 'lantánido', 9, 10], [65, 'Tb', 'Terbio', 158.9, 'lantánido', 9, 11], [66, 'Dy', 'Disprosio', 162.5, 'lantánido', 9, 12], [67, 'Ho', 'Holmio', 164.9, 'lantánido', 9, 13], [68, 'Er', 'Erbio', 167.3, 'lantánido', 9, 14], [69, 'Tm', 'Tulio', 168.9, 'lantánido', 9, 15], [70, 'Yb', 'Iterbio', 173.0, 'lantánido', 9, 16], [71, 'Lu', 'Lutecio', 175.0, 'lantánido', 9, 17], [89, 'Ac', 'Actinio', 227.0, 'actínido', 10, 3], [90, 'Th', 'Torio', 232.0, 'actínido', 10, 4], [91, 'Pa', 'Protactinio', 231.0, 'actínido', 10, 5], [92, 'U', 'Uranio', 238.0, 'actínido', 10, 6], [93, 'Np', 'Neptunio', 237.0, 'actínido', 10, 7], [94, 'Pu', 'Plutonio', 244.0, 'actínido', 10, 8], [95, 'Am', 'Americio', 243.0, 'actínido', 10, 9], [96, 'Cm', 'Curio', 247.0, 'actínido', 10, 10], [97, 'Bk', 'Berkelio', 247.0, 'actínido', 10, 11], [98, 'Cf', 'Californio', 251.0, 'actínido', 10, 12], [99, 'Es', 'Einstenio', 252.0, 'actínido', 10, 13], [100, 'Fm', 'Fermio', 257.0, 'actínido', 10, 14], [101, 'Md', 'Mendelevio', 258.0, 'actínido', 10, 15], [102, 'No', 'Nobelio', 259.0, 'actínido', 10, 16], [103, 'Lr', 'Lawrencio', 266.0, 'actínido', 10, 17]];

const colores = {'no metal': '#4CAF50', 'gas noble': '#FF9800', 'metal alcalino': '#F44336', 'alcalinotérreo': '#FF5722', 'transición': '#2196F3', 'post-transición': '#0373F4', 'metaloide': '#8BC34A', 'halógeno': '#E91E63', 'lantánido': '#9C27B0', 'actínido': '#673AB7', 'desconocido': '#607D8B'};

const coloresEstado = {
  "Gas": "#90CAF9",
  "Líquido": "#4DD0E1",
  "Sólido": "#A5D6A7",
  "Desconocido": "#B0BEC5"
};

const caracteristicas = {
  "metal alcalino": "Familia reactiva, frecuente en sales.",
  "alcalinotérreo": "Metal reactivo usado en aleaciones y minerales.",
  "transición": "Metal con aplicaciones industriales y tecnológicas.",
  "no metal": "Elemento esencial en numerosos compuestos.",
  "gas noble": "Gas muy poco reactivo, usado en iluminación y tecnología.",
  "halógeno": "Elemento reactivo, presente en sales y desinfectantes."
};

const tabla = document.getElementById("periodic-table");
const legend = document.getElementById("legend");
const search = document.getElementById("search");
const results = document.getElementById("results");
const info = document.getElementById("info");
const scale = document.getElementById("scale");
const favoriteBtn = document.getElementById("favorite-btn");
const compareBtn = document.getElementById("compare-btn");
const themeBtn = document.getElementById("theme-btn");
const preview = document.getElementById("preview");
const detailsModal = document.getElementById("details-modal");
const comparisonModal = document.getElementById("comparison-modal");

let selectedElement = null;
let hoveredElement = null;
let favorites = new Set();
let comparison = [];
let comparisonActive = false;
let filterCategory = null;
let darkTheme = true;

const elementNodes = new Map();

function estadoFisico(sym) {
  if (["H","He","N","O","F","Ne","Cl","Ar","Kr","Xe","Rn","Og"].includes(sym)) return "Gas";
  if (["Br","Hg"].includes(sym)) return "Líquido";
  if (["At","Ts"].includes(sym)) return "Desconocido";
  return "Sólido";
}

function colorEscala(valor, minimo, maximo) {
  const proporcion = maximo === minimo ? 0 : (valor - minimo) / (maximo - minimo);
  const rojo = Math.floor(52 + 200 * proporcion);
  const azul = Math.floor(220 - 160 * proporcion);
  return "#" + rojo.toString(16).padStart(2, "0") + "70" + azul.toString(16).padStart(2, "0");
}

const sonidoHover = new Audio("sonidos/hover_sonido.wav");

sonidoHover.volume = 0.4;

function playSound(type) {
    if (type === "hover") {
        sonidoHover.currentTime = 0;
        sonidoHover.play().catch(() => {});
    }
}

function crearTabla() {
  tabla.innerHTML = "";

  // Reservamos 18 columnas x 10 filas, igual que las posiciones del Canvas.
  elementos.forEach(el => {
    const [z, sym, nombre, masa, cat, fila, col] = el;

    const node = document.createElement("div");
    node.className = "element";
    node.dataset.z = z;
    node.dataset.row = fila;
    node.dataset.col = col;
    node.dataset.category = cat;
    node.style.gridColumn = col;
    node.style.gridRow = fila;

    node.innerHTML = `
      <span class="atomic-number">${z}</span>
      <span class="symbol">${sym}</span>
      <span class="star"></span>
    `;

    node.addEventListener("mouseenter", e => onHover(node, e));
    node.addEventListener("mouseleave", onLeave);
    node.addEventListener("click", () => seleccionarElemento(node));

    elementNodes.set(z, node);
    tabla.appendChild(node);
  });
}

function crearLeyenda() {
  legend.innerHTML = '<div class="legend-title">Leyenda:</div>';

  Object.entries(colores).forEach(([cat, color]) => {
    const item = document.createElement("div");
    item.className = "legend-item";
    item.dataset.category = cat;
    item.innerHTML = `
      <span class="legend-color" style="background:${color}"></span>
      <span>${cat.charAt(0).toUpperCase() + cat.slice(1)}</span>
    `;
    item.addEventListener("click", () => filtrarCategoria(cat));
    legend.appendChild(item);
  });
}

function actualizarEstilos() {
  const modo = scale.value;
  const masas = elementos.map(el => el[3]);
  const numeros = elementos.map(el => el[0]);

  elementos.forEach(el => {
    const [z, sym, nombre, masa, cat] = el;
    const node = elementNodes.get(z);

    let color;
    if (modo === "Escala: masa") {
      color = colorEscala(masa, Math.min(...masas), Math.max(...masas));
    } else if (modo === "Escala: número atómico") {
      color = colorEscala(z, Math.min(...numeros), Math.max(...numeros));
    } else if (modo === "Estado físico") {
      color = coloresEstado[estadoFisico(sym)];
    } else {
      color = colores[cat] || "#607D8B";
    }

    node.style.background = color;
    node.style.color = "white";
    node.classList.remove("dimmed");
  });

  aplicarFiltroVisual();
}

function aplicarFiltroVisual() {
  elementos.forEach(el => {
    const node = elementNodes.get(el[0]);
    const activo = !filterCategory || el[4] === filterCategory;

    if (!activo) {
      node.classList.add("dimmed");
      node.querySelectorAll(".atomic-number, .symbol").forEach(t => t.style.color = "#90A4AE");
    } else {
      node.classList.remove("dimmed");
      node.querySelectorAll(".atomic-number, .symbol").forEach(t => t.style.color = "white");
    }
  });

  if (selectedElement) restaurarElemento(selectedElement);
}

function restaurarElemento(node) {
  node.classList.toggle("selected", node === selectedElement);
}

function actualizarFavorito() {
  if (!selectedElement) {
    favoriteBtn.textContent = "☆ Favorito";
    return;
  }

  const z = Number(selectedElement.dataset.z);
  favoriteBtn.textContent = favorites.has(z) ? "★ Quitar favorito" : "☆ Favorito";
}

function alternarFavorito() {
  if (!selectedElement) {
    info.textContent = "Selecciona primero un elemento.";
    return;
  }

  const z = Number(selectedElement.dataset.z);

  if (favorites.has(z)) {
    favorites.delete(z);
    selectedElement.querySelector(".star").textContent = "";
    info.textContent = "Elemento eliminado de favoritos.";
  } else {
    favorites.add(z);
    selectedElement.querySelector(".star").textContent = "★";
    info.textContent = "Elemento añadido a favoritos.";
  }

  actualizarFavorito();
  playSound("clic");
}

function alternarComparacion() {
  comparison = [];
  comparisonActive = !comparisonActive;
  compareBtn.textContent = comparisonActive ? "Cancelar comparación" : "Comparar";
  info.textContent = comparisonActive
    ? "Selecciona dos elementos para compararlos."
    : "Comparación cancelada.";
}

function seleccionarElemento(node) {
  if (selectedElement && selectedElement !== node) {
    selectedElement.classList.remove("selected");
  }

  selectedElement = node;
  node.classList.add("selected");
  actualizarFavorito();
  playSound("clic");

  if (comparisonActive) {
    if (!comparison.includes(node)) comparison.push(node);

    if (comparison.length === 2) {
      mostrarComparacion();
      comparison = [];
      comparisonActive = false;
      compareBtn.textContent = "Comparar";
    } else {
      info.textContent = "Selecciona un segundo elemento para compararlo.";
    }
  } else {
    mostrarDetalles(obtenerElemento(node));
  }
}

function obtenerElemento(node) {
  return elementos.find(el => el[0] === Number(node.dataset.z));
}

function mostrarDetalles(el) {
  const [z, sym, nombre, masa, cat, fila, col] = el;
  const color = colores[cat] || "#607D8B";
  const estado = estadoFisico(sym);
  const caracteristica = caracteristicas[cat] || "Elemento con propiedades características de su familia.";

  ocultarPreview();

  document.getElementById("modal-content").innerHTML = `
    <div class="detail-symbol" style="color:${color}">${sym}</div>
    <div class="detail-name">${nombre}</div>
    <div class="detail-text">
      Número atómico: ${z}<br>
      Masa atómica: ${masa} u<br>
      Categoría: ${cat.charAt(0).toUpperCase() + cat.slice(1)}<br>
      Período: ${fila} | Grupo: ${col}<br>
      Estado físico: ${estado}<br><br>
      ${caracteristica}
    </div>
    <button class="detail-close-button" id="detail-close-button" style="background:${color}">Cerrar</button>
  `;

  detailsModal.hidden = false;
  document.getElementById("detail-close-button").onclick = cerrarDetalle;
}

function cerrarDetalle() {
  detailsModal.hidden = true;
}

function mostrarComparacion() {
  const a = obtenerElemento(comparison[0]);
  const b = obtenerElemento(comparison[1]);

  document.getElementById("comparison-content").innerHTML = `
    <h2>Comparación de elementos</h2>
    <div class="comparison-grid">
      <div>
        <h2>${a[1]} — ${a[2]}</h2>
        <p>Número atómico: ${a[0]}</p>
        <p>Masa atómica: ${a[3]} u</p>
        <p>Categoría: ${a[4]}</p>
        <p>Estado físico: ${estadoFisico(a[1])}</p>
        <p>Período / grupo: ${a[5]} / ${a[6]}</p>
      </div>
      <div>
        <h2>${b[1]} — ${b[2]}</h2>
        <p>Número atómico: ${b[0]}</p>
        <p>Masa atómica: ${b[3]} u</p>
        <p>Categoría: ${b[4]}</p>
        <p>Estado físico: ${estadoFisico(b[1])}</p>
        <p>Período / grupo: ${b[5]} / ${b[6]}</p>
      </div>
    </div>
  `;

  comparisonModal.hidden = false;
}

function buscarElemento() {
  const termino = search.value.trim().toLowerCase();

  if (!termino) {
    info.textContent = "Escribe un nombre, símbolo o número atómico.";
    return;
  }

  const encontrado = elementos.find(el =>
    String(el[0]).includes(termino) ||
    el[1].toLowerCase().includes(termino) ||
    el[2].toLowerCase().includes(termino)
  );

  if (encontrado) {
    const node = elementNodes.get(encontrado[0]);
    seleccionarElemento(node);
    node.scrollIntoView({ behavior: "smooth", block: "center", inline: "center" });
  } else {
    info.textContent = "No se encontró ningún elemento con esa búsqueda.";
  }
}

function actualizarResultados() {
  const termino = search.value.trim().toLowerCase();
  results.innerHTML = "";

  if (!termino) {
    results.hidden = true;
    return;
  }

  const encontrados = elementos.filter(el =>
    String(el[0]).includes(termino) ||
    el[1].toLowerCase().includes(termino) ||
    el[2].toLowerCase().includes(termino)
  ).slice(0, 6);

  encontrados.forEach(el => {
    const item = document.createElement("div");
    item.className = "result";
    item.textContent = `${el[1]} — ${el[2]} (${el[0]})`;
    item.onclick = () => {
      search.value = el[1];
      results.hidden = true;
      seleccionarElemento(elementNodes.get(el[0]));
      elementNodes.get(el[0]).scrollIntoView({ behavior: "smooth", block: "center", inline: "center" });
    };
    results.appendChild(item);
  });

  results.hidden = encontrados.length === 0;
}

function limpiarFiltro() {
  filterCategory = null;
  search.value = "";
  actualizarEstilos();
  info.textContent = "Filtro eliminado. Haz clic en un elemento para ver su información.";
}

function filtrarCategoria(categoria) {
  filterCategory = filterCategory === categoria ? null : categoria;
  actualizarEstilos();

  if (filterCategory) {
    info.textContent = `Filtro activo: ${categoria.charAt(0).toUpperCase() + categoria.slice(1)}. Pulsa otra vez la categoría para quitarlo.`;
  } else {
    info.textContent = "Filtro eliminado.";
  }
}

function mostrarPreview(node, event) {
  const el = obtenerElemento(node);
  const [z, sym, nombre, masa, cat] = el;
  const color = colores[cat] || "#607D8B";

  preview.innerHTML = `
    <div class="preview-symbol" style="color:${color}">${sym}</div>
    <div class="preview-text">${nombre}<br>N.º atómico: ${z} | ${masa} u</div>
  `;

  preview.hidden = false;

  const x = Math.min(event.clientX + 16, window.innerWidth - 225);
  const y = Math.min(event.clientY + 16, window.innerHeight - 90);
  preview.style.left = `${Math.max(5, x)}px`;
  preview.style.top = `${Math.max(5, y)}px`;
}

function ocultarPreview() {
  preview.hidden = true;
}

function onHover(node, event) {
  if (hoveredElement === node) return;

  if (hoveredElement) hoveredElement.classList.remove("hovered");
  hoveredElement = node;

  mostrarPreview(node, event);
  playSound("hover");
}

function onLeave() {
  if (hoveredElement) hoveredElement.classList.remove("hovered");
  hoveredElement = null;
  ocultarPreview();
}

function cambiarTema() {
  darkTheme = !darkTheme;
  document.body.classList.toggle("light", !darkTheme);
  themeBtn.textContent = darkTheme ? "Tema claro" : "Tema oscuro";
}

function moverSeleccion(direccion) {
  if (!selectedElement) {
    seleccionarElemento(elementNodes.get(elementos[0][0]));
    return;
  }

  const actual = obtenerElemento(selectedElement);
  const fila = actual[5];
  const col = actual[6];

  const candidatos = elementos.map(el => {
    const diferenciaFila = Math.abs(el[5] - fila);
    const diferenciaCol = Math.abs(el[6] - col);

    let valido = false;
    let score = Infinity;

    if (direccion === "izquierda" && el[6] < col) {
      valido = true;
      score = diferenciaCol * 10 + diferenciaFila;
    } else if (direccion === "derecha" && el[6] > col) {
      valido = true;
      score = diferenciaCol * 10 + diferenciaFila;
    } else if (direccion === "arriba" && el[5] < fila) {
      valido = true;
      score = diferenciaFila * 10 + diferenciaCol;
    } else if (direccion === "abajo" && el[5] > fila) {
      valido = true;
      score = diferenciaFila * 10 + diferenciaCol;
    }

    return { el, valido, score };
  }).filter(x => x.valido);

  if (candidatos.length) {
    candidatos.sort((a,b) => a.score - b.score);
    seleccionarElemento(elementNodes.get(candidatos[0].el[0]));
  }
}

document.getElementById("search-btn").onclick = buscarElemento;
document.getElementById("clear-btn").onclick = limpiarFiltro;
document.getElementById("favorite-btn").onclick = alternarFavorito;
document.getElementById("compare-btn").onclick = alternarComparacion;
document.getElementById("theme-btn").onclick = cambiarTema;
scale.onchange = actualizarEstilos;
search.oninput = actualizarResultados;
search.onkeydown = e => {
  if (e.key === "Enter") buscarElemento();
};

document.getElementById("modal-close").onclick = cerrarDetalle;
document.getElementById("comparison-close").onclick = () => comparisonModal.hidden = true;

detailsModal.addEventListener("click", e => {
  if (e.target === detailsModal) cerrarDetalle();
});

comparisonModal.addEventListener("click", e => {
  if (e.target === comparisonModal) comparisonModal.hidden = true;
});

document.addEventListener("keydown", e => {
  if (e.key === "ArrowLeft") moverSeleccion("izquierda");
  if (e.key === "ArrowRight") moverSeleccion("derecha");
  if (e.key === "ArrowUp") moverSeleccion("arriba");
  if (e.key === "ArrowDown") moverSeleccion("abajo");
  if (e.key === "Enter" && selectedElement) mostrarDetalles(obtenerElemento(selectedElement));
  if (e.key === "Escape") {
    cerrarDetalle();
    comparisonModal.hidden = true;
  }
});

crearTabla();
crearLeyenda();
actualizarEstilos();
