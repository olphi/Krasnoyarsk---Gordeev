from PIL import Image, ImageDraw


class GlassesImageDraw(ImageDraw.ImageDraw):
    def glasses(self, xy, fill):
      x = xy[0]
      y = xy[1]
      w = xy[2]

      self.ellipse((x, y, x + 5 * w, y + 5 * w), fill[1])
      self.ellipse((x + w // 4, y + w // 4, x + 5 * w - w // 4, y + 5 * w - w //4), fill[0])
      self.ellipse((x + 6 * w, y, x + 11 * w, y + 5 * w), fill[1])
      self.ellipse((x + 6 * w + w // 4, y + w // 4, x + 11 * w - w // 4, y + 5 * w - w // 4), fill[0])
      self.rectangle((x + 5 * w, y + 2.5 * w - w // 8, x + 6 * w, y + 2.5 * w + w // 8), fill[1])

img = Image.new('RGB', (240, 240), '#000000')
drw = GlassesImageDraw(img)
drw.glasses((10, 70, 20), ('#ffffff', '#999999'))
img.save('result.png')