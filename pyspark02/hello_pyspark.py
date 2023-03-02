# python 으로 spark 연결
# pip install pyspark==버전을 설치하면 spark 세션을 가져오는 것처럼 사용 가능
# SparkContext 

from pyspark import SparkContext

sc = SparkContext()

data = range(1, 100001) # 파이썬 코드로 데이터 생성

rdd = sc.parallelize(data)

print('rdd 타입 :', type(rdd))