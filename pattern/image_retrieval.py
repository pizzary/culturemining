import cv2
import numpy as np
import urllib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def compute_histogram(img):
    # 计算图像的直方图
    hist = cv2.calcHist([img], [0, 1], None, [180, 256], [0, 180, 0, 256])

    # 归一化直方图
    cv2.normalize(hist, hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    return hist

#def algorithm1():

def algorithm2(image_data, database_image_bytes, database_image_urls):


    def search_similar_images(image_data, database_image_bytes, database_image_urls):
        nparr0 = np.frombuffer(image_data, np.uint8)
        #print(image_data)
        image = cv2.imdecode(nparr0, cv2.IMREAD_COLOR)

        # 计算查询图像的直方图
        query_hist = compute_histogram(image)
        #print(query_hist)
        # 初始化结果列表
        results = []
        i = 0
        for (image_url, image_bytes) in zip(database_image_urls, database_image_bytes):
            i = i + 1

            # 将字节流转换为 numpy 数组
            nparr = np.frombuffer(image_bytes, dtype=np.uint8)
            #print(image_bytes)
            if image_data == image_bytes:
                print("yes!")
            else:
                print("NO")
            print(np.array_equal(nparr, nparr0))
            if i == 4:
                break
            # 解码图像
            db_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # 计算直方图
            db_hist = compute_histogram(db_image)
            #print(db_hist)
            # 计算直方图相似度（使用巴氏距离）
            similarity = cv2.compareHist(query_hist, db_hist, cv2.HISTCMP_CORREL)

            # 将图像路径和相似度添加到结果列表
            results.append((image_url, similarity))

        # 按相似度进行排序
        results.sort(key=lambda x: x[1], reverse=True)
        return results

    results = search_similar_images(image_data, database_image_bytes, database_image_urls)
    # 打印结果
    for image_path, similarity in results:
        print(image_path, 'Similarity score:', similarity)
    return results
