echo off
rem uncomment skip for production
rem uncomment switchtest to test class and breed error check listings with resnet, it executes the fastest
rem goto skip
goto switchtest
rem PURPOSE: Runs all three models to test which provides 'best' solution.
rem          Please note output from each run has been piped into a text file.
rem
rem Usage:  run_models_batchsbat    -- will run program from command line within Windows CMD
rem
:skip
echo on
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt > resnet_pet-images.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt
python check_images.py --dir pet_images/ --arch vgg  --dogfile dognames.txt > vgg_pet-images.txt

:switchtest
echo on
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt --incorrect_dog > resnet_pet-images_switch_incorrect_dog.txt
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt --incorrect_breed > resnet_pet-images_switch_incorrect_breed.txt
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt --incorrect_dog --incorrect_breed > resnet_pet-images_switch_incorrect_both.txt
