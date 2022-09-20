# アプリ
import streamlit as st
import numpy as np
from PIL import Image
import cv2
import os
import shutil


from yolov5 import detect2

## サイドパネル（インプット部）
# st.sidebar.header('Input Features')
 
# sepalValue = st.sidebar.slider('sepal length (cm)', min_value=0.0, max_value=10.0, step=0.1)
# petalValue = st.sidebar.slider('petal length (cm)', min_value=0.0, max_value=10.0, step=0.1)
 

 
# uploaded_file = st.file_uploader("ファイルアップロード", type='jpg')
# image=Image.open(uploaded_file)
# img_array = np.array(image)
# resize_img = cv2.resize(img_array, (640, 640))
# cv2.imwrite('/Users/yugonojima/practice/plivate/Cell-Count/cell-count-data/test/img.jpg', resize_img)

# def detect(resize_img):
#   detect.run(source=resize_img, weights='')
# # --source {testディレクトリのpath} --weights {best.ptのpath} --conf 0.25 --name trained_exp --exist-ok --save-conf


# st.image(resize_img,caption = 'サムネイル画像')

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
        # Make temp file path from uploaded file
        for uploaded_file in uploaded_files:
            image=Image.open(uploaded_file)
            img_array = np.array(image)
            resize_img = cv2.resize(img_array, (640, 640))
            img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2RGB)
            cv2.imwrite('/Users/yugonojima/practice/plivate/Cell-Count/cell-count-data/test0/img{}.jpg'.format(num), img)
            num += 1
        
      
        detect2.run(source='/Users/yugonojima/practice/plivate/Cell-Count/cell-count-data/test0',
         weights='/Users/yugonojima/practice/plivate/Cell-Count/yolov5/runs/train/exp2/weights/best.pt',
          name='/Users/yugonojima/practice/plivate/Cell-Count/cell-count-data/result',
          exist_ok=True)
        
        # files = glob.glob("cell-count-data/result/*")
        # for file in files:
        #  result_image=Image.open(file) 
        # st.image(result_image,caption = 'サムネイル画像')
        image_dir = "cell-count-data/result"
        fName_list = os.listdir(image_dir)# 画像ファイルのリストを取得
        img_file_num = len(os.listdir(image_dir))#画像ファイル数

        idx = 0

        for _ in range(len(fName_list)-1):
            cols = st.columns(2)

            if idx < len(fName_list):
                cols[0].image(f'./cell-count-data/result/{fName_list[idx]}', caption=fName_list[idx])
                print(os.path.join(image_dir, fName_list[idx]))
                idx += 1
            if idx < len(fName_list):
                cols[1].image(f'./cell-count-data/result/{fName_list[idx]}', caption=fName_list[idx])
                idx += 1
            
            else:
                break
    
    if st.button("削除"):
        shutil.rmtree('cell-count-data/result/')
        shutil.rmtree('cell-count-data/test0/')
        os.mkdir('cell-count-data/result/')
        os.mkdir('cell-count-data/test0/')
    st.write('※削除ボタンを押した後、ページを更新してください')


if __name__ == "__main__":
    main()