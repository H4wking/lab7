from task3.zip_processor import ZipProcessor
from task3.zip_replace import ZipReplace
from task3.scale_zip import ScaleZip


object = ZipReplace("data.txt.zip", "BAB", "ABA")
object_scale = ScaleZip('image.jpg.zip', (800, 300))
# res = ZipProcessor(text_link, object)
res = ZipProcessor('image.jpg.zip', object_scale)
res.process_zip()
