import rosbag
from sensor_msgs.msg import CompressedImage
import cv_bridge
import cv2
import sys

bag_path=sys.argv[1]
split_path=bag_path+'.split.bag'
in_bag=rosbag.Bag(bag_path,'r')
out_bag=rosbag.Bag(split_path,'w')
bridge = cv_bridge.CvBridge()
frame_cnt=0
for topic, msg, ts in in_bag.read_messages():
    img=bridge.compressed_imgmsg_to_cv2(msg)
    # print(img.shape)
    frame_cnt += 1
    img_width=img.shape[1]
    left=img[:, :img_width / 2, :]
    # print(left.shape)
    right=img[:, img_width / 2:, :]
    # print(right.shape)
    left_msg=bridge.cv2_to_compressed_imgmsg(left)
    left_msg.header=msg.header
    left_msg.header.frame_id='cam0'
    right_msg=bridge.cv2_to_compressed_imgmsg(right)
    right_msg.header=msg.header
    right_msg.header.frame_id='cam1'
    out_bag.write('insta360/cam0/compressed', left_msg, ts)
    out_bag.write('insta360/cam1/compressed', right_msg, ts)
print('{} images converted.'.format(frame_cnt))
in_bag.close()
out_bag.close()