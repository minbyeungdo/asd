#include "ros/ros.h"
#include "yh_difference/YhDifference.h"

bool add(yh_difference::YhDifference::Request& req,
        yh_difference::YhDifference::Response& res)
{
    if(req.a > req.b)
    {
        res.result = req.a - req.b;
        return true;
    }
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "yh_difference_server");
    ros::NodeHandle nh;
    
    ros::ServiceServer yh_difference_server = nh.advertiseService("yh_difference_service", difference);
    
    ros::spin();

    return 0;
}