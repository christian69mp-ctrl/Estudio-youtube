# DECISIONES DEL ESTUDIO (organización general, no de canal)

### D-ESTUDIO-001 — 2026-10-22 — Repositorio propio para el estudio
- Estado: aprobada (Christian: "a un repositorio propio, no tiene nada que ver con Reino Peludos")
- Qué se decidió: el estudio vive en el repositorio `estudio-youtube`, separado del tema de Shopify Reino Peludos.
- Por qué: son proyectos sin relación; mezclarlos complicaba ambos y podía disparar sincronizaciones de la tienda.
- Sustituye a: ubicación provisional dentro del repositorio Reino Peludos (nunca subida).
- Alcance: estudio

### D-ESTUDIO-002 — 2026-10-23 — Acceso a datos públicos de YouTube por API
- Estado: aprobada
- Qué se decidió: usar YouTube Data API v3 mediante secreto de red (`www.googleapis.com`, cabecera `X-Goog-Api-Key`) para datos públicos de canales propios y competencia.
- Por qué: la red de la sesión bloquea `www.youtube.com`; la API es oficial y no expone la clave.
- Uso: `curl "https://www.googleapis.com/youtube/v3/..."` sin `key=`. Cuota diaria limitada: priorizar llamadas baratas (channels, playlistItems, videos) y evitar `search` (coste alto) salvo necesidad.
- Límites: solo datos públicos (visualizaciones, likes, comentarios, duración, fechas). CTR, retención y fuentes de tráfico requieren YouTube Studio.
- Sustituye a: —
- Alcance: estudio
