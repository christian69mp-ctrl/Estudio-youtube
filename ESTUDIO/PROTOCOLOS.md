# PROTOCOLOS DEL ESTUDIO

Cómo ejecutar cada tarea. Las reglas de fondo están en `/CLAUDE.md`. Las plantillas están al final.

---

## 1. Comandos naturales

| Christian dice (o algo equivalente) | Qué hacer |
|---|---|
| "Modo estudio" | Resumen de canales, proyectos, prioridades y bloqueos desde `PANEL_GENERAL.md`, `CALENDARIO.md` y cada `ESTADO_ACTUAL.md`. |
| "Vamos con [canal]" | Guarda el punto del canal anterior. Carga `IDENTIDAD`, `ESTADO_ACTUAL`, `APRENDIZAJES` del nuevo. Resume pendientes y propone el siguiente paso. |
| "Nuevo vídeo sobre [tema]" | §3 Nuevo proyecto. Empieza por enfoque y fuentes, no por el guion. |
| "Dame título y miniatura" | §5. |
| "Escribe el guion" | §6, usando enfoque aprobado e investigación disponible. Si no hay enfoque aprobado, dilo y propón uno. |
| "Analiza estas métricas" | §8. |
| "Qué publico ahora" | Revisa proyectos en `listo`, encaje editorial, calendario y capacidad real. Una recomendación. |
| "Cierra sesión" | §2 Cierre. |
| "Continúa" | Lee `ESTADO_SESION.md` y retoma el proyecto activo. |
| "Muestra aprendizajes" | Resume `APRENDIZAJES.md` del canal separando patrones, indicios e hipótesis. |
| "Revisión semanal" | §10. |
| "Déjamelo listo para publicar" | §9. No implica autorización para publicar. |

---

## 2. Inicio y cierre de sesión

**Inicio:** `CLAUDE.md` → `ESTADO_SESION.md` → `PANEL_GENERAL.md` → archivos del canal/proyecto activo. Continúa desde el último punto confirmado.

**Cierre:**
1. Actualiza `ESTADO_ACTUAL.md` de cada canal tocado (fase, siguiente paso concreto).
2. Registra decisiones en `DECISIONES.md` del canal.
3. Actualiza `PANEL_GENERAL.md` y `CALENDARIO.md` si cambió algo.
4. Reescribe `ESTADO_SESION.md` (canal/proyecto activo, último punto confirmado, siguiente paso, preguntas abiertas).
5. Comprueba que los archivos se leen correctamente.
6. Informa del estado en git (commit hecho o no, subido o no). No subas sin autorización vigente.

---

## 3. Nuevo proyecto de vídeo

1. Confirma el canal. Si el tema no encaja en su promesa, dilo antes de crear nada y propón alternativa o canal.
2. Comprueba en `IDEAS.md` y en `VIDEOS/` que no esté repetido.
3. Crea `CANALES/[id]/VIDEOS/[AAAA-MM-DD_slug]/FICHA.md` (plantilla A).
4. Define el enfoque: público, promesa, pregunta narrativa, punto de vista diferencial.
5. Abre `INVESTIGACION.md` con fuentes primarias candidatas y lagunas.
6. Estado `propuesto` hasta que Christian apruebe el enfoque.

---

## 4. Selección de temas (cuando pida ideas)

Evalúa cada candidato frente a los criterios del canal (`ESTRATEGIA.md`):
encaje con la audiencia · promesa concreta · curiosidad y conflicto · diferenciación frente a lo publicado · disponibilidad de fuentes · viabilidad visual · esfuerzo de producción · relación con otros vídeos · riesgo de repetición o confusión de nicho.

- Pocas opciones bien razonadas; **una recomendada** y por qué.
- Puntuaciones = valoración editorial, no predicción de visitas. Dilo.
- Competidores: solo datos públicos verificables, con enlace. Nunca métricas privadas inventadas.
- Ideas aceptadas → `IDEAS.md` del canal correcto.

---

## 5. Título y miniatura (una sola promesa)

Primero el enfoque; después título y miniatura juntos.

**Entrega completa:**
1. Promesa central del vídeo.
2. Tres combinaciones título+miniatura **realmente distintas** (ángulo distinto, no un adjetivo distinto).
3. Combinación recomendada.
4. Motivo.
5. Riesgo principal de interpretación.
6. Versión final lista para producir.

**Título:** comprensible sin conocer el canal; lo importante al principio; específico y natural; nada que el vídeo no sostenga; no repite el texto de la miniatura.

**Miniatura — especificar siempre:**
- Composición · Sujeto principal · Fondo · Texto exacto y colocación (0–4 palabras; "sin texto" es válido) · Colores e iluminación · Elementos excluidos · Prompt de generación · Criterios de revisión.
- Un foco dominante. Secundarios solo si explican la historia. Flechas/círculos solo hacia una pista relevante. Legible a tamaño pequeño. Identidad del canal (`ESTILO.md`).

**Criterios de revisión estándar:** ¿se entiende a ~160 px de ancho? ¿un único foco? ¿el texto se lee en móvil? ¿añade algo que el título no dice? ¿corresponde al contenido real? ¿coherente con el canal? ¿podría confundirse con una fotografía real del suceso?

Guardar en `VIDEOS/[id]/TITULOS_Y_MINIATURAS.md` con versión y estado.

---

## 6. Investigación y guion largo

**Antes del guion** (en `FICHA.md`): público, promesa título+miniatura, pregunta narrativa principal, punto de vista diferencial, duración deseada, estructura, información imprescindible, fuentes pendientes.

**Investigación** (`INVESTIGACION.md`): fuentes primarias primero, con enlace; discrepancias registradas; cada afirmación clave con su fuente o marcada [PENDIENTE].

**Guion** (`GUION.md`):
- Cumple la promesa desde el inicio; sin saludos largos.
- Contexto cuando el espectador lo necesita.
- Alterna hechos, consecuencias, preguntas y respuestas. Tensión real, sin muletillas ("lo peor estaba por llegar").
- Cierra todas las preguntas abiertas. CTA breves y justificadas.
- Voz propia del canal (`ESTILO.md`).

**Extensión:** ritmo de locución de Christian **pendiente de calibrar**. Supuesto provisional: 140–160 palabras/minuto (≈ 1.400–1.600 palabras cada 10 min). Calibrar con la duración real del primer vídeo locutado y registrar en `ESTILO.md` del canal.

**Formato de entrega (cuando lo pida):**
1. Guion limpio para locución (sin acotaciones, pegable en herramienta de producción).
2. Indicaciones visuales separadas (por bloque numerado).
3. Fuentes.
4. Afirmaciones que requieren última comprobación.

---

## 6b. Plantilla de guion largo de alta retención (aprobada 2026-10-23)

Objetivo de diseño: retención alta (meta de Christian: ≥ 50 %). Es un objetivo, no una garantía; se valida con los datos de Studio.

1. **Super hook (0:00–0:30, ~70–90 palabras).** Entrar en el momento de máxima tensión o con el dato más fuerte y verificado. Plantear la pregunta del vídeo y prometer la respuesta. Sin saludo.
2. **Bienvenida breve (≤ 2 frases).** Nombre del canal + qué va a descubrir el espectador. Nada más.
3. **Cuerpo en actos de ~2–3 min.** Cada acto abre un bucle (pregunta) y cierra otro anterior. Micro hook cada ~45–90 s: dato concreto, giro, contradicción o «pero había un detalle…».
4. **Cliffhangers** antes de los puntos típicos de abandono (~25 %, 50 % y 75 %): cortar justo antes de una revelación y resolverla tras la transición.
5. **Datos impactantes solo verificados**, con fuente en `INVESTIGACION.md`. Las dramatizaciones se marcan.
6. **CTA:**
   - Suscripción breve justo después del primer gran pago de información (no al inicio).
   - Comentario: una pregunta concreta sobre la historia, hacia la mitad.
   - Final: puente al siguiente vídeo relacionado (pantalla final), sin despedida larga.
7. **Cierre:** responder la pregunta del super hook y dejar una última idea que dé valor al espectador (lección, consecuencia, giro final).
8. **Tono:** el de `ESTILO.md` de cada canal (D-TONO). Nunca la misma voz en todos los canales.
9. **Entrega (decisión de Christian, 2026-10-23):**
   - **Al editor:** `LOCUCION_EDITOR.txt` = solo el texto para la voz sintética. Sin títulos, sin notas, sin marcas, sin bloques recortables, sin nada de revisión. Solo se genera con todas las afirmaciones confirmadas o retiradas del texto.
   - **Interno (estudio):** `GUION.md` con locución, indicaciones visuales, fuentes y afirmaciones a verificar.

**Extensión (Christian, 2026-10-23: «cumple lo prometido»):** objetivo firme 3.600–3.900 palabras de locución; no entregar por debajo de 3.500 salvo que falten datos verificados, y entonces avisar.

**Extensión con voz sintética:** a 150–160 palabras/min, 4.000 palabras ≈ 25–27 min; a 190–200 palabras/min ≈ 20–21 min. Supuesto provisional: 3.600–4.000 palabras con bloques marcados como recortables. Calibrar con la duración real de la primera locución.

---

## 7. Shorts

Cada short funciona solo y pertenece al canal.
- Inicio inmediato: pregunta, contradicción o hecho concreto.
- Una sola idea → revelación → cierre breve → puente al largo solo si es pertinente.
- No forzar cortes cada dos segundos si perjudica la comprensión.
- Duración pedida → palabras ajustadas (supuesto provisional: ~2,3–2,7 palabras/segundo; 25–35 s ≈ 60–90 palabras).
- Entregar según lo pedido: locución, indicaciones visuales, texto en pantalla, título, descripción y hashtags, relación con el largo.
- Nunca sacrificar exactitud por el gancho.

Guardar en `VIDEOS/[id]/SHORTS.md`.

---

## 8. Análisis de métricas

1. **Extraer solo lo visible** de capturas. Señalar lo ilegible o ausente.
2. **Registrar** en `CANALES/[id]/METRICAS/registro_metricas.csv` (una fila por captura/periodo): canal, vídeo, fecha y hora de la captura, tiempo desde publicación, periodo (acumulado vs. concreto), impresiones, CTR, visualizaciones, duración del vídeo, duración media, % medio visto, caídas de retención, fuentes de tráfico, otros.
3. No mezclar % medio visto con duración media. Cualquier cálculo derivado, con la operación mostrada.
4. Shorts: usar sus métricas específicas; no aplicar el diagnóstico de vídeos largos.
5. **Analizar por separado:** (1) distribución y fuentes de tráfico; (2) atracción de título+miniatura; (3) cumplimiento de la promesa y retención; (4) encaje del tema; (5) continuidad hacia otros contenidos.
6. Comparar con vídeos similares **del mismo canal** a edad comparable. Sin CTR "universal". Sin conclusiones fuertes con muestras pequeñas. No atribuir a la miniatura lo que puede ser otra audiencia/fuente.

**Devolver:** Qué sabemos · Qué no podemos concluir · Hipótesis principal · Acción recomendada · Qué observar después · Qué dato cambiaría la recomendación. Si falta algo, pedir **solo** el dato más útil.

Nunca atribuir un mal resultado a "penalización", "algoritmo roto" o borrado de vídeos sin pruebas.

---

## 9. Paquete de publicación (`PUBLICACION.md`)

Título final · miniatura (archivo o concepto) · descripción natural · fuentes si corresponde · hashtags relevantes sin relleno · etiquetas solo si las pide · comentario fijado que abra una conversación concreta · lista de reproducción sugerida · capítulos solo con tiempos reales o marcados como provisionales · short de apoyo si lo pide.

Hashtags y etiquetas no son el motor del crecimiento. Preparar el paquete **no** autoriza publicar.

---

## 10. Revisión semanal

Por canal activo: qué se publicó (confirmado), resultados registrados, experimentos en curso, problemas y bloqueos. Cierre: **tres prioridades concretas** para la semana (con canal, proyecto y entregable).

---

## 11. Experimentos y cambios

Cada cambio necesita hipótesis. Registro en `CANALES/[id]/METRICAS/experimentos.csv` (plantilla D).
- Si se cambian título y miniatura a la vez, avisar de que no se podrán separar sus efectos.
- Antes de recomendar pruebas nativas de YouTube, verificar cómo funcionan en ese momento (fuente oficial).
- Sin plazos universales: depende de volumen, fuentes de tráfico y objetivo.
- Antes/después = indicio, no demostración de causalidad.
- No cambiar todo por ansiedad.

---

## PLANTILLAS

### A. FICHA.md de un vídeo
```markdown
# [Título de trabajo]
- Canal:
- ID proyecto: AAAA-MM-DD_slug
- Estado: propuesto
- Formato: largo / short / ambos
- Duración deseada:
- Creado: AAAA-MM-DD

## Enfoque
- Público objetivo:
- Promesa (qué se lleva el espectador):
- Pregunta narrativa principal:
- Punto de vista diferencial:
- Encaje con el canal (y riesgo de repetición):

## Estructura provisional
1.

## Imprescindible / fuentes pendientes
-

## Historial
- AAAA-MM-DD — [cambio de estado / decisión] — motivo
## Siguiente paso
-
```

### B. Entrada de APRENDIZAJES.md
```markdown
### AP-NNN — [enunciado breve]
- Canal / vídeo(s):
- Nivel: hipótesis | indicio | patrón repetido
- Evidencia (datos y fuente):
- Fecha y periodo observado:
- Interpretación:
- Limitaciones:
- Qué lo confirmaría o refutaría:
```

### C. Entrada de DECISIONES.md
```markdown
### D-NNN — AAAA-MM-DD — [decisión]
- Estado: propuesta | aprobada | sustituida por D-NNN
- Qué se decidió:
- Por qué:
- Sustituye a:
- Alcance (canal / vídeo):
```

### D. Columnas de experimentos.csv
`id,video,fecha_hora_cambio,variable,version_anterior,version_nueva,hipotesis,motivo,datos_previos,resultado_posterior,limitaciones,estado`
