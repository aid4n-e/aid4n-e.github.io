import shutil
from pathlib import Path
import cv2

CLIPS = Path("assets/clips/6")
FLAGGED = Path("assets/clips_flagged/6")   # flagged clips are moved here, not deleted
FLAGGED.mkdir(exist_ok=True)

detectors = [
    cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml"),
    cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml"),
]

def has_face(path):
    cap = cv2.VideoCapture(str(path))
    step = max(1, int(round(cap.get(cv2.CAP_PROP_FPS) or 24)))   # about 1 frame per second
    n = 0
    found = False
    while not found and cap.grab():
        if n % step == 0:
            ok, frame = cap.retrieve()
            if ok:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.equalizeHist(gray)
                for d in detectors:
                    if len(d.detectMultiScale(gray, 1.1, 5, minSize=(24, 24))):
                        found = True
                        break
        n += 1
    cap.release()
    return found

files = sorted(CLIPS.glob("*.mp4"))
moved = 0
for i, f in enumerate(files, 1):
    if has_face(f):
        shutil.move(str(f), str(FLAGGED / f.name))
        moved += 1
        print(f"[{i}/{len(files)}] FACE   {f.name}")
    else:
        print(f"[{i}/{len(files)}] ok     {f.name}")
print(f"\nDone. Moved {moved} of {len(files)} clips to {FLAGGED}")
