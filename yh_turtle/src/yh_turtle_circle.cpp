#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
 
int main(int argc, char** argv)
{
    ros::init(argc, argv, "vel_ctrl");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 10);

    ROS_INFO("draw_circle start...");

    while(ros::ok())
    {
        geometry_msgs::Twist vel_cmd;
 
        vel_cmd.linear.x = 4.0;
        vel_cmd.linear.y = 0.0;
        vel_cmd.linear.z = 0.0;
 
        vel_cmd.angular.x = 0;
        vel_cmd.angular.y = 0;
        vel_cmd.angular.z = 3.8; 
        pub.publish(vel_cmd);
 
        ros::spinOnce();
    }
    return 0;
}