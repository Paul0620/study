"""
Chapter4 Advanced(4) - 나만의 패키지 만들기(1)
Keyword - png(jpg) to gif, pil, image
"""
"""
패키지 작성
-> 정적이미지(JPG, PNG)를 -> GIF(애니메이션) 이미지로 변환하는 패키지 작성
"""

import glob
from PIL import Image

# 이미지, 결과 생성 경로
path_in = "./project/images/*.png"
path_out = "./project/image_out/result.gif"

# 첫 번째 이미지 & 모든 이미지 리스트 팩킹
# img, *images = [Image.open(f) for f in sorted(glob.glob(path_in))]

# 리사이즈(필요한 경우) - 이미지 사이즈 변경
img, *images = [
    Image.open(f).resize((360, 320), Image.ANTIALIAS)
    for f in sorted(glob.glob(path_in))
]

# 이미지 저장
img.save(
    fp=path_out,
    format="GIF",
    append_images=images,
    save_all=True,
    duration=500,  # 간격
    loop=0,  # 반복
)
