# アプリ
import streamlit as st
import numpy as np
from PIL import Image
import cv2
import os
import shutil
import torch


from yolov5 import detect2





def main():
    """Streamlit application
    """
    num = 0

    st.title("Auto Cell Counter App")

    uploaded_files = st.file_uploader("Choose your .jpg file", type="jpg", accept_multiple_files=True
    )
    if uploaded_files == [] :
        uploaded_files = None

    

    if uploaded_files is not None:
        input_image = []
        
        # Make temp file path from uploaded file
        for uploaded_file in uploaded_files:
            image=Image.open(uploaded_file)
            img_array = np.array(image)
            resize_img = cv2.resize(img_array, (640, 640))
            
            img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2RGB)
            
            input_image.append(img)
            cv2.imwrite('cell-count-data/test0/img{}.jpg'.format(num), img)
            num += 1
        
      
        detect2.run(source='cell-count-data/test0',
         weights='yolov5/runs/train/exp2/weights/best.pt',
        #   name='cell-count-data/result',
          exist_ok=True)
        
        # files = glob.glob("cell-count-data/result/*")
        # for file in files:
        #  result_image=Image.open(file) 
        # st.image(result_image,caption = 'サムネイル画像')


        image_dir = "yolov5/runs/detect/exp"
        fName_list = os.listdir(image_dir)# 画像ファイルのリストを取得
        img_file_num = len(os.listdir(image_dir))#画像ファイル数

        idx = 0

        for _ in range(len(fName_list)-1):
            cols = st.columns(2)

            if idx < len(fName_list):
                cols[0].image(f'yolov5/runs/detect/exp/{fName_list[idx]}', caption=fName_list[idx])
                print(os.path.join(image_dir, fName_list[idx]))
                idx += 1
            if idx < len(fName_list):
                cols[1].image(f'yolov5/runs/detect/exp/{fName_list[idx]}', caption=fName_list[idx])
                idx += 1
            
            else:
                break
    
    if st.button("削除"):
        shutil.rmtree('yolov5/runs/detect/exp/')
        shutil.rmtree('cell-count-data/test0/')
        # os.mkdir('cell-count-data/result/')
        os.mkdir('cell-count-data/test0/')
    st.write('※削除ボタンを押した後、ページを更新してください')


if __name__ == "__main__":
    main()