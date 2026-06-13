from __future__ import annotations

import random

from PIL import Image, ImageDraw

from CaptchaGenerator.core import CaptchaConfig, ChallengeResult, VisualChallenge


class Perspective3DCaptcha(VisualChallenge):
    """Identify a face of a pseudo-3D cube rendered in perspective."""

    def generate(
        self,
        *,
        name_export: str,
        path_export: str,
        labels: tuple[str, str, str] = ("A", "B", "C"),
        ask_face: str | None = None,
        skew: float = 0.35,
        config: CaptchaConfig | None = None,
    ) -> ChallengeResult:
        resolved = self._config(config)
        image = Image.new("RGB", resolved.size, resolved.background_color)
        draw = ImageDraw.Draw(image)
        side = min(resolved.width, resolved.height) * 0.34
        cx, cy = resolved.width / 2, resolved.height / 2 + side * 0.12
        dx, dy = side * skew, -side * skew
        front = [(cx - side / 2, cy - side / 2), (cx + side / 2, cy - side / 2),
                 (cx + side / 2, cy + side / 2), (cx - side / 2, cy + side / 2)]
        top = [front[0], front[1], (front[1][0] + dx, front[1][1] + dy),
               (front[0][0] + dx, front[0][1] + dy)]
        right = [front[1], front[2], (front[2][0] + dx, front[2][1] + dy),
                 (front[1][0] + dx, front[1][1] + dy)]
        faces = {"front": front, "top": top, "right": right}
        colors = resolved.accent_colors[:3]
        face_labels = dict(zip(faces, labels))
        font = self._load_font(list(resolved.fonts), resolved.font_size or int(side / 4))
        for (name, points), color in zip(faces.items(), colors):
            draw.polygon(points, fill=color, outline=resolved.foreground_color)
            x = sum(point[0] for point in points) / 4
            y = sum(point[1] for point in points) / 4
            label = face_labels[name]
            box = draw.textbbox((0, 0), label, font=font)
            draw.text((x - (box[2] - box[0]) / 2,
                       y - (box[3] - box[1]) / 2 - box[1]),
                      label, font=font, fill="white")
        target = ask_face or random.choice(tuple(faces))
        return self._save(
            image, path_export=path_export, name_export=name_export,
            answer=face_labels[target],
            prompt=f"Which label is on the {target} face?",
            metadata={"target_face": target, "labels": face_labels, "skew": skew},
            config=resolved,
        )
