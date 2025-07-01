import sys
import tkinter as tk
from .text import clr
from .traceback import err
from PIL import Image, ImageTk


def splash_screen(img_path: str, duration: int = 3) -> None:
    """
    Displays a splash screen for the given duration
    - Supports: GIFs / PNGs / JPGs / BMPs / ICOs

    __________________________________________

    [ EXAMPLE ]

    ```python
    from concurrent.futures import ThreadPoolExecutor
    ThreadPoolExecutor().submit(splash_screen, "splash.gif", duration=3)
    ```
    """

    class SplashScreen(tk.Toplevel):
        def __init__(self, img_path):
            super().__init__()
            self.img_path = img_path
            self.setup_window()
            self.load_image()
            self.animate_image()

        def setup_window(self):
            self.overrideredirect(True)
            self.wm_attributes("-topmost", True)
            # self.wm_attributes("-transparentcolor", "white")

            self.image = Image.open(self.img_path)
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()

            width = self.image.width
            height = self.image.height
            x = (screen_width - width) // 2
            y = (screen_height - height) // 2

            self.geometry(f"{width}x{height}+{x}+{y}")
            self.canvas = tk.Canvas(self, bg="black", highlightthickness=0)
            self.canvas.pack()

        def load_image(self):
            if self.img_path.lower().endswith(".gif"):
                self.frames = []
                for i in range(self.image.n_frames):
                    self.image.seek(i)
                    frame = ImageTk.PhotoImage(self.image)
                    self.frames.append(frame)
            else:
                self.frames = [ImageTk.PhotoImage(self.image)]

        def animate_image(self, current_frame=0):
            self.canvas.delete(tk.ALL)
            self.canvas.config(
                width=self.frames[current_frame].width(),
                height=self.frames[current_frame].height(),
            )
            self.canvas.create_image(
                self.frames[current_frame].width() // 2,
                self.frames[current_frame].height() // 2,
                image=self.frames[current_frame],
            )
            current_frame = (current_frame + 1) % len(self.frames)
            if len(self.frames) > 1:
                self.after(
                    int(1000 / self.image.info["duration"]),
                    self.animate_image,
                    current_frame,
                )

    try:
        root = tk.Tk()
        root.withdraw()
        SplashScreen(img_path)
        root.after(int(duration * 1000), root.quit)
        root.mainloop()
    except Exception as exc:
        sys.exit(clr(err((type(exc), exc, exc.__traceback__)), 2))
