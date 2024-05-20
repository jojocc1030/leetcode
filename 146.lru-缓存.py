#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class Node:
    def __init__(self, key=0, value=0) :
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.pre = self.dummy  #设置头节点让后续操作保持一致
        self.cache = dict()

    def getnode(self, key: int) -> Node:
        if key not in self.cache:
            return None
        else:
            cur = self.cache[key]
            self.remove(cur)
            self.put_front(cur)
            return cur

    def get(self, key: int) -> int:
        cur = self.getnode(key)
        if cur is None:
            return -1
        else:
            return cur.value



    def put(self, key: int, value: int) -> None:
        cur = self.getnode(key)
        if cur is None:
            # 若不存在，创建新的node并把他放在最前面
            new_node = Node(key, value)
            self.put_front(new_node)
            self.cache[key] = new_node
            # 字典的key的个数是len()!!!!
            if len(self.cache) > self.capacity:
                last = self.dummy.pre
                del self.cache[last.key]
                self.remove(last) # 删除最后一个节点
        else:
            #若存在，只需要更换value即可
            cur.value = value

    
    def remove(self, cur: Node):
        cur.pre.next = cur.next
        cur.next.pre = cur.pre

    def put_front(self, cur: Node): # 修改x的pre和next， 再修改x前后节点的next和pre
        cur.pre = self.dummy
        cur.next = self.dummy.next
        cur.pre.next = cur
        cur.next.pre = cur


        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

