# Graph Traversal - string
# # Problem: 11729
# # Memory: 29200KB
# Time: 68ms

cur_time = input()
target_time = input()

time_list = cur_time.split(':')
cur = (int(time_list[0]) * 60 * 60) + (int(time_list[1]) * 60) + int(time_list[2])
target_list = target_time.split(':')
target = (int(target_list[0]) * 60 * 60) + (int(target_list[1]) * 60) + int(target_list[2])

wait_time = 0
if target == cur:
    wait_time = (24 * 60 * 60)
elif target > cur:
    wait_time = target - cur
else:
    wait_time = (24 * 60 * 60) - cur + target

wait_time1 = wait_time // (60 * 60)
wait_time3 = wait_time % 60
wait_time2 = (wait_time - (wait_time1 * 60 * 60) - wait_time3) // 60

print('{0:02d}:{1:02d}:{2:02d}'.format(wait_time1, wait_time2, wait_time3))
