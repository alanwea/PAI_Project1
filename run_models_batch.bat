echo off
rem uncomment skip for production
rem uncomment switchtest to test class and breed error check listings with resnet(it executes the fastest)
#goto switchtest

rem PURPOSE: Runs all three models to test which provides 'best' solution.
rem          Please note output from each run has been piped into a text file.
rem
rem Usage:  run_models_batchsbat    -- will run program from command line within Windows CMD
rem
:skip
rem Note that --incorrect_dog and --incorrect_breed were added to original file
echo on
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt --incorrect_dog --incorrect_breed > resnet_pet-images.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt --incorrect_dog --incorrect_breed > alexnet_pet-images.txt
python check_images.py --dir pet_images/ --arch vgg  --dogfile dognames.txt --incorrect_dog --incorrect_breed > vgg_pet-images.txt
Exit

:switchtest
echo on
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt --incorrect_dog > resnet_pet-images_switch_incorrect_dog.txt
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt --incorrect_breed > resnet_pet-images_switch_incorrect_breed.txt
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt --incorrect_dog --incorrect_breed > resnet_pet-images_switch_incorrect_both.txt
