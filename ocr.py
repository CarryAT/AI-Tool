import cnocr
import os
import datetime


def recognize_text(txt_directory, image_directory):
    # 初始化 cnocr
    ocr = cnocr.CnOcr()

    text = []
    for filename in os.listdir(image_directory):
        if filename.endswith('.jpg'):
            startTime_pdf2img = datetime.datetime.now()  # 开始时间

            image_path = os.path.join(image_directory, filename)
            # 读取图片并识别文字
            results = ocr.ocr(image_path)
            # text = [result['text'] for result in results]
            text = ''.join([result['text'].replace('\n', '') for result in results])
            # print(text)
            # sys

            # 读取一张写入一张
            with open(txt_directory, 'a+', encoding='utf-8') as f:
                f.write(text + '\n')

            endTime_pdf2img = datetime.datetime.now()  # 结束时间
            print('img2txt时间 =', (endTime_pdf2img - startTime_pdf2img).seconds, ",", filename, "已写入")
    return text


if __name__ == "__main__":
    # 图片文件路径
    image_directory = './'
    # txt文件路径
    txt_directory = "./test.txt"
    # 识别文字
    recognize_text(txt_directory, image_directory)