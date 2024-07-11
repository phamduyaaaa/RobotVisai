#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
import math

#Thông số của xe:
a = 0.1   #Khoảng cách từ tâm đến mỗi bánh xe
r = 0.05    #bán kính của bánh xe

def tinh_van_toc(a,r,v,g): 

    Vg = (g*math.pi)/180  #van toc goc quay rad/s = theta đạo hàm

    #van toc quay quanh truc cua 2 banh
    Vr = (v + Vg*a)/r
    Vl = (v - Vg*a)/r

    #van toc tuyen tinh va van toc goc quay
    Vtt = (r/2)*(Vr + Vl)
    Vgq = (r/(2*a))*(Vr - Vl)

    return Vtt, Vgq, Vr, Vl

def di_chuyen(s,v,g):  #s: quang duong di (m), v: van toc di (m/s), g:goc quay moi giay (rad/s)
    Vtt, Vgq, Vr, Vl = tinh_van_toc(a,r,v,g)
    t = s/v  #thoi gian di
    count = 0
    while 1:
        count += 1
        if count <= t:
            mess = Twist()
            mess.linear.x = Vtt
            mess.angular.z = Vgq
            rospy.loginfo("Vr = %f , Vl = %f",Vr,Vl)
            pub.publish(mess)
            rate.sleep()
        else:
            stop = Twist()
            stop.linear.x = 0
            stop.angular.z = 0
            rospy.loginfo("Vr = 0 , Vl = 0")
            pub.publish(stop)
            break
def quay_tai_cho(g): #goc can quay
    v = 0 #van toc tuyen tinh = 0
    Vtt,Vgq,Vr, Vl=tinh_van_toc(a,r,v,g)
    mess = Twist()
    mess.linear.x = Vtt
    mess.angular.z = Vgq
    rospy.loginfo("Vr = %f , Vl = %f",Vr,Vl)
    pub.publish(mess)
    rate.sleep()


if __name__ == "__main__":
    rospy.init_node("control_robot",anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    rate = rospy.Rate(1)
    try:
        rospy.loginfo("di thang 1m; vận tốc 0.25 m/s; góc quay = 0")
        di_chuyen(1,0.25,0) 
        rospy.loginfo("dg cong ban kinh 1m")
        di_chuyen(math.pi/2,math.pi/8,22.5)
        rospy.loginfo("quay tai cho")
        quay_tai_cho(-60)
        rospy.loginfo("di thang 1m,vận tốc 0.25 m/s; góc quay = 0")
        di_chuyen(1,0.25,0)
    except rospy.ROSInterruptException:
        pass



    
    

    
    

