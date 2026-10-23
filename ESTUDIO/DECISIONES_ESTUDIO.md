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

### D-ESTUDIO-003 — 2026-10-23 — Paquete definitivo de título + miniatura
- Estado: aprobada (Christian)
- Qué se decidió:
  - Cada vídeo sale con **una sola versión definitiva** de título y miniatura, ya combinados y optimizados para móvil. No se entregan variantes ni se cambian después de publicar salvo que Christian lo pida.
  - **Clickbait permitido** para provocar el clic (curiosidad, tensión, pregunta abierta), **siempre que el vídeo cumpla lo prometido**: los guiones están pensados para enganchar y retener. Límite: nada que el vídeo no muestre o que contradiga los hechos (YouTube tiene normas contra metadatos engañosos y engañar al espectador castiga la retención).
  - Título y miniatura cuentan una historia visual juntos sin revelar el desenlace: el título da el contexto y la tensión; la miniatura, la pista visual; el texto de la miniatura no repite el título.
  - **Miniaturas: las genera Christian con Gemini.** Claude entrega el prompt listo para pegar, el texto exacto y la checklist de revisión.
  - **Títulos: los escribe Claude**, ya listos para subir.
- Sustituye a: PROTOCOLOS §5 (3 combinaciones + recomendada) para el flujo habitual. Las 3 combinaciones solo si Christian las pide.
- Alcance: todos los canales
