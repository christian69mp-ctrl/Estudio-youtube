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

### D-ESTUDIO-004 — 2026-10-23 — Objetivo de monetización
- Estado: **aprobada** (Christian, 2026-10-23: priorizar Código Mafia y la serie «Mafias en España»). ~~En espera~~ → **ACTIVA desde 2026-10-26**: 2 largos/semana, toda la capacidad a Código Mafia; resto de canales en pausa de producción nueva.
- Qué: priorizar Código Mafia (horas estimadas cerca de 4.000; faltan ~650 suscriptores). Ver `ESTUDIO/PLAN_MONETIZACION_2026.md`.
- Por qué: el 1/02/2027 los requisitos para nuevos solicitantes se duplican (8.000 h / 20 M Shorts); fuente oficial de YouTube.
- Alcance: estudio

### D-ESTUDIO-005 — 2026-10-26 — Solo vídeos largos en todos los canales
- Estado: aprobada (Christian); ampliada a todos los canales el mismo día
- Qué: **no se crean Shorts en ningún canal.** La audiencia se construye solo con vídeos largos.
- Por qué [DATO CHRISTIAN + INTERPRETACIÓN]: en Jager Aviación los Shorts captaron suscriptores que no ven largos (99 % de las vistas son Shorts; los largos recientes 4–30 vistas). No se quiere repetir.
- Sustituye a: la recomendación de Shorts de enlace (2026-10-25/26) y al punto «3 Shorts por cada largo» de `PLAN_MONETIZACION_2026.md`.
- Consecuencia: la vía a la monetización es solo por 4.000 horas de largos. Palancas: ritmo constante de largos, pantallas finales y tarjetas entre largos, listas de reproducción por serie, paquetes título+miniatura.
- Alcance: todos los canales (Jager Aviación, Código Mafia, Jager Crime, Archivos Sagrados, Jager Explica). Jager Aviación: los Shorts ya publicados no se tocan (borrar contenido público solo con orden expresa); simplemente no se publican más.

### D-ESTUDIO-006 — 2026-10-26 — Pixelido, editor de todos los canales
- Estado: aprobada (Christian)
- Qué: **Pixelido** edita los vídeos de todos los canales a partir de ahora.
- Entrega estándar a Pixelido por vídeo: `LOCUCION_EDITOR.txt` (solo texto para la voz sintética) + indicaciones visuales del `GUION.md` cuando hagan falta + paquete definitivo (título y prompt de miniatura para Gemini).
- Confirmado (26/10): ~~Pixelido no es el editor de PED-01~~ (malentendido, corregido el mismo día) → **PED-01 (10 guiones) es el primer pedido de Pixelido (PX-01)**; el siguiente (PX-02) será todo de Código Mafia. Pixelido es el editor definitivo. Capacidad 2 largos/semana. Pedidos por lotes (todos los vídeos a la vez) con tema, guion, descripción de edición y observaciones; fases guion → edición → miniatura, cada una aprobada por Christian. Detalle: `ESTUDIO/PIXELIDO.md`.
- Sustituye a: «el editor» genérico en PED-01 y en el plan de monetización.
- Alcance: todos los canales
