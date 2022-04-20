from PIL import Image,ImageDraw

with Image.open("image.png") as master:
  with Image.new("RGB",[master.width,master.height]) as output:
    output.paste(master)
    draw = ImageDraw.Draw(output)
    incr = 14*64
    y = incr
    while(y < output.height):
        print(f"h:{y}")
        draw.line((0,y,output.width,y),fill=(128,128,128),width=5)
        y += incr
    x = incr
    while(x < output.width):
        print(f"v:{x}")
        draw.line((x,0,x,output.height),fill=(128,128,128),width=5)
        x += incr
    print("saving...")
    output.save("final.png")










