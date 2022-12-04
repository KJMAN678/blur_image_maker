import random

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


def bul_image_maker(height: int, width: int, times: int) -> None:

    """
    ランダム + 累積和で画像を作って表示する

    args:
        height (int): 画像の縦サイズ
        width (int): 画像の横サイズ
        times (int): 累積和の計算を行う回数。数を増やすほどランダム性の高い画像となる
    return: None
    """

    H, W, N = (height, width, 256 // times)

    coef_list = [random.choice([-1, 1]) for i in range(times)]

    im = np.zeros((height, width))

    for time in range(times):

        st.write(f"{time}/{times}")

        H_start = random.randint((random.randint(1, H - 3)), H - 2)
        H_end = H_start
        W_start = random.randint(random.randint(1, W - 3), W - 2)
        W_end = W_start

        ABCD = []

        for i in range(N):
            ABCD.append(
                [
                    random.randint(1, H_start),
                    random.randint(1, W_start),
                    random.randint(H_end, H),
                    random.randint(W_end, W),
                ]
            )

        Z = [[0] * (W + 2) for i in range(H + 2)]  # Z = [[0] * (W+1)] * H だとダメっぽい
        answer = [[0] * (W + 2) for i in range(H + 2)]

        for i in range(N):
            A, B, C, D = ABCD[i][0], ABCD[i][1], ABCD[i][2], ABCD[i][3]

            Z[A][B] += 1 * coef_list[time]
            Z[C + 1][D + 1] += 1 * coef_list[time]
            Z[A][D + 1] -= 1 * coef_list[time]
            Z[C + 1][B] -= 1 * coef_list[time]

        # 横
        for i in range(1, H + 1):
            for j in range(1, W + 1):
                answer[i][j] = answer[i][j - 1] + Z[i][j]

        # 横
        for i in range(1, W + 1):
            for j in range(1, H + 1):
                answer[j][i] = answer[j - 1][i] + answer[j][i]

        im += np.array(answer)[1:-1, 1:-1]

    im = im + (np.max(im) - np.min(im))
    im = im * (255 / np.max(im))
    im = im / np.max(im)

    plt.axis("off")
    plt.imshow(im)

    return im
