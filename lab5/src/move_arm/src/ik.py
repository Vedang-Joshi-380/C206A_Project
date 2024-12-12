#!/usr/bin/env python
import rospy
from moveit_msgs.srv import GetPositionIK, GetPositionIKRequest, GetPositionIKResponse
from geometry_msgs.msg import PoseStamped
from moveit_commander import MoveGroupCommander
import numpy as np
from numpy import linalg
import sys
from move_arm.msg import Coords
from tf.transformations import quaternion_from_euler


from intera_interface import gripper as robot_gripper

def callback(message):
    # Wait for the IK service to become available
    rospy.wait_for_service('compute_ik')
    #rospy.init_node('service_query')
    print("we here")
    # Create the function used to call the service
    compute_ik = rospy.ServiceProxy('compute_ik', GetPositionIK)
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        
        #input('Press [ Enter ]: ')
        
        # Construct the request
        request = GetPositionIKRequest()
        request.ik_request.group_name = "right_arm"

        # If a Sawyer does not have a gripper, replace '_gripper_tip' with '_wrist' instead
        link = "right_gripper_tip"
        r.sleep()
        request.ik_request.ik_link_name = link
        #request.ik_request.attempts = 20
        request.ik_request.pose_stamped.header.frame_id = "base"

        print("Y: \"%s\"" % message.y + ", Z:  \"%s\"" % message.z + ", theta:  \"%s\"" % message.theta)
        
        # Set the desired orientation for the end effector HERE
        request.ik_request.pose_stamped.pose.position.x = 0.8
        request.ik_request.pose_stamped.pose.position.y = message.y * -1.14 + 0.444
        request.ik_request.pose_stamped.pose.position.z = message.z * -0.588 + 0.849

        q = quaternion_from_euler(message.theta, 0, np.pi)
        request.ik_request.pose_stamped.pose.orientation.x = q[0]
        request.ik_request.pose_stamped.pose.orientation.y = q[1]
        request.ik_request.pose_stamped.pose.orientation.z = q[2]
        request.ik_request.pose_stamped.pose.orientation.w = q[3]
        # request.ik_request.pose_stamped.pose.position.x = 0.8
        # request.ik_request.pose_stamped.pose.position.y = 0.6 #message.y * 1.212 - 0.045
        # request.ik_request.pose_stamped.pose.position.z = 0.35 #message.z * 0.764
        # request.ik_request.pose_stamped.pose.orientation.x = 0.0
        # request.ik_request.pose_stamped.pose.orientation.y = 1.0
        # request.ik_request.pose_stamped.pose.orientation.z = 0.0
        # request.ik_request.pose_stamped.pose.orientation.w = 0.0

        
        try:
            # Send the request to the service
            response = compute_ik(request)
            
            # Print the response HERE
            print(response)
            group = MoveGroupCommander("right_arm")

            # Setting position and orientation target
            group.set_pose_target(request.ik_request.pose_stamped)

            # TRY THIS
            # Setting just the position without specifying the orientation
            #y =  message.y * -1.212 + 0.045
            #z = message.z * -0.764 + 0.764
            #print("y: " + str(y) + "z: " + str(z))
            #group.set_position_target([0.8, y, z, 0.0, 1.0, 0.0, 0.0])

            # Plan IK
            plan = group.plan()
            # user_input = input("Enter 'y' if the trajectory looks safe on RVIZ")
            
            
            # Execute IK if safe
            # if user_input == 'y':
            group.execute(plan[1])
            break
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

def listener():
    rospy.Subscriber("user_messages", Coords, callback, queue_size=1)
    rospy.spin()

# Python's syntax for a main() method
if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    listener()
