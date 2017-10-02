#include "ros/ros.h"
#include "geometry_msgs/Pose2D.h"
#include <ncurses.h>
#include <sstream>

#ifndef CTRL
#define CTRL(c) ((c) & 037)
#endif

typedef geometry_msgs::Pose2D move;

int main(int argc, char **argv)
{
	ros::init(argc, argv, "published");
	ros::NodeHandle n;
	ros::Publisher pub = n.advertise<geometry_msgs::Pose2D>("moves", 1);

	ros::Rate loop_rate(10);
	int ch;

	printw("Hey, yo!\n");
	printw("Use arrows to move around\n");
	while ((ch = getch()) != CTRL('c'))
	{
		switch(ch)
		{
		case KEY_UP:
			pub.publish(move(0, -1));
			break;
		case KEY_DOWN:
			pub.publish(move(0, 1));
			break;
		case KEY_LEFT:
			pub.publish(move(-1, 0));
			break;
		case KEY_RIGHT:
			pub.publish(move(1, 0));
			break;
		case KEY_M:
			pub.publish(mode(2, 0));
			break;
		}
		ros::spinOnce();
	}
	getch();
	return 0;
}

