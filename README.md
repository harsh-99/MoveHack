# Installation
`bash 
$pip install -r requirments.txt
`

# Semantic Segmentation
Implement [Semantic Segmentation](http://arxiv.org/abs/1511.00561) in tensorflow,
successfully trained segnet-basic in Indian driving conditions dataset by Intel and IIIT hyderabad.


The model segments any input image into 14 classes along with the labels as follows 

- Background(0)
- Fence and walls(1)
- Road(2)
- Billboards, poles and bridges(3)
- Riders and regular vehicles (4) 
- People and animals(5) 
- Sidewalk(6)
- Curb(7)
- Parking(8)
- Drivable fallback(damaged parts of the road)(9)
- Heavy duty vehicles(truck, trailers, etc.)(10)
- Non-drivable fallback(damaged sidewalks, etc.)(11)
- Obstacles(garbage dumps, boulders)(12)
- Unlabelled(13)

# Road Damage detector 

Implemented Single Shot detector with MobileNet in tensorflow. The model detects the following 10 classes in input image and creates Bounding Box

-[alt text](a.png)

# Requirement

Check requirements.txt 


# Instructions for Running the code

Put all the testing images in a folder named test. 

Command for testing:
`bash
  $python run.py --folder test/
`
The Sematically Segmented images will be saved in the folder named out_image(each pixel lies between the value 0 to 13 depending on the class it belongs) and images with road damage detection will be saved in the folder named road_damage. The quality factor will be printed on the terminal along with the name of input image.  
