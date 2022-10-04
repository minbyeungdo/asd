#include "ros/ros.h"
#include "yh_difference/YhDifference.h"

bool add(yh_difference::YhDifference::Request& req,
        yh_difference::YhDifference::Response& res)
{
    res.result = req.a - req.b;
    ROS_INFO("request: a = %d, b = %d", req.a, req.b);
    ROS_INFO("response: result = %d", res.result);

    return true;
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "yh_difference_server");
    ros::NodeHandle nh;
    
    ros::ServiceServer yh_difference_server = nh.advertiseService("yh_difference", add);
    
    ROS_INFO("Ready to Service Server.");

    ros::spin();

    return 0;
}