import cv2, datetime
from cv2 import dnn_superres

print(f'Setting model... {datetime.datetime.now()}')

# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()

# Read image
image = cv2.imread('./temp/0.png')

# Read the desired model
path = "./models/EDSR_x4.pb"
sr.readModel(path)

# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("edsr", 4)


start_time = datetime.datetime.now()
print(f'Upscaling...{start_time}')

# Upscale the image
result = sr.upsample(image)

end_time = datetime.datetime.now()
print(f'Time consumed: {end_time - start_time}')



print(f'Saving...{datetime.datetime.now()}')
# Save the image
cv2.imwrite("./temp/0-up.png", result)

print(f'Done!{datetime.datetime.now()}')