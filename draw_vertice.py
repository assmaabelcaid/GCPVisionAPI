import io
from PIL import Image, ImageDraw, ImageFont

def drawVertices(image_source, vertices, display_text=''):
    pillow_image = Image.open(io.BytesIO(image_source))

    draw = ImageDraw.Draw(pillow_image)
    for i in range(len(vertices) - 1):
        draw.line(((vertices[i][0], vertices[i][1]), (vertices[i + 1][0],
                   vertices[i + 1][1])), fill='green', width=6)

    draw.line(((vertices[len(vertices)-1][0], vertices[len(vertices)-1][1]),
               (vertices[0][0], vertices[0][1])), fill='green',width=6)

    font = ImageFont.truetype('arial.ttf', 100)
    draw.text((vertices[0][0], vertices[0][1]), font=font, text=display_text, fill='green')

    pillow_image.show()
