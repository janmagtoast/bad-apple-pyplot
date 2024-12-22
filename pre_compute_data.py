import numpy as np
import pickle
from PIL import Image

img = [Image.open(f'badapple/frame_{i}.png').convert('1') for i in range(1, 6562, 2)]
# function breaks if frames have different resolutions
width, height = img[0].size

# convert images to matrices that we can later plot with plot_it.py
def convert_img(img, hor_res, line_amount):
    lines_amount = 3
    y_arr = np.zeros((line_amount,hor_res))

    for u in range(hor_res):
        w_current = u * width // hor_res
        
        line_counter = 0
        prev_yes_no = False
        for v in range(height):
            yes_no = img.getpixel((w_current, v)) != 0
            if yes_no != prev_yes_no:
                prev_yes_no = yes_no
                y_arr[line_counter,u] = height - v

                line_counter += 1
                if line_counter >= line_amount:
                    break
    return y_arr


# adjust for more detailed plots. these values worked decently enough for bad apple
hor_res = 240
line_amount = 30
x = np.arange(hor_res)
y = [convert_img(frame, hor_res, line_amount) for frame in img]

with open('already_computed_data.pkl', 'wb') as f:
    pickle.dump((width, height, hor_res, line_amount, x, y), f)
