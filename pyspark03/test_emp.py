from pyspark.sql import SparkSession

# 파이스파크의 시작은 스파크세션
spark_ses = SparkSession.builder.appName("Create DataFrame").getOrCreate()

# 파일에 있는 전체 데이터
sdf = spark_ses.read.options(header='True').csv('./EyEDi/data/employees.csv')

# 뷰 = 가상테이블
sdf.createOrReplaceTempView('sdfv_emp')

sdf_emp = spark_ses.sql('select first_name, salary, department_id' +
                        ' from sdfv_emp where salary>=10000')

sdf_emp_in = sdf_emp.withColumn('incentiv', sdf_emp['salary']*0.3)
sdf_emp.show()

# 뷰를 생성
# sdf.show()
