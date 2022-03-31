import sys
from PIL import Image
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

txt = tool.image_to_string(
    #文字認識対象の画像image.pngを用意する
    Image.open("./test.png"),
    lang="jpn",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)

print( txt )