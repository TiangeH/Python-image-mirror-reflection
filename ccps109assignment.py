# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:15:42 2020

@author: Tiange
"""
##Student Name:Tiange Hou
##student ID:500 868 312

#pip install Pillow

import PIL
import numpy as np
from PIL import Image
from numpy import asarray
image_list=[]#creat a list for image
#function insert
def refelction_change():
    number=int(input("Please enter a number between -50 and 50: "))
    direction=input("please enter v for vertial or h for horziontal")
    image_path=input("please enter the image path")
    
    while number<-50 or number> 50:
        number=int(input("Please enter a number between -50 and 50: "))
    while direction not in ('v','h'):
        direction=input("please enter v for vertial or h for horziontal")
    percentage=number
    #print(percentage)
    #print(direction)
    im=Image.open(image_path)
    #im.show()
 
    
    percentage=number/100
    direction_chosed=direction.lower()
    bw_image=im.convert("L")
    arrayof_image_bw=asarray(bw_image)
    image_height=arrayof_image_bw.shape[0]#the shape[h,w] size of image[w,h]
    image_width=arrayof_image_bw.shape[1]
    start_row_index=round(image_height*percentage)
    converted_list=arrayof_image_bw.tolist()
    
    if direction_chosed =='v':
        if percentage>0:
            reflection_lenth=round(image_height*percentage)
            #end_row_index=image_height-start_row_index
            chunk_for_reflection_bein=start_row_index+reflection_lenth #672-288=384
            list_for_reflection_create=converted_list[start_row_index:chunk_for_reflection_bein][::-1]#=[-288:][::1]
            list_for_reflection_create_height=len(list_for_reflection_create)
            original_part_cuted=converted_list[start_row_index:image_height]
            len(original_part_cuted)
            new_list=list_for_reflection_create+original_part_cuted
            new_list_array=np.asarray(new_list) 
            new_list_array.reshape(image_height,image_width) 
            new_list_array=np.int8(new_list_array)
            #the original array of lenna image is dtype=int8
            final_image=Image.fromarray(new_list_array,"L")
            #final_image.show()
            
        
        if percentage<0:
            reflection_lenth=round(image_height*percentage)
            end_row_index=image_height+start_row_index
            chunk_for_reflection_bein=end_row_index+reflection_lenth #672-288=384
            list_for_reflection_create=converted_list[chunk_for_reflection_bein:end_row_index][::-1]#=[-288:][::1]
            list_for_reflection_create_height=len(list_for_reflection_create)
            original_part_cuted=converted_list[0:end_row_index]
            len(original_part_cuted)
            new_list=original_part_cuted+list_for_reflection_create
            new_list_array=np.asarray(new_list) 
            new_list_array.reshape(image_height,image_width) 
            new_list_array=np.int8(new_list_array)
            #the original array of lenna image is dtype=int8
            final_image=Image.fromarray(new_list_array,"L")
            #final_image.show()    
        
        #if percentage==0:
            #im.resize((200,200)).show()
            #return arrayof_image_bw 
        
    if direction_chosed =='h':
        if percentage > 0:
            new_list_pre=[]
            new_list=[]
            end_sub=image_width-start_row_index
            for i in range(0,len(converted_list)):
                original_ap=converted_list[i][0:end_sub]        
                reversed_part=converted_list[i][end_sub-start_row_index:end_sub][::-1]
                merged=original_ap+reversed_part
                new_list.append(merged)#beacuse of array, can't use "+"
            
            
            new_list_array=np.asarray(new_list) 
            new_list_array.reshape(image_height,image_width) 
            new_list_array=np.int8(new_list_array)
                #the original array of lenna image is dtype=int8
            final_image=Image.fromarray(new_list_array,"L")
            #final_image.show()    

        
        if percentage < 0:
            new_list_pre=[]
            new_list=[]
            end_sub_r=start_row_index*2
            for i in range(0,len(converted_list)):
                original_ap=converted_list[i][-start_row_index:]        
                reversed_part=converted_list[i][-start_row_index:-end_sub_r][::-1]
                merged=reversed_part+original_ap
                new_list.append(merged)#beacuse of array, can't use "+"
                        
            new_list_array=np.asarray(new_list) 
            new_list_array.reshape(image_height,image_width) 
            new_list_array=np.int8(new_list_array)
            #the original array of lenna image is dtype=int8
            final_image=Image.fromarray(new_list_array,"L")
            #final_image.show()

        
        #if percentage==0:
            #im.resize((200,200)).show()
            #return arrayof_image_bw 
    if percentage==0:
        return arrayof_image_bw
    else:
        final_image.show()
        
    save_or_not=str(input("if you want to save the image, please enter Y/N:"))
    save_or_not=save_or_not.upper()
    if save_or_not=='Y':
        final_image=final_image.save("reflection.jpg")
        print("Your image has been saved ")        
    else:
        #final_image.show()
        return new_list_array    


def change_threshold():
    defined_threshold=int(input("Please enter a number between 0 and 255: "))
    image_path=input("please enter the image path")
    
    while defined_threshold< 0 or defined_threshold> 255:
        defined_threshold=int(input("Please enter a number between 0 and 255: "))
    im=Image.open(image_path)
    #im.show()
    
    bw_image=im.convert("L")
    arrayof_image_bw=asarray(bw_image)
    image_height=im.size[0]
    image_width=im.size[1]
    
                
    new_tuples_list=[]

    tuples_list=[]
    
    for sublists in arrayof_image_bw:
        for tuple_in in sublists:
            tuples_list.append(tuple_in)
    
    #test_tuples_list=tuples_list        
    new_tuples_list=[]
    
    for pixels_ind in range(0,len(tuples_list)):
        if tuples_list[pixels_ind] <= defined_threshold:
            new_tuples_list.append(0)
        else:
            new_tuples_list.append(255)

    test_list_to_array=np.asarray(new_tuples_list)
    rrshaped_test_list_to_array_bw=test_list_to_array.reshape(image_width,image_height)
    from_array_to_img_thre = Image.fromarray(rrshaped_test_list_to_array_bw)
    from_array_to_img_thre.show()
    
    save_or_not=str(input("if you want to save the image, please enter Y/N:"))
    if save_or_not=='Y':
        from_array_to_img_thre = from_array_to_img_thre.convert("RGB")
        from_array_to_img_thre=from_array_to_img_thre.save("threshold.jpg")
        print("Your image has been saved ")
    else:
        return rrshaped_test_list_to_array_bw

#to view the image    
def show_image(image):
    im_to_show=Image.open(image)
    im_to_show.show()
        
###########RGB
def reflection_rgb():
    number=int(input("Please enter a percentage between -50 and 50: "))
    direction=input("please enter v for vertial or h for horziontal")
    image_path=input("please enter the image path")
    
    while number<-50 or number> 50:
        number=int(input("Please enter a number between -50 and 50: "))
    while direction not in ('v','h'):
        direction=input("please enter v for vertial or h for horziontal")
    im=Image.open(image_path)
    
    percent=number/100
    direction_chosed=direction.lower()
    arrayof_image_RGB=asarray(im)    
    image_width=arrayof_image_RGB.shape[1]
    image_height=arrayof_image_RGB.shape[0]
    top_for_orig=int(round(abs(percent)*image_height))
    
    converted_list=arrayof_image_RGB.tolist()
    
    if direction_chosed =='v':
        if percent>0:
    #vertical >0
            orig_par=converted_list[top_for_orig:image_height]
            
            reflection_par=orig_par[:top_for_orig][::-1]
            
            merged_list=reflection_par+orig_par
            
            verti_array=np.asarray(merged_list)
            rrshaped_test_list_to_array_RBG=verti_array.reshape(image_height,image_width,3)
            final_array=np.int8(rrshaped_test_list_to_array_RBG)
            from_array_to_img = Image.fromarray(final_array,"RGB")
             
        if percent<0:
        
            end_for_orig=image_height-top_for_orig    
            orig_par=converted_list[:end_for_orig]    
            refelction_par=orig_par[-top_for_orig:][::-1]  
            
            merged_list=orig_par+refelction_par             
            verti_array=np.asarray(merged_list)
            rrshaped_test_list_to_array_RBG=verti_array.reshape(image_height,image_width,3)
            final_array=np.int8(rrshaped_test_list_to_array_RBG)
            from_array_to_img = Image.fromarray(final_array,"RGB")
      
    if direction_chosed =='h':   
        if percent>0:
            orig_par=[]
            for i in converted_list:
                orig_par.append(i[:-top_for_orig])
            
            merged_list=[]
            for sub_l in orig_par:
                reflection_par=sub_l[-top_for_orig:][::-1]
                pre_merged=sub_l+reflection_par
                merged_list.append(pre_merged)
            
                
            verti_array=np.asarray(merged_list)
            rrshaped_test_list_to_array_RBG=verti_array.reshape(image_height,image_width,3)
            final_array=np.int8(rrshaped_test_list_to_array_RBG)
            from_array_to_img = Image.fromarray(final_array,"RGB")    
   
        if percent<0:               
            orig_par=[]
            for i in converted_list:
                orig_par.append(i[top_for_orig:])
            
            merged_list=[]
            for sub_l in orig_par:
                reflection_par=sub_l[:top_for_orig][::-1]
                pre_merged=reflection_par+sub_l
                merged_list.append(pre_merged)
            
            verti_array=np.asarray(merged_list)
            rrshaped_test_list_to_array_RBG=verti_array.reshape(image_height,image_width,3)
            final_array=np.int8(rrshaped_test_list_to_array_RBG)
            from_array_to_img = Image.fromarray(final_array,"RGB")        
    
    if percent==0:
        return arrayof_image_RGB
    else:
        from_array_to_img.show()
    #return rrshaped_test_list_to_array_bw
    save_or_not=str(input("if you want to save the image as reflectionRGB.jpg, please enter Y/N:"))
    if save_or_not=='Y':
        #image_name=input("please enter file name you want to use")
        from_array_to_img=from_array_to_img.save("reflection.jpg")
        #image_list.append(image_name)
        print("Your image has been saved")
    else:
        return final_array             


