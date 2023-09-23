import travel.thailand  # travel 패키지의 thailand 모듈 가져오기

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

"""
import travel.thailand.ThailandPackage # 클래스 import 불가

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
"""

# travel.thailand 모듈에서 ThailandPackage 클래스 가져오기
from travel.thailand import ThailandPackage

trip_to = ThailandPackage()  # from~import 문에서는 travel.thailand. 제외
trip_to.detail()
