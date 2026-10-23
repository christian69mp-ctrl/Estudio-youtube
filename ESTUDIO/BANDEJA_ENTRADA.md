# BANDEJA DE ENTRADA

Material, ideas y dudas sin clasificar. Al procesar un elemento, muévelo a su canal/proyecto y márcalo como procesado.

## Pendiente de procesar

### 2026-10-22 — Dudas abiertas del arranque
- [x] Canales activos: Jager Aviación, Jager Crime, Archivos Sagrados, Código Mafia. Jager Explica inactivo, se reactivará. → procesado en INDICE_CANALES.md
- [x] Historias Prohibidas = nombre público de Jager Crime (2026-10-23).
- [ ] Jager Explica: enfoque y fecha de reactivación (hipotéticos, ciencia, economía o una combinación).
- [x] Jager Vibes, Plays, Bomb, Retro, Relaja2: no mencionados como activos → se tratan como inactivos.
- [ ] Canal y vídeo con el que empezamos.
- [x] Enlaces de los canales (2026-10-23). - [ ] Capturas de YouTube Studio (prioridad: largos de Jager Aviación).
- [ ] Ritmo de locución real de Christian (para calibrar extensión de guiones).
- [ ] Herramientas de producción (locución, edición, generación de imágenes) para adaptar los entregables.

### 2026-10-23 — Análisis de canales propios y competencia
- Christian enviará la URL de cada canal para analizar qué ha funcionado (propio y competencia).
- Limitación comprobada el 2026-10-23: la política de red de la sesión bloquea `www.youtube.com` e `i.ytimg.com`. `www.googleapis.com` sí responde (YouTube Data API, requiere clave).
- RESUELTO 2026-10-23: clave de YouTube Data API v3 (proyecto Google Cloud `estudio-youtube`, restringida a esa API) guardada como **secreto de red** del entorno "Predeterminado" para `www.googleapis.com`, cabecera `X-Goog-Api-Key`. Llamadas sin parámetro `key`; la clave no es visible en la sesión. Prueba OK el 2026-10-23. Ver D-ESTUDIO-002.
- Método previsto: por canal, inventario de vídeos (título, fecha, duración, visualizaciones públicas); comparación con la mediana del propio canal; 3–5 competidores por canal con datos públicos; patrones de tema, ángulo, título y miniatura marcados como indicio o hipótesis. Sin métricas privadas de terceros.

### 2026-10-23 — Guiones hechos sin publicar
- [ ] Christian tiene AF447 (no aparece entre los vídeos públicos). Pedir lista de guiones o vídeos ya hechos y no publicados de cada canal para no repetir (posible origen: chats «Guion mafia», «Guiones mister tops», «Guiones historias» en claude.ai).

## Procesado
- 2026-10-22 — Ubicación del estudio: repositorio propio `estudio-youtube`, separado de Reino Peludos (decisión de Christian). → ESTADO_SESION.md
