"""Inventario público de un canal de YouTube vía YouTube Data API v3.

Uso: python3 -I yt_inventario.py @handle salida.csv
La clave la añade el proxy (secreto de red); no se pasa `key=`.
Coste aproximado de cuota: 1 + 1 por cada 50 vídeos (playlistItems) + 1 por cada 50 vídeos (videos).
Shorts: se marcan por duración <= 180 s (aproximación; la API no indica si es Short).
"""
import csv, json, re, statistics, sys, urllib.parse, urllib.request
from datetime import datetime, timezone

API = "https://www.googleapis.com/youtube/v3/"

def get(endpoint, **params):
    url = API + endpoint + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)

def dur_s(iso):
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m: return None
    d, h, mi, s = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s

def main(handle, out):
    ch = get("channels", part="snippet,statistics,contentDetails", forHandle=handle.lstrip("@"))
    if not ch.get("items"):
        sys.exit(f"Canal no encontrado: {handle}")
    c = ch["items"][0]
    uploads = c["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, token = [], None
    while True:
        p = dict(part="contentDetails", playlistId=uploads, maxResults=50)
        if token: p["pageToken"] = token
        r = get("playlistItems", **p)
        ids += [i["contentDetails"]["videoId"] for i in r.get("items", [])]
        token = r.get("nextPageToken")
        if not token: break
    rows, now = [], datetime.now(timezone.utc)
    for k in range(0, len(ids), 50):
        r = get("videos", part="snippet,statistics,contentDetails", id=",".join(ids[k:k + 50]))
        for v in r.get("items", []):
            pub = datetime.fromisoformat(v["snippet"]["publishedAt"].replace("Z", "+00:00"))
            d = dur_s(v["contentDetails"].get("duration"))
            st = v.get("statistics", {})
            rows.append(dict(
                video_id=v["id"], titulo=v["snippet"]["title"],
                publicado=pub.strftime("%Y-%m-%d %H:%M UTC"), dias=(now - pub).days,
                duracion_s=d, formato="short?" if d is not None and d <= 180 else "largo",
                vistas=int(st.get("viewCount", 0)), likes=st.get("likeCount", ""),
                comentarios=st.get("commentCount", ""),
            ))
    for fmt in ("largo", "short?"):
        sub = [x["vistas"] for x in rows if x["formato"] == fmt]
        med = statistics.median(sub) if sub else 0
        for x in rows:
            if x["formato"] == fmt:
                x["ratio_vs_mediana_formato"] = round(x["vistas"] / med, 2) if med else ""
    rows.sort(key=lambda x: x["publicado"], reverse=True)
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["video_id"])
        w.writeheader(); w.writerows(rows)
    s = c["statistics"]
    print(json.dumps(dict(
        handle=handle, titulo=c["snippet"]["title"], id=c["id"], creado=c["snippet"]["publishedAt"][:10],
        suscriptores=s.get("subscriberCount") if not s.get("hiddenSubscriberCount") else "oculto",
        vistas_totales=s.get("viewCount"), videos_api=s.get("videoCount"), videos_listados=len(rows),
        consulta=now.strftime("%Y-%m-%d %H:%M UTC")), ensure_ascii=False))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
