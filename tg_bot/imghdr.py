def what(file, h=None):
    if h is None:
        try:
            with open(file, "rb") as f:
                h = f.read(32)
        except Exception:
            return None
    if not isinstance(h, (bytes, bytearray)):
        return None
    if h.startswith(b"\xff\xd8"):
        return "jpeg"
    if h.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if h[:6] in (b"GIF87a", b"GIF89a"):
        return "gif"
    if h.startswith(b"BM"):
        return "bmp"
    if h.startswith(b"II") or h.startswith(b"MM"):
        return "tiff"
    if h.startswith(b"RIFF") and h[8:12] == b"WEBP":
        return "webp"
    return None