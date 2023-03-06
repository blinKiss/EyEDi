from pyspark.sql import SparkSession
# location_id 가 1700인 부서의 목록을 모두 출력

spark_ses = SparkSession.builder.appName("create DF").getOrCreate()

sdf = spark_ses.read.options(header='True').csv('./EyEDi/data/departments.csv')

sdf.createOrReplaceTempView('sdf_view')

# 부서id 20 또는 60
sdf_dep = spark_ses.sql('select department_name, location_id' + 
                        ' from sdf_view where location_id=1700')


sdf_dep.show()
