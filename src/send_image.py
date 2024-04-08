from datetime import date
import os
import numpy as np
import pywhatkit
import dataframe_image as dfi
import pandas as pd
from src.vendeurs_phone import *


class SendImage:
    def __init__(self, dataframe, fdv: list[str], message: str) -> None:
        self.dataframe = dataframe
        self.fdv = fdv
        self.message = message

    def send_image(self):
        def highlight_max(s):
            if s.dtype == np.object:
                is_neg = [False for _ in range(s.shape[0])]
            else:
                is_neg = s < 0
            return ["color: red;" if cell else "color:black" for cell in is_neg]

        for i in self.fdv:
            df = self.dataframe.query(f"Vendeur== '{i}'")

            df = df.style.apply(highlight_max)
            image_name = f"images/{i}.jpg"
            dfi.export(df, image_name)

            pywhatkit.sendwhats_image(
                vendeur_number_phone[i], image_name, caption=self.message,wait_time=15
            )
            os.remove(image_name)



