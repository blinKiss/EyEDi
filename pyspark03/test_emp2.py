from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# employee.csv 파일
# employee_id, last_name, job_id, department_id 컬럼을 가져와서
# sdf_emp2 

spark_ses = SparkSession.builder.appName("create DF").getOrCreate()

sdf = spark_ses.read.options(header='True').csv('./EyEDi/data/employees.csv')

sdf.createOrReplaceTempView('sdfv_emp2')

# 부서id 20 또는 60
sdf_emp2 = spark_ses.sql('select employee_id, last_name, job_id, department_id'+
                       ' from sdfv_emp2 where department_id=20 or department_id=60')

sdf_emp2.show()

# commission 컬럼을 추가 0.2값 동일하게
sdf_emp3 = sdf_emp2.withColumn('commission', F.lit(0.2))
sdf_emp3.show()
