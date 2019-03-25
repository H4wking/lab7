from task3.scale_zip import ScaleZip

size = tuple(map(int, input("Enter new size separated with space:\n").split()))
zp = ScaleZip("image.jpg.zip", size)
zp.process_zip()