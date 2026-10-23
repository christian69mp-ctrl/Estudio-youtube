"""Vídeos con más visualizaciones de un nicho (búsqueda pública), para análisis de competencia.

Uso: python3 -I yt_nicho.py "consulta" AAAA-MM-DD salida.csv
Coste de cuota: search = 100 unidades por llamada (+1 videos, +1 channels). Usar con moderación.
Limitaciones: la búsqueda de YouTube no es exhaustiva; relevanceLanguage=es es una preferencia, no un filtro.
Shorts: duración <= 180 s (aproximación).
"""
import csv, json, re, sys, urllib.parse, urllib.request

API = "https://www.googleapis.com/youtube/v3/"
def get(e, **p):
    with urllib.request.urlopen(API + e + "?" + urllib.parse.urlencode(p), timeout=30) as r:
        return json.load(r)
def dur(iso):
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    d, h, mi, s = (int(x or 0) for x in m.groups()) if m else (0, 0, 0, 0)
    return d * 86400 + h * 3600 + mi * 60 + s

q, desde, out = sys.argv[1:4]
s = get("search", part="id", q=q, type="video", order="viewCount", maxResults=50,
        relevanceLanguage="es", publishedAfter=desde + "T00:00:00Z")
ids = [i["id"]["videoId"] for i in s.get("items", [])]
vs = get("videos", part="snippet,statistics,contentDetails", id=",".join(ids)).get("items", []) if ids else []
chs = {c["id"]: c for c in get("channels", part="statistics", id=",".join({v["snippet"]["channelId"] for v in vs})).get("items", [])} if vs else {}
rows = []
for v in vs:
    sn, st = v["snippet"], v.get("statistics", {})
    cs = chs.get(sn["channelId"], {}).get("statistics", {})
    d = dur(v["contentDetails"].get("duration"))
    rows.append(dict(consulta=q, video_id=v["id"], titulo=sn["title"], canal=sn["channelTitle"],
        canal_id=sn["channelId"], subs_canal=cs.get("subscriberCount", "oculto"),
        idioma=sn.get("defaultAudioLanguage", sn.get("defaultLanguage", "")),
        publicado=sn["publishedAt"][:10], duracion_min=round(d / 60, 1),
        formato="short?" if d <= 180 else "largo", vistas=int(st.get("viewCount", 0))))
rows.sort(key=lambda r: -r["vistas"])
with open(out, "a", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    if f.tell() == 0: w.writeheader()
    w.writerows(rows)
print(q, len(rows))
